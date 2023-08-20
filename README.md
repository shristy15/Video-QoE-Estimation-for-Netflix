# Video-QoE-Estimation-for-Netflix
## Introduction
Netflix is a popular video streaming platform that provides on-demand video
content to millions of users worldwide. Quality of Experience (QoE) refers to the
subjective quality of the video streaming experience perceived by the users. To
ensure a high-quality streaming experience, Netflix employs various techniques
to estimate QoE.Netflix estimates QoE based on several factors such as video
resolution, bitrate, buffering, and playback smoothness. These factors are
measured by monitoring the streaming video session and analyzing the user's
interaction with the video player.Netflix uses a variety of technical methods to
estimate QoE for its video streaming service. Here are some additional technical
details:
1. Video Resolution: Netflix uses adaptive video streaming technology to
adjust the resolution of the video based on the available network
bandwidth and the device being used to view the video. This helps to
ensure that the video quality is optimized for each viewer's specific device
and network conditions.
2. Bitrate: The video bitrate refers to the amount of data delivered per unit of
time, usually measured in kilobits per second (Kbps) or megabits per
second (Mbps). Netflix uses adaptive streaming to adjust the bitrate of the
video based on the available network bandwidth and the viewer's device
3. Buffering: When the video playback is halted due to a slow network
connection or other issues, buffering occurs.
4. Playback Smoothness: Any stutters or freezes in the video playback can
affect the quality of experience. Netflix monitors the playback smoothness
and adjusts its QoE calculations accordingly.
Netflix also employs machine learning algorithms to estimate QoE by analyzing
historical data of user interactions with the video player. This helps Netflix to
predict the QoE for new users and improve the overall streaming experience.
By using these technical methods to estimate QoE, Netflix can provide a
high-quality video streaming experience for millions of customers worldwide.

## **Final KPIs achieved with detailed explanation:**
### 1. Data sample collection from various devices and scenarios:-
Dataset captured from Netflix video traffic data using wireshark tool as
follows:
* Download and install Wireshark on the device you want to collect data
from. Wireshark is available for Windows, Mac, and Linux.
* Open Wireshark and start a new capture. Select the network interface you
want to capture traffic on, such as Wi-Fi or Ethernet.
<p align="center">
  <img width="600" height="400" src="https://github.com/shristy15/Video-QoE-Estimation-for-Netflix/assets/77338956/0ef85e3d-4bd8-4a5a-94e8-ee7be6969d06">
</p>
<p align="center" ><strong>Dialog Box for selecting the Network such as WiFi</strong></p>  

Apply capture filters to select the particular source and destination ID
addresses for NETFLIX and the device from which we wanted to capture
data.
* Most important step is to make sure that the device is connected to the
same Interface which we have selected in the wireshark.
* Start a Netflix video streaming session on the device and let it run for
several minutes to capture enough data.
<p align="center">
  <img width="700" height="350" src="https://github.com/shristy15/Video-QoE-Estimation-for-Netflix/assets/77338956/247b8bdd-8fc7-42dc-b1f9-b16b9f082c55">
</p>
<p align="center" ><strong>Packets getting captured</strong></p>  

* For getting the packet information for just netflix video stream we have
added the “source ip address” of the device in which we are streaming the
video and “destination ip address” of the netflix video which we got by
requesting netflix from their website for sending us our “personal activity”
over a period of time which has the IP address mentioned to the sectioned
mentioned below.
* Stop the capture in Wireshark and save the capture file.
* Analyze the capture file to extract relevant information for QoE estimation,
such as network bandwidth, packet loss, and buffering events.
* Then we repeated the same process for different devices and network
scenarios to collect a diverse range of data samples of netflix video
streams.

<p>Packet captures and built-in stats for nerds tool in Netflix were used to build the
dataset. Dataset consists of raw network flow features such as bandwidth, IAT,
application format etc. These raw features are then used to extract suitable
parameters for QoE calculation such as Stalling, Video bandwidth changes etc</p>

### 2. Understanding of network behaviors of captured data sample:-
Captured dataset provides information about the network behavior during video
streaming sessions. It includes several variables such as network throughput,
packet loss, and round-trip time (RTT). Description of these variables are as
follows:
* Packet loss refers to the percentage of data packets that are lost during
transmission over the network.It can occur due to various reasons like
network congestion, poor network conditions, or hardware/software
failures. This dataset provides information about packet loss during video
streaming sessions, which can help in understanding the impact on video
quality and identifying any issues that may need to be addressed.
* Network throughput refers to the rate at which data is transmitted over a
network connection, usually measured in bits per second (bps). This
dataset provides information about the throughput during video streaming
sessions, which can help in understanding the network capacity and its
impact on video quality.
* Round-trip time refers to the time it takes for a data packet to travel from
the sender to the receiver and back. It is typically measured in milliseconds
(ms) and can help in understanding the network latency or delay. This
dataset provides information about the RTT during video streaming
sessions, which can help in understanding the impact on video quality and
identifying any issues that may need to be addressed.
* Buffering events refer to the instances where the video playback is halted
due to slow network connections or other issues. Buffering events can
result in a poor quality viewing experience, as viewers may become
frustrated with the interruption to their viewing experience.
By analyzing these network behavior variables we gained insights into the
performance of video streaming over different types of networks and under
different conditions. This information can be used to identify network issues and
optimize network settings to improve the video streaming experience for users.

### 3. Study of different approaches for Video QoE estimation for Adaptive Video streaming:-
There are various approaches for estimating Quality of Experience (QoE) for
adaptive video streaming. We came across some of the common approaches
such as Objective Quality Metrics like Structural Similarity Index (SSIM), and
Video Multimethod Assessment Fusion (VMAF), Subjective Quality
Assessment,Hybrid Approaches while going through these below mentioned
research papers:
* [QoE Modeling for HTTP Adaptive Video Streaming–A Survey and Open
Challenges](https://ieeexplore.ieee.org/abstract/document/8666971)
* [Towards network-wide QoE fairness using openflow-assisted adaptive video
streaming](https://dl.acm.org/doi/abs/10.1145/2491172.2491181)
* [QoE-Driven Dynamic Adaptive Video Streaming Strategy With Future Information](https://ieeexplore.ieee.org/abstract/document/7898405)
* [Buffer State is Enough: Simplifying the Design of QoE-Aware HTTP Adaptive
Video Streaming](https://ieeexplore.ieee.org/abstract/document/8260530)

### 4. Analysis of user actions and various behavioral characteristics of network video:-
User actions and various behavioral characteristics of network video were
analyzed to estimate the QoE of video streaming on the Netflix platform. Some of
the key features and actions that were analyzed include:
* Bandwidth: The bandwidth of the user's network connection was analyzed
to determine if it is sufficient for the video quality being streamed.
* Buffering events: Buffering events occur when the video playback is
paused due to a lack of data being received. The frequency and duration
of buffering events were analyzed as they have a negative impact on the
user experience.
* Rebuffering ratio: The rebuffering ratio is the percentage of time the video
is paused due to buffering. This metric was analyzed to determine the
impact of buffering events on the overall user experience.
* Bitrate changes: Adaptive video streaming changes the bitrate of the video
being streamed based on the user's network conditions. The frequency of
bitrate changes and the duration between the changes were analyzed to
determine the impact on user experience.
* Video start time: The time it takes for the video to start playing was
analyzed to determine the impact on user experience.
* Video resolution: The resolution of the video being streamed was analyzed
to determine if it matches the user's device and network conditions.
* Video duration: The duration of the video being streamed was analyzed to
determine if it matches the user's expectations and if it is consistent with
the content description.
<p>By analyzing these features and actions, the project aimed to develop a model
that could accurately predict the QoE of video streaming on Netflix.</p>

### 5. Identifying the measurements needed for resolution and QoE score:-
<p align="center">
  <img width="600" height="450" src="https://github.com/shristy15/Video-QoE-Estimation-for-Netflix/assets/77338956/a9f30e50-7200-4af0-91e9-66fa026df8cc">
</p>
<p align="center" ><strong>Distribution of values for different attributes</strong></p>  

<p>Resolution refers to the clarity and detail of an image or video. In order to
measure resolution, the following measurements are required to compute the
resolution of a video frame from packet data. These features include, pixel count,
aspect ratio, and bitrate. Both bitrate and aspect ratio can be calculated by
analyzing the packet payload of the video packet.</p>
<p>For QoE score, we require network flow features instead of single packet
features. This is because, analyzing the packet flow will give information about
the buffering, latency, jitter etc. which are helpful in estimating the Quality of
Experience of the end user. Apart from these features, the audio features also
play a key role in determining the QoE. These features include audiorate,
audioloss etc.</p>
<p>The process of capturing network flow features is as follows, first we record the
features of the network packets for a certain time period and then perform
mathematical operations on them to get the desired network flow feature. For
example, to calculate bitrate, we get the sum of the packet sizes for a certain
time interval and divide the sum by the time interval. A similar procedure is
involved in calculating the buffering time, jitter, packet loss, audio loss etc.</p>

### 6. Implementation completion:-
**Data Collection Phase**

#### 1. Calculating Bitrate from Received Packets
<p>We have used python scripts to capture the incoming packets and calculate
various features such as bitrate, framerate, buffer etc. We have also used stats
for nerds feature in Netflix to expand our dataset size. For calculating flow
features from packet data we used the sniff function to extract the packet
features. Below, we demonstrate this process by showing the extraction process
of bitrate and framerate.</p>
For bitrate, we run a for loop that terminates after 20 seconds. Inside the loop we
get the packet size using the meta function and increment it. Once we exit the
loop after 20 seconds, we calculate the bitrate by using the formula Bitrate =
Total packet size/Time.



This code snippet demonstrates how to calculate the bitrate of received packets in Python using socket programming. It measures the time taken to receive packets and computes the bitrate based on the packet size and time duration.

```python
while end_time - start_time <= 20:
    data, address = sock.recvfrom(8090)
    packet = data.extract()
#increment the size of each packet received 
    pkt_size += packet.meta.size()

bitrate = pkt_size / (end_time - start_time)
```

#### 2. Calculating Frame Rate from Received Packets
<p>Calculation of frame rate is a little bit different from bitrate, as we have to analyze
the payload of the packet and extract its data. We again use the sniff function to
capture the packet data and then check if the packet includes video data by
looking for the ‘Raw’ layer and the “0x00 0x00 0x00 0x01” sequence, which is
used to delimit slices in video data.</p>
<p>If the packet includes video data, we extract the payload data and search for
slice headers by looking for the 0x00 0x00 0x00 0x01 sequence. Once we find
the slice headers, we count the number of frames by looking for slice headers
that correspond to the start of a frame (identified by the nal_unit_type field in the
slice header). Finally, we calculate the framerate using the formula Frame rate =
Number of frames/ Time.</p>

This code snippet demonstrates how to calculate frame rate of received packets in Python using socket programming. It measures the time taken to receive packets, calculates the frame rate by inspecting slice headers in the packet payload.

```python
while end_time - start_time <= 20:
    # Check if the packet contains slice headers
    if packet.haslayer(Raw) and b'\x00\x00\x00\x01' in packet[Raw].load:
        # Extract the payload
        payload = packet[Raw].load
        
        # Find slice headers in the payload
        slice_headers = [i for i in range(len(payload) - 4) if payload[i:i+4] == b'\x00\x00\x00\x01']
        
        # If slice headers are found, count the frames
        if slice_headers:
            num_frames = len([i for i in slice_headers if payload[i+4] & 0x1f == 1])

# Calculate the frame rate
framerate = num_frames / (end_time - start_time)
```
<p>For all the features that are generally present in all types of packet data, we used
a logic similar to bitrate calculation. For video data specific features, we have
extracted the packet payload, verified whether the packet consists of video data
and then calculated the required fields.</p>

### 7. Evaluation completion:-
Firstly, we used Multiple Linear Regression (MLR) as the machine learning
algorithm for estimating Quality of Experience (QoE) for Netflix data. We chose
MLR due to its simplicity, interpretability, and effectiveness in revealing the
relationship between multiple independent variables and a dependent variable.
<p align="center">
  <img width="600" height="450" src="https://github.com/shristy15/Video-QoE-Estimation-for-Netflix/assets/77338956/f441456c-89af-4f30-8a90-67f806d735ff">
</p>
<p align="center" ><strong>Correlation matrix of the features in the dataset</strong></p>  

#### Feature Selection
We used the following columns from the dataset as input features in our MLR model:
* Video Initial Max DL Rate (kbps)
* E2E RTT (ms)
* Average Rate of Playing phase (kbps)
* Initial Buffering Latency (ms)
* Stalling Ratio
* Video Total DL Rate (kbps)
* Stalling Length
* Playing Length
* Total time of Playing phase (kbps)
* Stalling times
* Video bitrate
* Video Initial buffer download
* SQuality
* SLoading
* Stalling
  
#### Dependent Variable:
Our dependent variable was the Video Mean Opinion Score (VMoS), which
represents the overall quality of experience as perceived by the user.
  
#### Data Preprocessing:
We first preprocessed the data by cleaning it and checking
for missing values. We then standardized the continuous features to ensure that
they were on a similar scale, which is important for the MLR model.
#### Model Training and Evaluation: 
We split the dataset into training and testing sets, using 80% of the data for training and 20% for testing. We trained the MLR model
on the training set and evaluated its performance using the testing set. We used
the coefficient of determination (R^2) and Root Mean Squared Error (RMSE) as
evaluation metrics to assess the model's performance.

### Results: 
The most significant factors influencing the VMoS were `Stalling Length`, `Playing Length`, ` Total time of
Playing phase (kbps)`, `Stalling times`, `video bitrate`

### Coefficient of MLR and it’s results:
**Mean Squared Error**: 0.3650

**Coefficients**: [ 1.33869030e-04 6.95710896e-02 1.27079715e-05 7.11430006e-05
1.19663396e-04 3.50166354e-04 1.70364643e-04 -1.12013789e-04
2.32443274e-07 -3.79482142e-07 7.01533045e-01 4.16534488e-01]

<p><strong>Intercept: -15.332094258255147 </strong></p>

<p>The values of QoE were estimated in 5 ranges and then later binary classification
was done on the basis of that as 0 (bad) and 1 (good) for the values from 0-2 and
2-5 respectively. Different machine learning algorithms to estimate the Quality of
Experience (QoE) for Netflix data. The algorithms used were Multivariate Linear
Regression, Logistic Regression, Support Vector Machines (SVM), K-Nearest
Neighbor (KNN), Naive Bayes, and a combination of K-means clustering and
Linear Regression (K-means + LR), which gave accuracy of upto around `85%`
upon modifying the hyperparameters. But in our proposed modelwe used the
XGBoost algorithm, an advanced implementation of gradient boosted decision
trees, to estimate the Quality of Experience (QoE) for Netflix data. This model
provided even better performance compared to the previously tested algorithms.</p>
<p>The XGBoost model achieved an accuracy of `93.47%`. These results indicate a
substantial improvement in the estimation of QoE, surpassing all the other
models, including our previously proposed K-means + Linear Regression
method. We define D value = |prediction − original|, where prediction and original
denote the prediction value and the original value, respectively. Table below the
deviance results of all the features and the corresponding rankings (sorting D
value in ascending order).</p>

| Features | Average D value | Average Ranking|
|-----------------|:---------------:|-----------------|
| Average rate of playing phase    | 0.0645    |7    |
| Video total DL rate   |0.0633   | 8    |
| Video bitrate   | 0.1876   | 4   |
| Initial max DL rate  | 0.3053   | 3   |
| E2E RTT   | 0.5400   |1    |
|Initial buffering latency    |0.0214    | 11 |
| Video initial buffer download  | 0.1026    | 6   |
| Playing time    | 0.0664   | 9   |
| Playing total duration  | 0.0750    | 10   |
|Stalling times   | 0.0243  | 5    |
| Stalling ratio   |0.0229|2   |

<p>XGBoost's good performance can be attributed to its ability to handle various
data patterns, robustness to outliers, and efficient handling of missing data.
Additionally, its capacity for parallel and distributed computing allows for faster
training, making it more suitable for large-scale applications.<p/>
<p>In conclusion, the XGBoost model provides the most accurate and reliable
estimation of QoE for Netflix data among the tested algorithms. The insights
gained from this analysis can be used to inform network management and
optimization strategies for improving the user experience.</p>












