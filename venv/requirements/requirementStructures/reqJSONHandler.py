import json
from reqStructs import *

#Encodes the lower level requirements into JSON format
def req_encoder(req):
    if isinstance(req, OrReq):
        return {'type': 'OR', 'classes': list(req.classes)}

    elif isinstance(req, AndReq):
        return {'type': 'AND', 'classes': list(req.classes)}

    elif isinstance(req, NumReq):
        return {'type': 'NUM', 'number': req.num, 'classes': list(req.classes)}

    elif isinstance(req, AboveNumReq):
        return {'type': 'ABOVENUM', 'num': req.num, 'creds': req.creds, 'minNum': req.minNum, 'minCreds': req.minCreds, 'exclusions': req.exclusions }

    raise TypeError(f'Object {req} is not a valid req type')

# TODO: Add serialization for ClassList class

# TODO: Add deserialization for all req classes

# TODO: Add deserialization for ClassList class