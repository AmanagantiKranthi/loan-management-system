
from decimal import Decimal
from db import get_connection


def add_customer(cust_name, cust_cibil_score, required_loan_amt):

    # Step 1: Validate customer name
    cust_name = cust_name.strip()

    if not cust_name:
        raise ValueError("Customer name cannot be empty")

    # Step 2: Validate CIBIL score
    cust_cibil_score = int(cust_cibil_score)

    if cust_cibil_score < 300 or cust_cibil_score > 900:
        raise ValueError("CIBIL score must be between 300 and 900")

    # Step 3: Validate loan amount
    required_loan_amt = Decimal(str(required_loan_amt))

    if required_loan_amt <= 0:
        raise ValueError("Loan amount must be greater than zero")

    connection = None
    cursor = None

    try:
        # Step 4: Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        # Step 5: Insert customer details
        query = """
            INSERT INTO customers
            (cust_name, cust_cibil_score, required_loan_amt)
            VALUES (%s, %s, %s)
            RETURNING cust_id
        """

        cursor.execute(
            query,
            (cust_name, cust_cibil_score, required_loan_amt)
        )

        # Step 6: Get generated customer ID
        result = cursor.fetchone()
        customer_id = result[0]

        # Step 7: Save transaction
        connection.commit()

        return customer_id

    except Exception:
        if connection is not None:
            connection.rollback()
        raise

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
