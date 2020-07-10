# 6. Command Desgin Pattern

### 1. 커맨드 디자인패턴 개요 

객체가 특정 기능을 바로 수행하거나 나중에 트리거할 때 필요한 모든 정보를 캡슐화 하는 기능 <br>
- 캡슐화 하는 정보  <br>
메소드명 <br>
메소드를 소유하는 객체 <br>
메소드 인자  <br>

### 2. 커맨드 패턴 구성 요소

- 각 객체 설명 <br>
1. Command  <br>
Receiver 객체에 대해 알고 있으며 Reciver 객체의 함수를 호출한다.  <br>
2. Receiver 함수의 인자는 Command 객체에 저장돼 있다.  <br>
3. Invoker는 명령을 수해안다.  <br>
4. Client는 Command 객체를 생성하고 Receiver를 저장한다.  <br>

- 커맨드 패턴의 목적  <br>
요청을 객체 속에 캡슐화  <br>
클라이언트의 다양한 요청을 매개변수화  <br>
요청을 큐에 저장  <br>
객체지향 콜백을 지원  <br>

- 적합 환경  <br>
수행할 명령에 따라 객체를 변수화  <br>
요청을 큐에 저장하고 각기 다른 시점에 수행  <br>
작은 단위의 연산을 기반으로 하는 상위 연산을 만들 때  <br>

```
__author__ = 'Chetan'

class Wizard():
    
    def __init__(self, src, rootdir):
        self.choices = []
        self.rootdir = rootdir
        self.src = src
    
    def preferences(self, command):
        self.choices.append(command)
    
    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, " to ", self.rootdir)
            else:
                print("No Operation")
    
    def rollback(self):
        print("Deleting the unwanted..", self.rootdir)


if __name__ == '__main__':
    ## Client code
    wizard = Wizard('python3.5.gzip', '/usr/bin/')
    ## Steps for installation. ## Users chooses to install Python only
    wizard.preferences({'python':True})
    wizard.preferences({'java':False})
    wizard.execute()
    
==================================================================
__author__ = 'Chetan'

from abc import ABCMeta, abstractmethod
class Command(metaclass=ABCMeta):
    def __init__(self, recv):
        self.recv = recv
    
    def execute(self):
        pass

class ConcreteCommand(Command):
        
    def __init__(self, recv):
        self.recv = recv
    
    def execute(self):
        self.recv.action()

class Receiver:
    
    def action(self):
        print("Receiver Action")

class Invoker:
    
    def command(self, cmd):
        self.cmd = cmd
    
    def execute(self):
        self.cmd.execute()

if __name__ == '__main__':
    recv = Receiver()
    cmd = ConcreteCommand(recv)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()

```
Command : 연산을 수행할 인터페이스를 정의 <br>
ConcreteCommand : Receiver 객체와 연산 간 바인딩을 정의  <br>
Client : ConcreteCommand 객체를 생성하고 Receiver를 설정  <br> 
Invoker : ConcreteCommand에 수행을 요청한다. <br>
Receiver: 요청에 관련된 연산을 관리한다.  <br>

### 3. 커맨드 패턴의 장단점
- 장점  <br>
작업을 요청하는 클래스와 실제로 작업을 수행하는 클래스를 분리한다.  <br>
큐에 커맨드를 순서대로 저장한다.  <br>
기존 코드를 수정하지 않고 새로운 커맨드를 쉽게 추가할 수 있다.  <br>
커맨드 패턴으로 롤백 시스템을 구현할 수 있다.  <br>
- 단점  <br>
클래스와 객체가 많다  <br>
-> 개라바는 신중하게 클래스를 작성해야 함  <br>
모든 작업이 독립적인 ConcreteCommand 클래스이므로 구현 및 유지모수해야 하는클래스가 많다.  <br>

