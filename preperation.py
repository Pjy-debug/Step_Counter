# visualization
# manual tailoring and subpackaging
# filtering

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# data is .csv version


if __name__ == "__main__":
    data_path_root = 'data\sensor_data_logger\\20251204103831R_pjinkim'
    
    # for sensorbox
    # acc_data = pd.read_csv('data\sensorbox\ENDLESS_04_12_2025_17_38_41\ACC.csv', 
    #                    header=0, 
    #                    sep = ';', 
    #                    names=["t_Android", "t_unix", "acc_x", "acc_y", "acc_z", "num_axises"])
    # acc_time = acc_data['t_Android'].tolist()
    # begin_time = acc_time[0]
    # acc_time = [(a_time - begin_time) / 1e9 for a_time in acc_time]
    # acc_x = acc_data['acc_x'].tolist()
    # acc_y = acc_data['acc_y'].tolist()
    # acc_z = acc_data['acc_z'].tolist()

    # for sensor data logger
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

    # Plot data
    plt.figure(figsize=(12, 6))
    plt.plot(acc_time, acc_x, color="red", linestyle="-", linewidth=1.5, label="accx (x-axis acceleration)")
    plt.plot(acc_time, acc_y, color="green", linestyle="-", linewidth=1.5, label="accy (y-axis acceleration)")
    plt.plot(acc_time, acc_z, color="blue", linestyle="-", linewidth=1.5, label="accz (z-axis acceleration)")
    plt.xlabel("time(s)", fontsize=12)
    plt.ylabel("accelaration(m/s²)", fontsize=12)
    plt.title("accelerometer x/y/z-axis time-series graph", fontsize=14, fontweight="bold")
    plt.legend(loc="best", fontsize=10)
    plt.grid(True, alpha=0.3, linestyle="--")
    plt.tight_layout()  # 自动调整布局，避免标签重叠
    acc_save_path = f'figure\sensor_data_logger\\{timename}\\acc_time_{timename}.png'
    if not os.path.exists(os.path.dirname(acc_save_path)):
        os.makedirs(os.path.dirname(acc_save_path))
    plt.savefig(acc_save_path, dpi=300)
    plt.clf()

    plt.figure(figsize=(12, 6))
    plt.plot(gyro_time, gyro_x, color="red", linestyle="-", linewidth=1.5, label="gyrox (x-axis gyroscope)")
    plt.plot(gyro_time, gyro_y, color="green", linestyle="-", linewidth=1.5, label="gyroy (y-axis gyroscope)")
    plt.plot(gyro_time, gyro_z, color="blue", linestyle="-", linewidth=1.5, label="gyroz (z-axis gyroscope)")
    plt.xlabel("time(s)", fontsize=12)
    plt.ylabel("angular velocity (rad/s)", fontsize=12)
    plt.title("gyroscope x/y/z-axis time-series graph", fontsize=14, fontweight="bold")
    plt.legend(loc="best", fontsize=10)
    plt.grid(True, alpha=0.3, linestyle="--")
    plt.tight_layout()  # 自动调整布局，避免标签重叠
    gyro_save_path = f'figure\sensor_data_logger\\{timename}\\gyro_time_{timename}.png'
    if not os.path.exists(os.path.dirname(acc_save_path)):
        os.makedirs(os.path.dirname(acc_save_path))
    plt.savefig(gyro_save_path, dpi=300)
    plt.clf()



    

    
