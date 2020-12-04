# Day 1 part 2 solution in nim
# Output :
# answer : 203481432
# time   : 41 milliseconds and 505 microseconds

import lists
import sequtils
import strutils
import times

var start = now()
var expenses = initSinglyLinkedList[int]()

for line in "01.txt".lines:
    expenses.append(parseInt(line))
let expe = toSeq(expenses)
for ii,i in pairs(expe):
    for jj, j in pairs(expe[ii .. ^1]):
        for k in expe[ii+jj .. ^1]:
            if i + j + k == 2020:
                echo "answer : ", i*j*k
                echo "time   : ", now() - start