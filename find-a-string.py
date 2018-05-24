def count_substring(string, sub_string):
    a=0
    count=0
    while a<len(string):
        a=string.find(sub_string)
        if a!=-1:
            count+=1
            string=string[a+1:]
        else:break
        
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)