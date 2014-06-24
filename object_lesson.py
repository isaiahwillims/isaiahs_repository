class Chair(object):
    
    def __init__(self, *args):
        self.people = []
        for person in args:
            self.people.append(person)
    
    def add_person(self, person):
       self.people.append(person)
    
c = Chair("mark")

c.add_person("mark")

c.people
# Chair.add_person(c, "mark")
# #objects are stupid
# c.people

# chairs = []
# for i in range(4):
#     chairs.append(Chair("mark"))
    
# chairs[0].add_person("john")

# print chairs[0].people