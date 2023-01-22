from create_one_attribute import Person

#Create an object named "p1" whose name is "Anvar"
p1 = Person('Anvar')
#Create an object named "p2" whose name is "Shavkat"
p2 = Person('Shavkat')
#Create an object named "p3" whose name is "Jasur"
p3 = Person('Jasur')
#Add these objects to the "persons" named list
persons = []
persons.append(p1.name)
persons.append(p2.name)
persons.append(p3.name)
print(persons)