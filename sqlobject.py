


from tools.sqlexpression import sqlexpression
from tools.sqloperation import sqloperation
        
                

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
                



        
