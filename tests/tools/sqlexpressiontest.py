__author__ = 'rabbiabram@gmail.com'

import unittest
from tools.sqlexpression import SQLExpression

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.sql_expression_1 = SQLExpression()
        self.sql_expression_2 = SQLExpression()

if __name__ == '__main__':
    unittest.main()
