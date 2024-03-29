import os
import json
import urllib.request


url = 'http://localhost:8080/project2-backend/api/'

taxonomy = "taxonomy"
user = "user"
product = "product"

dirFiles = os.listdir(taxonomy)
dirFiles = sorted(dirFiles,key=lambda x: int(os.path.splitext(x)[0]))

for file in dirFiles:
    filename = os.fsdecode(file)
    if filename.endswith(".json"):

        req = urllib.request.Request(url + taxonomy)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        
        with open(taxonomy + '/' + file) as f:
            jsondata = json.load(f)
        jsondata = json.dumps(jsondata)
        jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
        req.add_header('Content-Length', len(jsondataasbytes))
        print(jsondataasbytes)
        response = urllib.request.urlopen(req, jsondataasbytes)
        continue
    else:
        print("unable to can")
        continue

dirFiles = os.listdir(user)
dirFiles = sorted(dirFiles,key=lambda x: int(os.path.splitext(x)[0]))
for file in dirFiles:
    filename = os.fsdecode(file)
    if filename.endswith(".json"):

        req = urllib.request.Request(url + user)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        
        with open(user + '/' + file) as f:
            jsondata = json.load(f)
        jsondata = json.dumps(jsondata)
        jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
        req.add_header('Content-Length', len(jsondataasbytes))
        print(jsondataasbytes)
        response = urllib.request.urlopen(req, jsondataasbytes)
        continue
    else:
        print("unable to can")
        continue

dirFiles = os.listdir(product)
dirFiles = sorted(dirFiles,key=lambda x: int(os.path.splitext(x)[0]))
for file in dirFiles:
    filename = os.fsdecode(file)
    if filename.endswith(".json"):

        req = urllib.request.Request(url + product)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        with open(product + '/' + file) as f:
            jsondata = json.load(f)
            jsondata = json.dumps(jsondata)
            jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
            req.add_header('Content-Length', len(jsondataasbytes))
            print(jsondataasbytes)
            response = urllib.request.urlopen(req, jsondataasbytes)
    else:
        print("unable to can")
