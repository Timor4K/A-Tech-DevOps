import json

#dictionary with a list that its member is dictionary
mydict = {
    "person" : [
        {
            "name": "Name 1",
            "age": 20,
            "weight": 55
        },
        {
            "name": "Name 2",
            "age": 25,
            "weight": 60
        },
        {
            "name": "Name 3",
            "age": 30,
            "weight": 65
        }
    ]
}

#get mydict dictionary and export it to mydata.json file
json_string = json.dumps(mydict, indent=6)
with open('mydata.json','w') as f:
    f.write(json_string)

