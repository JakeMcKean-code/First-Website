from numpy.core.defchararray import lower
import streamlit as st
import sympy as sp
from sympy.core.sympify import SympifyError

""" TO DO

Add buttons to subsitute values in for the variables
Add button to output latex code for user 

"""


def check_input_parse(input):
    """Function to check that the equation or variable can be parsed"""
    try:
        sp.sympify(input)
        return True
    except SympifyError as e:
        st.error("Cannot parse equation or integration variable")
        return False


def check_variable(equation, variable):
    """Function to check if derivative variable is valid"""
    try:
        sp.integrate(equation, variable)
        return True
    except ValueError as e:
        st.error("Invalid intgration variable")
        return False


def create_page_layout():
    """Function to create the layout of the page"""

    st.header("Intgral Calculator")

    st.warning(
        "(use * for multiply, / for divide, exp for exponential, sqrt(-1) for i, and spell greek characters fully)"
    )
    eq_input = st.text_input("Enter equation you want to integrate:")
    var_input = st.text_input("Enter variable to integrate with respect to:")

    col_lower, col_upper = st.columns(2)
    with col_lower:
        lower_limit = st.text_input("Input lower limit")
    with col_upper:
        upper_limit = st.text_input("Input upper limit")

    if eq_input and var_input:
        if check_input_parse(eq_input) and check_input_parse(var_input):
            eq_sp = sp.sympify(eq_input)
            var_sp = sp.sympify(var_input)
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Inputted equation")
                st.latex(eq_sp)
            with col2:
                st.subheader("Integral")
                if check_variable(eq_sp, var_sp):
                    st.latex(sp.integrate(eq_sp, var_sp))

            if check_for_sub(lower_limit, upper_limit):
                if check_input_parse(lower_limit) and check_input_parse(upper_limit):
                    st.subheader(f"Definite integral: $\int_{lower_limit}^{upper_limit}$")
                    answer = sp.integrate(eq_sp,(var_sp,lower_limit, upper_limit))
                    st.latex(answer)

def check_for_sub(lower_limit, upper_limit):
    if lower_limit and upper_limit:
        return True
    else: 
        return False
