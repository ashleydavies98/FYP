import streamlit as st
import base64
import matplotlib.pyplot as plt
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import (plot_cost_history, plot_contour, plot_surface)
from pyswarms.utils.plotters.formatters import Mesher


# create the page
def app():
    # add a title to the page
    st.title('Parameters')
    # added text to page
    st.write("In this section, we demonstrate how changing parameters effects PSO.")

    st.write("As discussed before, c1 and c2 represent constraints that "
             "cause the particle to rely on themselves or each other respectively.")

    st.write("Below, two sets of PSO algorithms can be executed, with results being generated and displayed. ")

    st.write(
        "Try changing the parameters using the fields below and use the 'Generate Particle Swarms' tick box to regenerate new swarms with "
        "each change and see how the different swarms compare! "
        "The input boxes below contain some preset values which you can use for an initial test.")

    st.write("Both swarms that you generate below are created with the same amount of particles and iterations each. "
             "The only difference between them is the cognitive and social parameters that you select. ")

    st.subheader("Particle swarm parameters")

    st.info("HINT: use a value between 0.2 and 1.5 and see what happens when you flip the values for each swarm.")

    # parameter input fields, taking a float value
    options = {"c1": float(st.text_input("Cognitive parameter (c1)", 0.9)),
               "c2": float(st.text_input("Social parameter (c2)", 0.3)), 'w': 0.9}

    # create space in the page
    st.write("  \n")
    st.write("  \n")

    # inputting second swarm's parameters
    st.subheader("Second swarm's parameters")
    options2 = {"c1": float(st.text_input("Second swarm: Cognitive parameter (c1)", 0.3)),
                "c2": float(st.text_input("Second Swarm: Social parameter (c2)", 0.9)), 'w': 0.9}

    # swarm generation function
    def generateSwarms():
        # create the swarm with particles and dimensions and parameters
        optimising = ps.single.GlobalBestPSO(n_particles=15, dimensions=2, options=options)

        # optimise the swarm for the given amount of iterations on a spherical plain
        cost, pos = optimising.optimize(fx.sphere, iters=150)

        # create mesher within the shape of a sphere
        # plots results of the algorithm
        m = Mesher(func=fx.sphere)

        # create animation of the swarm
        # plot positions on a 2D sphere plain, with a marked minima at 0,0
        animation = plot_contour(pos_history=optimising.pos_history,
                                 mesher=m,  # surface plot provided
                                 mark=(0, 0))  # minima marked

        # Saves the animation to a usable gif file
        animation.save('PSOanimparam.gif', writer='imagemagick', fps=11)


        st.info("Swarm one:")

        """### gif from local file"""
        file = open("PSOanimparam.gif", "rb")
        readfile = file.read()
        data = base64.b64encode(readfile).decode("utf-8")
        file.close()

        st.markdown(
            f'<img src = "data:image/gif;base64,{data}" width="750" height="650">',
            unsafe_allow_html=True, )

        # 2nd particle swarm's generation

        optimising2 = ps.single.GlobalBestPSO(n_particles=15, dimensions=2, options=options2)
        # optimise the swarm for the given amount of iterations on a spherical plain
        cost, pos = optimising2.optimize(fx.sphere, iters=150)

     
        # create mesher within the shape of a sphere
        # used for plotting working results of objective functions
        m2 = Mesher(func=fx.sphere)

        # create animation of the swarm
        # plot positions on a 2D sphere plain, with a minima of 0,0
        animation2 = plot_contour(pos_history=optimising2.pos_history,
                                  mesher=m,  # surface plot provided
                                  mark=(0, 0))  # minima marked

        # Saves the animation to a usable gif file
        animation2.save('PSOanimparam2.gif', writer='imagemagick', fps=11)


        st.info("Swarm two:")
        
        """### gif from local file"""
        file2 = open("PSOanimparam2.gif", "rb")
        contents2 = file2.read()
        data2 = base64.b64encode(contents2).decode("utf-8")
        file2.close()
        st.markdown(
            #  f'<img src="data:image/gif;base64,{data_url2}" alt="cat gif">',
            f'<img src = "data:image/gif;base64,{data2}" width="750" height="650">',
            unsafe_allow_html=True)

        st.write("What do you notice about the two swarms? What differences can you observe between them?")

    st.info("Make sure you have set parameters for both swarms before clicking the generate button.")
    if st.checkbox("Generate Particle Swarms"):
        generateSwarms()
