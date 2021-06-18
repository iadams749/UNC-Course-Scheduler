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
nick = AboveNumReq('COMP',5,0.0,420,3.0,['COMP455','COMP550','COMP496','COMP690','COMP692H'])

print(json.dumps(nick, default=req_encoder, indent=4))

