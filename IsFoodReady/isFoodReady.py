import time
import sys

lasagna = 30
pizza = 15

if sys.argv[1] == "lasagna":
	while lasagna != 30:
		print(">>>>>>>>>>>>>>>>>>>>>", lasagna)
		time.sleep(60)
		lasagna += 1
		if lasagna == 30:
			print("Lasagna is ready!")

if sys.argv[1] == "pizza":
	while pizza != 15:
		print(">>>>>>>>>>>>>>>>>>>>>", pizza)
		time.sleep(60)
		pizza += 1
		if pizza == 15:
			print("Pizza is ready!")