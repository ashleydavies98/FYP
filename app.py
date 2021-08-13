"""Frameworks for running multiple Streamlit applications as a single app.
   This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps)
   framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar).
"""

import streamlit as st
from multiapp import MultiApp

# different page files, imported here
from pages import Introduction, PSOapplications, PSOcomponents, PSOprocesses, Visualising, Parameters, Test, PSOtype

# all pages are an instance of the multiapp framework
app = MultiApp()

# Title markdown
st.markdown("""
# Visualising Particle Swarm Optimisation
""")

# adding pages to the navigation list of pages
app.add_app("Introduction", Introduction.app)
app.add_app("Components of PSO", PSOcomponents.app)
app.add_app("Processes of PSO", PSOprocesses.app)
app.add_app("Visualising", Visualising.app)
app.add_app("Parameters", Parameters.app)
app.add_app("Types of PSO", PSOtype.app)
app.add_app("Applications of PSO", PSOapplications.app)
app.add_app("Test your learning", Test.app)



# The main app, used to execute the tool
app.run()


