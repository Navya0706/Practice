class mammal():
    def mammal_method():
        return "am mammall"
class animal(mammal):
    def animal_method():
        return "am animal"
class dog(animal):
    def dog_method():
        return "am an animal"
obj = dog
print(obj.dog_method())
print(obj.mammal_method())
print(obj.animal_method())