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
        
                

class sqlobject:
    OPERATIONS = ['SELECT','INSERT','UPDATE','DELETE']
    EXPRESSIONS = ['FROM', 'WHERE','INTO','VALUE','VALUES']
    def __init__(self,query = None):
        self.query = query
        self.operations_list = []
        self.operand = None
        self.options = []

    def optionExists(self,i):
        return True

    def getExpressions(self,i):
        return self.operations_list[i].getExpressions()
    def expressionExists(self, operation_number, expression_number):
        self.operations_list[operation_number].expressionExists(expression_number)
            
        

    def parse(self):
        subqueries = self.query.split(" ")
        i = 0
        op_flag = 0
        exp_flag = 0
        j = -1
        k = -1
        while i < len(subqueries):
            if subqueries[i] in self.OPERATIONS:
                self.operations_list.append(sqloperation(subqueries[i]))
                op_flag = 1
                j = j + 1
            elif ((subqueries[i] in self.EXPRESSIONS)):
                self.operations_list[j].addExpression(sqlexpression(subqueries[i]))
                k = k + 1
                exp_flag = 1
            elif (exp_flag == 1):
                self.operations_list[j].expressions[k].addOption(subqueries[i])
            else:
                self.operations_list[j].addOption(subqueries[i],k)
                exp_flag = 0
                op_flag = 0
            i = i + 1
    def toQuery(self):
        i = 0
        k = -1
        query = ""
        while i < len(self.operations_list):
            query = query + self.operations_list[i].getOperationName()
            if self.operations_list[i].preExpressionOptionExists():
                query = query + " " + self.operations_list[i].getPreExpressionOption()
            expressions = self.getExpressions(i)
            #return expressions
            j = 0
            while j < len(expressions):
                options = expressions[j].getOptions()
                options = " ".join(options)
                expr_name = expressions[j].getName()
                query = query + " " + expr_name + " " + options
                j = j + 1
    
            i = i + 1
                    
        return query
                



        
