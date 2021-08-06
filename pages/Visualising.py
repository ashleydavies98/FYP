
import streamlit as st

import base64
import matplotlib.pyplot as plt

import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import (plot_cost_history, plot_contour, plot_surface)
from pyswarms.utils.plotters.formatters import Mesher


def app():
    st.title('Visualising Particle Swarms')

    st.write('Next we will visualise how Particle Swarm Optimisation happens.')

    st.write('Below is a Particle Swarm, you have seen this example earlier, however, this time we will '
             'see how the swarm changes over the iterations of the optimisation process.')

    st.write("The swarm below uses Global best PSO. You may find this similar to a component which you "
             "have seen in earlier pages, known as Gbest. This is because Global best PSO means that "
             "the entire search space is considered as one neighbourhood of particles and therefore "
             "each particle communicates with each other throughout the entire swarm, resulting in them "
             "all sharing the same Gbest value.")


    st.write("Use the 'Generate Particle Swarm' tick box below to generate a swarm and what a Particle Swarm "
             "looks like during Optimisation. ")
    # add some more specifics to reiterate what is involved in the process

    # The swarm parameters, c1, c2 and inertia w
    parameters = {"c1": 0.5, "c2": 0.8, 'w': 0.9}

    # Generates a PSO algorithm
    def generateSwarm():

        # Create the swarm, using GBEST PSO, with 50 particles, a 2D plain, and the above parameters
        swarm = ps.single.GlobalBestPSO(n_particles=15, dimensions=2, options=parameters)

        # Optimise the swarm for the given amount of iterations on a spherical plain
        cost, pos = swarm.optimize(fx.sphere, iters=150)

        # creates a simple line graph using the iterations and the costs respectively for x,y
        plot_cost_history(cost_history=swarm.cost_history)


        # create mesher within the shape of a sphere
        # used for plotting working results of objective functions
        m = Mesher(func=fx.sphere)

        # create animation of the swarm
        # plot positions on a 2D sphere plain, with a minima of 0,0
        animation = plot_contour(pos_history=swarm.pos_history,
                         mesher=m,  # surface plot provided
                         mark=(0, 0))  # minima marked

        # Saves the animation to a usable gif file
        animation.save('PSOanim.gif', writer='imagemagick', fps=12)


        """### gif from url"""
        #st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")

        """### gif from local file"""
        file = open("PSOanim.gif", "rb")
        readfile = file.read()
        data = base64.b64encode(readfile).decode("utf-8")
        file.close()

        st.info('Generating Particle Swarm')

        st.markdown(
            f'<img src = "data:image/gif;base64,{data}" width="750" height="650">',
            unsafe_allow_html=True, )


    if st.checkbox("Generate Particle Swarm"):

        generateSwarm()

