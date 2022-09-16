
def fifo(ref_string,frame,frame_size):
    pagefault = 0
    for i in ref_string:
        if i not in frame and len(frame)>0 and len(frame)<frame_size:
            frame.append(i)
            pagefault += 1

            print(f"{i} ->")
            for i in range(len(frame)):
                print(frame[i],end=" ")
            print("\n")

        elif len(frame)==0:
            frame.append(i)
            pagefault += 1

            print(f"{i} ->")
            for i in range(len(frame)):
                print(frame[i],end=" ")
            print("\n")
            
        elif i not in frame and len(frame)==frame_size:
            frame.pop(0)
            frame.append(i)
            pagefault += 1

            print(f"{i} ->")
            for i in range(len(frame)):
                print(frame[i],end=" ")
            print("\n")
            
        else:
            continue
    print("Page Fault : ",pagefault)
    print("Page Hit : ",(len(ref_string)-pagefault))
        



refrence_string = [1,3,0,3,5,6,3]
frame_size = 3
frame = []
fifo(refrence_string,frame,frame_size)