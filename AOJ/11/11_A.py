class Dice:
    def __init__(self,decision,pip):
        self.decision = decision
        self.pip = pip
        
    def control(self):
        for i in range(len(self.decision)):
            if self.decision[i] == 'S':
                if i == (len(self.decision) - 1):
                    print(self.pip[4])
                self.pip = [self.pip[4],self.pip[0],self.pip[2],self.pip[3],self.pip[5],self.pip[1]]
            elif self.decision[i] == 'W':
                if i == (len(self.decision) - 1):
                    print(self.pip[2])
                self.pip = [self.pip[2],self.pip[1] , self.pip[5] ,self.pip[0] ,self.pip[4], self.pip[3]]
            elif self.decision[i] == 'N':
                if i == (len(self.decision) - 1):
                    print(self.pip[1])
                self.pip = [self.pip[1],self.pip[5],self.pip[2],self.pip[3],self.pip[0],self.pip[4]]
            elif self.decision[i] == 'E':
                if i == (len(self.decision) - 1):
                    print(self.pip[3])
                self.pip = [self.pip[3],self.pip[1],self.pip[0],self.pip[5],self.pip[4],self.pip[2]]

x = list(map(int, input().split()))
y = input()
sample = Dice(y,x)
sample.control()