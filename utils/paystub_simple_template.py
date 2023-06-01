from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def custom_Heading_subhead(c,x,y, key, value ):
   
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x, y, key)
    c.setFont("Helvetica", 10)
    c.drawString(x, y-13, value)
    
def create_pay_stub(pdf_name,title, data):
    buffer = BytesIO()

    c = canvas.Canvas(buffer, pagesize=letter)
    c.setTitle(title)
    width, height = letter
    print(width, height)
    c.rect(20, 500, 572, 255, stroke=1, fill=0)
    c.setFont("Times-Roman", 11)
    
    print(c.getAvailableFonts())
    print(width - 30)
    print(height/2)
    
    #**************************************************************************
    # Top headin
    c.drawString(30, height - 50, data['company_name'])
    c.drawString(30, height - 65, data['address'])
    
    c.setFont("Helvetica-Bold", 11)
    c.drawString(width - 150, height - 55, f"EARNING STATEMENT")
    c.line(20, height - 70, width - 20, height - 70)
    #**************************************************************************
    #First column
    # Employee information
    custom_Heading_subhead(c,30,height - 82,"EMPLOYEE NAME",data['employee_name'])
    # Social Security Number
    custom_Heading_subhead(c,180,height - 82,"SSN",data['ssn'])
    #employee ID
    custom_Heading_subhead(c,250,height - 82,"EMPL ID",data['EmployeeID'])
    #check number
    custom_Heading_subhead(c,310,height - 82,"CHECK NO",data['check_no'])
    # Reporting period
    custom_Heading_subhead(c,390,height - 82,"REPORTING PERIOD",data['pay_period'])
    # Pay date
    custom_Heading_subhead(c,525,height - 82,"PAY DATE",data['pay_date'])
    #**************************************************************************
    c.line(20, height - 100, width - 20, height - 100)
    #**************************************************************************
    # Second column
    # Earnings
    custom_Heading_subhead(c,30,height - 112,"RATE",str(data['rate']))
    # Hours
    custom_Heading_subhead(c,100,height - 112,"HOURS",str(data['hours']))
    # Gross earnings
    custom_Heading_subhead(c,170,height - 112,"GROSS EARNINGS",str(data['gross_pay'])+'$')
    #**************************************************************************
    c.line(285, height - 100, 285, 500)
    #**************************************************************************
    # Deductions Headings
    custom_Heading_subhead(c,300,height - 112,"DEDUCTIONS","Federal tax")
    c.drawString(300, height - 140, "State tax")
    c.drawString(300, height - 155, "SS tax")
    c.drawString(300, height - 170, "Medicare tax")
    c.drawString(300, height - 185, "Others")
    
    custom_Heading_subhead(c,400,height - 112,"CURR TOTAL", str(data['federal_tax'])+'$')
    c.drawString(400, height - 140, str(data['state_tax'])+'$')
    c.drawString(400, height - 155, str(data['fica_ss'])+'$')
    c.drawString(400, height - 170, str(data['fica_med'])+'$')
    c.drawString(400, height - 185, str(data['other_deductions'])+'$')
    
    custom_Heading_subhead(c,525,height - 112,"YTD TOTAL", str(data['ytd_deductions'])+'$')
    c.drawString(525, height - 140, str(data['ytd_state_tax'])+'$')
    c.drawString(525, height - 155, str(data['ytd_fica_ss'])+'$')
    c.drawString(525, height - 170, str(data['ytd_fica_med'])+'$')
    c.drawString(525, height - 185, str(data['ytd_other_deductions'])+'$')
   
    c.line(20, height - 250, width - 20, height - 250)
    #**************************************************************************
    # Third column
    # YTD and pay
    custom_Heading_subhead(c,30,height - 262,"YTD GROSS",str(data['ytd_gross'])+'$')
    custom_Heading_subhead(c,110,height - 262,"YTD DEDUCTIONS",str(data['ytd_deductions'])+'$')
    custom_Heading_subhead(c,220,height - 262,"YTD NET",str(data['ytd_net'])+'$')
    custom_Heading_subhead(c,300,height - 262,"GROSS PAY",str(data['gross_pay'])+'$')
    custom_Heading_subhead(c,400,height - 262,"DEDUCTIONS",str(data['current_total_deductions'])+'$')
    custom_Heading_subhead(c,525,height - 262,"NET PAY",str(data['net_pay'])+'$')
    #**************************************************************************

    c.save()
    pdf_data = buffer.getvalue()
    return pdf_data
# create_pay_stub("pay_stub.pdf", data)