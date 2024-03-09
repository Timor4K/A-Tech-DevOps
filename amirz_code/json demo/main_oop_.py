import json

class Person:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def print_info(self):
        print(self.name, self.age, self.weight)

    def get_older(self, years):
        self.age += years

    def save_to_json(self, filename):
        person_dict = {'name':self.name, 'age':self.age, 'weight':self.weight}
        with open(filename,'w') as f:
            f.write(json.dumps(person_dict, indent=4))

    def load_from_json(self, filename):
        with open(filename,'r') as f:
            data = json.loads(f.read())

        self.name = data['name']
        self.age = data['age']
        self.weight = data['weight']

person1 = Person("Mikel", 27, 30)
person1.print_info()
person1.get_older(100)
person1.save_to_json("oop_data.json")

person2 = Person(None,None,None)
person2.load_from_json("oop_data.json")
person2.print_info()
