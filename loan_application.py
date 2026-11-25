
from db import get_connection


def check_loan_eligibility(customer_id, loan_type):

    connection = None
    cursor = None

    try:
        # Step 1: Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        # Step 2: Find matching loan offers
        query = """
            SELECT
                c.cust_id,
                c.cust_name,
                c.cust_cibil_score,
                c.required_loan_amt,
                l.loan_id,
                l.loan_type,
                l.interest_rate,
                l.duration_months
            FROM customers c
            CROSS JOIN loan_offers l
            WHERE c.cust_id = %s
              AND l.loan_type = %s
              AND c.required_loan_amt
                  BETWEEN l.start_amount AND l.end_amount
              AND c.cust_cibil_score
                  BETWEEN l.cibil_score_start AND l.cibil_score_end
            ORDER BY l.interest_rate ASC, l.loan_id
        """

        # Step 3: Execute query
        cursor.execute(query, (customer_id, loan_type.upper()))

        # Step 4: Fetch eligible offers
        eligible_offers = cursor.fetchall()

        return eligible_offers

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
