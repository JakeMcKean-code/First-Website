import streamlit as st
import sympy as sp
from sympy.core.sympify import SympifyError

""" TO DO

Add better formatting for the output of the answer
Add buttons to subsitute values in for the variables
Add button to output latex code for user 

"""


def check_input_numeric(input):
    """Function to check"""
    if input.isnumeric():
        st.error(
            "Cannot differentiate with respect to a number, please input a valid integration variable"
        )
        return True
    else:
        return False


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
        equation.diff(variable)
        return True
    except ValueError as e:
        st.error("Invalid intgration variable")
        return False


def create_page_layout():
    """Function to create the layout of the page"""

    st.header("Derivative Calculator")

    st.warning(
        "(use * for multiply, / for divide, exp for exponential, sqrt(-1) for i, and spell greek characters fully)"
    )
    eq_input = st.text_input("Enter equation you want to differentiate.")
    var_input = st.text_input("Enter variable to differetiate with respect to:")

    if eq_input and var_input:
        # check_input_numeric(var_input)

        if check_input_parse(eq_input) and check_input_parse(var_input):
            eq_sp = sp.sympify(eq_input)
            var_sp = sp.sympify(var_input)

            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Inputted equation")
                st.latex(eq_sp)
            with col2:
                st.subheader("Derivative")
                if check_variable(eq_sp, var_sp):
                    st.latex(eq_sp.diff(var_sp))


def check_for_sub():
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Input lower limit")

    with col2:
        st.text_input("Input upper limit")
