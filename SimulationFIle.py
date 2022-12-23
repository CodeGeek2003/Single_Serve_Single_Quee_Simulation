import random

sim_len = int(input())
IAT, Arrival_Time, Service_Time, Service_Begin, Service_End, Waiting_Time, Time_Spent, Server_Idle = [], [], [], [], [], [], [], []
# creating random values for IAT and Service Time
total_service_time = 0
# getting the total service time to calculate the average
for i in range(sim_len):
    IAT.append(random.randint(1, 1001))
    Service_Time.append(random.randint(1, 101))
    total_service_time += Service_Time[i]
    if 1<=Service_Time[i]<=10:
        Service_Time[i]=1
    elif 11<=Service_Time[i]<=30:
        Service_Time[i] = 2
    elif 31<=Service_Time[i]<=60:
        Service_Time[i] = 3
    elif 61<=Service_Time[i]<=85:
        Service_Time[i] = 4
    elif 86<=Service_Time[i]<=95:
        Service_Time[i] = 5
    else:
        Service_Time[i]=6
    if 1<=IAT[i]<=125:
        IAT[i]=1
    elif 126<=IAT[i]<=250:
        IAT[i] = 2
    elif 251<=IAT[i]<=375:
        IAT[i] = 3
    elif 376<=IAT[i]<=500:
        IAT[i] = 4
    elif 501<=IAT[i]<=625:
        IAT[i] = 5
    elif 626<=IAT[i]<=750:
        IAT[i] = 6
    elif 751<=IAT[i]<=875:
        IAT[i] = 7
    else:
        IAT[i]=8

# computing the arrival time for the first customer
Arrival_Time.append(IAT[0])
# computing the arrival time for the rest of the customers
for i in range(1, sim_len):
    Arrival_Time.append((Arrival_Time[i - 1] + IAT[i]))
# computing the rest of components for first customer
Service_Begin.append(Arrival_Time[0])
Service_End.append(Service_Begin[0] + Service_Time[0])
Waiting_Time.append(0)
Time_Spent.append(Service_Time[0])
Server_Idle.append(0)
# computing the rest of components for the rest of the customers
total_waiting_time = 0
# getting the total waiting time to calculate the average
for i in range(1, sim_len):
    Service_Begin.append(max(Arrival_Time[i], Service_End[i - 1]))
    Service_End.append((Service_Begin[i] + Service_Time[i]))
    Waiting_Time.append((Service_Begin[i] - Arrival_Time[i]))
    total_waiting_time += Service_Begin[i] - Arrival_Time[i]
    Time_Spent.append((Waiting_Time[i] + Service_Time[i]))
    Server_Idle.append((Service_Begin[i] - Service_End[i - 1]))
# calculating average waiting time:
avg_waiting_time = total_waiting_time / sim_len
# calculate average service time:
avg_service_time = total_service_time / sim_len
print(
    "The table in the following order: Customer_ID | IAT | Arrival_Time | Service_Time | Service_Begin | Service_End | Waiting_Time | Time_Spent | Server_Idle ")
for i in range(sim_len):
    print("*", i + 1, "*", "|", IAT[i], "|", Arrival_Time[i], "|", Service_Time[i], "|", Service_Begin[i], "|",
          Service_End[i], "|", Waiting_Time[i], "|", Time_Spent[i], "|", Server_Idle[i])
    print('----------------------------------------')
print("The average waiting time is: ", avg_waiting_time)
print("The average service time is: ", avg_service_time)
