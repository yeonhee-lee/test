import random

class Lotto:
    def __init__(self):
        self.lottery = set()    #lottery num
        self.bonus = set()  #bonus_num
        self.myNum = list()  #input_num

    def init(self):
        self.lottery.clear()
        self.bonus.clear()
        self.myNum.clear()

        while len(self.lottery) < 6:
            self.lottery.add(random.randrange(1,46))

        while True:
            n = random.randrange(1,46)
            if n not in self.lottery: #deduplication
                self.bonus.add(n)
                break

    def inputNum(self):
        print("please enter 6 numbers that do not contains duplicates")
        self.myNum = list(map(int, input().split()))
        l_set = set(self.myNum)
        l_list = list(l_set)

        while len(l_list) < 6: #if duplicate exists
            dif = len(self.myNum) - len(l_list)
            count = abs(dif)
            print("please enter ", count, " more number(s) //duplicate number exists")
            newNum = list(map(int, input().split()))
            l_list.extend(newNum)
            tempSet = set(l_list)
            l_list = list(tempSet)
        self.myNum = l_list

    def printNum(self):
        print("My Lottery Number : ")
        temp = self.myNum
        temp.sort()
        print(temp)

    def printLotto(self):
        print("Real Lottery Number : ")
        temp = list(self.lottery)
        temp.sort()
        temp2 = list(self.bonus)
        print(temp, " + ", temp2)

    def match(self):
        myNumSet = set(self.myNum)
        matchNum = len(self.lottery.intersection(myNumSet))

        if matchNum == 6:
            print("You won 1st place (matching 6 numbers)")
        elif matchNum == 5 and myNumSet.intersection(self.bonus):
            print("You won 2nd place (matching 5 numbers and bonus number)")
        elif matchNum == 5:
            print("You won 3rd place (matching 5 numbers)")
        elif matchNum == 4:
            print("You won 4th place (matching 4 numbers)")
        elif matchNum == 3:
            print("You won 5th place (matching 3 numbers)")
        else:
            print("you have failed")

lotto = Lotto()
lotto.init()
lotto.inputNum()
lotto.match()
lotto.printLotto()
lotto.printNum()