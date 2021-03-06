from classObj import ClassObj
import re

#Requirements for one class from a list of classes
class OrReq:
    def __init__(self, classSet):
        self.classes = classSet

    def isSatisfied(self, classList):
        for c in classList:
            if (c.getComboTitle() in self.classes):
                return True

        return False

    def __repr__(self):
        return f'<Req: Type = {type(self)}, Classes = {self.classes}>'

#Requirements for a list of classes where all are needed
class AndReq:
    def __init__(self, classSet):
        self.classes = classSet

    def isSatisfied(self, classList):

        classComboTitles = set()

        for c in classList:
           classComboTitles.add(c.getComboTitle())

        for cl in self.classes:
            if not (cl in classComboTitles):
                return False

        return True

    def __repr__(self):
        return f'<Req: Type = {type(self)}, Classes = {self.classes}>'

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

    def __repr__(self):
        return f'<Req: Type = {type(self)}, Classes = {self.classes}, Num = {self.num}>'

#Requirements for things like "Five or more COMP classes numbered above 420 and three or more credit hours
class AboveNumReq:
    def __init__(self, subject, num, creds, minNum, minCreds, exclusions):
        self.subject = subject
        self.num = num
        self.creds = creds
        self.minNum = minNum
        self.minCreds = minCreds
        self.exclusions = exclusions

    def isSatisfied(self, classList):

        counter = 0
        credits = 0.0

        for c in classList:

            if (c.subAbb in self.subject) and (int(re.sub('\D','', c.number)) >= self.minNum) and (c.minCredits > self.minCreds) and not (c.getComboTitle() in self.exclusions):
                counter = counter + 1
                credits = credits + c.minCredits

        if (counter >= self.num) and (credits >= self.creds):
            return True
        else:
            return False

    def __repr__(self):
        return f'<Req: Type = {type(self)}, Subject = {self.subject}, Num = {self.num}, Creds = {self.creds}, MinNum = {self.minNum}, MinCreds = {self.minCreds}, Exclusions = {self.exclusions}>'

class MultiOrReq:
    def __init__(self, num, reqs):
        self.requirementList = []
        self.num = num
        for r in reqs:
            if isinstance(r, str):
                self.requirementList.append(AndReq({r}))
            else:
                self.requirementList.append(r)

    def isSatisfied(self, classList):

        counter = 0

        for r in self.requirementList:
            if r.isSatisfied(classList):
                counter = counter + 1

        if counter >= self.num:
            return True
        else:
            return False

    def __repr__(self):
        return f'<Req: Type = {type(self)}, Num = {self.num}, Reqs = {self.requirementList}>'


#Upper-level container for lower-level requirements
class ReqList:
    def __init__(self,reqs):
        self.requirementList = []
        for r in reqs:
            if isinstance(r, str):
                self.requirementList.append(AndReq({r}))
            else:
                self.requirementList.append(r)

    def printReqs(self):
        for r in self.requirementList:
            print(r.classes)

    def __repr__(self):
        return  f'<Req: Type = {type(self)}, Reqs = {self.requirementList}>'
