
from loan_repayment import make_loan_payment


cust_loan_id = 1
payment_amount = 1000


try:
    result = make_loan_payment(
        cust_loan_id,
        payment_amount
    )

    print("Loan repayment successful!")
    print("Payment ID:", result["payment_id"])
    print("Customer Loan ID:", result["cust_loan_id"])
    print("Payment Amount:", result["payment_amount"])
    print("Remaining Outstanding:", result["outstanding_amount"])

except Exception as error:
    print("Loan repayment failed!")
    print("Error:", error)



