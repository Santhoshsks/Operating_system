
#1st file named as a.py
def fac(num):
	ans = 1
	for i in range(1,num+1):
		ans *= i
	return ans

s = '''import b\nn = int(input("Enter n for b:"))\nprint(fac(n))\nexec(b.s1)'''

if __name__ == "__main__":
	import b
	n = int(input("Enter n for b:"))
	print(fac(n))
	exec(b.s1)

#2nd file named as b.py
def fac(num):
	ans = 1
	for i in range(1,num+1):
		ans *= i
	return ans

s1 = '''import a\nn = int(input("Enter n for a:"))\nprint(fac(n))\nexec(a.s)'''
