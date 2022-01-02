"""
Matrix page, add checkbox for:
    General arithmatic
    Eigenvalues + eigenvectors
    Inverses
"""

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
        sp.integrate(equation, variable)
        return True
    except ValueError as e:
        st.error("Invalid intgration variable")
        return False


def check_output_code(checkbox, integral):
    with st.expander("Open to see code to copy to clipboard"):
        integral_code = sp.latex(integral)
        output_code = L_string.latex_eq_start + integral_code + L_string.latex_eq_end
        st.code(output_code)
    return True


def create_page_layout():
    """Function to create the layout of the page"""

    st.header("Matrix Calculations")

    matrix_num = int(st.text_input("Enter number of matrices."))
    matrix_list = []

    mat_var = st.text_input("Enter Matrix variable name")
    mat = st.text_input("Enter Matirx in the form [ [1,2], [3,4] ]")
    savebox = st.checkbox("Click to save matrix")
    if(mat_var and mat and matrix_num):
        for i in range(matrix_num):
            if check_input_parse(mat_var) and check_input_parse(mat):
                matrix_list.append[mat_var, sp.Matrix(mat)]
            st.text(f"Matrix {i}/{matrix_num} saved")


"""
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

            check_for_code = st.checkbox("Output LaTeX code")
            if check_for_code:
                check_output_code(check_for_code, sp.integrate(eq_sp, var_sp))
            else:
                pass
"""
