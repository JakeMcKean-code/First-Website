import streamlit as st
import sympy as sp
import numpy as np


def create_page_layout():
    """Function to create the layout of the page"""

    eq_input = st.text_input("Enter equation you want to differentiate."
        "(use * for multiply, / for divide, exp for exponential, sqrt(-1) for i, and spell greek characters fully)")
    var_input = st.text_input("Enter variable to differetiate with respect to:")

    if eq_input and var_input:
        if var_input.isnumeric():
            st.text(
                "Cannot differentiate with respect to a number, please input a valid differentiation variable"
            )
        elif sp.sympify(eq_input)==False or sp.sympify(var_input)==False:
            st.text(
                "Cannot parse equation or variable, please rewrite"
            )
        else:
            eq_sp = sp.sympify(eq_input)
            var_sp = sp.sympify(var_input)

            st.latex(eq_sp)
            st.latex(var_sp)
            st.latex(eq_sp.diff(var_sp))
