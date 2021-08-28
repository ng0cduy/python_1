from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,name_):
        self.name = name_
    @abstractmethod
    def say_hi(self):
        pass
class Cat(Animal):
    def __init__(self, name_):
        super().__init__(name_)
    def say_hi(self):
        print("Hello, I'am "+self.name)
if __name__ == "__main__":
    cat_1 = Cat("Tom")
    cat_1.say_hi()
