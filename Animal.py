class Animal(object):
  """Makes cute animals."""
  is_alive = True # Member variable
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print (self.name)
    print (self.age)

hippo = Animal("Hippoo", 29)
hippo.description()
print (hippo.is_alive)
hippo.is_alive = False
print (hippo.is_alive)

cat = Animal("Cat", 22)
print (cat.is_alive)
