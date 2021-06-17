from classObj import ClassObj

#Requirements for one class from a list of classes
class OrReq:
    def __init__(self, classSet):
        self.classes = classSet

    def isSatisfied(self, classList):
        for c in classList:
            if (c.getComboTitle() in self.classes):
                return True

        return False

#Requirements for a list of classes where all are needed
class AndReq:
    def __init__(self, classSet):
        self.classes = classSet
        print(self.classes)

    def isSatisfied(self, classList):

        classComboTitles = set()

        for c in classList:
           classComboTitles.add(c.getComboTitle())

        for cl in self.classes:
            if not (cl in classComboTitles):
                return False

        return True

#Requrements for a certain number of classes from a list
class NumReq:
    def __init__(self, classSet, number):
        self.classes = classSet
        self.num = number

    def isSatisfied(self, classList):

        counter = 0

        for c in classList:
            if (c.getComboTitle() in self.classes):
                counter = counter+1

        if (counter >= self.num):
            return True
        else:
            return False