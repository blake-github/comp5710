import unittest
import source 


class TestCalc(unittest.TestCase):
    def testSub1(self):
        self.assertEqual(1, source.performSub(2, 1), "Bug in implementation. Results should be 1.")    

    def testSub2(self):
        self.assertEqual(10, source.performSub(20, 10), "Bug in implementation. Results should be 1.")
        
    def testSub3(self):
        self.assertEqual(-2, source.performSub(4, 6), "Bug in implementation. Results should be -2.")      
        
    def testMult1(self):
        self.assertEqual(10, source.performMult(5, 2), "Bug in implementation. Results should be 10.")
        
    def testMult2(self):
        self.assertEqual(0, source.performMult(5, 0), "Bug in implementation. Results should be 0.")
        
    def testMult3(self):
        self.assertEqual(-1, source.performMult(1, -1), "Bug in implementation. Results should be -1.")
        
    def testMult4(self):
        self.assertEqual(48, source.performMult(-12, -4), "Bug in implementation. Results should be 48.")
    
    def testDiv1(self):
        self.assertEqual("Divide by zero error", source.performDiv(5, 0), "Bug in implementation. Results should be an error.")
        
    def testDiv2(self):
        self.assertEqual(0, source.performDiv(0, 2), "Bug in implementation. Results should be 0.")
        
    def testDiv3(self):
        self.assertEqual(5, source.performDiv(45, 9), "Bug in implementation. Results should be 5.")
        
    def testDiv3(self):
        self.assertEqual(-1, source.performDiv(-1, 1), "Bug in implementation. Results should be -1.")
    
    def testDiv4(self):
        self.assertEqual(4, source.performDiv(-16, -4), "Bug in implementation. Results should be 4.")


if __name__ == '__main__': 
    unittest.main() 