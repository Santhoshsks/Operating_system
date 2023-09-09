while True:
	import os
	cmd=input("Enter command (exit to leave): ")
	print()
	try:
		if cmd!='exit':
			exec('os.system(cmd)')
		else:
			break
	except:
		print("Wrong command!")
