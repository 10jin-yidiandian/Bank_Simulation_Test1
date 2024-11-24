import random
import numpy as np

# 定义黄色客户的参数
alpha_yellow = 2
beta_yellow = 5

# 定义红色客户的参数
alpha_red = 2
beta_red = 2

# 定义蓝色客户的参数
alpha_blue = 5
beta_blue = 1

def simulate(alpha, beta, row = 200):
    # 模拟的时间步数
    num_steps = 10#10000
    # 存储每个客户的到达时间和处理时间
    arrival_times = []
    processing_times = []
    # 模拟客户到达和处理
    current_time = 0
    queue_length = 0
    waiting_times = []
    total_waiting_time = 0
    queue = []

    for _ in range(num_steps):
        # 生成客户的到达时间
        arrival_time = -np.log(1 - random.random()) * 100

        if total_waiting_time-arrival_time>0: #需要等待
            queue_length += 1
            total_waiting_time -= arrival_time
        else:
            total_waiting_time = 0
            queue_length = max(queue_length-1,0)
        waiting_time = total_waiting_time
        arrival_times.append(current_time + arrival_time) #叠加

        # 生成客户的处理时间
        x = random.random()
        processing_time = row * (x ** (alpha - 1)) / ((1 - x) ** (beta - 1))
        processing_times.append(processing_time)
        
        total_waiting_time += processing_time
        # 更新当前时间和队列长度
        current_time = max(current_time, arrival_time)
        queue_length = max(queue_length, 0)
        queue.append(queue_length)

        # 等待时间
        waiting_times.append(waiting_time)

    average_wt = sum(waiting_times)/len(waiting_times)
    maximum_wt = max(waiting_times)

    average_ql = sum(queue)/len(queue)
    maximum_ql = max(queue)

    return average_wt,maximum_wt,average_ql,maximum_ql
average_yellow_waiting_time,maximum_yellow_waiting_time,average_yellow_queue_length,maximum_yellow_queue_length = simulate(alpha_yellow,beta_yellow)
average_red_waiting_time,maximum_red_waiting_time,average_red_queue_length,maximum_red_queue_length = simulate(alpha_red,beta_red)
average_blue_waiting_time,maximum_blue_waiting_time,average_blue_queue_length,maximum_blue_queue_length = simulate(alpha_blue,beta_blue)

# 比较不同类型客户的平均等待时间和最大等待时间的差异
yellow_diff = abs(average_yellow_waiting_time - maximum_yellow_waiting_time)
red_diff = abs(average_red_waiting_time - maximum_red_waiting_time)
blue_diff = abs(average_blue_waiting_time - maximum_blue_waiting_time)

# 输出结果
print("只给定黄色客户：平均等待时间 =", average_yellow_waiting_time, "，最大等待时间 =", maximum_yellow_waiting_time)
print("只考虑红色顾客：平均队列长度 =", average_red_queue_length, "，最大队列长度 =", maximum_red_queue_length)
# 输出蓝色客户的结果（省略）

# 比较差异并输出最接近的类型
if yellow_diff <= min(red_diff,blue_diff):
    print("黄色客户的平均等待时间和最大等待时间之间的值最接近。")
elif red_diff <= min(yellow_diff,blue_diff):
    print("红色顾客的平均等待时间和最大等待时间之间的值最接近。")
else:
    print("蓝色顾客的平均等待时间和最大等待时间之间的值最接近。")
print("黄、红、蓝对应差值分别为：",yellow_diff,red_diff,blue_diff)