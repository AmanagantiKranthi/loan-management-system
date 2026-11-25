
from db import get_connection


def submit_loan_application(customer_id, loan_id):

    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO customer_loans
            (
                cust_id,
                loan_id,
                loan_amount,
                outstanding_amount
            )
            SELECT
                c.cust_id,
                l.loan_id,
                c.required_loan_amt,
                0
            FROM customers c
            CROSS JOIN loan_offers l
            WHERE c.cust_id = %s
              AND l.loan_id = %s
              AND c.required_loan_amt
                  BETWEEN l.start_amount AND l.end_amount
              AND c.cust_cibil_score
                  BETWEEN l.cibil_score_start AND l.cibil_score_end
            RETURNING cust_loan_id
        """

        cursor.execute(query, (customer_id, loan_id))

        result = cursor.fetchone()

        if result is None:
            raise ValueError(
                "Customer is not eligible for this loan offer."
            )

        cust_loan_id = result[0]

        connection.commit()

        return cust_loan_id

    except Exception:
        if connection is not None:
            connection.rollback()
        raise

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
