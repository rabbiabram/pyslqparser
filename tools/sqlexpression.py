__author__ = 'абрам'

class sqlexpression:
    def __init__(self,expression = None):
        self.name = expression
        self.options = []
    def addOption(self,option):
        self.options.append(option)
    def getName(self):
        return self.name
    def getOptions(self):
        return self.options
    def optionsToString(self):
        " ".join(self.options)