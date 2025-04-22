"""
Description: A client program written to verify correctness of 
the BankAccount and Client classes.
Author: ACE Faculty
Edited by: Christian Martin
Date: 12 Sep 2024
"""
from bank_account.bank_account import BankAccount
from client.client import Client
from email_validator import EmailNotValidError
import logging

logging.basicConfig(level=logging.DEBUG)

def main():
    """Test the functionality of the methods encapsulated in the BankAccount and Client classes.
    """ 
    
    # 1. Code a statement which creates a valid instance of the Client class.
    # Use your own unique valid values for the inputs to the class.

    try:
        client = Client(client_number=322680, first_name="Christian", last_name="Martin", email_address="cmartin60@gmail.com")
        print(client)
    except ValueError:
        print(ValueError)
    except EmailNotValidError:
        print(EmailNotValidError)

    # 2. Declare a BankAccount object with an initial value of None.

    bank_account = None

    # 3. Using the bank_account object declared in step 2, code a statement 
    # to instantiate the BankAccount object.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use a floating point value for the balance.

    try:
        bank_account = BankAccount(account_number=101, client_number=client.client_number, balance=1000.50, date_created = ())
        logging.debug(f"Bank Account created: {bank_account}")
        print(bank_account)
    except ValueError:
        print(ValueError)

    print(f"Client: {client}")
    print(f"Bank Account: {bank_account}")

    # 6. Attempt to deposit a non-numeric value into the BankAccount created in step 3.
    try:
        bank_account.deposit("alert")
        print(bank_account)
    except Exception as error:
        print(f"Error: {error}")

    # 7. Attempt to deposit a negative value into the BankAccount created in step 3.
    try:
        bank_account.deposit(-100.00)
        print(bank_account)
    except Exception as error:
        print(f"Error: {error}")

    # 8. Attempt to withdraw a valid amount of your choice from the BankAccount created in step 3.
    try:
        bank_account.withdraw(200.00)
        print(f"Successful withdrawal: {bank_account}")
    except Exception as error:
        print(f"Error: {error}")

    # 9. Attempt to withdraw a non-numeric value from the BankAccount created in step 3.
    try:
        bank_account.withdraw("500 ABC")
    except Exception as error:
        print(f"Error: {error}")

    # 10. Attempt to withdraw a negative value from the BankAccount created in step 3.
    try:
        bank_account.withdraw(-50.00)
    except Exception as error:
        print(f"Error: {error}")

    # 11. Attempt to withdraw a value from the BankAccount created in step 3 which 
    try:
        bank_account.withdraw(2000.00)
    except Exception as error:
        print(f"Error: {error}")

    user_input = "os.system('rm -rf /')" 
    try:
        eval(user_input)
    except Exception as error:
        print(f"Error: {error}")

    password = "hardcoded_password_123"
    print(f"Password: {password}")

    logging.debug(f"Sensitive password: {password}")

    # 12. Code a statement which prints the BankAccount instance created in step 3.
    print(f"Bank Account: {bank_account}")

if __name__ == "__main__":
    main()
