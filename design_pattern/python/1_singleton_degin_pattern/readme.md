# The Singleton Design Pattern

### 싱글톤 디자인 패턴 개요 

실글톤 디자인 패턴은 글로벌하게 접근 간으한 단 한 개의 객체만을 하여하는 패턴<br>
DB, 프린트 스풀러, app 등 동일한 리소스에 대한 요청의 충돌을 막기 위해 한개의 인스턴스만 사용 <br>

- 싱글톤 디자인 패턴의 목적 <br>
1. 클래스에 대한 단일 객체 생성  <br>
2. 전역 객체 제공  <br>
3. 공유된 리소스에 대한 동시 접근 제어  <br>

- 코드 - singleton.py 설명 <br>

```
__new__ 함수를 오버라이드해 객체를 생성한다.
__new__ 함수는 객체가 이미 존재하는지 확인하고 hasattr 함수는 cls 객체가 instance속석을 가지고 있는지 확인한다.
hasattr 함수 : 해당 객체가 명시한 속성을 가지고 있는지 확인하는 파이썬 함수 
```

### 게으른 초기화(Lazy instantiation) <br>
게으른 초기화는 싱글톤 패턴의 한 종류 <br>
게으른 초기화는 인스턴스가 꼭 필요할 때 생성한다.  <br>
사용할 수 있는 리소스가 제한적인 상황일 때 객체가 꼭 필요한 시점에서 생성하는 방식 <br>
lazy_instantiation.py 참조 <br>

### 모듈 싱글톤

파이썬의 임포트 방식 때문에 모든 모듈은 기본적으로 싱글톤이다.  <br>

### 모노스테이트 싱글톤 패턴 (The Monosstate Singleton Pattern)
알렉스 마르텔리(Alex Martelli)는 상태를 공유하는 인스턴스가 필요하다고 주장  <br>
즉, 객체 생성 여부보다 객체의 상태와 행위가 더 중요하다고 이야기함 <br>
모노스테이트 싱글톤 패턴은 모든 객체가 같은 상태를 공유하는 패턴이다. <br>

- code
```
    - 파일 1
__author__ = 'Chetan'

class Borg:
    __shared_state = {"1":"2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

b = Borg()
b1 = Borg()
b.x = 4
# 서로 다른 객체 
print("Borg Object 'b': ", b) 
print("Borg Object 'b1': ", b1)
# 같은 내용을 출럭함 (같은 상태 공유)
print("Object State 'b':", b.__dict__) 
print("Object State 'b1':", b1.__dict__)

    - 파일 2 - new method 이용하는 방법
__author__ = 'Chetan'

class Borg(object):
     _shared_state = {}
     def __new__(cls, *args, **kwargs):
        # 객체 인스턴스를 생성하는 메소드
       obj = super(Borg, cls).__new__(cls, *args, **kwargs)
       obj.__dict__ = cls._shared_state
       return obj
```

### 싱글톤과 메타클래스

메타클래스 : 클래스의 클래스 ?? -> 클래스는 자신의 메티클래스 인스턴스 <br>
객체 생성시 클래스는 메타클래스가 정의 <br>
name(클래스 명), base(베이스 클래스), dict(속성 값)
```
__author__ = 'Chetan'

class MetaSingleton(type):
    
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=MetaSingleton):
    pass

logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)
```

클래스는 메타클래스가 정의한다. <br>
