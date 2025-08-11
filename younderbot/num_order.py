n=int(input("Enter the value: "))
num=list(range(1,n+1))

miss_value=5
num.remove(miss_value)
print("list with missed num: ",num)

total_sum=n*(n+1)//2
list_sum=sum(num)
missing=total_sum-list_sum
print("Missing number is: ",missing)