no_of_proc = int(input("Enter no of proc : "))
proc = []                                                   # This List contain [arrival time , burst time]
print("Enter ArrivalTime BurstTime : ")
for i in range(no_of_proc):
    proc.append(list(map(int,input().split(" "))))
    proc.sort()                                             # sorting makes the proc with least arrival time comes the first in proc list 

completeion_time = []

for i in range(len(proc)):
    if i==0:
        completeion_time.append(proc[i][0]+proc[i][1])      # This will append sum of arrival time and burst time in completion_time list 
    else:
        completeion_time.append(max(completeion_time[-1],proc[i][0])+proc[i][1])        # The logic is that the completion time of current process will be the sum of 
                                                                                        # burst time of current proc and max of (currentproc[arrivaltime] or completiontime[last proc] )                                                                                        
turn_around_time = []

for i in range(len(proc)):
    turn_around_time.append(completeion_time[i]-proc[i][0])

waiting_time = []

for i in range(len(proc)):
    waiting_time.append(turn_around_time[i]-proc[i][1])

print("Arrival-Time \t Burst-Time \t Completion-Time \t Turn-Around-Time \t Waiting Time")
for i in range(len(proc)):
    print(str(proc[i][0])+"\t\t\t"+ str(proc[i][1])+"\t\t\t"+str(completeion_time[i])+"\t\t\t"+str(turn_around_time[i])+"\t\t\t"+str(waiting_time[i]))