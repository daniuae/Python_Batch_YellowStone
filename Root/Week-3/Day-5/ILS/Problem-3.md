# Case Study: Bank Account Management System

## Objective

Build a secure Bank Account Management System using **Encapsulation** and **Private Members** to protect sensitive account information such as account number and balance.

---

# Learning Outcomes

By completing this case study, you will learn:

* Encapsulation in Python
* Private Attributes (`__variable`)
* Private Methods (`__method`)
* Public Methods
* Data Hiding
* Account Security
* Input Validation
* Real-world OOP Design

---

# Step 1: Create a New Python File

Create a file named:

```text
bank_account.py
```

---

# Step 2: Define the BankAccount Class

Create a class with private attributes.

```python
class BankAccount:

    def __init__(self, account_number, account_holder, initial_balance):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = initial_balance
```

---

## Explanation

| Attribute          | Purpose                |
| ------------------ | ---------------------- |
| `__account_number` | Stores account number  |
| `__account_holder` | Stores customer name   |
| `__balance`        | Stores account balance |

### Why Use Double Underscores?

```python
self.__balance
```

The double underscore (`__`) makes the variable private.

This prevents direct modification from outside the class.

---

# Step 3: Add a Public Method to Display Account Details

```python
def get_account_details(self):
    return (
        f"Account Number: {self.__account_number}, "
        f"Account Holder: {self.__account_holder}"
    )
```

---

## Explanation

This method provides controlled access to private data.

Example:

```python
print(account.get_account_details())
```

Output:

```text
Account Number: 12345, Account Holder: Alice
```

---

# Step 4: Add a Method to Check Balance

```python
def check_balance(self):
    return self.__balance
```

---

## Explanation

Since balance is private, users must use this method.

Example:

```python
print(account.check_balance())
```

Output:

```text
1000
```

---

# Step 5: Add a Deposit Method

```python
def deposit(self, amount):

    if amount > 0:
        self.__balance += amount

        print(
            f"Deposited ${amount}. "
            f"New Balance: ${self.__balance}"
        )

    else:
        print("Deposit amount must be positive.")
```

---

## Test Deposit

```python
account.deposit(500)
```

Output:

```text
Deposited $500. New Balance: $1500
```

---

# Step 6: Add a Withdrawal Method

```python
def withdraw(self, amount):

    if 0 < amount <= self.__balance:

        self.__balance -= amount

        print(
            f"Withdrew ${amount}. "
            f"New Balance: ${self.__balance}"
        )

    else:
        print(
            "Insufficient funds or invalid withdrawal amount."
        )
```

---

## Test Withdrawal

```python
account.withdraw(300)
```

Output:

```text
Withdrew $300. New Balance: $1200
```

---

# Step 7: Test Insufficient Balance

```python
account.withdraw(1500)
```

Output:

```text
Insufficient funds or invalid withdrawal amount.
```

---

# Step 8: Add a Private Helper Method

Private methods should only be used internally.

```python
def __calculate_interest(self):
    return self.__balance * 0.02
```

---

## Explanation

This method calculates:

```text
2% interest on balance
```

Example:

```text
Balance = 1200
Interest = 24
```

---

# Step 9: Test Private Access

Attempt to access a private variable directly.

```python
account = BankAccount(
    12345,
    "Alice",
    1000
)

print(account.__balance)
```

Output:

```text
AttributeError:
'BankAccount' object has no attribute '__balance'
```

---

## Why Does This Happen?

Private variables cannot be accessed outside the class.

This is called:

### Encapsulation

The object's internal data is protected from external modification.

---

# Step 10: Use Getter Method

Use the public method instead.

```python
print(
    f"Balance: ${account.check_balance()}"
)
```

Output:

```text
Balance: $1000
```

---

# Step 11: Add Public Interest Calculation

Use the private helper method internally.

```python
def calculate_interest(self):

    return (
        f"Interest on current balance: "
        f"${self.__calculate_interest():.2f}"
    )
```

---

## Test Interest Calculation

```python
print(account.calculate_interest())
```

Output:

```text
Interest on current balance: $24.00
```

---

# Step 12: Add Account Locking Feature

Enhance security.

Add the following variable inside constructor.

```python
self.__is_locked = False
```

---

## Lock Account Method

```python
def lock_account(self):

    self.__is_locked = True

    print("Account locked.")
```

---

## Unlock Account Method

```python
def unlock_account(self):

    self.__is_locked = False

    print("Account unlocked.")
```

---

# Step 13: Prevent Transactions When Locked

Modify the withdrawal method.

```python
def withdraw(self, amount):

    if self.__is_locked:

        print(
            "Transaction denied. "
            "Account is locked."
        )
        return

    if 0 < amount <= self.__balance:

        self.__balance -= amount

        print(
            f"Withdrew ${amount}. "
            f"New Balance: ${self.__balance}"
        )

    else:
        print(
            "Insufficient funds or invalid withdrawal amount."
        )
```

---

# Step 14: Test Account Locking

```python
account.lock_account()

account.withdraw(100)

account.unlock_account()

account.withdraw(100)
```

---

## Expected Output

```text
Account locked.
Transaction denied. Account is locked.
Account unlocked.
Withdrew $100. New Balance: $1100
```

---

# Complete Program

```python
class BankAccount:

    def __init__(
        self,
        account_number,
        account_holder,
        initial_balance
    ):

        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = initial_balance

        self.__is_locked = False

    def get_account_details(self):

        return (
            f"Account Number: {self.__account_number}, "
            f"Account Holder: {self.__account_holder}"
        )

    def check_balance(self):
        return self.__balance

    def deposit(self, amount):

        if self.__is_locked:
            print(
                "Transaction denied. "
                "Account is locked."
            )
            return

        if amount > 0:

            self.__balance += amount

            print(
                f"Deposited ${amount}. "
                f"New Balance: ${self.__balance}"
            )

        else:
            print(
                "Deposit amount must be positive."
            )

    def withdraw(self, amount):

        if self.__is_locked:

            print(
                "Transaction denied. "
                "Account is locked."
            )
            return

        if 0 < amount <= self.__balance:

            self.__balance -= amount

            print(
                f"Withdrew ${amount}. "
                f"New Balance: ${self.__balance}"
            )

        else:

            print(
                "Insufficient funds or "
                "invalid withdrawal amount."
            )

    def __calculate_interest(self):
        return self.__balance * 0.02

    def calculate_interest(self):

        return (
            f"Interest on current balance: "
            f"${self.__calculate_interest():.2f}"
        )

    def lock_account(self):

        self.__is_locked = True

        print("Account locked.")

    def unlock_account(self):

        self.__is_locked = False

        print("Account unlocked.")


def main():

    account = BankAccount(
        12345,
        "Alice",
        1000
    )

    print(account.get_account_details())

    print(
        f"Balance: "
        f"${account.check_balance()}"
    )

    account.deposit(500)

    account.withdraw(300)

    account.withdraw(1500)

    print(account.calculate_interest())

    account.lock_account()

    account.withdraw(100)

    account.unlock_account()

    account.withdraw(100)

    print(
        f"Final Balance: "
        f"${account.check_balance()}"
    )


if __name__ == "__main__":
    main()
```

---

# Sample Output

```text
Account Number: 12345, Account Holder: Alice
Balance: $1000

Deposited $500. New Balance: $1500

Withdrew $300. New Balance: $1200

Insufficient funds or invalid withdrawal amount.

Interest on current balance: $24.00

Account locked.

Transaction denied. Account is locked.

Account unlocked.

Withdrew $100. New Balance: $1100

Final Balance: $1100
```

---

# Real-World Banking Features Demonstrated

| Feature              | Implemented |
| -------------------- | ----------- |
| Encapsulation        | ✅           |
| Private Variables    | ✅           |
| Private Methods      | ✅           |
| Deposit              | ✅           |
| Withdraw             | ✅           |
| Balance Inquiry      | ✅           |
| Interest Calculation | ✅           |
| Account Locking      | ✅           |
| Security Controls    | ✅           |
| Input Validation     | ✅           |

---

# Key Concepts Learned

✅ Object-Oriented Programming (OOP)

✅ Encapsulation

✅ Private Attributes

✅ Private Methods

✅ Getter Methods

✅ Secure Data Access

✅ Banking Transactions

✅ Business Rules

✅ Account Security

✅ Real-World Application Design

---

# Challenge Exercises

### Exercise 1

Add a transfer method to transfer money between two accounts.

---

### Exercise 2

Add a transaction history feature.

---

### Exercise 3

Add a PIN-based authentication system.

---

### Exercise 4

Add a minimum balance requirement.

---

### Exercise 5

Add a savings account class using inheritance.
