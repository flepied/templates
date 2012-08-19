#---------------------------------------------------------------
# Project         : @APPLICATION@
# File            : @FILE_NAME@
# Copyright       : (C) @YEAR@ by 
# Author          : @USER_FULL_NAME@
# Created On      : @CURRENT_TIME@
# Purpose         : 
#---------------------------------------------------------------

class @BASEFILENAME_WITHOUT_EXT@:
    def __init__(self):
        @DOT@

if __name__ == "__main__":
    import unittest
    
    class @BASEFILENAME_WITHOUT_EXT@Test(unittest.TestCase):
    
        def test1(self):
            return self.assert_(False)
    
    unittest.main()
                                        
# @FILE_NAME@ ends here
