__author__ = 'rabbiabram@gmail.com'

class SQLExpression:
    def __init__(self,expression = None):
        self.name = expression
        self.options = []
        self.raw_expression = ''
        self.OPERATION_TYPES = ['SELECT', 'USE', 'CREATE', 'DELETE', 'INSERT', 'UPDATE']

    def set_raw_expression(self, raw_expression):
        self.raw_expression = raw_expression

    def get_raw_expression(self):
        return self.raw_expression

    def parse(self):
        return True