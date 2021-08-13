# import Streamlit
import streamlit as st

# Import PSO related modules
import matplotlib.pyplot as plt
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
# unused 'plotters' imports exist in case further expansion is to be made in displayed content
from pyswarms.utils.plotters import (plot_cost_history, plot_contour, plot_surface)
from pyswarms.utils.plotters.formatters import Mesher


# create the page as an accessible app function, so that the page can be accessed from the navigation bar
def app():
    global checkboxBool
    checkboxBool = False

    st.title('Visualising Particle Swarms')

    st.write("This page covers how Particle Swarm Optimisation can be visualised. In this tool, "
             "visualisation of Particle Swarm Optimisation is shown with an animation, displaying "
             "a PSO algorithm from start to finish.")

    st.write("The swarm that can be generated below uses Global best PSO, which as already discussed"
             "means that the entire search space is considered as one neighbourhood of particles and "
             "therefore each particle communicates with each other throughout the entire swarm, resulting "
             "in them converging at a similar time.")


    st.write("Use the 'Generate Particle Swarm' tick box below to generate a PSO algorithm and its results.")
    # add some more specifics to reiterate what is involved in the process

    # The swarm parameters, c1, c2 and inertia w
    parameters = {"c1": 0.3, "c2": 0.5, 'w': 0.9}

    # Generates a PSO algorithm
    def generateSwarm():
        with st.spinner('Generating Particle Swarm, this may take a minute'):
            progressbar = st.progress(0)

            # Create the swarm, using GBEST PSO, with 50 particles, a 2D plain, and the above parameters
            swarm = ps.single.GlobalBestPSO(n_particles=15, dimensions=2, options=parameters)

            progressbar.progress(20)
            # Optimise the swarm for the given amount of iterations to solve a sphere function
            cost, pos = swarm.optimize(fx.sphere, iters=150)
            progressbar.progress(40)

            # creates a simple line graph using the iterations and the costs respectively for x,y
            plot_cost_history(cost_history=swarm.cost_history)


            # save cost graph
            plt.savefig('PSOcost.png')

            # create mesher within the shape of a sphere
            # used for plotting working results of objective functions
            m = Mesher(func=fx.sphere)
            progressbar.progress(50)

            # create animation of the swarm
            # plot positions on a 2D sphere plain, with a minima of 0,0
            animation = plot_contour(pos_history=swarm.pos_history,
                         mesher=m,  # surface plot provided
                         mark=(0, 0), title="Particle Swarm Animation")  # minima marked
            progressbar.progress(65)

            # Saves the animation to a usable gif file
            animation.save('PSOanim.gif', writer='imagemagick', fps=12)
            progressbar.progress(75)


            progressbar.progress(100)

            st.header("Generated Particle Swarm")
            st.image(f'PSOanim.gif')

            st.write("Best position found by the swarm: ")
            st.text(pos)

            progressbar.empty()





    # displays a checkbox in which if clicked, generates the PSO algorithm
    if st.checkbox("Generate Particle Swarm"):

        checkboxBool = True
        generateSwarm()

        st.write("  \nAs you can see from the gif above, particles follow the processes discussed "
                 "previously and populate the search space far apart from each other. As time goes on, "
                 "they begin to converge closer towards the optima/minima, which in this case is marked "
                 "by the red 'x' at 0, 0.")

        st.info("The Particle Swarm Optimisation algorithm above was generated with the following "
                "parameters:  \n"
                "c1: 0.3   \n c2: 0.5   \n  w: 0.9")


    if checkboxBool == True:
        with st.form("Question form"):

            st.write("Based on the above parameters, which component is influencing movement the most?")
            # Add a question select box
            q1 = st.selectbox(
                 'Answer choices',
                ('PBEST', 'GBEST')
            )
            submit = st.form_submit_button("Submit")

            if submit:
                if q1 == 'GBEST':
                    st.write("Correct!")
                else:
                    st.write("Incorrect, try again!")
