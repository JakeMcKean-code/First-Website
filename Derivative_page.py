from numpy.core.defchararray import lower
import streamlit as st
import sympy as sp
from sympy.core.sympify import SympifyError
import LaTeX_eq_strings as L_string


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


def check_for_sub(limit):
    if limit:
        return True
    else:
        return False


def check_output_code(checkbox, derivative):
    with st.expander("Open to see code to copy to clipboard"):
        derivative_code = sp.latex(derivative)
        output_code = L_string.latex_eq_start + derivative_code + L_string.latex_eq_end
        st.code(output_code)
    return True


def create_page_layout():
    """Function to create the layout of the page"""

    st.header("Derivative Calculator")

    st.warning(
        "(use * for multiply, / for divide, exp for exponential, sqrt(-1) for i, and spell greek characters fully)"
    )
    eq_input = st.text_input("Enter equation you want to differentiate.")
    var_input = st.text_input("Enter variable to differetiate with respect to:")

    st.info("Substitution not required")
    sub = st.text_input("Input substitution")

    if eq_input and var_input:

        if check_input_parse(eq_input) and check_input_parse(var_input):
            eq_sp = sp.sympify(eq_input)
            var_sp = sp.sympify(var_input)

            col_eq, col_d = st.columns(2)
            with col_eq:
                st.subheader("Inputted equation")
                st.latex(eq_sp)
            with col_d:
                st.subheader("Derivative")
                if check_variable(eq_sp, var_sp):
                    st.latex(eq_sp.diff(var_sp))

            if check_for_sub(sub):
                if check_input_parse(sub):
                    st.subheader(f"Derivative at ${var_sp}$ = ${sp.sympify(sub)}$")
                    answer = eq_sp.diff(var_sp).subs(var_sp, sub)
                    st.latex(answer)

            check_for_code = st.checkbox("Output LaTeX code")
            if check_for_code:
                check_output_code(check_for_code, eq_sp.diff(var_sp))
            else:
                pass
