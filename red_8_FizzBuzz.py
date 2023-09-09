
# def fizzBuzz(n):
#     # Write your code here
    
#     data3 = []
#     data5 = []
#     for i in range(n):
#         i3 = i*3
#         data3.append(i3)
#         i5 = i*5
#         data5.append(i5)
    
#     for i in range(1, n+1):
        
#         if i in data3:
#             print(f'{i} Fizz')
#         elif i in data5:
#             print(f'{i} Buzz')
#         else:
#             print(i)
    

# if __name__ == '__main__':
#     n = 15 #int(input().strip())

#     fizzBuzz(n)

def fizzBuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(f'{i} FizzBuzz')
        elif i % 3 == 0:
            print(f'{i} Fizz')
        elif i % 5 == 0:
            print(f'{i} Buzz')
        else:
            print(i)

if __name__ == '__main__':
    n = int(input()).strip()

    fizzBuzz(n)

