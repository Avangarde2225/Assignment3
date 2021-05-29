def deposit(balance, amount):
    balance += amount
    return balance

def main():
    balance = int(input("Initial balance: "))
    while True:
        amount = int(input("Deposit 0 to quit: "))
        if amount == 0:
            break
        balance = deposit(balance, amount)

if __name__ == '__main__':
    main()