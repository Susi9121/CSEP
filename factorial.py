#Factorial  of a number
def recur_factorial(n):
	if n==1:
		return n
	else:
		return n*recur_factorial(n-1)
n=7
if n<0:
	print("factorial doesn't exist")
elif n==0:
	print("the factorial of 0 is 1")
else:
	print("the factorial of",n,"is",recur_factorial(n)) 
