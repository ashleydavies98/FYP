"""Frameworks for running multiple Streamlit applications as a single app.
   This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps)
   framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar).

"""
import streamlit as st

class MultiApp:
    # initialise the array of pages
    def __init__(self):
        self.apps = []

    # a function a allows the addition of a new app to the array of pages
    def add_app(self, title, func):
        """Adds a new application.

        func: the app function within each page to present its content.
        title: app title, to be shown within the navigation bar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    # runs the selected app from the navigation bar
    def run(self):
        # create select box of pages
        app = st.selectbox(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title'])
        # calls the relevant app's app function, which displays the content within it
        app['function']()

