import streamlit as st
import sympy as sp
from sympy.core.sympify import SympifyError

''' TO DO

Add better formatting for the output of the answer
Add buttons to subsitute values in for the variables
Add button to output latex code for user 

'''

def check_input_numeric(input):
    if input.isnumeric():
            st.error(
                "Cannot differentiate with respect to a number, please input a valid integration variable"
            )
            return
    else:
        return


def create_page_layout():
    """Function to create the layout of the page"""

    st.header("Derivative Calculator")

    st.warning(
        "(use * for multiply, / for divide, exp for exponential, sqrt(-1) for i, and spell greek characters fully)"
    )
    eq_input = st.text_input("Enter equation you want to differentiate.")
    var_input = st.text_input("Enter variable to differetiate with respect to:")

    if eq_input and var_input:
        check_input_numeric(var_input)
        #if var_input.isnumeric():
        #    st.error(
        #        "Cannot differentiate with respect to a number, please input a valid integration variable"
        #    )
        #else:
        try:
            eq_sp = sp.sympify(eq_input)
            var_sp = sp.sympify(var_input)

            try:
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Inputted equation")
                    st.latex(eq_sp)
                with col2:
                    st.subheader("Derivative")
                    st.latex(eq_sp.diff(var_sp))
                    # st.latex(var_sp)

            except ValueError as e:
                st.error("Invalid intgration variable")

        except SympifyError as e:
            st.error("Cannot parse equation or integration variable")


def check_for_sub():
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Input lower limit")
    
    with col2:
        st.text_input("Input upper limit")
    
    
