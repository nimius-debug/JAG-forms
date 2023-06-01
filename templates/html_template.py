def get_html_code(data):
    html_content = f'''
    <html>
    <head>
        <title>Paystub Template</title>
        <style>
            .paystub {{
                padding: 10px; 
                border: 3px solid black;
                overflow: hidden;
                font-family: Helvetica, sans-serif;
                background-color: white;
                color: black;
            }}
            .scrollable-table {{
                overflow-x: auto;
                padding-top: 10px;
            }}
            .column1 {{
                width: 49.5%; 
                float: left;
            }}
            .column2 {{
                width: 49.5%; 
                float: right;
            }}
            table {{
                width: 100%; 
                border-collapse: collapse; 
            }}
            td, th {{ 
                padding: 10px;
                text-align: left;  /* Add this line */
                border:none;
            }}
            .header {{ 
                font-weight: bold; 
                background-color: lightgray;

            }}
            .container2 td, .container2 th {{
                width: 50%; 
                border:none;
            
            }}
            .container3 td:nth-child(1), .container3 th:nth-child(1), {{
                width: 33.33%; 
                border:none;
            
            }}
            .container4 td, .container4 th  {{ ;
                width: 25%; 
                border:none;
            }}
            .container6 td, .container6 th {{
                border:none;
                }}
            .container6 td:nth-child(1), .container6 th:nth-child(1) {{
                width: 35%; 
                border:none;
            }}
            .container6 td:nth-child(2), .container6 th:nth-child(2) {{
                width: 15%; 

            }}
            .container6 td:nth-child(3), .container6 th:nth-child(3) {{
                width: 15%; 
            }}
            .container6 td:nth-child(4), .container6 th:nth-child(4) {{
                width: 15%; 
            }}
            .container6 td:nth-child(5), .container6 th:nth-child(5) {{
                width: 10%; 
            }}
            .container6 td:nth-child(6), .container6 th:nth-child(6) {{
                width: 10%; 
            }}

            .containerlast td, .containerlast th {{ 
                width: 16.66%; 
                border:none;
            }}
            .container3 tr:nth-child(odd) {{
                background-color: #f2f2f2;
            }}
            h3 {{
                text-align:right;
                color : black;
            }}
            
        </style>
    </head>
    <body>
        <div class="paystub">
            <div class="scrollable-table">
                <table class="container2">
                    <tr>
                        <td>{data["company_data"]["company_name"]}<br>{data["company_data"]["address"]}</td>
                        <td><h3>EARNING STATEMENT</h3></td>
                    </tr>
                </table>
            </div>
            <div class="scrollable-table">
                <table class="container6">
                    <tr>
                        <th class="header">Employee Info</th>
                        <th class="header">SSN</th>
                        <th class="header">Pay Period</th>
                        <th class="header">Pay Date</th>
                        <th class="header">Employee ID</th>
                        <th class="header">Check No</th>
                    </tr>
                    <tr>
                        <td>{data["employee_data"]["employee_name"]}<br> {data["employee_data"]["employee_address"]} <br> {data["employee_data"]["employee_city"]}, {data["employee_data"]["employee_state"]}, {data["employee_data"]["employee_zipcode"]}</td>
                        <td>{data["employee_data"]["ssn"]}</td>
                        <td>{data["employee_data"]["pay_period"]}</td>
                        <td>{data["employee_data"]["pay_date"]}</td>
                        <td>{data["employee_data"]["EmployeeID"]}</td>
                        <td>{data["employee_data"]["check_no"]}</td>
                    </tr>
                </table>
            </div>
            <div class="column1">
                <div class="scrollable-table">
                    <table class="container4">
                        <tr>
                            <th class="header">Earnings</th>
                            <th class="header">Hours</th>
                            <th class="header">Rate</th>
                            <th class="header">Total</th>
                        </tr>
                        <tr>
                            <td>{data["paystub_earning_data"]["earnings"]}</td>
                            <td>{data["paystub_earning_data"]["hours"]}</td>
                            <td>{data["paystub_earning_data"]["rate"]}</td>
                            <td>{data["paystub_earning_data"]["gross_pay"]}</td>
                        </tr>
                    </table>
                </div>
            </div>
            <div class="column2">
                <div class="scrollable-table">
                    <table class="container3">
                        <tr>
                            <th class="header">Statutory Deductions</th>
                            <th class="header">Total</th>
                            <th class="header">YTD</th>
                        </tr>
                        <tr>
                            <td>FICA-Medicare </td>
                            <td>{data["paystub_deduction_data"]["fica_med"]}</td>
                            <td>{data["paystub_deduction_data"]["ytd_fica_med"]}</td>
                        </tr>
                        <tr>
                            <td>FICA-Social Security </td>
                            <td>{data["paystub_deduction_data"]["fica_ss"]}</td>
                            <td>{data["paystub_deduction_data"]["ytd_fica_ss"]}</td>
                        </tr>
                        <tr>
                            <td>State Tax</td>
                            <td>{data["paystub_deduction_data"]["state_tax"]}</td>
                            <td>{data["paystub_deduction_data"]["ytd_state_tax"]}</td>
                        </tr>
                            <td>Federal Tax </td>
                            <td>{data["paystub_deduction_data"]["federal_tax"]}</td>
                            <td>{data["paystub_deduction_data"]["ytd_federal_tax"]}</td>
                        </tr>
                    </table>
                </div> 
            </div>
            <div style="clear:both;"></div>
            <div style="margin-top:20px;" class="scrollable-table">
                <table class="containerlast">
                    <tr>
                        <th class="header">Header 1</th>
                        <th class="header">Header 2</th>
                        <th class="header">Header 3</th>
                        <th class="header">Header 4</th>
                        <th class="header">Header 5</th>
                        <th class="header">Header 6</th>
                    </tr>
                    <tr>
                        <td>Cell 1 </td>
                        <td>Cell 2</td>
                        <td>Cell 3</td>
                        <td>Cell 4</td>
                        <td>Cell 5</td>
                        <td>Cell 6</td>
                    </tr>
                </table>
            </div>
        </div>
    </body>
    </html>
    '''
    return html_content