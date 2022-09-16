no_of_proc = int(input("Enter no of proc : "))
proc = []
print("Enter ArrivalTime BurstTime : ")
for i in range(no_of_proc):
    proc.append(list(map(int,input().split(" "))))
    proc.sort()

print(proc)
for i in range(len(proc)):
    current_arr_time = proc[i][1]
    index = i
    for j in range(i+1,len(proc)):
        if proc[j][1] < current_arr_time:
            current_arr_time = proc[j][1]
            index = j
    proc[i][1] , proc[index][1] = proc[index][1] , proc[i][1] 
    proc[i][0] , proc[index][0] = proc[index][0] , proc[i][0] 

print("Your proc are sorted according to burst time here is new arrival time and burst time list : ")
print("Arrival-Time \t Burst-Time")
for i in range(len(proc)):
    for j in range(len(proc[0])):
        print(str(proc[i][j])+"\t\t",end=" ")
    print()


#   ***IMP***  =>    After sorting we can apply same logic as fcfs for turn-around-time and waiting-time and completion-time
completeion_time = []

for i in range(len(proc)):
    if i==0:
        completeion_time.append(proc[i][0]+proc[i][1])
    else:
        completeion_time.append(max(completeion_time[-1],proc[i][0])+proc[i][1]) 

turn_around_time = []

for i in range(len(proc)):
    turn_around_time.append(completeion_time[i]-proc[i][0])

waiting_time = []

for i in range(len(proc)):
    waiting_time.append(turn_around_time[i]-proc[i][1])

print("Arrival-Time \t Burst-Time \t Completion-Time \t Turn-Around-Time \t Waiting Time")
for i in range(len(proc)):
    print(str(proc[i][0])+"\t\t\t"+ str(proc[i][1])+"\t\t\t"+str(completeion_time[i])+"\t\t\t"+str(turn_around_time[i])+"\t\t\t"+str(waiting_time[i]))