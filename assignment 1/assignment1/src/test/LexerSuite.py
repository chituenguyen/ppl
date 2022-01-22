import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    def test_mixed_id(self):
        self.assertTrue(TestLexer.test("aAsVN3","aAsVN,3,<EOF>",103))
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("123a123","123,a,123,<EOF>",104))
    def test_decimal(self):
        """test integers"""
        self.assertTrue(TestLexer.test("1_234","1234,<EOF>",105))
    def test_octal(self):
        self.assertTrue(TestLexer.test("012_3","0123,<EOF>",106))
    def test_hex(self):
        self.assertTrue(TestLexer.test("0x1_A","0x1A,<EOF>",107))
    def test_binary(self):
        self.assertTrue(TestLexer.test("0b11111","0b11111,<EOF>",108))
    def test_float_1(self):
        self.assertTrue(TestLexer.test("1.234","1.234,<EOF>",109))
    def test_float_2(self):
        self.assertTrue(TestLexer.test(".023E-1",".023E-1,<EOF>",110))
    def test_float_3(self):
        self.assertTrue(TestLexer.test("7E-10","7E-10,<EOF>",111))
    def test_float_4(self):
        self.assertTrue(TestLexer.test("1_234.567","1234.567,<EOF>",112))
    def test_boolean(self):
        self.assertTrue(TestLexer.test("False","False,<EOF>",113))
    def test_boolean(self):
        self.assertTrue(TestLexer.test("This is a string containing tab \t","This is a string containing tab,<EOF>",114))
    
        