procs = 5 # NO of proc
res = 3 # NO of resources

# res a = 10 , res b = 5 , res c = 7

alloc = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
max_need = [[7,5,3],[3,2,2],[9,0,2],[4,2,2],[5,3,3]]
avail = [3,3,2]

remain_need = [[0 for i in range(res)] for j in range(procs)]

for i in range(procs):
    for j in range(res):
        remain_need[i][j] = max_need[i][j] - alloc[i][j]                # Ramin Need = Maximum Nedd - Allocated 


ans =[0,0,0,0,0]                            # to store the index of process which will compltete first
ans_indx = 0
finis = [0,0,0,0,0]                         # to check if a proc is finsihed or not 

for k in range(procs):                      
    for l in range(procs):
        if(finis[l] == 0):
            flag = 0
            for m in range(res):
                if(remain_need[l][m] > avail[m]):
                    flag = 1
                    break
            if(flag==0):
                ans[ans_indx] = l
                ans_indx += 1
                for n in range(res):
                    avail[n] += alloc[l][n]
                finis[l] = 1

print(ans)


#https://www.geeksforgeeks.org/bankers-algorithm-in-operating-system-2/