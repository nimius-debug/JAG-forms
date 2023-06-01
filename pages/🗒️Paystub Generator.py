import streamlit as st
from templates.paystub_data_table import data
# from templates.html_template import get_html_code
from PIL import Image
from streamlit_extras.buy_me_a_coffee import button
import datetime
from utils.paystub_simple_template import create_pay_stub
from paystub_pro_html import *


# PAGE CONFIG ******************************************************************* 
st.set_page_config(
        page_title="Paystub Generator",
        page_icon="📎",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'mailto:jag.solutionshub@gmail.com',
            'Report a bug': "mailto:jag.solutionshub@gmail.com",
            'About': "Welcome to our Paystub Generator!. \
                This tool is your ticket to hassle-free payroll. \
                Just input the necessary details, and get a professionally formatted paystub in an instant. \
                It's not just a time-saver; it's a game-changer. By minimizing errors and streamlining the payroll process,\
                we're making life easier for you and your business. \
                Experience the simplicity of payroll with the JAG Forms Paystub Generator today"
        }
    )
#*******************************************************************************

# SESSION STATE *****************************************************************
if "disabled" not in st.session_state:
    st.session_state["disabled"] = False

def disable():
    st.session_state["disabled"] = True
#*******************************************************************************
#Sidebar
with st.sidebar:
    logo = Image.open('img/JAGforms_white.png')
    st.image(logo,use_column_width=True)
    st.header("Instructions")
    st.write("Please fill out the form below to generate a paystub.")
    st.title('PDF Paystub Generator ')
    st.markdown("- **Simple**: This template provides a straightforward, professional paystub layout. \
                It is the standard payroll template, delivering the information clearly , simple and professional.")
    st.markdown("- **Pro**: The Pro template goes a step further.\
                It is designed for those who wish to extensively customize their paystubs, \
                offering the ability to add detailed information and personalized themes.")
    st.header("How to Use")
    st.write("Once you submit the form, the application will generate a PDF paystub that \
        includes all the details entered. The generated PDF is styled for clarity and professionalism.")
    button(username="jagcoffee", floating=False, width=221)
#*********************************************************************************************************************
def util_time_range(key = "0"):
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=7)
    pay_period = st.date_input('Pay Period', value=(start_date, end_date), help="Select a date between your pay period", key=key+"_pay_period")
    if len(pay_period) == 2: 
        start_date_string = pay_period[0]
        end_date_string = pay_period[1]
    else:
        start_date_string = pay_period[0]
        end_date_string = pay_period[0]
    date_range_str = f"{start_date_string.strftime('%m/%d/%Y')} - {end_date_string.strftime('%m/%d/%Y')}"
    return date_range_str

#************************************input utils*********************************************************************************
PAY_OPTIONS = ['Hourly', 'Salary']
def input_company_info(key = "0"):
    st.header("Company Information")
    company_name = st.text_input('Company Name', key=key + "_company_name", value=data['company_name'])
    address = st.text_input('Company Address', key=key + "_company_address", value=data['address'])
    return company_name, address

def input_paystub_info(pay_option, key = "0"):
    st.header("Current Paystub Information")    
    if pay_option == 'Hourly':
        rate = st.number_input('Hourly Rate', value=0.00, key=key + "_hourly_rate")
        hours = st.number_input('Hours Worked', value=0.00, key=key + "_hours_worked")
        gross_pay = st.number_input('Gross Pay/Earnings', value=rate*hours, key=key + "_gross_pay_hourly")
    else:   
        rate = st.text_input('Hourly Rate', value="Salary", disabled=True, key=key + "_salary_rate")
        hours = st.text_input('Hours Worked', value="---", key=key + "_hours_worked_salary")
        gross_pay = st.number_input('Gross Pay/Earnings', value=0.00, key=key + "_gross_pay_salary")
    return rate, hours, gross_pay

def pro_input_paystub_info(pay_option, key = "0"):
    st.header("Current Paystub Information")    
    if pay_option == 'Hourly':
        rate = st.number_input('Hourly Rate', value=0.00, key=key + "_hourly_rate")
        hours = st.number_input('Hours Worked', value=0.00, key=key + "_hours_worked")
        gross_pay = st.number_input('Gross Pay/Earnings', value=rate*hours, key=key + "_gross_pay_hourly")
    else:   
        rate = st.text_input('Hourly Rate', value="---", disabled=True, key=key + "_salary_rate")
        hours = st.text_input('Hours Worked', value="---", key=key + "_hours_worked_salary")
        gross_pay = st.number_input('Gross Pay/Earnings', value=0.00, key=key + "_gross_pay_salary")
    return rate, hours, gross_pay

def input_employee_info(key = "0"):
    st.header("Employee Information")
    employee_name = st.text_input('Employee Name',value=data['employee_name'] , key=key + "_employee_name")
    employee_address = st.text_input('Employee Address', key=key + "_employee_address", value=data['employee_address'])
    ssn = st.text_input('SSN', value=data["ssn"], key=key + "_ssn")
    EmployeeID = st.text_input('Employee ID', value='000', help="Leave blank if not applicable", key=key + "_employee_id")
    check_no = st.text_input('Check Number', help="Enter the check number leave blank ", value='----', key=key + "_check_no")
    return employee_name, employee_address, ssn, EmployeeID, check_no

def pro_input_employee_info(key = "0"):
    st.header("Employee Information")
    employee_name = st.text_input('Employee Name', key=key + "_employee_name", value=data['employee_name'])
    employee_address = st.text_input('Employee Address', key=key + "_employee_address", value=data['employee_address'])
    employee_city = st.text_input('Employee City', key=key + "_employee_city", value=data['employee_city'])
    employee_state = st.text_input('Employee State', key=key + "_employee_state",value=data['employee_state'] )
    employee_zip = st.text_input('Employee Zip', key=key + "_employee_zip", value=data['employee_zipcode'])
    ssn = st.text_input('SSN', value=data['ssn'], key=key + "_ssn")
    EmployeeID = st.text_input('Employee ID', value='000', help="Leave blank if not applicable", key=key + "_employee_id")
    check_no = st.text_input('Check Number', help="Enter the check number or leave blank ", value='----', key=key + "_check_no")
    return employee_name, employee_address, employee_city, employee_state, employee_zip, ssn, EmployeeID, check_no

def input_date_info(key = "0"):       
    st.header("Pay Date")
    date_range_str = util_time_range(key + "_date_range")
    pay_date = st.date_input('Pay Date', key=key+"_pay_date", help="Select a date between your pay period")
    pay_date_str = pay_date.strftime('%m/%d/%Y')
    return date_range_str, pay_date_str

def input_deduction_info(contractor=False, key = "0"):
    st.header("Current Deductions")
    if contractor:
        federal_tax = st.number_input('Federal Tax', value=0.00,disabled=True, key=key + "_federal_tax_contractor")
        state_tax = st.number_input('State Tax', value=0.00,disabled=True, key=key + "_state_tax_contractor")
        fica_medicare_tax = st.number_input('FICA Medicare Tax', value=0.00,disabled=True, key=key + "_fica_medicare_tax_contractor")
        social_security_dectuctions = st.number_input('Social Security Deductions', value=0.00,disabled=True, key=key + "_social_security_dectuctions_contractor")
        other_deductions = st.number_input('Other Deductions', value=0.00,disabled=True, key=key + "_other_deductions_contractor")
    else:
        federal_tax = st.number_input('Federal Tax', value=0.00,disabled=False, key=key + "_federal_tax")
        state_tax = st.number_input('State Tax', value=0.00,disabled=False, key=key + "_state_tax")
        fica_medicare_tax = st.number_input('FICA Medicare Tax', value=0.00,disabled=False, key=key + "_fica_medicare_tax")
        social_security_dectuctions = st.number_input('Social Security Deductions', value=0.00,disabled=False, key=key + "_social_security_dectuctions")
        other_deductions = st.number_input('Other Deductions', value=0.00,disabled=False, key=key + "_other_deductions")
    return federal_tax, state_tax, fica_medicare_tax, social_security_dectuctions, other_deductions

def input_ytd_deductions(contractor=False, key = "0"):
    st.header("YTD Deductions")
    if contractor:
        ytd_federal_tax = st.number_input('YTD Federal Tax', value=0.00,disabled=True, key=key + "_ytd_federal_tax_contractor")
        ytd_state_tax = st.number_input('YTD State Tax', value=0.00,disabled=True, key=key + "_ytd_state_tax_contractor")
        ytd_fica_medicare_tax = st.number_input('YTD FICA Medicare Tax', value=0.00,disabled=True, key=key + "_ytd_fica_medicare_tax_contractor")
        ytd_social_security_dectuctions = st.number_input('YTD Social Security Deductions', value=0.00,disabled=True, key=key + "_ytd_social_security_dectuctions_contractor")
        ytd_other_deductions = st.number_input('YTD Other Deductions', value=0.00,disabled=True, key=key + "_ytd_other_deductions_contractor")
    else:
        ytd_federal_tax = st.number_input('YTD Federal Tax', value=0.00,disabled=False, key=key + "_ytd_federal_tax")
        ytd_state_tax = st.number_input('YTD State Tax', value=0.00,disabled=False, key=key + "_ytd_state_tax")
        ytd_fica_medicare_tax = st.number_input('YTD FICA Medicare Tax', value=0.00,disabled=False, key=key + "_ytd_fica_medicare_tax")
        ytd_social_security_dectuctions = st.number_input('YTD Social Security Deductions', value=0.00,disabled=False, key=key + "_ytd_social_security_dectuctions")
        ytd_other_deductions = st.number_input('YTD Other Deductions', value=0.00,disabled=False, key=key + "_ytd_other_deductions")
    return ytd_federal_tax, ytd_state_tax, ytd_fica_medicare_tax , ytd_social_security_dectuctions, ytd_other_deductions

def input_earnings_info(key = "0"):
    st.header("Earnings Summary (YTD)")
    ytd_gross = st.number_input('YTD Gross', value=0.00, key=key + "_ytd_gross")
    ytd_deductions = st.number_input('YTD Deductions', value=0.00, key=key + "_ytd_deductions")
    ytd_net = st.number_input('YTD Net', value=ytd_gross-ytd_deductions, key=key + "_ytd_net")
    return ytd_gross, ytd_deductions, ytd_net

#************************************************************************************************************************************
def Paystub_Generator():
    colmn1, colmn2 = st.columns([1,2], gap="large")
    with colmn1:
        st.title('PDF Paystub Generator ')
        st.markdown("The **PDF Paystub Generator** \
                    is a seamless and powerful instrument designed to streamline your payroll process. \
                    With this tool, you can produce high-quality, printable paystubs in a convenient PDF format, \
                    making payroll management a breeze.Our PDF Paystub Generator offers two distinct templates:")
    with colmn2:
        img_placeholder = st.empty()
    
    tab_option = st.radio("tabs", ["Simple 📗", "Pro 📚"], horizontal=True, label_visibility="collapsed")
    if tab_option == "Simple 📗":
        image = Image.open('img/pay_stub_t1.png')
        img_placeholder.image(image, caption='Simple Professional template', use_column_width=True)
        column1, column2 = st.columns(2)
        with column1:
            col1, col2 = st.columns(2)
            with col1:
                company_name, address = input_company_info()
                st.header("How are you paid?")
                pay_option = st.selectbox('Select how are you paid',key="simple_pay_option",
                            options=PAY_OPTIONS,
                            help="if salary is selected, the rate and hours worked will be disabled"
                            )
                rate, hours, gross_pay = input_paystub_info(pay_option)
            with col2:
                employee_name,employee_address, ssn, EmployeeID, check_no = input_employee_info()
                date_range_str, pay_date_str = input_date_info()
                contractor = st.checkbox('Contractor' , key="simple_contractor",
                                    help="contractors are responsible for paying their own taxes, \
                                    selecting this option will remove all tax deductions from the paystub.")
        with column2:
            col3, col4 = st.columns(2)
            with col4:
                federal_tax, state_tax,fica_med_ss, social_security_dectuctions, other_deductions = input_deduction_info(contractor)
                st.header("Current Earnings")
                if contractor:
                    total_deductions = st.number_input('Current Total Deductions', value=0.00,disabled=True)
                else:
                    total_ded_value = federal_tax+state_tax+fica_med_ss+social_security_dectuctions+other_deductions
                    total_deductions = st.number_input('Current Total Deductions', value=total_ded_value,disabled=False)
                net_pay = st.number_input('Net Pay', value=gross_pay-total_deductions),
            with col3:
                ytd_gross, ytd_deductions, ytd_net = input_earnings_info()
                ytd_federal_tax, ytd_state_tax,ytd_fica_med_ss ,ytd_social_security_dectuctions, ytd_other_deductions = input_ytd_deductions(contractor)
        
        simpledata = { 
            "company_name": company_name,
            "address": address,
            "employee_name": employee_name,
            "employee_address": employee_address,
            "ssn": ssn,
            "pay_period": date_range_str,
            "EmployeeID": EmployeeID,
            "pay_date": pay_date_str,
            "check_no": check_no,
            "earnings": gross_pay,
            "rate": rate,
            "hours": hours,
            "gross_pay": gross_pay,
            "net_pay": net_pay,
            "ytd_gross": ytd_gross,
            "ytd_net": ytd_net,
            "fica_med": fica_med_ss,
            "fica_ss": social_security_dectuctions,
            "federal_tax": federal_tax,
            "state_tax": state_tax,
            "other_deductions": other_deductions,
            "current_total_deductions": total_deductions,
            "ytd_fica_med": ytd_fica_med_ss,
            "ytd_fica_ss": ytd_social_security_dectuctions,
            "ytd_federal_tax": ytd_federal_tax,
            "ytd_state_tax": ytd_state_tax,
            "ytd_other_deductions": ytd_other_deductions,
            "ytd_deductions": ytd_deductions,
        }
        print(simpledata)   
        print("*********************************************************")              
        
        submit_button = st.button(label='Generate Paystub')
        if submit_button:
            pdf_name = f"{simpledata['employee_name']}_{datetime.date.today().strftime('%m-%d-%Y')}_paystub.pdf"
            title = f"{simpledata['employee_name']} {simpledata['pay_date']} Paystub"
            simple_pdf = create_pay_stub(pdf_name, title, simpledata)
            print(simple_pdf)
            st.success('Paystub created successfully.')
            st.balloons()
            st.download_button(
                "⬇️ Download PDF",
                data=simple_pdf,
                file_name=pdf_name,
                mime="application/pdf",
            )
#***************************************************Tab 2****************************************************************
    elif tab_option == "Pro 📚":  
        img_placeholder = st.empty()
        col1, col2 = st.columns([1,2], gap="large")
        with col1:
            company_name, company_adr = input_company_info("1")
            employee_name, employee_adr,employee_city,employee_state,employee_zip, ssn, EmployeeID, check_no = pro_input_employee_info("1")
            st.header("How are you paid?")
            pay_option = st.selectbox('Select how are you paid',
                            options=PAY_OPTIONS,
                            help="if salary is selected, the rate and hours worked will be disabled",
                            key="pro_pay_option"
                            )
            rate, hours, gross_pay = pro_input_paystub_info(pay_option,key="1")
            date_range_str, pay_date_str = input_date_info(key="1")
            contractor = st.checkbox('Contractor' , key="pro_contractor",
                        help="contractors are responsible for paying their own taxes, \
                        selecting this option will remove all tax deductions from the paystub.")
            federal_tax, state_tax,fica_med_ss, social_security_dectuctions, other_deductions = input_deduction_info(contractor)
            st.header("Current Earnings")
            if contractor:
                total_deductions = st.number_input('Current Total Deductions', value=0.00,disabled=True)
            else:
                total_ded_value = federal_tax+state_tax+fica_med_ss+social_security_dectuctions+other_deductions
                total_deductions = st.number_input('Current Total Deductions', value=total_ded_value,disabled=False)
            net_pay = st.number_input('Net Pay', value=gross_pay-total_deductions)
            ytd_gross, ytd_deductions, ytd_net = input_earnings_info()
            ytd_federal_tax, ytd_state_tax,ytd_fica_med_ss ,ytd_social_security_dectuctions, ytd_other_deductions = input_ytd_deductions(contractor)
            with st.expander("Color Theme"):
                theme = st.radio("Select a color theme", options=[st.color_picker("Build your theme",value="#D3D3D3"),"Default", "Modern"], key="color_theme",horizontal=True)
                if theme == "Default":
                    theme = "lightgray"
                elif theme == "Modern":
                    theme = "lightblue"
                
            data.update({
                "company_name": company_name,
                "address": company_adr,
                "employee_name": employee_name,
                "employee_address": employee_adr,
                "employee_city": employee_city,
                "employee_state": employee_state,
                "employee_zipcode": employee_zip,
                "ssn": ssn,
                "pay_period": date_range_str,
                "EmployeeID": EmployeeID,
                "pay_date": pay_date_str,
                "check_no": check_no,
                "earnings": pay_option,
                "rate": rate,
                "hours": hours,
                "gross_pay": gross_pay,
                "net_pay": net_pay,
                "ytd_gross": ytd_gross,
                "ytd_net": ytd_net,
                "fica_med": fica_med_ss,
                "fica_ss": social_security_dectuctions,
                "federal_tax": federal_tax,
                "state_tax": state_tax,
                "other_deductions": other_deductions,
                "current_total_deductions": total_deductions,
                "ytd_fica_med": ytd_fica_med_ss,
                "ytd_fica_ss": ytd_social_security_dectuctions,
                "ytd_federal_tax": ytd_federal_tax,
                "ytd_state_tax": ytd_state_tax,
                "ytd_other_deductions": ytd_other_deductions,
                "ytd_deductions": ytd_deductions,
                "theme_color": theme,
            })
        with col2:
            html_template = render_template(data=data,other_deduction_flag=False)
            st.markdown(html_template, unsafe_allow_html=True)  
        
        pdf_button = st.button(label='Generate Paystub' , help="Generate a PDF of the paystub")

        if pdf_button:
            pro_pdf = generate_pdf(html_template)
            filename = f"{data['employee_name']}_{datetime.date.today().strftime('%m-%d-%Y')}_paystub.pdf"
            st.success('Paystub created successfully.')
            st.balloons()
            st.download_button(
                "⬇️ Download PDF",
                data=pro_pdf,
                file_name=filename,
                mime="application/pdf",
            )
    # Run the paystub generation function'
    
if __name__ == '__main__':
    Paystub_Generator()
