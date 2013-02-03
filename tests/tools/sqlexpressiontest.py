__author__ = 'rabbiabram@gmail.com'

import unittest
from tools.sqlexpression import sqlexpression

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.sqlexptession1 = sqlexpression()
        self.sqlexptession2 = sqlexpression()
    def test_something(self):
        self.assertEqual(True, True)
    def test_constract(self):
        self.assertEqual(self.sqlexptession1.name,self.sqlexptession2.name)
        newexpression = sqlexpression('SELECT')
        self.assertNotEqual(self.sqlexptession1.name,newexpression.name)
    def test_addOption(self):
        self.sqlexptession1.addOption('*')
        self.assertNotEqual(self.sqlexptession1.options, self.sqlexptession2.options)
        self.sqlexptession2.addOption('*')
        self.assertEqual(self.sqlexptession1.options, self.sqlexptession2.options)
    def test_optionsToString(self):
        testString = '* tablename'
        self.assertNotEqual(testString,self.sqlexptession1.optionsToString())
        self.sqlexptession1.addOption('*')
        self.sqlexptession1.addOption('tablename')
        self.assertEqual(testString, self.sqlexptession1.optionsToString())
        self.sqlexptession1.addOption('fail')
        self.assertNotEqual(testString, self.sqlexptession1.optionsToString())
    def test_getName(self):
        name = 'Test'
        self.sqlexptession1.name = name
        self.assertEqual(self.sqlexptession1.getName(), name)
        self.assertNotEqual(self.sqlexptession2.getName(), name)

if __name__ == '__main__':
    unittest.main()
