import json

with open('mydata.json','r') as f:
    json_object = json.loads(f.read())

#get one item from the data.json file through the object and print it
#print(json_object['person'][0]['name'])

#print all the data.json file
# Check if the loaded JSON object is a dictionary
if isinstance(json_object, dict):
    # Print all values in the dictionary in ONE LINE
    #for key, value in json_object.items():
     #   print(f"{key}: {value}")
    # Print all values in the dictionary with an indentation of 4
    formatted_json = json.dumps(json_object, indent=4)
    print(formatted_json)
else:
    print("The loaded JSON object is not a dictionary.")