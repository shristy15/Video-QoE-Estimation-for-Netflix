import socket
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import time
from scapy.all import *
from sklearn.preprocessing import *

# define the  IP address and port number to listen on
#Can change this values depending on usecase
ip = "10.0.0.1"
port = 8090

# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to the local IP address and port number
sock.bind((ip, port))

# load your trained ML model
model = RandomForestClassifier()
model.load("QoE_model.pkl")

# loop to receive and process incoming packets
while True:
    start_time = time.time()
    end_time = time.time()
    pkt_size = 0
    num_frames = 0
    sps_width = 0
    sps_height = 0
    buffering_count = 0
    buffering_time = 0
    audio_loss = 0
    audio_rate = 0

    while end_time-start_time<=20:
        data, address = sock.recvfrom(8090)
        packet = data.extract()
        #increment the size of each packet received 
        pkt_size += packet.meta.size()
        #increment the number of frames received by checking if the payload has slice headers
        if packet.haslayer(Raw) and b'\x00\x00\x00\x01' in packet[Raw].load:
            # Extract payload
            payload = packet[Raw].load
            # Find the slice headers in the payload
            slice_headers = [i for i in range(len(payload)-4) if payload[i:i+4] == b'\x00\x00\x00\x01']
            # If we find slice headers, count the frames
            if slice_headers:
                num_frames = len([i for i in slice_headers if payload[i+4] & 0x1f == 1])
        
        # Calculate buffering by checking if the packet consists of the next playback segment
        if segment_start_packet is not None and packet.time > segment_start_packet.time:
        # Calculate the buffering time
            buffering_time = packet.time - segment_start_packet.time - segment_duration

        # Check if the packet includes the start of the next playback segment
        if packet.haslayer(Raw) and b'SEGMENT_START' in packet[Raw].load:
            # Save the packet as the start of the next segment
            global segment_start_packet, segment_duration
            segment_start_packet = packet
            segment_duration = end_time - start_time

        # Check the resolution of incoming packet
        if packet.haslayer(Raw) and b'\x00\x00\x00\x01' in packet[Raw].load:
        # Extract the payload data
            payload = packet[Raw].load

        # Find the sequence parameter set (SPS) header in the payload
        sps_header = b'\x67'

        # Check if the payload includes the SPS header
        if sps_header in payload:
            # Extract the SPS data (which includes the frame size)
            sps_data = payload[payload.find(sps_header)+1:]
            sps_size = ((sps_data[0] & 0x3) << 8) | sps_data[1]
            sps_width = ((sps_data[1] & 0xFC) >> 2) | ((sps_data[2] & 0xF) << 6)
            sps_height = ((sps_data[2] & 0xF0) >> 4) | ((sps_data[3] & 0x3F) << 4)

        if packet.haslayer(Raw) and b'\xff\xf1' in packet[Raw].load:
            # Extract the payload data
            payload = packet[Raw].load

            # Find the audio header in the payload
            audio_header = payload[payload.find(b'\xff\xf1'):payload.find(b'\xff\xf2')]

            # Extract the audio rate from the header
            audio_rate = int(audio_header[-2:].hex(), 16)
        
        end_time = time.time()
    
    bitrate = pkt_size/(end_time - start_time)
    framerate = num_frames/(end_time - start_time)
    df = [sps_width, sps_height, bitrate, framerate, audio_loss, audio_rate, buffering_count, buffering_time]
    # unpickle the data to extract the feature vector
    feature_vector = pickle.loads(df)
    
    # preprocess the feature vector (if necessary)
    feature_vector = preprocess(feature_vector)
    
    # deploy the ML model on the feature vector
    prediction = model.predict(np.array([feature_vector]))
    print(f"QoE: {prediction}")
    # send the prediction back to the client
    sock.sendto(pickle.dumps(prediction), address)
    
# close the socket
sock.close()