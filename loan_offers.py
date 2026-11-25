
from db import get_connection


def get_loan_offers():

    connection = None
    cursor = None

    try:
        # Step 1: Connect to database
        connection = get_connection()
        cursor = connection.cursor()

        # Step 2: Retrieve loan offers
        query = """
            SELECT
                loan_id,
                loan_type,
                start_amount,
                end_amount,
                cibil_score_start,
                cibil_score_end,
                interest_rate,
                duration_months
            FROM loan_offers
            ORDER BY loan_id
        """

        cursor.execute(query)

        # Step 3: Fetch all records
        offers = cursor.fetchall()

        return offers

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
