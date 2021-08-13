# import necessary libraries
import streamlit as st
from multiapp import MultiApp


# Streamlit widgets (using st.) automatically positions themselves below other widgets in the order they are interpreted
def app():
    # displays a title
    st.title('What is Particle Swarm Optimisation?')

    # displays an area of text, st.write is used for displaying many large areas of informative text throughout the tool
    st.write("Particle Swarm Optimisation or PSO, is a artificial intelligence algorithm "
             "that aims to optimise a objective function (a problem) by iteratively improving "
             "potential solutions.  ")

    st.write("PSO originates from Population-Based optimisation algorithms. These are algorithms that use a set of "
             "currently bad solutions to generate far better solutions. "
             "'Population' refers to the current solution set, "
             "which better solutions are generated from.")

    st.subheader("How does PSO work?")

    st.write("In simple terms, candidate solutions for a problem, in the form of Particles, are placed "
             "inside an area known as the search space. The Particles then oscillate around the search space "
             "with similar movement to a flock of birds. This oscillation movement is done "
             "based on a Velocity value that attempts to drive Particle movement towards the "
             "most optimal solutions, which are represented by positions within the search space. "
             "The main version of PSO we cover is Global Best PSO, which means that all Particles are "
             "one large neighbourhood, where Velocity is influenced by the Particle with the best known "
             "position found at any given time. \n")

    # create an expanding widget with relevant label
    expander = st.beta_expander(label='PSO and birdflocks')
    # add image and text to expander
    expander.image('images/flocking.png')
    expander.write("Particles on the right are grouped and oscillate around in a similar fashion to the bird "
                   "flock on the left. Some PSO variants like the Global Best variant we are discussing use "
                   "the best position found so far for judging movement. This means the Particles follow the "
                   "strongest Particle, which similar to how birds in a flock commonly follow "
                   "the strongest bird in the flock. ")

    st.write("The Velocity value mentioned above is an important "
             "factor of Particle Swarm Optimisation and how it improves candidate solutions.   \n"
             "Velocity's usage and functionality will be covered greatly throughout this app as "
             "this tool focuses on the 'Position/Velocity update' variant of Particle Swarm Optimisation, "
             "meaning that the movement of Particles "
             "is entirely based on Velocity updates between Iterations, causing Particles to move to new positions.")

    st.write("Particle Swarm Optimisation is done continuously until certain terms are met.  \n"
             "These terms are: ")
    st.info("- A specified number of Iterations.  \n"
            "- A criterion of error being surpassed.  \n"
            "- An optimum solution being achieved.  \n")

    # what the software will cover
    # displays within an info box widget
    st.subheader("What this tool covers:")
    st.info(
            "- The components that make up a PSO algorithm.  \n"
            "- The processes that occur during PSO.  \n"
            "- How PSO can be visualised.  \n"
            "- How different parameters can effect the results of PSO.  \n"
            "- Types of PSO and how they influence Particles differently.  \n"
            "- PSO's applications to real problems, which also covers how PSO "
            "can be advanced to perform more accurate and complex optimisations.  \n"
            "- A test of your PSO knowledge, ensuring that you have understood the topics that we cover.")




