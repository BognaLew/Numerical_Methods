class fusionAlgorithm:
    numberOfActions = 0
    money = 0

    def __init__(self, numberOfActions, money):
        self.numberOfActions = numberOfActions
        self.money = money

    def decide(self, macdDayBefore, macdToday, signalDayBefore, signalToday, price):
        if macdDayBefore < signalDayBefore and macdToday >= signalToday and self.money >= 2*price:
            #BUYING
            rest = (self.money/2) % price
            moneyToSpent = self.money/2 - rest
            self.numberOfActions += (moneyToSpent / price)
            self.money = round(self.money - moneyToSpent, 2)
        elif macdDayBefore > signalDayBefore and macdToday <= signalToday and self.numberOfActions > 0:
            #SELLING
            self.money += self.numberOfActions * price
            self.money = round(self.money, 2)
            self.numberOfActions = 0
        return

    def printWallet(self, price, valueAtBegining):
        print("Number of actions in the wallet: " + str(self.numberOfActions))
        print("Money in the wallet: " + str(self.money))
        value = round(self.money + self.numberOfActions * price, 2)
        print("Total value: " + str(value))
        income = (-valueAtBegining + value) * 100 / valueAtBegining
        print("Income: " + str(round(income, 2)) + "%")
        return
