import streamlit as st
from PIL import Image
from streamlit_extras.buy_me_a_coffee import button

st.set_page_config(
        page_title="Paystub Generator",
        page_icon="📇",
        layout="centered",
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

def Home():
    with st.sidebar: 
        logo = Image.open('img/JAGforms_white.png')
        st.image(logo,use_column_width=True)
        st.header("Instructions")
        st.write("Please fill out the form to generate a the PDF.")
        feat = ["Interactive Form", "PDF Generation", "Sidebar Instructions"]
        st.header("Features")
        st.markdown('\n'.join(f'- {item}' for item in feat))
        
        
        button(username="jagcoffee", floating=False, width=221)
        
    logo = Image.open('img/JAGforms_white.png')
    st.image(logo,width=300)
    st.title('Jag Forms: Your Paperwork, Simplified!')

    st.markdown("""
    At Jag Forms, we believe in making your life easier, one form at a time.
    """)

    st.header('Why Choose Jag Forms?')

    st.markdown("""
    - **Effortless Form Filling**: No more manual entries or dealing with hard-to-understand formats. \
        Simply input your details, and we'll take care of the rest.

    - **Paystub Generator**: Wage statements should be straightforward and professional. \
        With our paystub generator, they can be. Enter your details, and receive a polished, ready-to-use paystub.

    - **Ever-Evolving Library**: We're not just stopping here. Our library of forms is always growing, \
        adapting to your needs. Today, you might use Jag Forms for your paystubs. Tomorrow, who knows? \
        Tax forms, rental agreements, invoices... The sky's the limit!

    - **Customization**: Coming soon, Jag Forms will offer enhanced customization.\
        Imagine forms that not only simplify your life, but also reflect your personality.
    """)

    st.header('More Features Coming Soon!')

    st.markdown("""
    We're always striving to make Jag Forms even better, and we've got some exciting plans for the future:

    - **AI Implementation**: Our AI will learn your preferences and common entries, making form filling even faster and easier.\
        It will also help to ensure that your forms are filled out correctly, catching common mistakes before they happen.

    - **Expanded Library**: We'll be adding even more forms to our library. Look forward to a wide range of business forms, \
        tax forms, and much more.

    We can't wait for you to see what we have in store!
    """)

    st.markdown("""
    We're excited for you to embark on this journey with us. Let's turn the paperwork maze into a walk in the park!
    """)

if __name__ == "__main__":
    Home()
