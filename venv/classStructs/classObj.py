class ClassObj:
    def __init__(self):
        self.subAbb = 'AAAA'
        self.number = '000'
        self.title = 'Class Title'
        self.minCredits = 0.0
        self.maxCredits = 0.0
        self.hasCreditRange = False
        self.genEds = []



    def setSubAbb(self, str):
        self.subAbb = str

    def setNumber(self, n):
        self.number = n

    def setTitle(self, str):
        self.title = str

    def setCredits(self, minCreds, maxCreds):
        if(minCreds == maxCreds):
            self.hasCreditRange = False
            self.minCredits = minCreds
            self.maxCredits = maxCreds

        if(minCreds != maxCreds):
            self.hasCreditRange = True
            self.minCredits = minCreds
            self.maxCredits = maxCreds

    def setGenEds(self, ge):
        self.genEds = ge

    def getComboTitle(self):
        return f'{self.subAbb}{self.number}'

    def __str__(self):
        return f'{self.subAbb} {self.number} {self.title} {self.minCredits} {self.maxCredits} \n {self.hasCreditRange} \n {self.genEds}'