import pdfkit
from jinja2 import Environment, FileSystemLoader, select_autoescape
from templates.paystub_data_table import data

def render_template(data, other_deduction_flag=False):
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape()
    )
    template = env.get_template("template.html")
    rendered_template = template.render(data=data, other_deduction_flag=other_deduction_flag)
    return rendered_template

def generate_pdf(rendered_template):
    options = {
        'dpi': 300,
        'margin-top': '5mm',
        'margin-right': '5mm',
        'margin-bottom': '5mm',
        'margin-left': '5mm',
        'encoding': "UTF-8",
    }
    return pdfkit.from_string(rendered_template,False, options=options)

