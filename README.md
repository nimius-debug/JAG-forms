# paystub-generator
The Paystub Generator is a Python application that generates pay stubs as PDF files using the ReportLab library.
## Installation
Before running the application, you need to install ReportLab. You can install it via pip:
```bash
pip install requierment.txt
```
## Usage
The Paystub Generator expects data in the form of a dictionary, where each key-value pair corresponds to a piece of information to be included on the pay stub. Here's an example of what the input data might look like:
```python
data = {
    "company_name": "John Doe Inc.",
    "address": "123 north street, New York, NY 10001",
    "check_no": '106',
    "employee_information":"Jane Doe",
    "ssn":" ***-**-1234",
    "reporting_period":"4/21/2023 - 5/5/2023",
    "EmployeeID":'146',
    "pay_date": "5/5/2023",
    "rate": 25.00,
    "hours": 200.00,
    "ytd_gross": 6000.00,
    "ytd_net": 6000.00,
    "current_total_deductions": 0.0,
    "gross_pay": 600.00,
    "ytd_deductions": 0.0,
    "net_pay": 600.00,
    "federal_tax": 0.0,
    "state_tax": 0.0,
    "social_security_dectuctions": 0.0,
    "other_deductions": 0.0,
}
```

To generate a pay stub, call the create_pay_stub function with the name of the PDF file you want to generate and the data dictionary:
```bash
create_pay_stub("pay_stub.pdf", data)
```
This will create a PDF file named pay_stub.pdf with the provided pay stub information.
## Customization
You can customize the pay stub by modifying the create_pay_stub function in the script. This function determines how the pay stub is laid out and what information is included.