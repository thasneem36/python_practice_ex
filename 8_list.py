if __name__ == '__main__':
    N = int(input()) #loop times
    data = [] #store the list
    
    #              0*       1*      2*       3*      4*     5       6
    list_add = ['insert','print','remove','append','sort','pop','reverse']
        
    for i in range(N):
        add = input().split()
        
        #type print show the data
        if add [0] == list_add[1]:
            print(data)
        
        #type append 
        elif add [0] == list_add[3]:
            data.append(int( add[1] ))
            
        #type insert
        elif add[0] == list_add[0]:
            data.insert( int( add[1]) , int( add[2]) )

        #type remove
        elif add[0] == list_add[2]:
            data.remove( int( add[1] ) )
            
        #type sort
        elif add[0] == list_add[4]:
            data.sort()

        #type pop
        elif add[0] == list_add[5]:
            data.pop()
            
        #type revers
        elif add[0] == list_add[6]:
            data.reverse()
            