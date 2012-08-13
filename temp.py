#---------------------------------------------------------------
# Project         : @APPLICATION@
# File            : @FILE_NAME@
# Copyright       : (C) @YEAR@ by 
# Author          : @USER_FULL_NAME@
# Created On      : @CURRENT_TIME@
# Purpose         : 
#---------------------------------------------------------------

class @CAMELIZED_FILE_NAME@:
    def __init__(self):
        @DOT@

if __name__ == "__main__":
    import unittest
    
    class @CAMELIZED_FILE_NAME@Test(unittest.TestCase):
    
        def test_(self):
            return self.assert_(False)
    
    unittest.main()
    
# @FILE_NAME@ ends here
