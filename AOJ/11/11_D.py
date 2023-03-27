import random
#AOJ11-Cのような2種類のサイコロが同一の物か判定する関数controlを持つクラスDice
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

#入力された値に対して各サイコロの目のリストをn個分含むリストのリストarrayを作成            
n  = int(input())
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

#arrayから2種類のリストを取り出してクラスDiceを使って同一か確かめる。それを全ての組み合わせで確かめる。
for i in range(n - 1):
    for j in range(i+1,n):
        direction1 = ['W','N','S','E']
        direction = []
        for k in range(100):
            direction.append(random.choice(direction1))   
        sample = Dice(direction,array[i],array[j])
        sample.control()
if Dice.check == True:
    print('No')
else:
    print('Yes')
