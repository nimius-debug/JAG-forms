import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image, ImageDraw, ImageFont
# the rest of your imports and functions here...
from paystub_gen import create_pay_stub
def app():
    st.title('PDF Paystub Generator')
    st.write("The PDF Paystub Generator is a simple and effective tool for generating professional\
             ,printable paystubs in PDF format.")
    
    with st.sidebar:
        st.header("Instructions")
        st.write("Please fill out the form below to generate a paystub.")
        feat = ["Interactive Form", "PDF Generation", "Sidebar Instructions"]
        st.header("Features")
        st.markdown('\n'.join(f'- {item}' for item in feat))
        st.header("How to Use")
        st.write("Once you submit the form, the application will generate a PDF paystub that \
            includes all the details entered. The generated PDF is styled for clarity and professionalism.")
    
    column1, column2 = st.columns(2)
    with column1:
        with st.form(key='my_form'):
            col1, col2 = st.columns(2)

            with col1:
                st.header("Employee Information")
                data = {
                    "company_name": st.text_input('Company Name'),
                    "address": st.text_input('Company Address'),
                    "check_no": st.text_input('Check Number'),
                    "employee_information": st.text_input('Employee Name'),
                    "ssn": st.text_input('SSN', value='***-**-****'),
                    "reporting_period": st.text_input('Reporting Period'),
                    "EmployeeID": st.text_input('Employee ID', value='000'),
                    "pay_date": st.text_input('Pay Date', value='MM-DD-YYYY'),
                    
                }

            with col2:
                st.header("Payment Information")
                data.update({
                    "rate": st.number_input('Rate', value=0.00),
                    "hours": st.number_input('Hours Worked', value=0.00),
                    "ytd_gross": st.number_input('YTD Gross', value=0.00),
                    "ytd_net": st.number_input('YTD Net', value=0.00),
                    "current_total_deductions": st.number_input('Current Total Deductions', value=0.00),
                    "gross_pay": st.number_input('Gross Pay', value=0.00),
                    "ytd_deductions": st.number_input('YTD Deductions', value=0.00),
                    "net_pay": st.number_input('Net Pay', value=0.00),
                    "federal_tax": st.number_input('Federal Tax', value=0.00),
                    "state_tax": st.number_input('State Tax', value=0.00),
                    "social_security_dectuctions": st.number_input('Social Security Deductions', value=0.00),
                    "other_deductions": st.number_input('Other Deductions', value=0.00),
                })
        
            submit_button = st.form_submit_button(label='Generate Paystub')
            
    with column2:
        image = Image.open('pay_stub_t1.png')
        st.image(image, caption='template 1', use_column_width=True)
        
    if submit_button:
        pdf_name = f"{data['employee_information']}{data['pay_date']}_paystub.pdf"
        title = f"{data['employee_information']}{data['pay_date']} Paystub"
        create_pay_stub(pdf_name, title, data)
        st.success('Paystub created successfully.')

if __name__ == '__main__':
    app()
