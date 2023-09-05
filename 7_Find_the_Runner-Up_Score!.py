if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    maxl = list(set(arr))
    maxl.sort(reverse=True)
    
    run=maxl[1]
    print(run)
    
    