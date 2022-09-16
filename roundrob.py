n = int(input("Enter no of proc : "))
quantum = int(input("Enter time quantum : "))
proc = []
bt = []
wt = []
ct = []

for i in range(1,n+1):
    proc.append(i)
    wt.append(0)
    bt.append(int(input(f"Enter Burst time of proc {i} : ")))

rem_bt = [0]*n
for i in range(len(rem_bt)):
    rem_bt[i] = bt[i]
    ct.append(0)
t=0

while(1):
        done = True
 
        # Traverse all processes one by
        # one repeatedly
        for i in range(n):
             
            # If burst time of a process is greater
            # than 0 then only need to process further
            if (rem_bt[i] > 0) :
                done = False # There is a pending process
                 
                if (rem_bt[i] > quantum) :
                 
                    # Increase the value of t i.e. shows
                    # how much time a process has been processed
                    t += quantum
 
                    # Decrease the burst_time of current
                    # process by quantum
                    rem_bt[i] -= quantum
                 
                # If burst time is smaller than or equal 
                # to quantum. Last cycle for this process
                else:
                 
                    # Increase the value of t i.e. shows
                    # how much time a process has been processed
                    t = t + rem_bt[i]
                    ct[i] = t
                    # Waiting time is current time minus
                    # time used by this process
                    wt[i] = t - bt[i]
 
                    # As the process gets fully executed
                    # make its remaining burst time = 0
                    rem_bt[i] = 0
                 
        # If all processes are done
        if (done == True):
            break

print(wt)
print(ct)