
from loan_approval import approve_loan_application


cust_loan_id = 4
decision = "APPROVED"

try:
    result = approve_loan_application(
        cust_loan_id,
        decision
    )

    print("Loan application processed successfully!")
    print("Customer Loan ID:", result)
    print("Decision:", decision)

except Exception as error:
    print("Loan approval failed!")
    print("Error:", error)
