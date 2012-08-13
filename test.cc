//===========================================================================
// Project         : @APPLICATION@
// File            : @FILE_NAME@
// Copyright       : (C) @YEAR@ by 
// Author          : @USER_FULL_NAME@
// Created On      : @CURRENT_TIME@
// Purpose         : 
//===========================================================================

static const char rcs_id[] = "@VERSION_STRING@";
static const char compile_id[] = "$Compile: " __FILE__ " " __DATE__ " " __TIME__ " $";

#include <CppUTest/TestHarness.h>
#include <CppUTest/CommandLineTestRunner.h>
#include <CppUTestExt/MockSupport.h>

extern "C" {
#include "@BASEFILENAME_WITHOUT_TEST@.h"
}

TEST_GROUP(@CAMELIZED_FILE_NAME@Group)
{
  void setup() {
  }
  void teardown() {
  }
};

TEST(@CAMELIZED_FILE_NAME@Group, FirstTest)
{
  @DOT@FAIL("Fail me!");
}

int
main(int ac, char** av)
{
  return CommandLineTestRunner::RunAllTests(ac, av);
}

//
// Local variables:
// mode: c++
// End:
//
// @FILE_NAME@ ends here
//
