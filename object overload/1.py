class Point:

    def __init__(self,a):
        self.a = a

    def __lt__(self,other):
        if(self.a<other.a):
            return "obj2 is greater than obj1"
        else:
            return "obj1 is greater than obj2"
    
    def __eq__(self,other):
        if(self.a == other.a):
            return "they are equal"
        else:
            return "they are not equal"
        
obj1 = Point(3)
obj2 = Point(2)
print(obj1 < obj2)

obj3 = Point(5)
obj4 = Point(4)
print(obj3 == obj4)