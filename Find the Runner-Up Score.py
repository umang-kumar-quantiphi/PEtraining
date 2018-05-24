if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    max1=max(arr)
    max2=-9999999999
    for x in arr:
        if(x>max1): 
            max1=x
            
        elif(x>max2 and x<max1):max2=x
            
    print max2   
