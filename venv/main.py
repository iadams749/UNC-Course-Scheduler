from classObj import *
from reqStructs import *

classesTaken = set()

joey = ClassObj()
joey.setSubAbb('ASTR')
joey.setNumber('101')

jay = ClassObj()
jay.setSubAbb('COMP')
jay.setNumber('210')

thomas = ClassObj()
thomas.setSubAbb('MATH')
thomas.setNumber('347')

classesTaken.add(joey)
classesTaken.add(jay)
classesTaken.add(thomas)

reqClasses = {'ASTR101','MATH347','RELI109'}
nick = NumReq(reqClasses,2)

print(nick.isSatisfied(classesTaken))

print('poop')