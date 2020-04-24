m, n = map(int, input().split(" "))
L =list(map(int,input().split(" ")))
for i in range(n):
	t = int(input())
	while True:
		if t in L:
 			t=t+1
		else:
			print(t)
			break