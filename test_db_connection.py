
from db import get_connection


def test_database_connection():

    connection = None
    cursor = None

    try:
        # Get database connection
        connection = get_connection()

        # Create cursor
        cursor = connection.cursor()

        # Execute test query
        cursor.execute("""
            SELECT
                current_database(),
                current_user,
                version();
        """)

        result = cursor.fetchone()

        print("Database connection successful!")
        print("Database:", result[0])
        print("User:", result[1])
        print("PostgreSQL Version:", result[2])

    except Exception as error:
        print("Database connection failed!")
        print("Error:", error)

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()

        print("Database connection closed.")


if __name__ == "__main__":
    test_database_connection()
