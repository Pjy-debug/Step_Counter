# frequency domain analysis
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift

# the data must be a list
def fft_analysis(data_list, label_list, sample_rate, is_save = False, save_path = None, max_freq = 100):
    fft_list = []
    plt.figure(figsize=(12, 6))
    plt.title('FFT Analysis')
    for i, (data, label) in enumerate(zip(data_list, label_list)):
        N = len(data)  # 采样点数
        yf = fft(data)  # 复数形式的频域结果
        xf = fftfreq(N, 1/sample_rate)  # 计算频率轴（未移位，包含正负频率）
        
        # 处理频域结果（幅值归一化 + 只保留正频率）
        # 幅值：复数的模，归一化（除以采样点数），正频率部分乘以2（能量守恒）
        amplitude = 2.0 / N * np.abs(yf)
        # 只保留正频率（采样频率的一半为奈奎斯特频率）
        positive_freq_mask = xf >= 0
        xf_pos = xf[positive_freq_mask]
        amplitude_pos = amplitude[positive_freq_mask]
        fft_list.append((xf_pos, amplitude_pos))

        plt.plot(xf_pos, amplitude_pos, linestyle="-", linewidth=1.5, label=label)
        plt.xlabel('frequency (Hz)')
        plt.ylabel('amplitude')
        plt.xlim(0, max_freq)  # 只显示0-100Hz（聚焦目标频率）
        plt.grid(True)
        plt.legend(loc="best", fontsize=10)
        plt.grid(True, alpha=0.3, linestyle="--")
        
        plt.tight_layout()
    if not os.path.exists(os.path.dirname(save_path)):
        os.makedirs(os.path.dirname(save_path))
    plt.savefig(save_path, dpi=300) if is_save and save_path else None
    return fft_list
    

if __name__ == "__main__":
    # for sensor data logger
    data_path_root = 'data\sensor_data_logger\\20251204095727R_pjinkim'
    acc_data_path = os.path.join(data_path_root, 'linacce.txt')
    gyro_data_path = os.path.join(data_path_root, 'gyro.txt')
    sample_name = os.path.basename(data_path_root)
    timename = sample_name[:14]

    acc_data = pd.read_csv(
        acc_data_path,  
        sep='\s+',  
        header=None,  
        skiprows=1, 
        names=['t_Android', 'acc_x', 'acc_y', 'acc_z']  
    )
    acc_time = acc_data['t_Android'].tolist()
    begin_time = acc_time[0]
    acc_time = [(a_time - begin_time) / 1e9 for a_time in acc_time]
    acc_x = acc_data['acc_x'].tolist()
    acc_y = acc_data['acc_y'].tolist()
    acc_z = acc_data['acc_z'].tolist()

    time_gap = np.diff(acc_time)
    time_mean = np.mean(time_gap)
    time_var = np.var(time_gap)
    # print(time_mean)
    # print(time_var)    
    
    # sampling var of time is acceptable
    time = [i * time_mean for i in range(len(acc_time))]

    gyro_data = pd.read_csv(
        gyro_data_path,  
        sep='\s+',  
        header=None,  
        skiprows=1, 
        names=['t_Android', 'gyro_x', 'gyro_y', 'gyro_z']
    )
    gyro_time = gyro_data['t_Android'].tolist()
    begin_time = gyro_time[0]
    gyro_time = [(g_time - begin_time) / 1e9 for g_time in gyro_time]
    gyro_x = gyro_data['gyro_x'].tolist()
    gyro_y = gyro_data['gyro_y'].tolist()
    gyro_z = gyro_data['gyro_z'].tolist()

    fft_analysis(data_list=[acc_x, acc_y, acc_z], 
                 label_list=['acc_x', 'acc_y', 'acc_z'],
                 sample_rate=1/time_mean,
                 is_save=True,
                 save_path='figure\sensor_data_logger\\'+timename+'\\acc_fft_'+timename+'.png',
                 max_freq=10
                 )
    
    fft_analysis(data_list=[gyro_x, gyro_y, gyro_z],
                 label_list=['gyro_x', 'gyro_y', 'gyro_z'],
                 sample_rate=1/time_mean,
                 is_save=True,
                 save_path='figure\sensor_data_logger\\'+timename+'\\gyro_fft_'+timename+'.png',
                 max_freq=10
                 )

