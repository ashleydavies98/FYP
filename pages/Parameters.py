# import Streamlit
import streamlit as st

# import PSO related modules
import base64
import matplotlib.pyplot as plt
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx

# unused 'plotters' imports exist in case further expansion is to be made in displayed content
from pyswarms.utils.plotters import (plot_cost_history, plot_contour, plot_surface)
from pyswarms.utils.plotters.formatters import Mesher


# create the page as an accessible app function, so that the page can be accessed from the navigation bar
def app():
    # add a title to the page
    st.title('Parameters')
    # added text to page
    st.write("In this section, we demonstrate how changing parameters effects PSO.")

    st.write("As discussed before, c1 and c2 represent constraints that "
             "cause the Particle to rely on themselves or each other respectively.")

    st.write("Below, two sets of PSO algorithms can be executed, with results being generated and displayed for you to "
             "analyse differences between the two. ")

    st.write(
        "Try changing the parameters using the fields below and use the 'Generate Particle Swarms' tick box to regenerate new swarms with "
        "each change and see how the different swarms compare! "
        "The input boxes below contain some preset values which you can use for an initial test.")

    st.write("Both swarms that you generate below are created with the same amount of Particles and iterations each. "
             "The only difference between them is the cognitive and social parameters that you select. ")

    st.subheader("Particle swarm parameters")

    st.info("HINT: use a value between 0.2 and 1.5 and see what happens when you flip the values for each swarm.")

    # parameter input fields, taking a float value
    options = {"c1": float(st.text_input("Cognitive parameter (c1)", 1.5)),
               "c2": float(st.text_input("Social parameter (c2)", 0.6)), 'w': 0.7}

    # create space in the page
    st.write("  \n")
    st.write("  \n")

    # inputting second swarm's parameters
    st.subheader("Second swarm's parameters")
    options2 = {"c1": float(st.text_input("Second swarm: Cognitive parameter (c1)", 0.6)),
                "c2": float(st.text_input("Second Swarm: Social parameter (c2)", 1.5)), 'w': 0.7}


    #ADD CHECKS FOR ENSURING NO VALUES INPUT TOO HIGH

    # swarm generation function
    def generateSwarms():
        with st.spinner('Generating both Particle Swarms'):
            progressbar = st.progress(0)
            # create the swarm with Particles and dimensions and parameters
            optimising = ps.single.GlobalBestPSO(n_particles=15, dimensions=2, options=options)
            progressbar.progress(10)


            # optimise the swarm for the given amount of iterations on a spherical plain
            cost, pos = optimising.optimize(fx.sphere, iters=170)
            progressbar.progress(20)


            # create mesher within the shape of a sphere
            # plots results of the algorithm
            m = Mesher(func=fx.sphere)
            progressbar.progress(30)

            # create animation of the swarm
            # plot positions on a 2D sphere plain, with a marked minima at 0,0
            animation = plot_contour(pos_history=optimising.pos_history,
                                     mesher=m,  # surface plot provided
                                     mark=(0, 0),  # minima marked
                                     title="Particle Swarm Animation")

            progressbar.progress(45)

            # Saves the animation to a usable gif file
            animation.save('PSOanimparam.gif', writer='imagemagick', fps=11)
            progressbar.progress(48)

            """### gif from local file"""
            file = open("PSOanimparam.gif", "rb")
            readfile = file.read()
            data = base64.b64encode(readfile).decode("utf-8")
            file.close()
            progressbar.progress(50)
        #st.markdown(
          #  f'<img src = "data:image/gif;base64,{data}" width="750" height="650">',
          #  unsafe_allow_html=True, )

            # 2nd particle swarm's generatiom
            optimising2 = ps.single.GlobalBestPSO(n_particles=15, dimensions=2, options=options2)

            # optimise the swarm for the given amount of iterations on a spherical plain
            cost2, pos2 = optimising2.optimize(fx.sphere, iters=170)
            progressbar.progress(65)



            # create mesher within the shape of a sphere
            # used for plotting working results of objective functions
            m2 = Mesher(func=fx.sphere)

            # create animation of the swarm
            # plot positions on a 2D sphere plain, with a minima of 0,0
            animation2 = plot_contour(pos_history=optimising2.pos_history,
                                  mesher=m2,  # surface plot provided
                                  mark=(0, 0), # minima marked
                                  title="Particle Swarm Animation")
            progressbar.progress(80)
            # Saves the animation to a usable gif file
            animation2.save('PSOanimparam2.gif', writer='imagemagick', fps=11)
            progressbar.progress(85)

            """### gif from local file"""
            file2 = open("PSOanimparam2.gif", "rb")
            contents2 = file2.read()
            data2 = base64.b64encode(contents2).decode("utf-8")
            file2.close()

            progressbar.progress(92)

            st.header("Swarm one")
            st.image(f'PSOanimparam.gif')
            progressbar.progress(95)
            st.write("Best position found by the swarm: ")
            st.text(pos)


            st.header("Swarm Two")
            st.image(f'PSOanimparam2.gif')
            st.write("Best position found by the swarm: ")
            st.text(pos2)
            progressbar.empty()

        #column1, column2 = st.beta_columns(2)
        #column1.header("Swarm One")
        #column1.image(f'PSOanimparam.gif')

      #  column2.header("Swarm Two")
       # column2.image(f'PSOanimparam2.gif')


            st.info("What do you notice about the two swarms and what key "
                    "differences can you observe between them?")

            # create an expanding widget with relevant label
            expander = st.beta_expander(label='Differences when using a higher Cognitive value')
            # add  text to expander
            expander.write("Particles on the right are grouped and oscillate around in a similar fashion to the bird "
                           "flock on the left. Some PSO variants like the Global Best variant we are discussing use "
                           "the best position found so far for judging movement. This means the Particles follow the "
                           "strongest Particle, which similar to how birds in a flock commonly follow "
                           "the strongest bird in the flock. ")


            expander2 = st.beta_expander(label='Differences when using a higher Social value')

            expander2.write("Particles on the right are grouped and oscillate around in a similar fashion to the bird "
                           "flock on the left. Some PSO variants like the Global Best variant we are discussing use "
                           "the best position found so far for judging movement. This means the Particles follow the "
                           "strongest Particle, which similar to how birds in a flock commonly follow "
                           "the strongest bird in the flock. ")

    st.info("Make sure you have set parameters for both swarms before clicking the generate button.")
    if st.checkbox("Generate Particle Swarms"):
        generateSwarms()
