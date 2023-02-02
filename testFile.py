#testFile.py
from Apartment import Apartment
from lab06 import ensureSortedAscending, mergesort, getBestApartment, getWorstApartment, getAffordableApartments

def test_Apartment():
    a0 = Apartment(1599, 800, "average")
    a1 = Apartment(1599, 800, "average")
    a2 = Apartment(7000, 600, "excellent")

    assert a1.getRent() == 1599
    assert a2.getMetersFromUCSB() == 600
    assert a0.getCondition() == "average"

    assert a0.getApartmentDetails() == "(Apartment) Rent: $1599, Distance From UCSB: 800m, Condition: average"

    assert (a0 == a1) == True
    assert (a0 == a2) == False
    assert (a2 > a0) == True
    assert (a0 > a2) == False
    assert (a2 < a0) == False
    assert (a0 < a2) == True

def test_ensureSortedAscending():
    a0 = Apartment(2200, 150, "average")
    a1 = Apartment(1350, 230, "bad")
    a2 = Apartment(1230, 205, "average")
    a3 = Apartment(1230, 300, "excellent")
    a4 = Apartment(700, 500, "bad")
    a5 = Apartment(500, 600, "average")

    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert ensureSortedAscending(apartmentList) == False
    
    apartmentList = [a5, a4, a2, a3, a1, a0]
    assert ensureSortedAscending(apartmentList) == True

    apartmentList = [a5, a4, a3, a2, a0, a1]
    assert ensureSortedAscending(apartmentList) == False

def test_mergeSort():
    a0 = Apartment(2200, 150, "average")
    a1 = Apartment(1350, 230, "bad")
    a2 = Apartment(1230, 205, "average")
    a3 = Apartment(1230, 300, "excellent")
    a4 = Apartment(700, 500, "bad")
    a5 = Apartment(500, 600, "average")

    apartmentList = [a5, a0, a4, a2, a3, a1]
    assert ensureSortedAscending(apartmentList) == False

    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True

def test_getApts():
    a0 = Apartment(2200, 150, "average")
    a1 = Apartment(1350, 230, "bad")
    a2 = Apartment(1230, 205, "average")
    a3 = Apartment(1230, 300, "excellent")
    a4 = Apartment(700, 500, "bad")
    a5 = Apartment(500, 600, "average")

    apartmentList = [a5, a0, a4, a2, a3, a1]

    assert getBestApartment(apartmentList) == "(Apartment) Rent: $500, Distance From UCSB: 600m, Condition: average"
    assert getWorstApartment(apartmentList) == "(Apartment) Rent: $2200, Distance From UCSB: 150m, Condition: average"

    assert getAffordableApartments(apartmentList, 0) == ""
    assert getAffordableApartments(apartmentList, 700) == "(Apartment) Rent: $500, Distance From UCSB: 600m, Condition: average\n" \
    "(Apartment) Rent: $700, Distance From UCSB: 500m, Condition: bad"
    