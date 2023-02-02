#lab06.py
from Apartment import Apartment

def ensureSortedAscending(apartmentList):
	if len(apartmentList) == 0:
		return True #Might need to be false
	elif len(apartmentList) == 1:
		return True
	else:
		for i in range(len(apartmentList) - 1):
			if apartmentList[i] > apartmentList[i + 1]:
				return False
		
		return True

def mergesort(apartmentList):
	if len(apartmentList) > 1:
		mid = len(apartmentList) // 2

		lefthalf = apartmentList[:mid]
		righthalf = apartmentList[mid:]

		mergesort(lefthalf)
		mergesort(righthalf)

		i = 0 
		j = 0 
		k = 0 

		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] == righthalf[j] or lefthalf[i] < righthalf[j]:
				apartmentList[k] = lefthalf[i]
				i = i + 1
			else:
				apartmentList[k] = righthalf[j]
				j = j + 1
			k = k + 1
    
		while i < len(lefthalf):
			apartmentList[k] = lefthalf[i]
			i = i + 1
			k = k + 1

		while j < len(righthalf):
			apartmentList[k] = righthalf[j]
			j = j + 1
			k = k + 1

def getBestApartment(apartmentList):
	mergesort(apartmentList)

	return apartmentList[0].getApartmentDetails()

def getWorstApartment(apartmentList):
	mergesort(apartmentList)

	last = len(apartmentList) - 1
	return apartmentList[last].getApartmentDetails()

def getAffordableApartments(apartmentList, budget):
	mergesort(apartmentList)

	temp = ''
	for apt in range(len(apartmentList) - 1):
		if apartmentList[apt].getRent() < budget or apartmentList[apt].getRent() == budget:
			temp += str(apartmentList[apt].getApartmentDetails()) + "\n"
		else:
			return temp[:-1]
