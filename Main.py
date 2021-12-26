import streamlit as st


class Multiplage:
    """Class to crete a multipage streamlit application"""

    def __init__(self) -> None:
        """Constructor that instantiates the object and creates the empty list of pages"""
        self.pages = []

    def add_page(self, title, func) -> None:
        """Function to add pages to the website"""

        self.pages.append({"title": title, "function": func})

    def run(self) -> None:

        page = st.sidebar.selectbox("Choose page",self.pages,format_func=lambda page: page['title'])

        page['function']()