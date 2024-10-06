import threading

class BankAccount:
    def __init__(self):
        self.balance = 1000  # Начальный баланс
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited {amount}, new balance is {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}, new balance is {self.balance}")
            else:
                print(f"Insufficient funds to withdraw {amount}, current balance is {self.balance}")

def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)

# Создаем объект банковского счета
account = BankAccount()

# Создаем потоки для пополнения и снятия денег
deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

# Запускаем потоки
deposit_thread.start()
withdraw_thread.start()

# Дожидаемся завершения потоков
deposit_thread.join()
withdraw_thread.join()

print(f"Final balance is {account.balance}")