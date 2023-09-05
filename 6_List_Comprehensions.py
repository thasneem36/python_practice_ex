if __name__ == '__main__':
    x =int(input())
    y =int(input())
    z =int(input())
    n =int(input())
    
    
    permutations = []
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                permutation = [i,j,k]
                total = sum(permutation)             
                if total != n:
                    permutations.append(permutation)
    print(permutations)
    