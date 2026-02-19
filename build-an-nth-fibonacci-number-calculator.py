** start of main.py **

def fibonacci(n):
    sequence=[0,1]
    if n==0:
        return 0
    if n==1:
        return 1
    for i in range(2,n+1):
        sequence.append(sequence[i-1]+sequence[i-2])
    return sequence[n]


** end of main.py **

