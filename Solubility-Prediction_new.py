import streamlit as st
from streamlit_option_menu import option_menu

import home,project,contact
import sys

st.title("Check Python Version")

python_version = sys.version
st.write(f"Python version: {python_version}")




