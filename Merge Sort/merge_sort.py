#!/usr/bin/env python


def mmerge(list1, list2):
	#Merge step of the sort procedure
	lenArray = len(list1) + len(list2)
	i = 0
	j = 0
	c = []
	for k in range(lenArray):
		if i < len(list1) and j < len(list2):
			if(list1[i] <= list2[j]):
				c.append(list1[i])
				i = i+1
			elif(list1[i] > list2[j]):
				c.append(list2[j])
				j = j+1
		if i < len(list1) and j == len(list2):
			c.append(list1[i])
			i = i+1
		elif j < len(list2) and i == len(list1):
			c.append(list2[j])
			j = j+1	
	return c
	

def msort(array):
	#The recursive sort function 
	if len(array) <= 1:
		#Base condition: return the number if the length is 1
		return array
		
	elif len(array) >= 2:
		#Recursive condition: Split the list by 2 and send it recursively
		split1 = array[:len(array)/2]
		split2 = array[len(array)/2:]
		
		#Pass it in recursion
		result1 = msort(split1)
		result2 = msort(split2)
		
		#Merge the obtained results
		resultArray = mmerge(result1,result2)
		return resultArray
		
	
