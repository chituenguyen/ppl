import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    # def test_mixed_id(self):
    #     self.assertTrue(TestLexer.test("aAsVN3","aAsVN3,<EOF>",103))
    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.test("123a123","123,a,123,<EOF>",104))
    def test_decimal(self):
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
    def test_14(self):
        self.assertTrue(TestLexer.test("\"ahihi xin chao\"","ahihi xin chao,<EOF>",114))
    def test_15(self):
        self.assertTrue(TestLexer.test("0","0,<EOF>",115))
    def test_16 (self):
        self.assertTrue(TestLexer.test("0x342_42_53_5353","0x34242535353,<EOF>",116))
    def test_17(self):
        self.assertTrue(TestLexer.test("1.20043242","1.20043242,<EOF>",117))
    def test_18(self):
        self.assertTrue(TestLexer.test("1.0000000","1.0000000,<EOF>",118))
    def test_19(self):
        self.assertTrue(TestLexer.test("0.","0.,<EOF>",119))
    def test_20(self):
        self.assertTrue(TestLexer.test(".0e32",".0e32,<EOF>",120))
    def test_21(self):
        self.assertTrue(TestLexer.test(".e+32",".e+32,<EOF>",121))
    def test_22(self):
        self.assertTrue(TestLexer.test(".58439538e+32",".58439538e+32,<EOF>",122))
    def test_23(self):
        self.assertTrue(TestLexer.test("12_434_43.58439538e+32","1243443.58439538e+32,<EOF>",123))
    def test_24(self):
        self.assertTrue(TestLexer.test("True","True,<EOF>",124))
    def test_25(self):
        self.assertTrue(TestLexer.test("False","False,<EOF>",125))
    def test_26(self):
        self.assertTrue(TestLexer.test('Array(1,2)','Array(1,2),<EOF>',126))
    # def test_26(self):
    #     self.assertTrue(TestLexer.test('Array(1, 2, 4)','Array(1,2,4),<EOF>',127))