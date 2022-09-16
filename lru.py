refrence_string = [ 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2,1,2,0,1,7,0,1]
capacity = 4

s = []
pagefault = 0

for i in refrence_string:
    if i not in s:
        if(len(s)==capacity):
            s.pop(0)
            s.append(i)
        else:
            s.append(i)

        pagefault += 1
    else:
        s.remove(i)
        s.append(i)

print(pagefault)