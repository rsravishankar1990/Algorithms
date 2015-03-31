#!/usr/bin/env python

def splitDistance(pointList):
	#O(n) implementation of the distance finding
	i = 0
	minDist = 10000000000
	minPoints = [(0,0),(0,0),1000000]
	while(i <= len(pointList)-1):
		#Run a loop to go through the next 7 points or the end of the list
		j = i+1
		jend = min(j+7, len(pointList))
		while(j<jend):
			distance = euclidDist(pointList[i],pointList[j])
			if distance <= minDist:
				minDist = distance
				minPoints[0] = pointList[i]
				minPoints[1] = pointList[j]
				minPoints[2] = minDist
			j += 1
		i +=1
	return minPoints	

def euclidDist(point1, point2):
	#Calculate the euclidean distance for two points
	distance = pow((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2, 0.5)
	return distance

def bruteForce(pointList):
	#Brute force for finding distance
	minDist = 10000000000
	minPoints = [(0,0),(0,0),1000000]
	for i in range(len(pointList)-1):
		j = i + 1
		while (j < len(pointList)):
			#Go through the entire list of points and calculate the min dist
			distance = euclidDist(pointList[i],pointList[j])
			if distance <= minDist:
				minDist = distance
				minPoints[0] = pointList[i]
				minPoints[1] = pointList[j]
				minPoints[2] = minDist
			j += 1
	return minPoints	
	
def msort(pointList,index):
	#mergeSort routine for sorting the points based on x-coordinates
	#The recursive sort function 
	if len(pointList) <= 1:
		#Base condition: return the number if the length is 1
		return pointList
		
	elif len(pointList) >= 2:
		#Recursive condition: Split the list by 2 and send it recursively
		split1 = pointList[:len(pointList)/2]
		split2 = pointList[len(pointList)/2:]
		
		#Pass it in recursion
		result1 = msort(split1,index)
		result2 = msort(split2,index)
		
		#Merge the obtained results
		resultArray = mmerge(result1,result2,index)
		return resultArray
		

def mmerge(list1, list2, index):
	#Merge step of the sort procedure
	lenArray = len(list1) + len(list2)
	i = 0
	j = 0
	c = []
	for k in range(lenArray):
		if i < len(list1) and j < len(list2):
			if(list1[i][index] <= list2[j][index]):
				c.append(list1[i])
				i = i+1
			elif(list1[i][index] > list2[j][index]):
				c.append(list2[j])
				j = j+1
		if i < len(list1) and j == len(list2):
			c.append(list1[i])
			i = i+1
		elif j < len(list2) and i == len(list1):
			c.append(list2[j])
			j = j+1	
	return c
	
def closestDistance(pointXList,pointYList):
	#Get the list of points whose distance is to be found out:
	#Once the points have been found, split until the list of points is 3 and find the distance
	if len(pointXList) <= 3:
		#Code for using brute force to find the distance
		points = bruteForce(pointXList)
		return points
	
	elif len(pointXList) > 3:
		#Code for recursion:
		mid = len(pointXList)/2
		pointLeft = pointXList[:mid]
		pointRight = pointXList[mid:]
		
		pointYLeft = []
		pointYRight = []
		for point in pointYList:
			#Find the sorted y points on the left side and right side
			if point[0] <= pointXList[mid-1][0]:
				pointYLeft.append(point)
			elif point[0] > pointXList[mid-1][0]:
				pointYRight.append(point)
				
		
		distLeft = closestDistance(pointLeft,pointYLeft)
		distRight = closestDistance(pointRight,pointYRight)
		
		#Find the minimum distance from left and right points
		if distLeft[2] <= distRight[2]:
			minDist = distLeft[2]
			minPoint = distLeft
		else:
			minDist = distRight[2]
			minPoint = distRight
		
		#Conquer phase for the same 
		#find the strip distance 
		midDist = pointXList[mid-1][0]
		stripLeft = midDist - minDist
		stripRight = midDist + minDist
		strip = []
		for point in pointYList:
			if point[0] >= stripLeft and point[0] <= stripRight:
				strip.append(point)
				
		splitPoint = splitDistance(strip)
		
		#Return the closest points
		if splitPoint[2] < minDist:
			return splitPoint
		else:
			return minPoint
		
		
	
