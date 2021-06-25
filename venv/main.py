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

# nick = AboveNumReq('COMP',5,0.0,420,3.0,['COMP455','COMP550','COMP496','COMP690','COMP692H'])
# json_string = json.dumps(nick, default=req_encoder)
# json_loaded = json.loads(json_string)
# print(type(json_loaded))
# ben = req_decoder(json_string)
# print(ben)

# nick = MultiOrReq(2,[AndReq({'ASTR101', 'ASTR101L'}), AndReq({'BIOL101', 'BIOL101L'}), 'BIOL202', 'BIOL205', AndReq({'CHEM101', 'CHEM101L'}), AndReq({'CHEM102', 'CHEM102L'}), AndReq({'GEOL101', 'GEOL101L'}), 'PHYS115', 'PHYS116', 'PHYS117', 'PHYS118', 'PHYS119', 'PHYS351', 'PHYS352'])
# item = json.dumps(nick, default=reqList_encoder)
# print(req_decoder(item))

f = open('venv/requirements/requirementsJSONs/ComputerScienceBS.json')
nick = json.load(f)
print(req_decoder(nick))

