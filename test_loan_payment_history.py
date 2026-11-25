
from loan_repayment import make_loan_payment


# TC-02: Payment exceeds outstanding balance

cust_loan_id = 4
payment_amount = 450000

print("Testing Excess Payment Validation")
print("Loan ID:", cust_loan_id)
print("Payment Amount:", payment_amount)

try:
    result = make_loan_payment(
        cust_loan_id,
        payment_amount
    )

    print("Unexpected Success!")
    print("Result:", result)

except Exception as error:
    print("Loan repayment failed!")
    print("Error:", error)
