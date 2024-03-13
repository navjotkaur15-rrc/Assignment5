"""
Description: Chatbot application.  Allows user to perform 
balance inquiries and make deposits to their accounts.
Author: Navjot Kaur
Modified by: Navjot Kaur
Date: 2024-03-13
Usage: From the console: python src/chatbot.py
"""

# GIVEN CONSTANT COLLECTIONS
ACCOUNTS = {
    123456: {"balance": 1000.0},
    789012: {"balance": 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

# FUNCTION DEFINITIONS
def get_account() -> int:
    """
    Prompts the user for an account number and returns it as an integer.
    
    Returns:
        int: The user-entered account number.
        
    Raises:
        ValueError: When the account number is not numeric or does not exist.
    """
    try:
        account_number = int(input("Please enter your account number: "))
    except ValueError:
        raise ValueError("Account number must be a whole number.")
    
    if account_number not in ACCOUNTS:
        raise ValueError("Account number entered does not exist.")
    
    return account_number

def user_selection() -> str:
    """
    Prompts the user to select an action and returns the selected action.
    
    Returns:
        str: The selected action (either 'balance', 'deposit', or 'exit').
        
    Raises:
        ValueError: When the user enters an invalid action.
    """
    valid_actions = {"balance", "deposit", "exit"}
    
    while True:
        action = input("Please select an action (balance, deposit, exit): ").lower()
        if action in valid_actions:
            return action
        else:
            print("Invalid action. Please try again.")
def get_amount() -> float:
    """
    Prompts the user for the amount to deposit and returns it as a float.

    Returns:
        float: The user-entered amount.

    Raises:
        ValueError: When the amount is not numeric or is zero/negative.
    """
    try:
        amount = float(input("Enter the transaction amount: "))
    except ValueError:
        raise ValueError("Invalid amount. Amount must be numeric.")
    
    if amount <= 0:
        raise ValueError("Invalid amount. Please enter a positive number.")
    
    return amount
def get_balance(account: int) -> str:
    """
    Retrieves the balance of a specified account.

    Args:
        account (int): The account number.

    Returns:
        str: A message containing the account number and its balance.

    Raises:
        ValueError: When the account number does not exist.
    """
    if account not in ACCOUNTS:
        raise ValueError("Account number does not exist.")

    balance = ACCOUNTS[account]["balance"]
    return f"Your current balance for account {account} is ${balance:.2f}."


def chatbot():
    '''
    The main program.  Uses the functionality of the functions:
        get_account()
        get_amount()
        get_balance()
        make_deposit()
        user_selection()
    '''

    print("Welcome! I'm the PiXELL River Financial Chatbot!  Let's get chatting!")

    keep_going = True
    while keep_going:
        try:
            # CALL THE user_selection FUNCTION HERE 
            # CAPTURING THE RESULTS IN A VARIABLE CALLED
            # selection:

            selection = user_selection()  
            if selection != "exit":
                
                # Account number validation.
                valid_account = False
                while valid_account == False:
                    try:
                        # CALL THE get_account FUNCTION HERE
                        # CAPTURING THE RESULTS IN A VARIABLE 
                        # CALLED account:


                        valid_account = True
                    except ValueError as e:
                        # Invalid account.
                        print(e)
                if selection == "balance":
                        # CALL THE get_balance FUNCTION HERE
                        # PASSING THE account VARIABLE DEFINED 
                        # ABOVE, AND PRINT THE RESULTS:
                        pass

                else:

                    # Amount validation.
                    valid_amount = False
                    while valid_amount == False:
                        try:
                            # CALL THE get_amount FUNCTION HERE
                            # AND CAPTURE THE RESULTS IN A VARIABLE 
                            # CALLED amount:


                            valid_amount = True
                        except ValueError as e:
                            # Invalid amount.
                            print(e)
                # CALL THE make_deposit FUNCTION HERE PASSING THE 
                # VARIABLES account AND amount DEFINED ABOVE AND 
                # PRINT THE RESULTS:


            else:
                # User selected 'exit'
                keep_going = False
        except ValueError as e:
            # Invalid selection:
            print(e)

    print("Thank you for banking with PiXELL River Financial.")

if __name__ == "__main__":
    chatbot()
