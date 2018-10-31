import datetime
import pytz


class Account:
    """Add, subtract, and show balance of account"""
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_log = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited {}, balance is ".format(amount) + str(self.__balance))
            self._transaction_log.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if self.__balance > amount > 0:
            self.__balance -= amount
            print("Withdrew {}, balance is ".format(amount) + str(self.__balance))
            self._transaction_log.append((Account._current_time(), -amount))
        else:
            print("Insufficient funds, cannot withdraw {}, balance is ".format(amount) + str(self.__balance))

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transaction_log(self):
        for date, amount in self._transaction_log:
            if amount >= 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":
    tim = Account("checking", 0)
    # tim.show_balance()
    tim.deposit(1000)
    tim.withdraw(10000)
    tim.withdraw(500)
    tim.deposit(5500)
    tim.show_balance()
    tim.show_transaction_log()

    john = Account("checking", 800)
    john.deposit(100)
    john.withdraw(200)
    john.show_transaction_log()
    # Hacks, re-factor methods to single underscore show they are for internal use only
    # Double underscore "hides" attribute by mangling it
    john.__balance = 25000
    john.show_balance()
    print(john.__dict__)
    john._Account__balance = 25000
    john.show_balance()
