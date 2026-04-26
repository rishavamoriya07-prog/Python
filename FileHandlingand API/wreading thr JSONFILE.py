#read json file as string

import json
with open('C:\\Users\\Aman amoriya\\Rishabh python\\FileHandlingand API\\Music.json','r') as f :
    json_string = f.read()
    print(json_string)
    
with open('C:\\Users\\Aman amoriya\\Rishabh python\\FileHandlingand API\\new 2.json', 'r') as d:
    data = json.load(d)
    print(data)
    
with open('C:\\Users\\Aman amoriya\\Rishabh python\\FileHandlingand API\\tech.json', 'r') as e :
    json_string = e.read()
    data = json.loads(json_string)
    print(data)