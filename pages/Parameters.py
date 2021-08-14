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
             "The only difference between them is the parameters that you select. ")

    st.subheader("Particle swarm parameters")

    st.info("HINT: ONLY use values between 0.1 and 2 for c1 and c2. Also, use opposite c1 and c2 values for each swarm "
            "to see differences between the two. Test using the parameters below to start with so that you have "
            "an idea of what values to set as parameters.")

    # parameter input fields, taking a float value
    parameters = {"c1": float(st.text_input("Cognitive parameter (c1)", 2)),
               "c2": float(st.text_input("Social parameter (c2)", 0.6)),
               'w': float(st.text_input("Social parameter (w)", 0.7))}

    # create space in the page
    st.write("  \n")
    st.write("  \n")
    st.info("If this section shows an error, simply refresh the page.")
    # inputting second swarm's parameters
    st.subheader("Second swarm's parameters")

    parameters2 = {"c1": float(st.text_input("Second swarm: Cognitive parameter (c1)", 0.6)),
                "c2": float(st.text_input("Second Swarm: Social parameter (c2)", 2)),
                'w': float(st.text_input("Second Swarm: Inertia parameter (w)", 0.7))}


    #ADD CHECKS FOR ENSURING NO VALUES INPUT TOO HIGH, AND INERTIA VALUES CHECKED TO BE GOOD AND NOT RIDICULOUS

    # swarm generation function

    def generateSwarms():
        with st.spinner('Generating both Particle Swarms'):
            progressbar = st.progress(0)
            # create the swarm with Particles and dimensions and parameters
            swarm = ps.single.GlobalBestPSO(n_particles=20, dimensions=2, options=parameters)
            progressbar.progress(10)


            # optimise the swarm for the given amount of iterations on a spherical plain
            cost, pos = swarm.optimize(fx.sphere, iters=150)
            progressbar.progress(20)


            # create mesher within the shape of a sphere
            # plots results of the algorithm
            m = Mesher(func=fx.sphere)
            progressbar.progress(30)

            # create animation of the swarm
            # plot positions on a 2D sphere plain, with a marked minima at 0,0
            animation = plot_contour(pos_history=swarm.pos_history,
                                     mesher=m,  # surface plot provided
                                     mark=(0, 0),  # minima marked
                                     title="Particle Swarm Animation")

            progressbar.progress(45)

            # Saves the animation to a usable gif file
            animation.save('PSOanimparam.gif', writer='imagemagick', fps=11)
            progressbar.progress(48)

            # 2nd particle swarm's generatiom
            swarm2 = ps.single.GlobalBestPSO(n_particles=20, dimensions=2, options=parameters2)

            # optimise the swarm for the given amount of iterations on a spherical plain
            cost2, pos2 = swarm2.optimize(fx.sphere, iters=150)
            progressbar.progress(65)

            # create mesher within the shape of a sphere
            # used for plotting working results of objective functions
            m2 = Mesher(func=fx.sphere)

            # create animation of the swarm
            # plot positions on a 2D sphere plain, with a minima of 0,0
            animation2 = plot_contour(pos_history=swarm2.pos_history,
                                  mesher=m2,  # surface plot provided
                                  mark=(0, 0), # minima marked
                                  title="Particle Swarm Animation")
            progressbar.progress(80)
            # Saves the animation to a usable gif file
            animation2.save('PSOanimparam2.gif', writer='imagemagick', fps=11)
            progressbar.progress(85)

            st.info("To Generate a new set of Particle Swarms, input new parameters and then retick "
                    "the generate box. This may make the page glitch for a moment.")
            st.header("Swarm one")
            st.image(f'PSOanimparam.gif')
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
            expander = st.beta_expander(label='Differences when using a higher Cognitive trust value')
            # add  text to expander
            expander.write("Particle Swarms with a higher cognitive trust factor are naturally more exploitative "
                           "and therefore will explore the search space more, This is because they follow "
                           "their own personal best (PBEST) position when determining their next movement."
                           "")

            expander2 = st.beta_expander(label='Differences when using a higher Social trust value')

            expander2.write("Particles that are given a higher social and low cognitive trust factors will perform the "
                            "opposite and will explore less of the search space due to being drawn towards positions "
                            "explored by other Particles that have been determined as a more optimal."
                            "")

            expander3 = st.beta_expander(label='Conclusion of parameter effects')

            expander3.write("You may notice that the swarms do not perform that differently from each other if both "
                            "of them have a value above 0.1 for the trust factor with the lowest set value. "
                            "While lower value trust parameters will discourage Particles to be influenced "
                            "by either PBEST or GBEST values, any existent trust in these values still allows the "
                            "swarm to rely on other particles for movement, which inherently can improve PBEST values.")

            expander3.subheader("So how do we make swarm parameters create observable differences?")
            expander3.write("As you have seen earlier when learning Convergence and potentially when experimenting "
                            "with the parameters above, Inertia massively effects the speed at which Particles "
                            "Converge to the Global minima of the given problem function. Finding the "
                            "appropriate Inertia value to ensure that PSO does not converge too early or too "
                            "late is one of PSO's many problems that has been subject to much research.")

            expander3.write("Another factor is that so far, all Particle Swarms generated by this tool have used "
                            "Global Best PSO. The version used for this swarm adopts the 'star' topology. "
                            "In the next section, we will experiment with different variants/types of PSO that change "
                            "how Particles can communicate.")

    st.info("Make sure you have set parameters for both swarms before clicking the generate button.")
    if st.checkbox("Generate Particle Swarms"):
        generateSwarms()
