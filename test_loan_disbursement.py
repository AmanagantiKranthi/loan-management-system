
from loan_disbursement import disburse_loan


cust_loan_id = 4

try:
    result = disburse_loan(cust_loan_id)

    print("Loan disbursed successfully!")
    print("Customer Loan ID:", result)
    print("Status: ACTIVE")

except Exception as error:
    print("Loan disbursement failed!")
    print("Error:", error)
