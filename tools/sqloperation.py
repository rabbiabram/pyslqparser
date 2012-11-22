__author__ = 'rabbiabram@gmail.com'


class sqloperation:
    def __init__(self,operation = None):
        self.name = operation
        self.expressions = []
        self.options = []
    def getOperationName(self):
        return self.name
    def addExpression(self,expression):
        self.expressions.append(expression)
    def getExpressions(self):
        return self.expressions
    def expressionsToArray(self):
        expr_array = []
        i = 0
        while i < len(self.expressions):
            expr_array.append([ self.expressions[i].getName(), self.expressions[i].getOptions()])
            i = i + 1
        return expr_array
    def addOption(self,option,prevent_expr = None):
        self.options.append([option, prevent_expr])
    def getPreExpressionOption(self):
        k = -1
        if self.options[0][1] == k:
            return self.options[0][0]
        else:
            return ""
    def preExpressionOptionExists(self):
        k = -1
        if len(self.options) > 0:
            return (self.options[0] != None) and (self.options[0][1] == k)
        else:
            return False
    def expressionExists(self,i):
        return (i < len(self.expressions)) and (i >= 0)
