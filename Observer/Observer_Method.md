## Oberver Method (觀察者模式)
---
Observer Pattern，又稱作 Publish-Subscribe Pattern

- 當事件發生時，Publisher(Subject) 通知 Subscribers(Observer)
- 定義Subject的一對多關係
- 一種Behavioural design pattern
- MVC(Model, View, Controller)重要的觀念


### Elements
Subject：abstract，提供保存觀察者物件的集合以及增加Subscriber的方法、刪除Subscriber的方法以及通知Subscriber的抽象方法。

ConcreteSubject：具體目標，實作抽象目標中的通知方法。具體目標內部發生改變時會通知所有加入的觀察者物件。

Observer：abstract，可以是抽象類別或是介面。含有update自己的抽象方法。

ConcreteObserver：實作抽象觀察者，在目標更改狀態時接收通知並更改自身狀態。


### UML
UML
![Alt text](image-3.png)

### Design Considerations

- 檢視邏輯中，有資料狀態上的變化，去定義其中的Subject , Observer
- Declare Subscriber Interface 去 update 即時資訊
- Declare Publisher  Interface 去 add , remove Subscribers

### When To Use?
當多個 Class (Subscriber)都需要接收同一種資料的變化(real_time)時，就適合使用 Observer Pattern

### When Not To Use?

優:
- 新增Subscriber時，符合OCP(Open/Closed Principle)
- 多組的對象在較少的依賴下實現合作，降低耦合

缺:
- 通知的順序問題
- 當Subscriber很多時，針對通知不好作Debug且可能影響效能


