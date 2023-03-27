import random
class Dice:
    check = False
    def __init__(self,decision,pip,original):
        self.decision = decision
        self.pip = pip
        self.original = original
        
    def control(self):
        for i in range(len(self.decision)):
            if self.decision[i] == 'S':
                self.pip = [self.pip[4],self.pip[0],self.pip[2],self.pip[3],self.pip[5],self.pip[1]]
            elif self.decision[i] == 'W':
                self.pip = [self.pip[2],self.pip[1] , self.pip[5] ,self.pip[0] ,self.pip[4], self.pip[3]]
            elif self.decision[i] == 'N':
                self.pip = [self.pip[1],self.pip[5],self.pip[2],self.pip[3],self.pip[0],self.pip[4]]
            elif self.decision[i] == 'E':
                self.pip = [self.pip[3],self.pip[1],self.pip[0],self.pip[5],self.pip[4],self.pip[2]]
            
            if self.pip == self.original:
                Dice.check = True
        

x = list(map(int,input().split()))
y = list(map(int,input().split()))
direction1 = ['W','N','S','E']
direction = []
for i in range(1000):
    direction.append(random.choice(direction1))
sample = Dice(direction,x,y)
sample.control()
if Dice.check:
    print('Yes')
else:
    print('No')