import fileinput
import shlex
for eachline in fileinput.input():
    l = shlex.split(eachline)
    microtime = l.pop(4)
    l[3] = " ".join((l[3], microtime))
    print l
