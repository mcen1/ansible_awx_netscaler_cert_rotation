#!/bin/env python3
import json
import sys
import ast
import yaml

# argument 1 is filename
# argument 2 is the sslkeybinding we care about

def loadFile(myfile,mytarget):
  matchingvservers={"sni_certs":[], "nonsni_certs": []}
  with open(myfile) as f: 
    data = f.read() 
  d = ast.literal_eval(data) 
#  js = json.loads(data) 
  for item in d:
    vservername=item['vservername']
    if 'sslvserver_sslcertkey_binding' in item:
      for binding in item['sslvserver_sslcertkey_binding']:
        if 'certkeyname' in binding and binding['certkeyname']==mytarget:
          if binding['snicert']==True:
            matchingvservers["sni_certs"].append(vservername)
          else:
            matchingvservers["nonsni_certs"].append(vservername)
  return matchingvservers


if __name__ == '__main__':
  print(f"Looking for vservers that are linked to {sys.argv[2]}...")
  myres=loadFile(sys.argv[1],sys.argv[2])
  print(yaml.dump(myres))
  with open('tmpdata.yml', 'w') as outfile:
    yaml.dump(myres, outfile, default_flow_style=False)
  print("Done!")
