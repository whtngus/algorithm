# 5. 옵서버 패턴(The Observer Pattern)

### 1. 옵서버 패턴 개요
행위 디자인 패턴 중 하나(3~5) <br>
객체(서브젝트)는 자식(옵서버)의 목록을 유지하며 서브젝트가 옵서버에 정의된 메소드를 호출할 때마다 옵서버에 이를 알린다.  <br>

- 옵서버 패턴의 목적  <br>
객체 간 일대다 관계를 형성하고 객체의 상태를 다른 종속 객체에 자동으로 알린다. <br>
서브젝트의 핵심 부분을 캡슐화한다. <br>

- 옵서버 패턴에 적용시킬 상황  <br>
1. 분산 시스템의 이벤트 서비스  <br>
2. 뉴스 에이전시 프레임워크  <br>
3. 주식시장 모델  <br>

- 코드  <br>

```
__author__ = 'Chetan'

class NewsPublisher:
    
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None
    
    def attach(self, subscriber):
        self.__subscribers.append(subscriber)
    
    def detach(self):
        return self.__subscribers.pop()
    
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]
    
    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()
    
    def addNews(self, news):
        self.__latestNews = news
    
    def getNews(self):
        return "Got News:", self.__latestNews


from abc import ABCMeta, abstractmethod

class Subscriber(metaclass=ABCMeta):
    
    @abstractmethod
    def update(self):
        pass


class SMSSubscriber:
    
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    
    def update(self):
        print(type(self).__name__, self.publisher.getNews())

class EmailSubscriber:
    
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    
    def update(self):
        print(type(self).__name__, self.publisher.getNews())

class AnyOtherSubscriber:
    
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    
    def update(self):
        print(type(self).__name__, self.publisher.getNews())


if __name__ == '__main__':
    news_publisher = NewsPublisher()
    
    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(news_publisher)
        print("\nSubscribers:", news_publisher.subscribers())
        
        news_publisher.addNews('Hello World!')
        news_publisher.notifySubscribers()
        
        print("\nDetached:", type(news_publisher.detach()).__name__)
        print("\nSubscribers:", news_publisher.subscribers())
        
        news_publisher.addNews('My second news!')
        news_publisher.notifySubscribers()

------------------------------------------------
__author__ = 'Chetan'

class Subject:
    
    def __init__(self):
        self.__observers = []
    
    def register(self, observer):
        self.__observers.append(observer)
    
    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class Observer1:
    
    def __init__(self, subject):
        subject.register(self)
    
    def notify(self, subject, *args):
        print(type(self).__name__,':: Got', args, 'From', subject)

class Observer2:
    
    def __init__(self, subject):
        subject.register(self)
    
    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)


subject = Subject()
observer1 = Observer1(subject)
observer2 = Observer2(subject)
subject.notifyAll('notification')

```
 

### 2. 옵서버 패턴 역할 
- 서브젝트(subject) <br>
Subject는 Observer를 관리한다.  <br>
Observer는 Subject클래스의 register, deregister 메소드를 호출해 자신을 등록한다.  <br>
Subject는 여러 옵서버를 관리한다.  <br>
- 옵서버(Observer)  <br>
서브젝트를 감시하는 객체를 위한 인터페이스를 제공  <br>
서브젝트의 상태를 알 수 있도록 ConcreteObserver가 구현해야 하는 메소드 정의  <br>
- ConcreteObserver  <br>
Subject의 상태를 저장.  <br>
서브젝트에 대한 정보와 실제 상태를 일관되게 유지하기 ㅜ이해 Observer 인터페이스를 구현  <br>

### 3. 옵서버 패턴 메소드  
Subject는 변경 사항을 Observer에 알리는 방법에는 푸쉬와 풀 두가지 모델이 있다.  <br>
- 풀 모델  <br>
Subject는 변경 사항이 있므을 등록된 observer에 브로드케스트한다. <br>
Observer는 직접 게시자에게 변경 사항을 요청하고 끌어와야한다 - pull  <br>
풀 모델은 Subject가 Observer에 아릴는 단계와 Observer가 Subject로부터 필요한 데이터를 받아오는 두 단계가 필요함으로 비효율적  <br>

- 푸쉬 모델 <br>
풀 모델과 달리 Subject가 Observer에 데이터를 보낸다. <br>
Subject는 Observer가 필요로 하지 않는 데이터까지 보낼 수 있다. <br>
성능을 위해 Subject는 오직 필요한 데이터만 보내야 한다.  <br>

### 4. 느슨한 결합과 옵서버 패턴 

- 효과  <br>
한 부분에 대한 수정이 예기치 않게 다른 부분까지 영향을 끼치는 위험을 줄인다. <br>
테스트와 유지 보수 및 장애 처리가 쉽다  <br>
시스템을 쉽게 여러 부분으로 분리할 수 있다.  <br>

- 옵서버 패턴의 느슨한 결합 추구  <br>
Subject는 정확히 Observer가 어떤 인터페이스를 구현하는지 모른다.  <br>
ConcreateObserver의 존재를 모른다.  <br>
새로운 Observer를 추가할 수 있다.  <br>
-> Observer추가시 Subject를 수정할 필요 없다.  <br>
Subject 또는 Observer는 독립적  <br>
-> Observer는 필요 시 어디에서도 재사용될 수 있다.

### 5. 옵서버 패턴의 장단점

- 장점  <br>
1. 객체 간의 느슨한 결합  <br>
2. Subject or Observer 클래스를 수정하지 않고 객체 간 자유룝게 데이터를 주고받을 수 있다.  <br>
3. 새로운 Observer를 언제든지 추가/제거할 수 있다.
- 단점  <br>
1. ConcreateObserver는 상속을 통해 Observer인터페이스를 구현함으로, 컴포지션에 대한 선택권한이 없다.  <br>
2. 잘 구현 못하면 Observer 클래스는 복잡도를 높인다.  <br>
3. app알림 기능 혹은 신뢰할 수 없는 레이스 상태(Race Condition) 또는 비일관성을 초래할 수 있다.  <br>















 