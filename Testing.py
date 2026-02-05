def swap_values(a,b,c,d):
    return b,a,d,c


if __name__ == '__main__': 
    # Type your code here. Your code must call the function.

    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    a,b,c,d = swap_values(a,b,c,d)
    print(a,b,c,d)
