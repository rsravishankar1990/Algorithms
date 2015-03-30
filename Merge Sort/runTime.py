#!/usr/bin/env python

import merge_sort
import naive_sort
import timeit
import random
import pandas
import pylab

if __name__ == "__main__":
	#Create an array of different times for O(n2) and O(nlogn)
	j = 1000
	nSortTime = []
	mSortTime = []
	sortAmount = []
	while j< 20000:
		print "The value of j is :\t" + str(j)
		sortAmount.append(j)
		number = [] #The list used for sorting
		for i in range(j):
			number.append(random.random() * j)
			
		#Clock the naive sort 
		nSortStart = timeit.default_timer()
		result = naive_sort.naiveSort(number)
		nSortStop = timeit.default_timer()
		nTime = float(nSortStop) - float(nSortStart)
		nSortTime.append(nTime)
		
		#Clock the merge sort
		mSortStart = timeit.default_timer()
		result = merge_sort.msort(number)
		mSortStop = timeit.default_timer()
		mTime = float(mSortStop) - float(mSortStart)
		mSortTime.append(mTime)
		
		#Increment j
		j = j + 1000

	timeDict = {'n':sortAmount, 'mergeTime':mSortTime, 'naiveTime':nSortTime}
	timeDF = pandas.DataFrame(timeDict)
	print "Output Ready:\n"
	print timeDF
	
	pylab.scatter(sortAmount,mSortTime, color = 'k')
	pylab.scatter(sortAmount,nSortTime, color='g')
	pylab.show()
