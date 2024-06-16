class mammal():
    def speak():
        return "am mammall"
class animal(mammal):
    def speak():
        return "am animal"
class dog(animal):
    def speak():
        return "am an animal"
Mammal=mammal
Animal=animal
Dog=dog
print(animal.speak())
print(mammal.speak())
print(dog.speak())

