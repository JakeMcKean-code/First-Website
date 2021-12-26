import streamlit as st
import sympy as sp
from sympy.core.sympify import SympifyError


def create_page_layout():
    """Function to create the layout of the page"""

    eq_input = st.text_input(
        "Enter equation you want to differentiate."
        "(use * for multiply, / for divide, exp for exponential, sqrt(-1) for i, and spell greek characters fully)"
    )
    var_input = st.text_input("Enter variable to differetiate with respect to:")

    if eq_input and var_input:
        if var_input.isnumeric():
            st.text(
                "Cannot differentiate with respect to a number, please input a valid integration variable"
            )
        else:
            try:
                eq_sp = sp.sympify(eq_input)
                var_sp = sp.sympify(var_input)

                try:
                    st.latex(eq_sp)
                    st.latex(var_sp)
                    st.latex(eq_sp.diff(var_sp))
                except ValueError as e:
                    st.text("Invalid intgration variable")

            except SympifyError as e:
                st.text("Cannot parse equation or integration variable")
