
from loan_submission import submit_loan_application


try:
    cust_loan_id = submit_loan_application(
        customer_id=6,
        loan_id=3
    )

    print("Loan application submitted successfully!")
    print("Customer Loan ID:", cust_loan_id)

except Exception as error:
    print("Loan application failed!")
    print("Error:", error)
