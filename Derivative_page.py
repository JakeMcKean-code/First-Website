import streamlit as st
import sympy as sp


def create_page_layout():
    """Function to create the layout of the page"""

    eq_input = st.text_input("Enter equation you want to differentiate:")
    var_input = st.text_input("Enter variable to differetiate with respect to:")

    if eq_input and var_input:
        eq_sp = sp.sympify(eq_input)
        var_sp = sp.sympify(var_input)

        st.latex(eq_sp.diff(var_sp))
