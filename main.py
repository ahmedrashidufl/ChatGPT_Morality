import os
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table
import numpy as np

def calculate_ss(data):
    if len(data) == 0:
        raise ValueError("Data list cannot be empty.")

    ss = sum(x ** 2 for x in data)

    return ss

def create_moral_orientation(df,n):
  stage_1_pro_w = df['qw1'].loc[df.index[n]]
  stage_1_con_w = df['qw12'].loc[df.index[n]]
  stage_2_pro_w = df['qw5'].loc[df.index[n]]
  stage_2_con_w = df['qw9'].loc[df.index[n]]
  stage_3_pro_w = df['qw3'].loc[df.index[n]]
  stage_3_con_w = df['qw11'].loc[df.index[n]]
  stage_4_pro_w = df['qw2'].loc[df.index[n]]
  stage_4_con_w = df['qw7'].loc[df.index[n]]
  stage_5_pro_w = df['qw6'].loc[df.index[n]]
  stage_5_con_w = df['qw10'].loc[df.index[n]]
  stage_6_pro_w = df['qw4'].loc[df.index[n]]
  stage_6_con_w = df['qw8'].loc[df.index[n]]
  stage_1_pro_d = df['qd3'].loc[df.index[n]]
  stage_1_con_d = df['qd10'].loc[df.index[n]]
  stage_2_pro_d = df['qd4'].loc[df.index[n]]
  stage_2_con_d = df['qd11'].loc[df.index[n]]
  stage_3_pro_d = df['qd6'].loc[df.index[n]]
  stage_3_con_d = df['qd7'].loc[df.index[n]]
  stage_4_pro_d = df['qd5'].loc[df.index[n]]
  stage_4_con_d = df['qd12'].loc[df.index[n]]
  stage_5_pro_d = df['qd2'].loc[df.index[n]]
  stage_5_con_d = df['qd8'].loc[df.index[n]]
  stage_6_pro_d = df['qd1'].loc[df.index[n]]
  stage_6_con_d = df['qd9'].loc[df.index[n]]

  stage_1_sum = stage_1_pro_w + stage_1_con_w + stage_1_pro_d + stage_1_con_d
  stage_2_sum = stage_2_pro_w + stage_2_con_w + stage_2_pro_d + stage_2_con_d
  stage_3_sum = stage_3_pro_w + stage_3_con_w + stage_3_pro_d + stage_3_con_d
  stage_4_sum = stage_4_pro_w + stage_4_con_w + stage_4_pro_d + stage_4_con_d
  stage_5_sum = stage_5_pro_w + stage_5_con_w + stage_5_pro_d + stage_5_con_d
  stage_6_sum = stage_6_pro_w + stage_6_con_w + stage_6_pro_d + stage_6_con_d

  stage_1_avg = stage_1_sum/4
  stage_2_avg = stage_2_sum/4
  stage_3_avg = stage_3_sum/4
  stage_4_avg = stage_4_sum/4
  stage_5_avg = stage_5_sum/4
  stage_6_avg = stage_6_sum/4

  stage_avg = [stage_1_avg, stage_2_avg, stage_3_avg, stage_4_avg, stage_5_avg, stage_6_avg]
  return stage_avg

def create_c_score(df,n):
  stage_1_pro_w = df['qw1'].loc[df.index[n]]
  stage_1_con_w = df['qw12'].loc[df.index[n]]
  stage_2_pro_w = df['qw5'].loc[df.index[n]]
  stage_2_con_w = df['qw9'].loc[df.index[n]]
  stage_3_pro_w = df['qw3'].loc[df.index[n]]
  stage_3_con_w = df['qw11'].loc[df.index[n]]
  stage_4_pro_w = df['qw2'].loc[df.index[n]]
  stage_4_con_w = df['qw7'].loc[df.index[n]]
  stage_5_pro_w = df['qw6'].loc[df.index[n]]
  stage_5_con_w = df['qw10'].loc[df.index[n]]
  stage_6_pro_w = df['qw4'].loc[df.index[n]]
  stage_6_con_w = df['qw8'].loc[df.index[n]]
  stage_1_pro_d = df['qd3'].loc[df.index[n]]
  stage_1_con_d = df['qd10'].loc[df.index[n]]
  stage_2_pro_d = df['qd4'].loc[df.index[n]]
  stage_2_con_d = df['qd11'].loc[df.index[n]]
  stage_3_pro_d = df['qd6'].loc[df.index[n]]
  stage_3_con_d = df['qd7'].loc[df.index[n]]
  stage_4_pro_d = df['qd5'].loc[df.index[n]]
  stage_4_con_d = df['qd12'].loc[df.index[n]]
  stage_5_pro_d = df['qd2'].loc[df.index[n]]
  stage_5_con_d = df['qd8'].loc[df.index[n]]
  stage_6_pro_d = df['qd1'].loc[df.index[n]]
  stage_6_con_d = df['qd9'].loc[df.index[n]]

  all_stages = [stage_1_pro_w, stage_1_con_w, stage_1_pro_d, stage_1_con_d,
  stage_2_pro_w, stage_2_con_w, stage_2_pro_d, stage_2_con_d,
  stage_3_pro_w, stage_3_con_w, stage_3_pro_d, stage_3_con_d,
  stage_4_pro_w, stage_4_con_w, stage_4_pro_d, stage_4_con_d,
  stage_5_pro_w, stage_5_con_w, stage_5_pro_d, stage_5_con_d,
  stage_6_pro_w, stage_6_con_w, stage_6_pro_d, stage_6_con_d]

  stage_1_sum = stage_1_pro_w + stage_1_con_w + stage_1_pro_d + stage_1_con_d
  stage_2_sum = stage_2_pro_w + stage_2_con_w + stage_2_pro_d + stage_2_con_d
  stage_3_sum = stage_3_pro_w + stage_3_con_w + stage_3_pro_d + stage_3_con_d
  stage_4_sum = stage_4_pro_w + stage_4_con_w + stage_4_pro_d + stage_4_con_d
  stage_5_sum = stage_5_pro_w + stage_5_con_w + stage_5_pro_d + stage_5_con_d
  stage_6_sum = stage_6_pro_w + stage_6_con_w + stage_6_pro_d + stage_6_con_d

  stage_1_sum_squared = stage_1_sum * stage_1_sum
  stage_2_sum_squared = stage_2_sum * stage_2_sum
  stage_3_sum_squared = stage_3_sum * stage_3_sum
  stage_4_sum_squared = stage_4_sum * stage_4_sum
  stage_5_sum_squared = stage_5_sum * stage_5_sum
  stage_6_sum_squared = stage_6_sum * stage_6_sum
  stage_sum_squared = stage_1_sum_squared + stage_2_sum_squared + stage_3_sum_squared + stage_4_sum_squared +\
                      stage_5_sum_squared + stage_6_sum_squared

  sum_squared = calculate_ss(all_stages)



  w_pro_sum = stage_1_pro_w + stage_2_pro_w + stage_3_pro_w + stage_4_pro_w + stage_5_pro_w + stage_6_pro_w
  w_con_sum = stage_1_con_w + stage_2_con_w + stage_3_con_w + stage_4_con_w + stage_5_con_w + stage_6_con_w
  d_pro_sum = stage_1_pro_d + stage_2_pro_d + stage_3_pro_d + stage_4_pro_d + stage_5_pro_d + stage_6_pro_d
  d_con_sum = stage_1_con_d + stage_2_con_d + stage_3_con_d + stage_4_con_d + stage_5_con_d + stage_6_con_d

  mean_sum_squared = (w_pro_sum + w_con_sum + d_pro_sum + d_con_sum)
  mean_sum_squared = mean_sum_squared * mean_sum_squared
  mean_sum_squared = mean_sum_squared/24

  unadjust_stage_sum = stage_sum_squared/4
  adjust_stage_sum = unadjust_stage_sum - mean_sum_squared
  sum_stage_dev = sum_squared - mean_sum_squared

  r_squared = adjust_stage_sum/sum_stage_dev
  c_score = r_squared * 100
  return c_score


# Provide the path to your CSV file
worker_0_10_file_path = '3_5_Data/csv/array_w_0_10.csv'
worker_10_20_file_path = '3_5_Data/csv/array_w_10_20.csv'
worker_20_30_file_path = '3_5_Data/csv/array_w_20_30.csv'
worker_30_40_file_path = '3_5_Data/csv/array_w_30_40.csv'
worker_40_50_file_path = '3_5_Data/csv/array_w_40_50.csv'
doctor_0_10_file_path = '3_5_Data/csv/array_d_0_10.csv'
doctor_10_20_file_path = '3_5_Data/csv/array_d_10_20.csv'
doctor_20_30_file_path = '3_5_Data/csv/array_d_20_30.csv'
doctor_30_40_file_path = '3_5_Data/csv/array_d_30_40.csv'
doctor_40_50_file_path = '3_5_Data/csv/array_d_40_50.csv'

# Read the CSV file into a dataframe
worker_0_10 = pd.read_csv(worker_0_10_file_path)
worker_10_20 = pd.read_csv(worker_10_20_file_path)
worker_20_30 = pd.read_csv(worker_20_30_file_path)
worker_30_40 = pd.read_csv(worker_30_40_file_path)
worker_40_50 = pd.read_csv(worker_40_50_file_path)
doctor_0_10 = pd.read_csv(doctor_0_10_file_path)
doctor_10_20 = pd.read_csv(doctor_10_20_file_path)
doctor_20_30 = pd.read_csv(doctor_20_30_file_path)
doctor_30_40 = pd.read_csv(doctor_30_40_file_path)
doctor_40_50 = pd.read_csv(doctor_40_50_file_path)


combined_worker = pd.concat([worker_0_10, worker_10_20, worker_20_30, worker_30_40, worker_40_50], ignore_index=True)
combined_doctor = pd.concat([doctor_0_10, doctor_10_20, doctor_20_30, doctor_30_40, doctor_40_50], ignore_index=True)
combined_worker.to_csv('worker_full.csv', index = True)
combined_doctor.to_csv('doctor_full.csv', index = True)
combined_worker.describe().to_csv('worker_describe.csv', index = True)
combined_doctor.describe().to_csv('doctor_describe.csv', index = True)


combined_iterations = pd.DataFrame(columns=['qw1','qw2','qw3','qw4','qw5','qw6','qw7','qw8','qw9','qw10','qw11','qw12',
                                            'qd1','qd2','qd3','qd4','qd5','qd6','qd7','qd8','qd9','qd10','qd11','qd12'])
for n in range(0, 55):
   worker_row = combined_worker.loc[n, :].values.tolist()
   doctor_row = combined_doctor.loc[n, :].values.tolist()
   full_row = worker_row + doctor_row
   combined_iterations.loc[len(combined_iterations)] = full_row

combined_iterations = combined_iterations.dropna()
combined_iterations = combined_iterations.reset_index(drop=True)

c_scores = []
stage_avgs_1 = []
stage_avgs_2 = []
stage_avgs_3 = []
stage_avgs_4 = []
stage_avgs_5 = []
stage_avgs_6 = []
for n in range(50):
  c_score = create_c_score(combined_iterations,n)
  c_scores.append(c_score)
  stage_avg = create_moral_orientation(combined_iterations,n)
  stage_avgs_1.append(stage_avg[0])
  stage_avgs_2.append(stage_avg[1])
  stage_avgs_3.append(stage_avg[2])
  stage_avgs_4.append(stage_avg[3])
  stage_avgs_5.append(stage_avg[4])
  stage_avgs_6.append(stage_avg[5])

c_scores_avg = sum(c_scores) / len(c_scores)
print(c_scores_avg)

combined_iterations['c_scores'] = c_scores
combined_iterations['stage 1'] = stage_avgs_1
combined_iterations['stage 2'] = stage_avgs_2
combined_iterations['stage 3'] = stage_avgs_3
combined_iterations['stage 4'] = stage_avgs_4
combined_iterations['stage 5'] = stage_avgs_5
combined_iterations['stage 6'] = stage_avgs_6

combined_iterations.to_csv('Output.csv', index = True)
combined_iterations.describe().to_csv('Output_describe.csv', index = True)
