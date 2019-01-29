# codeforces
n,k=map(int,input().split(" "))
nums=list(map(int,input().split(" ")))
x=nums[k-1]
count=0
if(x==0):
    for i in nums:
        if(i>x):
            count+=1
    print(count)
else:
    for i in nums:
        if(i==0):
            count+=1
    if(count==len(nums)):
        print("0")
    else:
        count=0
        for i in nums:
            if(i>=x):
                count+=1
        print(count)
