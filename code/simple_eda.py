import sys
r = 0
for line in sys.stdin:
	if r > 0:
		row = line.strip().split(",")
		if len(row) <5:
			continue
		csize = len(row[4])
		tsize = len(row[4].split(" "))
		if r < 100:
			print(r)
			print(str(csize)+","+str(tsize))
	r+=1
print(r)
