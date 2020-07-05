# 3. The Structural & Facade Design Pattnern

### 1. 구조 디자인 패턴

- 구조 디자인 패턴의 특징 <br>
객체와 클래스가 병합해 더 큰 구조를 만든다. <br>
개체의 관계를 더 쉽게 식별할 수 있다. <br>
클래스 패턴(The Class Pattern)은 상속을 통해 추상화해 인터페이스를 제공 <br>
객체 패턴(The Object Pattern)은 한 개의 객체를 더 큰 객체로 확장

- 구조 다자인 패턴 용어
1) 어댑터 패턴(The Adapter Pattern)<br>
크라이언트의 요구에 따라 특정 인터페이스를 다른 인터페이스에 맞춘다.<br>
2) 브릿지 패턴(The Bridge Pattern)<br>
객체의 인터페이스와 구현을 분리해 독립적으로 동작할 수 있게 한다.<br>
3) 데코레이터 패턴(The Decorator Pattern) <br>
런타임에 객체의 책임을 붙인다.

### 2. 퍼사드 디자인 패턴 개요 

퍼사드(facode) : 건물의 정면, 특히 돋보이는 쪽을 의미 <br>

- 퍼사드 패턴의 목적<br>
서브시스템의 인터페이스를 통합시킨 단일 인터페이스를 제공해 클라이언트가 쉽게 서브시스템에 접근 <br>
단일 인터페이스 객체로 복잡한 시스템을 대체 <br>
클라이언트와 내부 구현을 분리 <br>

- 퍼사드 패턴의 역할 <br>
요청에 알맞는 인터페이스를 알고 있다. <br>
컴포지션을 통해 클라이언트의 요청을 적합한 서브시스템 객체에 전달 <br>

- 시스템의 역할 <br>
서브시스템의 기능을 구현 <br>
퍼사드 객체가 지시한 일을 담당 하지만 퍼사드를 참조하지 않는다. <br>

- 클라이언트 역할 <br>
퍼사드를 인스턴스화하는 클래스 <br>
퍼사드에 서비싀스템을 통해 작업을 수행 <br>

- 코드 예시

```
__author__ = 'Chetan'

class Hotelier(object):
    
    def __init__(self):
        print("Arranging the Hotel for Marriage? --")
    
    def __isAvailable(self):
        print("Is the Hotel free for the event on given day?")
        return True
    
    def bookHotel(self):
        if self.__isAvailable():
            print("Registered the Booking\n\n")


class Florist(object):
    
    def __init__(self):
        print("Flower Decorations for the Event? --")
    
    def setFlowerRequirements(self):
        print("Carnations, Roses and Lilies would be used for Decorations\n\n")


class Caterer(object):
    
    def __init__(self):
        print("Food Arrangements for the Event --")
    
    def setCuisine(self):
        print("Chinese & Continental Cuisine to be served\n\n")

class Musician(object):
    
    def __init__(self):
        print("Musical Arrangements for the Marriage --")
    
    def setMusicType(self):
        print("Jazz and Classical will be played\n\n")

# 모든 역할을 다하는 클래스 
class EventManager(object):
    
    def __init__(self):
        print("Event Manager:: Let me talk to the folks\n")
    
    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()
        
        self.florist = Florist()
        self.florist.setFlowerRequirements()
        
        self.caterer = Caterer()
        self.caterer.setCuisine()
        
        self.musician = Musician()
        self.musician.setMusicType()


class You(object):
    
    def __init__(self):
        print("You:: Whoa! Marriage Arrangements??!!!")
    
    def askEventManager(self):
        print("You:: Let's Contact the Event Manager\n\n")
        em = EventManager()
        em.arrange()
    
    def __del__(self):
        print("You:: Thanks to Event Manager, all preparations done! Phew!")

you = You()
you.askEventManager()
```

EventManager 객체에서 모든 클래스 생성을 하여 인터페이스를 간소화 시켜준다. <br>

### 3. 최소지식 원칙

최소지식 원칙은 상호작용하는 객체를 아주 가까운 몇 개의 객체로 최소화 한다.  <br>
시스템을 설계할 때 생성하는 모든 객체가 몇 개의 클래스와 연관되며 어떤 식으로 대화하는지 알아야 한다. <br>
지나치게 서로 얽혀있는 클래스를 만드는 것을 지양해야 한다.  <br>
클래스 간의 의존도가 높아질수록 시스템 유지보수가 힘들어진다. 한 부분을 수정시 다른 부분이 변경될 수 있음. 주의  <br>

