
import json
import random
import string
from pathlib import Path


class Bank:

    database = "data.json"
    data = []

    try:
        if Path(database).exists():
            with open(database, "r") as file:
                data = json.load(file)
        else:
            data = []

    except Exception as err:
        print(f"An error occurred: {err}")
        data = []

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as file:
            json.dump(cls.data, file, indent=4)

    @classmethod
    def __accountgenerate(cls):

        letters = random.choices(
            string.ascii_letters,
            k=3
        )

        numbers = random.choices(
            string.digits,
            k=3
        )

        special = random.choices(
            "!@#$%^&*",
            k=1
        )

        account = letters + numbers + special

        random.shuffle(account)

        return "".join(account)

    @classmethod
    def create_account(cls, name, age, email, pin):

        if age < 18:
            return False, "You must be at least 18 years old."

        if len(pin) != 4 or not pin.isdigit():
            return False, "PIN must contain exactly 4 digits."

        account_number = cls.__accountgenerate()

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": account_number,
            "balance": 0
        }

        cls.data.append(info)
        cls.__update()

        return True, account_number

    @classmethod
    def find_user(cls, account_number, pin):

        for user in cls.data:

            if not isinstance(user, dict):
                continue

            if (
                user.get("accountNo") == account_number
                and user.get("pin") == pin
            ):
                return user

        return None

    @classmethod
    def deposit(cls, account_number, pin, amount):

        user = cls.find_user(
            account_number,
            pin
        )

        if not user:
            return False, "Invalid account number or PIN."

        if amount <= 0:
            return False, "Amount must be greater than 0."

        if amount > 10000:
            return False, "You can deposit a maximum of Rs. 10000."

        user["balance"] += amount

        cls.__update()

        return True, user["balance"]

    @classmethod
    def withdraw(cls, account_number, pin, amount):

        user = cls.find_user(
            account_number,
            pin
        )

        if not user:
            return False, "Invalid account number or PIN."

        if amount <= 0:
            return False, "Amount must be greater than 0."

        if amount > user["balance"]:
            return False, "Insufficient balance."

        user["balance"] -= amount

        cls.__update()

        return True, user["balance"]

    @classmethod
    def get_details(cls, account_number, pin):

        return cls.find_user(
            account_number,
            pin
        )

    @classmethod
    def update_details(
        cls,
        account_number,
        pin,
        name,
        email,
        new_pin
    ):

        user = cls.find_user(
            account_number,
            pin
        )

        if not user:
            return False, "Invalid account number or PIN."

        if name:
            user["name"] = name

        if email:
            user["email"] = email

        if new_pin:

            if len(new_pin) != 4 or not new_pin.isdigit():
                return False, "PIN must contain exactly 4 digits."

            user["pin"] = new_pin

        cls.__update()

        return True, "Details updated successfully."

    @classmethod
    def delete_account(cls, account_number, pin):

        user = cls.find_user(
            account_number,
            pin
        )

        if not user:
            return False, "Invalid account number or PIN."

        cls.data.remove(user)

        cls.__update()

        return True, "Account deleted successfully."

