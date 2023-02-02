#Apartment.py

class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}" \
        .format(self.rent, self.metersFromUCSB, self.condition)

    #1. Rent price, lower is better
    #2. Distance from UCSB, lower is better
    #3. Condition (bad, avg., or excellent)
    def __gt__(self, rhs): #apt1 > apt2 returns True if apt1 is worse 
        if self.getRent() == rhs.getRent():
            if self.getMetersFromUCSB() == rhs.getMetersFromUCSB():
                if self.getCondition() == rhs.getCondition():
                    return False #Might need to return False/True
                else:
                    if self.getCondition() == "excellent": 
                        return False
                    elif rhs.getCondition() == "excellent":
                        return True
                    elif self.getCondition() == "average":
                        return False
                    else:
                        return True
            else:
                if self.getMetersFromUCSB() > rhs.getMetersFromUCSB():
                    return True
                else:
                    return False
        else:
            if self.getRent() > rhs.getRent():
                return True
            else:
                return False

    def __lt__(self, rhs): #apt1 < apt2 returns True if apt1 is better
        if self.getRent() == rhs.getRent():
            if self.getMetersFromUCSB() == rhs.getMetersFromUCSB():
                if self.getCondition() == rhs.getCondition():
                    return False #Might need to return False
                else:
                    if self.getCondition() == "excellent":
                        return True
                    elif rhs.getCondition() == "excellent":
                        return False
                    elif self.getCondition() == "average":
                        return True
                    else:
                        return False
            else:
                if self.getMetersFromUCSB() < rhs.getMetersFromUCSB():
                    return True
                else:
                    return False
        else:
            if self.getRent() < rhs.getRent():
                return True
            else:
                return False

    def __eq__(self, rhs):
        if self.getRent()== rhs.getRent():
            if self.getMetersFromUCSB() == rhs.getMetersFromUCSB():
                if self.getCondition() == rhs.getCondition():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
