# This is the final work for the class "intelligent sensing"
## Introduction
This is the final work for the class "intelligent sensing". The work is count steps from the IMU data collected from cellphone. The data is collected by the [sensor data logger](github.com/PyojinKim/Sensors-Data-Logger). The data includes the time, acceleration, gyroscope, magnetic field, etc. The preliminary idea of data processing is to use the FFT to analyze the frequency domain of the data, furtherly figuring out the step frequency and total counts.
## Data Preparation
Sensor data logger was packed into an apk with Android Studio. Then data was collected from this apk in a cellphone and was saved in the local storage of the cellphone in the format of .txt file. Then they were sent to the computer for further processing.
## Data Analysis
A possible way of step-counting is:
1. Use a window function (like Hamming FIR filter) to smooth the data and sample the data in a certain length of time slice.
2. Find out the largest frequency component in certain frequency range (like 0.3Hz-5Hz) in the frequency domain of the smoothed data.
3. Let this frequency component be the step frequency. Integrate the step frequency in time domain to get the total counts.
## Other Possible Ways
+ Peak detection
+ Deep learning