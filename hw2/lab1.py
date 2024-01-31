class Pupa:
    def __init__(self):
        self.bob = 0
    def do_work(self, spisok1: list, spisok2: list):
        for i in range(len(spisok1)):
            spisok1[i] -= spisok2[i]
        self.bob += 1000
    def take_salary(self):
        print(self.bob)
        self.bob = 0

class Lupa:
    def __init__(self):
        self.bob = 0
    def do_work(self, spisok1: list, spisok2: list):
        for i in range(len(spisok1)):
            self.bob += 10
            spisok1[i] += spisok2[i]
        
            
    def take_salary(self):
        print(self.bob)
        self.bob = 0

class Accountant():
    def __init__(self, worker) -> None:
        super().__init__()
        self.worker = worker   

    def give_salary(self):
        self.worker.take_salary()

Lup = Lupa()
Lup.do_work([5,123,23,543,5,46,54,1,47,56,7,1], [5,123,23,543,5,46,54,1,47,56,7,1])
Pup = Pupa()
Pup.do_work([5,123,23,543,5,46,54,1,47,56,7,1], [5,123,23,543,5,46,54,1,47,56,7,1])

Ivanovna = Accountant(Lup).give_salary()
Ivanovna = Accountant(Pup).give_salary()