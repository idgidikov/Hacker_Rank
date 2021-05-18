def print_formatted(number):
    spacing = len(bin(n)[2:])

    for i in range(1,n+1):
       print (str(i).rjust(spacing, ' '),str(oct(i)[2:]).rjust(spacing, ' '),str(hex(i)[2:].upper()).rjust(spacing, ' '),str(bin(i)[2:]).rjust(spacing, ' '))
        
        
   
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)