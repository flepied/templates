#---------------------------------------------------------------
# Project         : @APPLICATION@
# File            : @FILE_NAME@
# Copyright       : (C) @YEAR@ by 
# Author          : @USER_FULL_NAME@
# Created On      : @CURRENT_TIME@
# Purpose         : 
#---------------------------------------------------------------

import unittest

import @BASEFILENAME_WITHOUT_TEST@

class @CAMELIZED_FILE_NAME@Test(unittest.TestCase):
    
    def test_@DOT@(self):
        return self.assert_(False)

if __name__ == "__main__":
    unittest.main()
                                        
# @FILE_NAME@ ends here
