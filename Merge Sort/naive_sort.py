#!/usr/bin/env python

def naiveSort(Array):
	i = 0
	for i in range(len(Array)):
		j = i+1
		while (j< len(Array)):
			#Check if the number is lower than A[i]
			if Array[j] < Array[i]:
				temp = Array[i]
				Array[i] = Array[j]
				Array[j] = temp
			j += 1
	
	return Array
