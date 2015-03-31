#!/usr/bin/env python

def euclidDist(point1, point2):
	#Calculate the euclidean distance for two points
	distance = pow((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2, 0.5)
	return distance

def naiveClosest(pointList):
	length = len(pointList)
	i = 0
	minDist = 10000000000
	minPoints = [(0,0),(0,0),100000000]
	while(i<length-1):
		j = 0
		while(j<length):
			if (i != j):
				distance = euclidDist(pointList[i],pointList[j])
				if distance <= minDist:
					minDist = distance
					minPoints[0] = pointList[i]
					minPoints[1] = pointList[j]
					minPoints[2] = minDist
			j+=1
		i +=1
	return minPoints
