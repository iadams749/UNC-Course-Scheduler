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
        return {'type': 'ABOVENUM', 'subject': req.subject, 'num': req.num, 'creds': req.creds, 'minNum': req.minNum, 'minCreds': req.minCreds, 'exclusions': req.exclusions }

    elif isinstance(req, MultiOrReq):
        return json.loads(json.dumps(req, default=reqList_encoder))

    raise TypeError(f'Object {req} is not a valid req type')

#Encodes a ReqList as well as a MultiOrReq
def reqList_encoder(reqs):

    if isinstance(reqs, MultiOrReq):
        dictList = []

        for r in reqs.requirementList:
            dictList.append(json.loads(json.dumps(r,default=req_encoder)))

        return {'type': 'MULTIOR', 'num': reqs.num, 'reqs' : dictList}

    if isinstance(reqs, ReqList):
        dictList = []

        for r in reqs.requirementList:
            dictList.append(json.loads(json.dumps(r,default=req_encoder)))

        return dictList

    raise TypeError(f'Object {reqs} is not a valid reqList')

#Deserializes the reqs from their JSON format
def req_decoder(json_str):

    # json_str = json.loads(req)

    if isinstance(json_str, list):
        reqs = []
        for r in json_str:
            reqs.append(req_decoder(r))

        return ReqList(reqs)

    elif json_str['type'] == 'AND':
        classSet = set(json_str['classes'])
        return AndReq(classSet)

    elif json_str['type'] == 'OR':
        classSet = set(json_str['classes'])
        return OrReq(classSet)

    elif json_str['type'] == 'NUM':
        classSet = set(json_str['classes'])
        num = json_str['number']
        return NumReq(classSet, num)

    elif json_str['type'] == 'ABOVENUM':
        subject = json_str['subject']
        num = json_str['num']
        creds = json_str['creds']
        minNum = json_str['minNum']
        minCreds = json_str['minCreds']
        exclusions = json_str['exclusions']
        return AboveNumReq(subject, num, creds, minNum, minCreds, exclusions)

    elif json_str['type'] == 'MULTIOR':
        num = json_str['num']
        reqs = []
        for r in json_str['reqs']:
            reqs.append(req_decoder(r))

        return MultiOrReq(num, reqs)