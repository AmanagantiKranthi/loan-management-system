
from db import get_connection


def make_loan_payment(cust_loan_id, payment_amount):

    connection = None
    cursor = None

    try:
        # Step 1: Validate payment amount
        if payment_amount <= 0:
            raise ValueError(
                "Payment amount must be greater than zero."
            )

        # Step 2: Connect to PostgreSQL
        connection = get_connection()
        cursor = connection.cursor()

        # Step 3: Fetch loan application
        select_query = """
            SELECT
                cust_loan_id,
                loan_amount,
                outstanding_amount,
                status
            FROM customer_loans
            WHERE cust_loan_id = %s
            FOR UPDATE
        """

        cursor.execute(select_query, (cust_loan_id,))

        loan = cursor.fetchone()

        # Step 4: Check loan exists
        if loan is None:
            raise ValueError(
                f"Loan ID {cust_loan_id} not found."
            )

        outstanding_amount = loan[2]
        current_status = loan[3]

        # Step 5: Validate loan status
        if current_status != "ACTIVE":
            raise ValueError(
                f"Payment not allowed. "
                f"Current loan status: {current_status}"
            )

        # Step 6: Validate payment amount
        if payment_amount > outstanding_amount:
            raise ValueError(
                "Payment amount cannot exceed outstanding amount."
            )

        # Step 7: Insert payment record
        insert_query = """
            INSERT INTO customer_loan_payments
            (
                cust_loan_id,
                amount_paid,
                payment_date
            )
            VALUES
            (
                %s,
                %s,
                CURRENT_TIMESTAMP
            )
            RETURNING payment_id
        """

        cursor.execute(
            insert_query,
            (cust_loan_id, payment_amount)
        )

        payment = cursor.fetchone()
        payment_id = payment[0]

        # Step 8: Calculate new outstanding amount
        new_outstanding = outstanding_amount - payment_amount

        # Step 9: Update loan balance and status
        if new_outstanding == 0:

            update_query = """
                UPDATE customer_loans
                SET
                    outstanding_amount = %s,
                    status = 'CLOSED'
                WHERE cust_loan_id = %s
            """

            cursor.execute(
                update_query,
                (new_outstanding, cust_loan_id)
            )

        else:

            update_query = """
                UPDATE customer_loans
                SET outstanding_amount = %s
                WHERE cust_loan_id = %s
            """

            cursor.execute(
                update_query,
                (new_outstanding, cust_loan_id)
            )

        # Step 10: Commit transaction
        connection.commit()

        return {
            "payment_id": payment_id,
            "cust_loan_id": cust_loan_id,
            "payment_amount": payment_amount,
            "outstanding_amount": new_outstanding
        }

    except Exception:

        # Step 11: Rollback transaction
        if connection is not None:
            connection.rollback()

        raise

    finally:

        # Step 12: Close database resources
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
