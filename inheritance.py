class father:
    def father_method():
        return "am father"
class mother:
    def mother_method():
        return "am mother"
class child(father,mother):
    def child_method():
        return "am childd"
obj1=child
print(obj1.father_method())
print(obj1.mother_method())
print(obj1.child_method())