def fac(num):
	ans = 1
	for i in range(1,num+1):
		ans *= i
	return ans

s1 = '''import a\nn = int(input("Enter n for a:"))\nprint(fac(n))\nexec(a.s)'''
