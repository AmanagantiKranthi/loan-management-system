
from db import get_connection


def get_payment_history(cust_loan_id):

    connection = None
    cursor = None

    try:
        # Step 1: Validate Loan ID
        if cust_loan_id <= 0:
            raise ValueError(
                "Customer Loan ID must be greater than zero."
            )

        # Step 2: Connect to PostgreSQL
        connection = get_connection()
        cursor = connection.cursor()

        # Step 3: Fetch payment history
        select_query = """
            SELECT
                payment_id,
                cust_loan_id,
                amount_paid,
                payment_date
            FROM customer_loan_payments
            WHERE cust_loan_id = %s
            ORDER BY payment_date, payment_id
        """

        cursor.execute(
            select_query,
            (cust_loan_id,)
        )

        payments = cursor.fetchall()

        # Step 4: Check payment records
        if not payments:
            return []

        # Step 5: Convert records into dictionaries
        payment_history = []

        for payment in payments:

            payment_record = {
                "payment_id": payment[0],
                "cust_loan_id": payment[1],
                "amount_paid": payment[2],
                "payment_date": payment[3]
            }

            payment_history.append(payment_record)

        # Step 6: Return payment history
        return payment_history

    except Exception:
        raise

    finally:
        # Step 7: Close database resources
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
