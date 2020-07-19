# 9. state desgom [atterm 

### 1. 상태 디자인 패턴 개요 
행위 디자인패턴은 객체의 역할에 중점을 둔다 <br>
객체는 내부 상태에 따라 여러 행위를 캡슐화 한다. 상태 패턴은 런타임에 객체의 행위를 변경  <br>

- 상태 디자인 패턴의 구성 요소  <br>
State : 객체의 행위를 캡슐화하는 인터페이스  <br>
ConcreteState : State 인터페이스를 구현하는서브클래스.  <br>
Context : 사용자가 선택한 인터페이스를 정의. 특정 상태의 구현한 ConcreteState 서브클래스의 인스턴스를 가지고 있다.  <br>

```
__author__ = 'Chetan'

from abc import abstractmethod, ABCMeta

class State(metaclass=ABCMeta):
    
    @abstractmethod
    def doThis(self):
        pass

class StartState (State):
    def doThis(self):
        print("TV Switching ON..")

class StopState (State):
    def doThis(self):
        print("TV Switching OFF..")

class TVContext(State):
    
    def __init__(self):
        self.state = None
    
    def getState(self):
        return self.state
    
    def setState(self, state):
        self.state = state
    
    def doThis(self):
        self.state.doThis()


context = TVContext()
context.getState()
start = StartState()
stop = StopState()

context.setState(stop)
context.doThis()
```

- 위 코드에서의 역할 <br>
State : Handle() 추상 메소드를 정의하는 인터페이스  <br>
-> ConcreteState가 구현 <br>
ConcreteState : State 설정에 따라 실행될 각 Handle() 메소드를 구현 <br>
Context : 사용자의 요청을 넘겨받는 클래스  <br>

### 2. 상태 디자인 패턴의 장단점 
- 상태 디자인 패턴의 장점  <br>
상황에 따라 if else와 같은 조건부 연산을 줄일 수 있다.  <br>
다형성(Polymorphic) 구현이 쉬우며 새로운 상태를 쉽게 추가할 수 있다 <br>
상태 관련 행위가 모두 ConcreteState 클래스에 있으므로 응집도(Cohesion)가 높아진다.  <br>
새로운 ConcreteState 클래스를 추가해 쉽게 신규 기능을 구현할 수 있다.  <br>
- 상태 디자인 패턴의 단점  <br>
클래스 남발(Class Explosion)이 나타단다.  <br>
새로운 행위는 ConcreteState를 새로 추가하면 되지만 Context 클래스도 맞게 수정해줘야 한다.  <br>









 
