import streamlit as st
import random
import string
import time
import re
import qrcode
import base64
from io import BytesIO


st.set_page_config(page_title='ThunderLock', page_icon='key.png', layout="centered", initial_sidebar_state="auto",
                   menu_items=None)

hide_streamlit_style = """
    <style>
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def e1():
    def generate_password(length):
        characters = string.ascii_letters + string.digits + string.punctuation
        first_char = random.choice(string.ascii_letters)
        last_char = random.choice(string.ascii_letters)
        mid_chars = ''.join(random.choice(characters) for _ in range(length - 2))
        password = first_char + mid_chars + last_char
        return password

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Password "
        "Generator</h1></center>",
        unsafe_allow_html=True)

    length = st.slider("Select password length", min_value=8, max_value=32, value=12, step=1)

    if st.button("Generate Password"):
        with st.spinner("Generating Password..."):
            password = generate_password(length)

            time.sleep(2)

        st.success("Password Generated Successfully")

        st.code(password)



def e6():
    def generate_password(length, use_capital, use_small, use_number, use_symbol):
        characters = ''
        if use_capital:
            characters += string.ascii_uppercase
        if use_small:
            characters += string.ascii_lowercase
        if use_number:
            characters += string.digits
        if use_symbol:
            characters += string.punctuation

        if not characters:
            return "Please select at least one option for the password."

        if use_capital and use_small and use_number and use_symbol:
            first_char = random.choice(string.ascii_uppercase + string.ascii_lowercase)
            last_char = random.choice(string.ascii_uppercase + string.ascii_lowercase)
            middle_chars = ''.join(random.choice(characters) for _ in range(length - 2))
            password = first_char + middle_chars + last_char
        else:
            password = ''.join(random.choice(characters) for _ in range(length))

        return password

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Password "
        "Generator</h1></center>",
        unsafe_allow_html=True)

    length = st.number_input("Enter password length", min_value=1, step=1, value=8)

    col1, col2 = st.columns(2)
    with col1:
        use_capital = st.checkbox("Include capital letters")
        use_small = st.checkbox("Include small letters")
    with col2:
        use_number = st.checkbox("Include numbers")
        use_symbol = st.checkbox("Include symbols")

    if st.button("Generate Password"):
        with st.spinner():
            time.sleep(2)
            password = generate_password(length, use_capital, use_small, use_number, use_symbol)
            st.success("Password Generated Successfully!!")
            st.code(password)






def e2():
    def check_password_strength(password):
        if len(password) < 8:
            return "Weak"

        if not re.search(r"[a-z]", password) or not re.search(r"[A-Z]", password):
            return "Medium"

        if not re.search(r"\d", password):
            return "Medium"

        if not re.search(r"[!@#$%^&*()\-_=+{}[\]|\\;:'\",<.>/?]", password):
            return "Medium"

        return "Strong"

    def main():
        st.markdown(
            "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>Password Strength Checker</h1></center>",
            unsafe_allow_html=True)

        password = st.text_input("Enter your password:", type="password")

        if st.button("Check Password"):
            if password:
                strength = check_password_strength(password)
                if strength == "Strong":
                    st.success("Password strength: **Strong**")
                elif strength == "Medium":
                    st.info("Password strength: **Medium**")
                else:
                    st.warning("Password strength: **Weak**")
            else:
                st.warning("Please enter a password.")

    if __name__ == "__main__":
        main()



def e5():
    def main():
        st.markdown(
            "<center><h1 style='font-family: Comic Sans MS; font-size: 32px;'>QR Code Generator</h1></center>",
            unsafe_allow_html=True)
        st.markdown("---")
        text = st.text_area("Enter the text to encode into QR code:")

        generate_button = st.button("Generate QR Code", key="generate_button")

        if generate_button:
            if text:
                qr = qrcode.QRCode(version=1, box_size=10, border=4)
                qr.add_data(text)
                qr.make(fit=True)

                qr_image = qr.make_image(fill="black", back_color="white")
                img_byte_arr = BytesIO()
                qr_image.save(img_byte_arr, format="PNG")
                img_byte_arr.seek(0)
                img_bytes = img_byte_arr.getvalue()
                img_data = BytesIO()
                qr_image.save(img_data, format="PNG")
                download_button_str = create_download_button(img_bytes, "qrcode.png")
                st.markdown(
                    f'<div style="display: flex; justify-content: center;">{download_button_str}</div>',
                    unsafe_allow_html=True
                )
            else:
                st.warning("Please enter some text.")

    def create_download_button(file_content, file_name):
        b64 = base64.b64encode(file_content).decode()
        button_str = (
            f'<a href="data:image/png;base64,{b64}" '
            f'download="{file_name}" class="btn" style="text-decoration: none; display: inline-block; padding: 0.5em 1em; border: 1px solid #000; background-color: #173928; color: #FFFFFF; text-align: center;">'
            f'<img src="data:image/png;base64,{b64}" width="300"><br>Download QR Code as PNG</a>'
        )
        return button_str

    if __name__ == "__main__":
        main()


st.sidebar.markdown("""
            <style>
                .sidebar-text {
                    text-align: center;
                    font-size: 32px;
                    font-family: 'Comic Sans MS', cursive;
                }
            </style>
            <p class="sidebar-text">GuardianKey</p>
            <br/>
        """, unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        width: 50%;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThPMDvG3JhnVfQtBPBIUt_0XA2Bsu87wgI5w&usqp=CAU")
sidebar_options = {
    "Password Generator": e1,
    "Password Generator PRO": e6,
    "Password Str Checker": e2,
    "QR Code Generator":e5
}

selected_option = st.sidebar.radio("Please Select One:", list(sidebar_options.keys()))

sidebar_options[selected_option]()
