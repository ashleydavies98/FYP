# import necessary libraries
import streamlit as st


# create the page as an accessible app
# Streamlit widgets (using st.) automatically positions themselves below other widgets in the order they are interpreted
def app():
    # displays a title
    st.title('Introduction')
    # displays a subheading under the title
    st.subheader("Welcome to this teaching tool for Particle Swarm Optimisation!")

    st.subheader("What is PSO?")



#EXPLAIN PSO'S ORIGIN, LOOK AT LEARNING PROCESS IN REPORT AND IMPLEMENT IT!!!!!!!!!!


    # displays an area of text, st.write is used for displaying many large areas of informative text throughout the tool
    st.write("Particle Swarm Optimisation or PSO, is a artificial intelligence algorithm that aims to optimise a problem by iteratively improving "
             "the solution based on a given measure.  ")

    st.write("Particle Swarm Optimisation is used within multiple real world scenarios to decrease costs and make usage of resources more efficient. Such scenarios "
             "are discussed in this tool. ")

    st.subheader("How does PSO work?")

    st.write("Candidate solutions for the given problem, in the form of Particles, oscillate around an area known as the search space. This is done "
             "based on a velocity value that drives the particle's movement towards the most optimal solutions found by the algorithm.  \n")


    st.write("This velocity value is an important factor of PSO and ability to optimise problems. "
             "Its usage and functionality will be covered greatly throughout this app.  \n"
             "This tool focuses on the canonical Position/Velocity variant of Particle Swarm Optimisation, meaning that the movement of particles "
             "is entirely based on the best known positions of particles.")

    st.write("Canonical PSO is done continuously until certain terms are met.  \nThese terms range from a specified number of iterations, "
             "a criterion of error being surpassed, or an optimum solution being achieved.")

    # what the software will cover
    # displays within an info box widget
    st.subheader("What this tool covers:")
    st.info(
            "- The components that make up a PSO algorithm.  \n"
            "- The processes that create PSO.  \n"
            "- How PSO can be visualised.  \n"
            "- How different parameters can effect the results of PSO.  \n"
            "- Types of PSO and how they influence particles differently.  \n"
            "- PSO's applications to real problems, which also covers how PSO can be advanced to perform more accurate and complex optimisations.  \n"
            "- A test of your PSO knowledge, ensuring that you have understood the topics that we cover.")



