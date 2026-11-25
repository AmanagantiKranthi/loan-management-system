
from db import get_connection


def disburse_loan(cust_loan_id):

    connection = None
    cursor = None

    try:
        # Step 1: Connect to PostgreSQL
        connection = get_connection()
        cursor = connection.cursor()

        # Step 2: Fetch loan application
        select_query = """
            SELECT
                cust_loan_id,
                cust_id,
                loan_amount,
                outstanding_amount,
                status
            FROM customer_loans
            WHERE cust_loan_id = %s
        """

        cursor.execute(select_query, (cust_loan_id,))

        application = cursor.fetchone()

        # Step 3: Check application exists
        if application is None:
            raise ValueError(
                f"Loan application ID {cust_loan_id} not found"
            )

        # Step 4: Validate application status
        current_status = application[4]

        if current_status != "APPROVED":
            raise ValueError(
                f"Only APPROVED loans can be disbursed. "
                f"Current status: {current_status}"
            )

        # Step 5: Update loan disbursement details
        update_query = """
            UPDATE customer_loans
            SET
                status = 'ACTIVE',
                outstanding_amount = loan_amount
            WHERE cust_loan_id = %s
              AND status = 'APPROVED'
            RETURNING cust_loan_id
        """

        cursor.execute(update_query, (cust_loan_id,))

        result = cursor.fetchone()

        # Step 6: Verify update
        if result is None:
            raise ValueError(
                "Loan disbursement failed. "
                "Application status may have changed."
            )

        # Step 7: Commit transaction
        connection.commit()

        return result[0]

    except Exception:
        # Step 8: Rollback transaction
        if connection is not None:
            connection.rollback()

        raise

    finally:
        # Step 9: Close database resources
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
