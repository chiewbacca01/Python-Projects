from itertools import count
import math
import random
lst = []
while True:
	line = input("Enter a number: ")
	if line == "done":
		break
	else:
		ele = int(line)
		lst.append(ele)
print(sum(lst), end=" ")
print(len(lst), end=" ")
print(sum(lst)/len(lst), end=" ")