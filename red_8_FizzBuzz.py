

def fizzBuzz(n):
    # Write your code here
    
    for i in range(1,n+1):
        i3 = i+3
        if i == n:
            print('FizzBuzz')
        elif i in [3,6,9,12,15]:
            print('Fizz')
        elif i in [5,10,15]:
            print('Buzz')
        else:
            print(i)
            
        
    

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
