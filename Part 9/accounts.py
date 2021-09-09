import datetime
import pytz


class Account:
    """ Simple account class with __balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more than your account __balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdraw"
                amount *= -1
            print("{:5} {} on {} (local time was {}]".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    taj = Account("Taj", 0)
    taj.show_balance()

    taj.deposit(1000)
    # taj.show_balance()
    taj.withdraw(400)
    # taj.show_balance()

    taj.withdraw(2000)
    taj.show_transactions()

    vante = Account("Vante", 900)
    vante.deposit(100)
    vante.withdraw(200)
    vante.show_transactions()
    vante.show_balance()
    print(vante.__dict__)
    vante._Account__balance = 40
    vante.show_balance()
