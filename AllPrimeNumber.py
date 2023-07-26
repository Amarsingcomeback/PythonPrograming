# Problem: All Prime Number
# Statement: 
# you are given an interger N. You need to print the series of all prime numbers till N.
# input:
# the first and only line of the input contains a single interger N denoting the number till where you 
# need to find the series of prime number.
# Output:
# print the desired Output in single line separated by spaces.
# test case    input    Output
# test1        9        2357

# solution
n= int(input())
i=2
while (i<=n):
	flag=0
	for var in range(2,i):
		if(i%var==0):
		flag=1
		break
	if(flag==0):
		print(i,end=" ")
	i=i+1