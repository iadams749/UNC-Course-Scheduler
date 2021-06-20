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

# nick = MultiOrReq(2,['ASTR101', 'COMP211', OrReq({'MATH347','COMP283'})])
# print(json.dumps(nick, default=reqList_encoder, indent=4))
# reqClasses = {'ASTR101','MATH347','RELI109'}

nick = ReqList(['BUSI102', 'ECON101', 'ENGL105', OrReq({'MATH152', 'MATH231', 'MATH232', 'STOR113'}), 'STOR155',\
                'BUSI403', 'BUSI406', 'BUSI408', 'BUSI411', AboveNumReq('BUSI', 0, 4.5, 0, 0.0, ['BUSI102', 'BUSI403', 'BUSI406', 'BUSI408', 'BUSI411'])])

j = open("venv/requirements/requirementsJSONs/BusinessAdministrationMinor.json",'w')
j.write(json.dumps(nick,default=reqList_encoder,indent=2))
j.close()
