"""
Description:Unit tests for the functions in the chatbot module.
Author:Navjot Kaur
Date:13th 03 2024
Usage:These tests verify the behavior and functionality of the chatbot functions, ensuring they perform as expected under different scenarios.
"""
import unittest
from unittest.mock import patch
from src.chatbot import get_account, get_amount,get_balance,make_deposit


class ChatbotTests(unittest.TestCase):
    def test_get_account_valid(self):
        # Arrange
        with patch("builtins.input", return_value="123456"):
            # Act
            account_number = get_account()
        
        # Assert
        self.assertEqual(account_number, 123456)

    def test_get_account_non_numeric(self):
        # Arrange
        with patch("builtins.input", return_value="non_numeric_data"):
            # Act and Assert
            with self.assertRaises(ValueError) as context:
                get_account()
            self.assertEqual(str(context.exception), "Account number must be a whole number.")

    def test_get_account_not_exist(self):
        # Arrange
        with patch("builtins.input", return_value="112233"):
            # Act and Assert
            with self.assertRaises(ValueError) as context:
                get_account()
            self.assertEqual(str(context.exception), "Account number does not exist.")
     def test_get_amount_valid(self):
        # Arrange
        with patch("builtins.input", return_value="500.01"):
            # Act
            amount = get_amount()
        
        # Assert
        self.assertEqual(amount, 500.01)

    def test_get_amount_non_numeric(self):
        # Arrange
        with patch("builtins.input", return_value="non_numeric_data"):
            # Act and Assert
            with self.assertRaises(ValueError) as context:
                get_amount()
            self.assertEqual(str(context.exception), "Invalid amount. Amount must be numeric.")

    def test_get_amount_negative(self):
        # Arrange
        with patch("builtins.input", return_value="-100"):
            # Act and Assert
            with self.assertRaises(ValueError) as context:
                get_amount()
            self.assertEqual(str(context.exception), "Invalid amount. Please enter a positive number.")
     def test_get_balance_valid(self):
        # Arrange
        account_number = 123456

        # Act
        balance_message = get_balance(account_number)

        # Assert
        self.assertEqual(balance_message, 'Your current balance for account 123456 is $1000.00.')

    def test_get_balance_nonexistent_account(self):
        # Arrange
        account_number = 112233

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            get_balance(account_number)
        self.assertEqual(str(context.exception), "Account number does not exist.") 
    def test_make_deposit_valid(self):
        # Arrange
        account_number = 123456
        ACCOUNTS[account_number] = {"balance": 1000.0}
        deposit_amount = 1500.01

        # Act
        deposit_message = make_deposit(account_number, deposit_amount)

        # Assert
        self.assertEqual(ACCOUNTS[account_number]["balance"], 2500.01)
        self.assertEqual(deposit_message, 'You have made a deposit of $1500.01 to account 123456.')

    def test_make_deposit_nonexistent_account(self):
        # Arrange
        account_number = 112233
        deposit_amount = 1500.01

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            make_deposit(account_number, deposit_amount)
        self.assertEqual(str(context.exception), "Account number does not exist.")

    def test_make_deposit_negative_amount(self):
        # Arrange
        account_number = 123456
        deposit_amount = -50.01

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            make_deposit(account_number, deposit_amount)
        self.assertEqual(str(context.exception), "Invalid Amount. Amount must be positive.") 
        def test_user_selection_lowercase(self):
        # Arrange
        with patch("builtins.input", return_value="balance"):
            # Act
            selection = user_selection()
        
        # Assert
        self.assertEqual(selection, "balance")

    def test_user_selection_uppercase(self):
        # Arrange
        with patch("builtins.input", return_value="DEPOSIT"):
            # Act
            selection = user_selection()
        
        # Assert
        self.assertEqual(selection, "deposit")

    def test_user_selection_invalid(self):
        # Arrange
        with patch("builtins.input", return_value="invalid_selection"):
            # Act and Assert
            with self.assertRaises(ValueError) as context:
                user_selection()
            self.assertEqual(str(context.exception), "Invalid task. Please choose balance, deposit, or exit.")
              
if __name__ == '__main__':
    unittest.main()
