# 7. The Template Method Pattern

### 1. 템플릿 메소드패턴 개요 
템플릿 메소드 패턴에서 단계를 원시 연산(Primitive Operation)이라고 한다.<br>
각 단계에 추상 메소드가 있고, 템플릿 메소드가 전체 알고리즘을 구현한다. <br>

- 템플릿 메소드 패턴이 적합한 상황 <br>
여러 알고리즘 또는 클래스가 비슷하거나 같은 로직을 구현할 때 <br>
알고리즘을 단계벌로 서브클래스화해 코드의 중복을 줄일 수 있는 경우 <br>
서브클래스를 오버라이드해 여러 알고리즘을 구현할 수 있는 경우 <br>

### 2. 템플릿 메소드패턴의 이해 

- 목적<br>
알고리즘의 뼈대를 원시 연산으로 구현<br>
알고리즘의 구조를 수정하지 않고 일부 서브클래스를 재정의 <br>
코드의 재사용과 중복 최소화 <br>
공통 인터페이스 및 구현 활용 <br>

- 구성 요소 <br>
AbstractClass : 알고리즘의 단계를 정의하는 인터페이스 <br>
ConcreteClass : 단계별 서브클래스 <br>
template_method() : 단계별 메소드를 호출하는 알고리즘 정의 <br>

### 3. 코드 및 설명 

```
__author__ = 'Chetan'

from abc import  ABCMeta, abstractmethod

class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collectSource(self):
        pass

    @abstractmethod
    def compileToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()

class iOSCompiler(Compiler):
    def collectSource(self):
        print("Collecting Swift Source Code")

    def compileToObject(self):
        print("Compiling Swift code to LLVM bitcode")

    def run(self):
        print("Program runing on runtime environment")


iOS = iOSCompiler()
iOS.compileAndRun()
```

- AbstractClass <br>
알고리즘의 각 단계를 정의하는 추상 메소드로 구성돼 있다.<br>
구상 서브클래스가 오버라이트한다. <br>
- template_method() <br>
알고리즘의 뼈대를 정의 <br>
전체 알고리즘을 정의하는 여러 추상 메소드를 호출 <br>
- ConcreteClass <br>
여러 추상 메소드로 구성된알고리즘의 서브클래스를 구현한다. <br>

### 4. 후크(Hook)
후크는 추상 클래스에 정의된 메소드 <br>
후크는 서브클래스가 알고리즘 중간 단계를 제어할 수 있는 기능을 제공한다. <br>
서브클래스는 후크를 꼭 사용하지 않아도 된다. <br>

서브클래스가 반드시 구현해야 하는 부분은 추상 메소드를 사용하고 선택적인 부분은 후크를 사용 <br>
-> 정의해야하는 일부 메소드를 후크를 사용하여 따로 사용  <br>

### 5. 할리우드 원칙(Hollywood Principle)과 탬플릿 메소드 
할리우드 원칙은 "먼저 연락하지 마세요. 저희가 연락드리겠습니다."(Don't call us, we'll call you) 에 기반 
객체지향에서 하위 요소는 할리우드 원칙을 기반으로 메인 시스템에 끼어 들어갈(Hook이용) 수 있다. <br>
하지만 상위 요소가 언제 어떤 하위 요소가 필요한지 결정 <br>
-> 저희가 연락드리겠습니다.  <br>
템플릿 메소드 패턴은 상위추상 클래스가 알고리즘에 필요한 단계를 정의한다. <br>
즉, 알고리즘에 따라 각 단계에 ㅏㅁㅈ는 하위 클래스가 호출됨 <br>

### 6. 탬플릿 메소드 패턴의 장담점
- 장점 <br>
코드의 중복이 없다.<br>
컴퓨지션이 아닌 상속을 사용함으로 코드 재활용 가능 <br>
-> 일부 함수만 오버라이드 <br>
알고리즘의 각 단계를 서브클래스에서 구현할 수 있는 유연성 제공 <br>
- 단점 <br>
코드 디버깅 및 이해가 어려울 수 있음 <br>
구현하지 않아도 되는 메소드를 구현 혹은 추상 메소드를 구현하지 않는 실수할수 있다. <br>
어떤 계층에서라도 수정한다면 전체 구조 및 구현에 영향을 줄 수 있어 유지보수가 어렵다 <br>









