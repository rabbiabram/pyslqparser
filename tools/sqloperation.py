__author__ = 'rabbiabram@gmail.com'


class SQLOperation:
    def __init__(self,operation = None):
        self.name = operation
        self.expressions = []
        self.options = []

    def get_operation_name(self):
        return self.name

    def add_expression(self,expression):
        self.expressions.append(expression)

    def get_expressions(self):
        return self.expressions

    def expressions_to_array(self):
        expr_array = []
        i = 0
        while i < len(self.expressions):
            expr_array.append([ self.expressions[i].getName(), self.expressions[i].getOptions()])
            i = i + 1
        return expr_array

    def add_option(self,option,prevent_expr = None):
        self.options.append([option, prevent_expr])

    def get_pre_expression_option(self):
        k = -1
        if self.options[0][1] == k:
            return self.options[0][0]
        else:
            return ""

    def pre_expression_option_exists(self):
        k = -1
        if len(self.options) > 0:
            return (self.options[0] != None) and (self.options[0][1] == k)
        else:
            return False

    def expression_exists(self,i):
        return (i < len(self.expressions)) and (i >= 0)
