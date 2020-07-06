# 4. procss pattern - 객체 접근 제어

### 1. 프록시 디자인패턴 개요
요청자와 공급자사이의 중재자 <br>
proxy 클래스는 객체의 인터페이스 역할  <br>
객체 - 네트워크 연결, 메모리, 파일에 저장된 객체

- 프록시 패턴의 역할  <br>
복잡한 시스템을 간단하게 표현할 수 있다.  <br>
객체에 대한 보안을 제공 <br>
다른 서버에 존재하는 외부 객체 대한 로컬 인터페이스를 제공  <br>
메모리 사용량이 높은 객체를 다루는 가벼운 핸들러 역할  <br>

- 코드 예시

```
__author__ = 'Chetan'

class Actor(object):
    
    def __init__(self):
        self.isBusy = False
    
    def occupied(self):
        self.isBusy = True
        print(type(self).__name__ , "is occupied with current movie")
    
    def available(self):
        self.isBusy = False
        print(type(self).__name__ , "is free for the movie")
    
    def getStatus(self):
        return self.isBusy

class Agent(object):
    
    def __init__(self):
        self.principal = None
    
    def work(self):
        self.actor = Actor()
        if self.actor.getStatus():
            self.actor.occupied()
        else:
            self.actor.available()


if __name__ == '__main__':
    r = Agent()
    r.work()
    
====================================================

__author__ = 'Chetan'

from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
    
    @abstractmethod
    def do_pay(self):
        pass

class Bank(Payment):
    
    def __init__(self):
        self.card = None
        self.account = None
    
    def __getAccount(self):
        self.account = self.card # Assume card number is account number
        return self.account
    
    def __hasFunds(self):
        print("Bank:: Checking if Account", self.__getAccount(), "has enough funds")
        return False
    
    def setCard(self, card):
        self.card = card
    
    def do_pay(self):
        if self.__hasFunds():
            print("Bank:: Paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds!")
            return False

class DebitCard(Payment):
    
    def __init__(self):
        self.bank = Bank()
    
    def do_pay(self):
        card = input("Proxy:: Punch in Card Number: ")
        self.bank.setCard(card)
        return self.bank.do_pay()

class You:
    
    def __init__(self):
        print("You:: Lets buy the Denim shirt")
        self.debitCard = DebitCard()
        self.isPurchased = None
    
    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()
    
    def __del__(self):
        if self.isPurchased:
            print("You:: Wow! Denim shirt is Mine :-)")
        else:
            print("You:: I should earn more :(")

you = You()
you.make_payment()
```

객체의 대리 겍체를 제공해 접근을 제어 <br>
분산구조를 지원하기 위한 인터페이스를 제공  <br>
의도하지 않은 케이스로부터 객체를 보호  <br>

### 2. 각 객체의 역할

- Proxy <br>
실 객체에 접근할 수 있는 레퍼런스를 유지
- Subject  <br>
RealSubject와 Proxy를 책임진다.  <br>
RealSubject를 Proxy로 대체할 수 있다.  <br>
- RealSubject
Proxy가 대체하는 실 겍체를 나타낸다.

### 3. 프록시의 여러 유형

1. 가상 프록시(Virtual Proxy)  <br>
인스턴스화하기엔 무거운 객체의 플레이스 홀더 역할을 한다.  <br>
클라이언트가 객체를 처음 요청하거나 접근했을 때 실 객체를 생성 -> 데이터가 크기 때문에  <br>
2. 원격 프록시 (Remote Proxy)  <br>
원격 프록시는 원격 서버나 다른 주소 공간에 존재하는 객체에 대한 로컬 인스턴스를 생성  <br>
원격 객체를 로컬에서 제어할 수 있는 원격 프록시 객체를 생성하여 사용  <br>
3. 보호 프록시  (Protective Proxy)  <br>
RealSubject의 중요한 부분에 대한 접근을 제어한다.  <br>
사용자의 인증과 허가를 담당하는 인증 서비스 - 서보호 프록시 서버  <br>
4. 스마트 프록시 (Smart Proxy)  <br>
사용자가 객체에 접근했을 때 추가적인 행동을 취한다.  <br>
ex) 서비스에 여러번 접근항 경우 프록시가 객체의 잠금 상태 및 접근 제어를 함  <br>

### 4. 프록시패턴의 장점 및 퍼사드 패턴과 비교

- 프록시 패턴의 장점  <br>
1. 무거운 객체 특히 자주 사용되는 객체를 캐싱해 어플리케이션의 성능을 향상  <br>
2. RealSubject에 대한 접근 요청을 인증  <br>
3. 원격 프록시는 원격 서버 간의 네트워크 연결과 DB연결 구현에 적합 , 모니터링 용도로 사용 가능  <br>

- 퍼사드와 프록시 패턴 비교  <br>
1. 퍼사드 패턴  <br>
클래스의 서브시스템에 대한 인터페이스 제공  <br>
서브시스템 간의 의존도와 통신을 최소화  <br>
퍼사드 객체는 하나의 통합된 간단한 인터페페이스를 제공  <br>
2. 프록시 패턴  <br>
실 객체의 대리 객체를 제공해 접근을 제어  <br>
타겟 객체와 동일한 인터페이스 구조를 가지며 타겟에 대한 참조  <br>
클라이너트와 감싸고 있는 객체 사이의 중재자 역할  <br>

















