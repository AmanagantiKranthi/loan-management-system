
from loan_offers import get_loan_offers


try:
    offers = get_loan_offers()

    print("\nAVAILABLE LOAN OFFERS")
    print("-" * 60)

    for offer in offers:
        print("Loan ID:", offer[0])
        print("Loan Type:", offer[1])
        print("Minimum Amount:", offer[2])
        print("Maximum Amount:", offer[3])
        print("Minimum CIBIL:", offer[4])
        print("Maximum CIBIL:", offer[5])
        print("Interest Rate:", offer[6])
        print("Duration:", offer[7], "months")
        print("-" * 60)

except Exception as error:
    print("Unable to retrieve loan offers")
    print("Error:", error)
