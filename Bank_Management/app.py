
import streamlit as st
from main import Bank


st.set_page_config(
    page_title="Bank Management System",
    layout="wide"
)


st.sidebar.title("Bank Management System")

option = st.sidebar.radio(
    "Select Operation",
    [
        "Home",
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Account Details",
        "Update Details",
        "Delete Account"
    ]
)


if option == "Home":

    st.title("Bank Management System")

    st.write(
        "Manage your bank account using the options provided in the sidebar."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Accounts",
            len(Bank.data)
        )

    with col2:
        total_balance = sum(
            user["balance"] for user in Bank.data
        )

        st.metric(
            "Total Balance",
            f"Rs. {total_balance}"
        )

    with col3:
        st.metric(
            "Bank Status",
            "Active"
        )


elif option == "Create Account":

    st.title("Create Account")

    name = st.text_input("Full Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        step=1
    )

    email = st.text_input("Email")

    pin = st.text_input(
        "PIN",
        type="password",
        max_chars=4
    )

    if st.button("Create Account"):

        if not name or not email or not pin:
            st.warning("Please fill all the fields.")

        elif age < 18:
            st.error("You must be at least 18 years old.")

        elif len(pin) != 4 or not pin.isdigit():
            st.error("PIN must contain exactly 4 digits.")

        else:

            success, account_number = Bank.create_account(
                name,
                age,
                email,
                pin
            )

            if success:

                st.success("Account created successfully.")

                st.info(
                    f"Your account number is: {account_number}"
                )

                st.write(
                    "Please save your account number."
                )


elif option == "Deposit Money":

    st.title("Deposit Money")

    account_number = st.text_input("Account Number")

    pin = st.text_input(
        "PIN",
        type="password"
    )

    amount = st.number_input(
        "Amount",
        min_value=0,
        step=100
    )

    if st.button("Deposit"):

        success, result = Bank.deposit(
            account_number,
            pin,
            amount
        )

        if success:

            st.success(
                f"Rs. {amount} deposited successfully."
            )

            st.write(
                f"Current Balance: Rs. {result}"
            )

        else:
            st.error(result)


elif option == "Withdraw Money":

    st.title("Withdraw Money")

    account_number = st.text_input("Account Number")

    pin = st.text_input(
        "PIN",
        type="password"
    )

    amount = st.number_input(
        "Amount",
        min_value=0,
        step=100
    )

    if st.button("Withdraw"):

        success, result = Bank.withdraw(
            account_number,
            pin,
            amount
        )

        if success:

            st.success(
                f"Rs. {amount} withdrawn successfully."
            )

            st.write(
                f"Remaining Balance: Rs. {result}"
            )

        else:
            st.error(result)


elif option == "Account Details":

    st.title("Account Details")

    account_number = st.text_input("Account Number")

    pin = st.text_input(
        "PIN",
        type="password"
    )

    if st.button("View Details"):

        user = Bank.get_details(
            account_number,
            pin
        )

        if user:

            st.write("Name:", user["name"])
            st.write("Age:", user["age"])
            st.write("Email:", user["email"])
            st.write("Account Number:", user["accountNo"])
            st.write("Balance:", f"Rs. {user['balance']}")

        else:

            st.error(
                "Invalid account number or PIN."
            )


elif option == "Update Details":

    st.title("Update Account Details")

    account_number = st.text_input("Account Number")

    pin = st.text_input(
        "Current PIN",
        type="password"
    )

    new_name = st.text_input("New Name")

    new_email = st.text_input("New Email")

    new_pin = st.text_input(
        "New PIN",
        type="password",
        max_chars=4
    )

    if st.button("Update Details"):

        success, message = Bank.update_details(
            account_number,
            pin,
            new_name,
            new_email,
            new_pin
        )

        if success:
            st.success(message)

        else:
            st.error(message)


elif option == "Delete Account":

    st.title("Delete Account")

    account_number = st.text_input("Account Number")

    pin = st.text_input(
        "PIN",
        type="password"
    )

    confirm = st.checkbox(
        "I want to delete my account."
    )

    if st.button("Delete Account"):

        if not confirm:

            st.warning(
                "Please confirm account deletion."
            )

        else:

            success, message = Bank.delete_account(
                account_number,
                pin
            )

            if success:
                st.success(message)

            else:
                st.error(message)

