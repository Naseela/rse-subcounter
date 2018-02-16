#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rsg
#
# Created:     16/02/2018
# Copyright:   (c) rsg 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import locationcounter


def test_countrycode():
    assert locationcounter.countrycode("gmail.com")==".com"

def test_codedictionary():
    codeimport = locationcounter.codedictionary()
    assert ".uk" in codeimport
    assert codeimport[".uk"] == "United Kingdom"

test_codedictionary()
def test_comparison():
    assert locationcounter.comparison("york.ac.uk") == "United Kingdom"
