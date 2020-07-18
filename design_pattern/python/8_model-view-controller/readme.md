# 8. MVC(model-view-controller) pattern

### 1. 컴파운드 패턴 개요
GoF에 따르면 '컴파운드 패턴은 2개 이사의 패턴을 합쳐 문제를 해결'하는 패턴 <br>
그러나 컴파운드패턴은 단순히 여러 패턴의 조합이 아닌 문제를 해결하는 독립적인 솔류션  <br>

### 2. MVC 패턴
MVC패턴은 유저 인터페이스를 구현할수 있는 유지보수가 용이한 디자인 패턴 <br>

- MVC 패턴의 원리  <br>
사용자는 뷰를 통해 요청을 보낸다. <br>
컨트롤러는 뷰에 전달받은 잇풋을 모델로 보낸다. <br>
컨트롤러는 사용자의 요청에 따라 버튼 교체 및 UI 추가 등을 뷰에 지시 <br>
모델은 뷰에 상태 변경을 알림 <br>
뷰는 모델이 전달한 상태를 출력 <br>

- MVC 역할 <br>
모델 : 데이터를 저장하고 조작 <br>
뷰 : 유저 인터페이스와 데이터의 시각적 표현을 담당하는 클래스 <br>
컨트롤러 : 모델과 뷰를 연결하는 클래스 <br>
클라이언트 : 목적에 따라 정보를 요청하는 클래스 <br>

- MVC 적합 환경  <br>
비지니스 로직을 건드리지 않고 표현 계층만 수정해야 하는 경우  <br>
유저 인터페이스를 수정하는 데 다수의 컨트롤러와 뷰가 사용될 수 있다  <br>
모델은 뷰를 수정하지 않아도 변결될 수 있으므로 독립적  <br>

- MVC 목적  <br>
데이터 조작과 표현의 분리  <br>
쉬운 유지보수와 구현  <br>
유연한 데이터 저장과 표현 방식의 수정  <br>

### 3. 상세 설명
##### 1. 모델  <br>
모델은 뷰와 컨트롤러와는 독립적인 애플리케이션의 일부  <br>
사용자가 요청한 데이터를 제공  <br>
데이터를 저장하고 반환하는 DB 테이블  <br>

##### 2. 뷰 <br>
뷰는 사용자가 인터페이스에서 보게 되는 데이터의 시각적 표현  <br>
뷰를 독립적으로 작성할 수 있느나 복잡한 로직을 포함하며 안됨  <br>
DB와 직접 통신하지않고 모든 정보는 모델에게 의존해서 얻는다  <br>

##### 3. 컨트롤러  <br>
사용자의 행동을 제어  <br>
사용자가 인터페이스에서 행동을 하면 특정 요소를 감지해 모델을 호출해 데이터는 변형함  <br>
컨트롤러는 뷰에 데이터를 전달  <br>

```
__author__ = 'Chetan'
class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2,},
        'sms': {'number': 1000, 'price': 10,},
        'voice': {'number': 1000, 'price': 15,},
    }

class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc, ' ')

    def list_pricing(self, services):
            for svc in services:
                print("For" , Model.services[svc]['number'],
                      svc, "message you pay $",
                      Model.services[svc]['price'])


class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_services(self):
        services = self.model.services.keys()
        return(self.view.list_services(services))

    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_pricing(services))

class Client(object):
    controller = Controller()
    print("Services Provided:")
    controller.get_services()

    print("Pricing for Services:")
    controller.get_pricing()
```

### 4. MVC 패턴의 장점
유지보수가 쉽고 요소 간의 독립성이 높아져 복잡성이 줄어든다 <br>
백엔드 로직을 거의 건드리지 않고 독립적으로 프론트앤드를 수정할 수 있다  <br>
모델이나 비즈니스 로직도 마찬가지로 뷰와 상관없이 수정될 수 있다.  <br>
컨트롤러 또한 뷰와 모델과는 독립적으로 수정될 수 있다.  <br>
플랫폼 개발자와 UI 개발자 같이 특정 부냥의 전문가들이 독립적으로 일할 수 있는 환경을 제공  <br>







