#!/usr/bin/env python3
import aocd


def main():
	# read file
	f = open("day1.txt", "r")
	for ln in f:
		if ln == "":
			print(repr("emptyline!"))
		else:
			print(repr(ln))

if __name__ == "__main__":
	main()