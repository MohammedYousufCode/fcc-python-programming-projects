#** start of main.py **

def hanoi_solver(no_of_disks):
    # Initialize rods
    rod_1=sorted(range(1,no_of_disks+1),reverse=True)
    rod_2=[]
    rod_3=[]

    states=[]
    states.append(f"{rod_1} {rod_2} {rod_3}")

    def arrange(n,source,destination,auxiliary):
        if n==1:
            destination.append(source.pop())
            states.append(f"{rod_1} {rod_2} {rod_3}")
        else:
            arrange(n-1,source,auxiliary,destination)

            destination.append(source.pop())
            states.append(f"{rod_1} {rod_2} {rod_3}")

            arrange(n-1,auxiliary,destination,source)

    arrange(no_of_disks,rod_1,rod_3,rod_2)
    return "\n".join(states)
hanoi_solver(3)



#** end of main.py **

