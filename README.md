# Loan Management System (LMS)

A Python and PostgreSQL based Loan Management System built using Functional Programming.

## Project Overview

This project implements the end-to-end loan lifecycle, including customer management, loan eligibility, application submission, approval, disbursement, repayment, and payment history.

## Technology Stack

- Python 3.12
- PostgreSQL 16
- pg8000
- python-dotenv
- Docker
- VS Code
- DBeaver

## Programming Approach

The application follows Procedural and Functional Programming.

- Business logic is implemented using Python functions.
- PostgreSQL manages application data.
- Parameterized SQL queries are used.
- Database transactions use commit and rollback.
- No custom classes or OOP concepts are used.

## Database Tables

| Table | Purpose |
|---|---|
| customers | Customer information |
| loan_offers | Loan products and eligibility criteria |
| customer_loans | Loan applications and balances |
| customer_loan_payments | Repayment transactions |

## Project Modules

1. Database Connection
2. Customer Management
3. Loan Offers
4. Loan Eligibility
5. Loan Submission
6. Loan Approval
7. Loan Disbursement
8. Loan Repayment
9. Payment History

## Loan Processing Workflow

Customer Registration → Loan Eligibility → Loan Submission → Loan Approval → Loan Disbursement → Loan Repayment → Payment History

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/AmanagantiKranthi/loan-management-system.git
cd loan-management-system
```

### 2. Create Virtual Environment

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
LMS_DB_PASSWORD=your_database_password
```

Never upload `.env` to GitHub.

### 5. Run Tests

```powershell
python test_db_connection.py
python test_customer.py
python test_loan_offers.py
python test_loan_eligibility.py
python test_loan_submission.py
python test_loan_approval.py
python test_loan_disbursement.py
python test_loan_repayment.py
python test_loan_payment_history.py
```

Run tests against a suitable test database because some tests modify database records.

## Project Objective

To demonstrate a practical database-driven business application using Python Functional Programming and PostgreSQL.

**Repository:** https://github.com/AmanagantiKranthi/loan-management-system
