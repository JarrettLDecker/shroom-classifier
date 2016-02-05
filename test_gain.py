#!/usr/bin/env python
#
# filename: test_gain.py
# authors:  Jon David and Jarett Decker
# date:     Thursday, February 4, 2016
#

from j2d2_datadef import ShroomDefs
from j2d2_database import ShroomDatabase
from j2d2_id3 import *

deffilename = "_shroom.data.definition"
trainfilename = "./data/training.dat"

print "\n"
print "definition file: ", deffilename
print "training set: ", trainfilename

mydefs = ShroomDefs(deffilename)
mydb = ShroomDatabase(trainfilename)
        
gain_table = calc_all_gain(mydb, mydefs)
print "\nGain table:"
print "==========================="
for attr in gain_table:
    gain = gain_table[attr]
    print attr, ": ", gain

rmend_attr, gain = recommend_next_attr(gain_table)
print "\nRecommend: ", rmend_attr, ", ", gain
