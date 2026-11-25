
from db import get_connection


def approve_loan_application(cust_loan_id, decision):

    # Step 1: Validate decision
    decision = decision.strip().upper()

    if decision not in ("APPROVED", "REJECTED"):
        raise ValueError(
            "Decision must be APPROVED or REJECTED"
        )

    connection = None
    cursor = None

    try:
        # Step 2: Connect to PostgreSQL
        connection = get_connection()

        # Step 3: Create cursor
        cursor = connection.cursor()

        # Step 4: Fetch loan application
        query = """
            SELECT
                cust_loan_id,
                cust_id,
                loan_amount,
                status
            FROM customer_loans
            WHERE cust_loan_id = %s
        """

        cursor.execute(query, (cust_loan_id,))

        application = cursor.fetchone()

        # Step 5: Check application exists
        if application is None:
            raise ValueError(
                f"Loan application ID {cust_loan_id} not found"
            )

        # Step 6: Validate current application status
        current_status = application[3]

        if current_status != "APPLIED":
            raise ValueError(
                f"Application cannot be processed. "
                f"Current status: {current_status}"
            )

        # Step 7: Update application status
        update_query = """
            UPDATE customer_loans
            SET
                status = %s,
                granted_at = CASE
                    WHEN %s = 'APPROVED'
                    THEN CURRENT_TIMESTAMP
                    ELSE NULL
                END
            WHERE cust_loan_id = %s
              AND status = 'APPLIED'
            RETURNING cust_loan_id
        """

        cursor.execute(
            update_query,
            (decision, decision, cust_loan_id)
        )

        updated_application = cursor.fetchone()

        # Step 8: Check update result
        if updated_application is None:
            raise ValueError(
                "Application status changed or update failed."
            )

        # Step 9: Commit transaction
        connection.commit()

        return updated_application[0]

    except Exception:
        # Step 10: Rollback if any error occurs
        if connection is not None:
            connection.rollback()

        raise

    finally:
        # Step 11: Close cursor and connection
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
