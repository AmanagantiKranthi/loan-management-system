
from customer import add_customer


try:
    customer_id = add_customer(
        cust_name="Ravi Kumar",
        cust_cibil_score=750,
        required_loan_amt=500000
    )

    print("Customer registered successfully!")
    print("Customer ID:", customer_id)

except Exception as error:
    print("Customer registration failed!")
    print("Error:", error)
