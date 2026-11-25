
from loan_application import check_loan_eligibility


offers = check_loan_eligibility(
    customer_id=6,
    loan_type="PERSONAL"
)

if offers:
    print("\nELIGIBLE LOAN OFFERS")
    print("-" * 40)

    for offer in offers:
        print("Customer:", offer[1])
        print("CIBIL Score:", offer[2])
        print("Loan ID:", offer[4])
        print("Loan Type:", offer[5])
        print("Interest Rate:", offer[6])
        print("Duration:", offer[7], "months")
        print("-" * 40)

else:
    print("No eligible loan offers found.")
