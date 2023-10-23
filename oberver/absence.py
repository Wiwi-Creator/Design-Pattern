from abc import ABC, abstractmethod


# Observer
class Observer(ABC):
    @abstractmethod
    def update(self, absence: str, designee: str):
        pass


# ConcreteObserver
class ObserverPhone(Observer):
    def update(self, absence: str, designee: str):
        print("[Phone] 已指定轉接{0}的來電給{1}!".format(absence, designee))


class ObserverMail(Observer):
    def update(self, absence: str, designee: str):
        print("[Mail Server] 已設定將{0}的信cc給{1}!".format(absence, designee))


# Subject
class Subject(ABC):
    def __init__(self):
        self.observers = []

    @abstractmethod
    def attach(self, observer: Observer): 
        pass

    def detach(self, observer: Observer):
        pass

    def notify(self, absence: str, designee: str):
        pass
    

# ConcreteSubject
class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()

    def attach(self, observer: Observer): 
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, absence: str, designee):
        for observer in self.observers:
            observer.update(absence, designee)
            
            
class main:
    # Create observers
    HR = ObserverPhone()
    Boss = ObserverMail()
        
    # Create subject
    subject = ConcreteSubject()
    subject.attach(HR)
    subject.attach(Boss)
    
    # Notify when Wiwi is leave of absence
    subject.notify("Wiwi", ["Stone", "Tony"])


if __name__ == '__main__':
    main()