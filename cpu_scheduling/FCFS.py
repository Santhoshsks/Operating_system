class processes:
	def __init__(self, pid, at, bt, ct=0):
		self.pid = pid
		self.at = at
		self.bt = bt
		self.ct = ct
		self.tat = 0
		self.wt = 0
		
	def update_data(self):
		self.tat = self.ct-self.at
		self.wt = self.tat-self.bt

	def get(self):
		print(f"{self.pid}\t{self.at}\t{self.bt}\t{self.ct}\t{self.tat}\t{self.wt}")

	def turnaround(self):
		return self.tat

	def waiting(self):
		return self.wt


num = int(input("Enter the Number of Processes:"))
ov = int(input("Over head:"))
l = []

for i in range(num):

	print(f'Process {i+1}')
	at = int(input("Enter the Arrival Time:"))
	bt = int(input("Enter the Burst Time:"))
	l.append(processes(i+1, at, bt))
	print("\n")

q = sorted(l,key = lambda x : x.at)

ct = 0
for p in q:
	if p.at == ct or p.at < ct:
		ct += ov + p.bt
		p.ct = ct
		p.update_data()
		
	else:
		ct = ov + p.at + p.bt
		p.ct = ct
		p.update_data()
	
avg_tat = 0
avg_wat = 0
tot_ov = num * ov
ut = ct - tot_ov
eff = (ut / ct) * 100

print("PID\tAT\tBT\tCT\tTAT\tWT")
for process in l:
	process.get()

for process in l:
	avg_tat += process.turnaround()
	avg_wat += process.waiting()
print(f"Average turnaround:{avg_tat/num}\nAverage Waiting time:{avg_wat/num}\nEfficiency:{eff}%")
