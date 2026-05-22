class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.locked = False
        self.failed_attempts = 0

accounts = {}

def create():
    name = input('> CREATE Account: ')
    
    if name in accounts:
        print('Error, Account already exists')
    else:
        accounts[name] = BankAccount(name)
        print(f'Account created. Balance £0')

def deposit():
    deposit_account = input('> ACCOUNT: ')
    deposit_amount = int(input('> DEPOSIT Amount: '))

    if deposit_account in accounts:

        account = accounts[deposit_account]
        account.balance += deposit_amount
        print(f'£{deposit_amount} deposited into {account.name}. Balance: £{account.balance} 💰')

    else:
        print('Error, Account does not exist')

def withdraw():
    withdraw_account = input('> ACCOUNT: ')
    withdraw_amount = int(input('> WITHDRAW Amount: '))
    
    if withdraw_account in accounts:
        account = accounts[withdraw_account]
    else:
        print('Account does not exist')

    if account.locked == False:

        if account.balance >= withdraw_amount:
            account.balance -= withdraw_amount
            print(f'Withdrawn £{withdraw_amount} from {account.name}. Balance: £{account.balance} 💰')
        else:
            print(f'❌ INSUFFICIENT FUNDS. Balance: £{account.balance}')
            account.failed_attempts += 1
                
            if account.failed_attempts >= 3:
                account.locked = True

    
    else:
        print('ACCOUNT LOCKED 🔒🚨')

def transfer():
    source_accounts = input('> SOURCE Account: ')
    destination_accounts = input('> DESTINATION Account: ')
    transfer_amount = int(input('> AMOUNT: '))

    if source_accounts in accounts and destination_accounts in accounts:

        source_account = accounts[source_accounts]
        destination_account = accounts[destination_accounts]

        if source_account.balance >= transfer_amount:
            
            source_account.balance -= transfer_amount
            destination_account.balance += transfer_amount
            print(f'Transfered £{transfer_amount}, from {source_account.name} to {destination_account.name}')

        else:
            print('❌ INSUFFICIENT FUNDS.')

    else:
        print('Make sure account exists & inputed correctly')

def unlock():
    password = "hack3r"
    unlock_account = input('> ACCOUNT: ')
    unlock_input = input('> ENTER Password: ')

    if unlock_account in accounts:
        account = accounts[unlock_account]
    else:
        print('Account does not exist')

    if unlock_input == password:
        account.locked = False
    else:
        print('Incorrect password...')



actions = {
    'create': create,
    'deposit': deposit,
    'withdraw': withdraw,
    'transfer': transfer,
    'unlock': unlock
}

while True:

    options = '/'.join(actions)
    action = input(f'\n> ACTION ({options}/quit): ').lower()

    if action == 'quit':
        break

    elif action in actions:
        actions[action]()
    
    else:
        print('Unknown command, please try again.')
