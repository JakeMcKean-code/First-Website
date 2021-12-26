import streamlit as st
import sympy as sp


def create_page_layout():
    """Function to create the layout of the page"""

    eq_input = st.text_input("Enter equation you want to integrate:")
    var_input = st.text_input("Enter variable to integrate with respect to:")

    if eq_input and var_input:
        eq_sp = sp.sympify(eq_input)
        var_sp = sp.sympify(var_input)

        st.latex(eq_sp)
        st.latex(var_sp)
        st.latex(sp.integrate(eq_sp, var_sp))
