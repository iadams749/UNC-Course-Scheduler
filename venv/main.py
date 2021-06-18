from classObj import *
from reqStructs import *
import json
from reqJSONHandler import *

classesTaken = set()

joey = ClassObj()
joey.setSubAbb('ASTR')
joey.setNumber('101')

jay = ClassObj()
jay.setSubAbb('COMP')
jay.setNumber('210')
jay.setCredits(3.0,3.0)

thomas = ClassObj()
thomas.setSubAbb('MATH')
thomas.setNumber('347')

classesTaken.add(joey)
classesTaken.add(jay)
classesTaken.add(thomas)

reqClasses = {'ASTR101','MATH347','RELI109'}
nick = ReqList(['COMP210','COMP211',OrReq({'COMP283','MATH381'}),AndReq({'ASTR101','ASTR101L'}),AboveNumReq('COMP',5,0.0,420,3.0,[])])


