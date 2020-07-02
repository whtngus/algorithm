# 2. factory_method_pattern

### 팩토리 패턴 개요

가장 많이 쓰이는 디자인 패턴 <br>

- 팩토리 패턴의 장점 <br>
1. 객체 생성과 클래스 구현을 나눠 상호 의존도를 줄인다. <br>
2. 클라이언트는 생성하려는 개체 클래스 구현과 상관없이 사용할 수 있다. <br>
3. 코드를 수정하지 않고 간단하게 팩토리에 새로운 클래스를 추가할 수 있다. <br>
4. 이미 생성된 객체를 팩토리가 재활용할 수 있다. <br>

- 팩토리 패턴의 종류  <br>
1. 심플 팩토리 패턴 (The Simple Factory Pattern) <br> 
-> 인터페이스는 객체 생성에 필요한 로직을 숨기고 객체를 생성 <br>
2. 팩토리 메소드 패턴(The Factory Method Pattern) <br> 
-> 서브클래스가 객체 생성에 필요한 클래스를 선택  <br>
3. 추상 팩토리 패턴(The Abstract Factory Pattern) <br> 
-> 객체 생성에 필요한 클래스를 노출하지 않고 객체를 생성하는 인터페이스  <br>
   
### 1. 심플 팩토리 패턴  <br>
팩토리 메소드와 추상 팩토리 메소드 패턴을 이해하기 위한 기본 개념  <br>

- code <br>

```
__author__ = 'Chetan'
from abc import ABCMeta, abstractmethod\
class Animal(metaclass = ABCMeta):
    
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):
    
    def do_say(self):
        print("Bhow Bhow!!")

class Cat(Animal):
    
    def do_say(self):
        print("Meow Meow!!")


## forest factory defined
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()

## client code
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("Which animal should make_sound Dog or Cat?")
    ff.make_sound(animal)
```

Animal 이라는 상품을 추상화한 코드. <br> 
ABCMeta는 파이썬에서특정 클래스를 Abstract로 선언하는 특수 메타클래스 <br>

### 2. 팩토리 메소드 패턴 <br>

- 인터페이스를 통해 객체를 생성하지만 팩토리가 아닌 서브 클래스가 해당 객체
  생성을 위해 어떤 클래스를 호출할지 결정 <br>
- 팩토리 메소드는 인스턴스화가 아닌 상속을 통해 객체를 생성  <br>
- 팩토리 메소드 디자인은 유동적(객체가 아닌 인스턴스나 서브 클래스 객체 반환
  가능)  <br>
  
```
__author__ = 'Chetan'

from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    
    def describe(self):
        print("Personal Section")


class AlbumSection(Section):
    
    def describe(self):
        print("Album Section")


class PatentSection(Section):
    
    def describe(self):
        print("Patent Section")


class PublicationSection(Section):
    
    def describe(self):
        print("Publication Section")

------------------ 응용 예시 ------------------------------
class Profile(metaclass=ABCMeta):
    
    def __init__(self):
        self.sections = []
        self.createProfile()
    
    @abstractmethod
    def createProfile(self):
        pass
    
    def getSections(self):
        return self.sections
    
    def addSections(self, section):
        self.sections.append(section)


class linkedin(Profile):
    
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())


class facebook(Profile):
    
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


if __name__ == '__main__':
    profile_type = input("Which Profile you'd like to create? [LinkedIn or FaceBook]")
    profile = eval(profile_type.lower())()
    print("Creating Profile..", type(profile).__name__)
    print("Profile has sections --", profile.getSections())
```

factoryMethod()는 객체 생성을 담당. <br> 
Creator 인터페이스의 factoryMethod()와 ConcreateCreator 클래스는 Product 클래스의 어떤 서브 클래스를 생성할지 결정  <br>
팩토리 메소드 패턴은 객체를 생성하는 인터페이스를 정의하고 어떤 클래스를 초기화할지는 서브 클래스의 결정에 맡긴다  <br>

- 팩토리 메소드 패턴의 장점  <br>
1. 유연성과 포괄성을 갖추며 한 클래스에 종속되지 않는다.  <br>
2. 객체를 생성하는 코드와 활용하는 코드를 분리해 의존성이 줄어든다.  <br>


### 3. 추상 팩토리 패턴

클래스를 직접 호출하지 않고 관련된 객체를 생성하는 인터페이스를 제공  <br>
팩토리 메소드가 인스턴스 생성을 서브 클래스에게 맡기는 반면 추상 팩토리 메소드는 관련된 객체의 집합을 생성  <br>

```
__author__ = 'Chetan'
from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):
    
    @abstractmethod
    def createVegPizza(self):
        pass
    
    @abstractmethod
    def createNonVegPizza(self):
        pass

class IndianPizzaFactory(PizzaFactory):
    
    def createVegPizza(self):
        return DeluxVeggiePizza()
    def createNonVegPizza(self):
        return ChickenPizza()

class USPizzaFactory(PizzaFactory):
    
    def createVegPizza(self):
        return MexicanVegPizza()
    def createNonVegPizza(self):
        return HamPizza()

class VegPizza(metaclass=ABCMeta):
    
    @abstractmethod
    def prepare(self, VegPizza):
        pass

class NonVegPizza(metaclass=ABCMeta):
    
    @abstractmethod
    def serve(self, VegPizza):
        pass

class DeluxVeggiePizza(VegPizza):
    
    def prepare(self):
        print("Prepare ", type(self).__name__)

class ChickenPizza(NonVegPizza):
    
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Chicken on ", type(VegPizza).__name__)

class MexicanVegPizza(VegPizza):
    
    def prepare(self):
        print("Prepare ", type(self).__name__)

class HamPizza(NonVegPizza):
    
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Ham on ", type(VegPizza).__name__)

class PizzaStore:
    
    def __init__(self):
        pass
    
    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)


pizza = PizzaStore()
pizza.makePizzas()
```


### 4. 정리


- 추상 팩토리 메소드 특징  <br>
관련된 객체 집단을 생성하기 위해 한 개 이상의 팩토리 메소드가 필요 <br>
다른 클래스 객체를 생성하기 위해 컴포지션을 사용  <br>
관련된 객체 집단을 사용  <br>

- 팩토리 메소드와 비교   <br>
객체 생성에 필요한 메소드가 사용자에게 노출  <br>
어떤객체를 생성할지 결정하는 상속과 서브 클래스가 필요  <br>
한 개의 객체를 생성하는 팩토리 메소드를 사용  <br>

















