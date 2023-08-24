'''
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.
'''

# 1st way
n=int(input("Enter an integer: "))

if (n%2) !=0:
    print("Weird")
elif n%2 == 0:
    if 2<= n <=5:
        print("Not Weird")
    elif 6<= n <=20:
        print("Weird")
    elif n>20:
        print("Not Weird")
        
# 2nd way
n = int(input("Enter an integer: ")) 

if n % 2 != 0: 
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5: 
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:  
    print("Not Weird")
