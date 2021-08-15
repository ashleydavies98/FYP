# import Streamlit
import streamlit as st
# import numpy for use with bounds
import numpy as np

# import PSO related modules
import base64
import matplotlib.pyplot as plt
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import (plot_cost_history, plot_contour, plot_surface)
from pyswarms.utils.plotters.formatters import Mesher

# create the page as an accessible app function, so that the page can be accessed from the navigation bar
def app():
    global checkboxTicked
    st.title('Types of Particle Swarm Optimisation algorithms')

    st.write("As just discussed, here we will expand on how using different types of neighbourhood topologies "
             "can effect the results of a PSO algorithm.")
    st.write("Neighbourhood topology refers to how Particles can be grouped into 'neighbourhoods' "
             "that change how they interact with other Particles in the swarm. ")
    st.write("So far, Particle swarm's in this tool have only used Global Best PSO, a variant of PSO that uses "
             "the entire swarm's GBEST value to influence Particle movement. Now we will use Local Best PSO. "
             "The main focus here will be on the differences in using Local Best PSO and Global Best PSO, which "
             "respectively represent the two 'ring' and 'star' topologies that we will discuss.")
    st.subheader("So what's the difference?")
    st.write("The parameters discussed previously effect how Particles rely on the positions found by "
             "other Particles, being either "
             "they rely more on the Global Best value (social) for influence, or their own Personal Best "
             "position (cognitive).  \n"
             "A specific neighbourhood topology however, will effect how Particles group together and rely on "
             "each other in groups of neighbourhoods, which determine how they can communicate with other "
             "particles. ")

    column1, column2 = st.beta_columns(2)
    column1.subheader("Ring Topology")
    column1.write("Within a 'ring' topology, Particles have corresponding neighbours, who are the only "
                  "Particles that they can compare performance with. This means that each Particle is "
                  "attracted to the Best Positions (PBESTS) found by its nearest neighbouring Particles, rather than "
                  "the Best Positions (GBESTS) found by the entire swarm.")
   # column1.image("")
    column2.subheader("Star Topology")
    column2.write("Within a 'star' topology, Particles rely on the best position taken from a single Particle in the "
                  "entire swarm at the time (iteration). Specifically, this is the Particle with the best performing "
                  "PBEST position out of the entire swarm. This value replaces the GBEST of the search space.")
   # column2.image("")

    st.title("The effect on convergence")
    # create an expanding widget with relevant label
    expander = st.beta_expander(label='Local Best Topology')
    # add  text to expander
    expander.subheader("Local Best topologies")
    expander.write("As you now know, Particles here share best position information with a set of Particles within "
                   "their neighbourhood in a swarm. These sets can be adapted by changing the number of neighbours (k) "
                   "to create different PSO variants that allow algorithms to return vastly different convergence "
                   "rates. This can create more exploration but it also can cause different groupings "
                   "of Particles to hardly converge at all or converge prematurely at local optimas. ")
    expander.write("Premature Convergence to "
                   "local optimas mean that sets of neighbouring Particles converge at positions in the "
                   "search space that they cannot escape from, due to their lack of ability to explore without a "
                   "neighbouring Particle with a better position. However, a large amount of present local "
                   "optima/minima can mean that the algorithm is in fact Mutlimodal. Multimodal algorithms aim "
                   "to discover mutliple fit solutions for a given problem by optimising to find "
                   "multiple local minima. This will be expanded on later in the tool when applications of PSO are "
                   "discussed.")
    expander.image("images/ringtop.png")

    # SHOW EXAMPLE OF RING HERE, MAYBE INCLUDE CONVERGENCE EXAMPLE TOO, OF LOCAL OPTIMUMS?
    expander2 = st.beta_expander(label='Global Best Topology')
    expander2.subheader("Global Best topologies")
    expander2.write("By using a star topology, all Particles are connected to one centre node. This can cause very "
                    "little exploration around the search space as all Particles are attempting to follow one "
                    "Particle's PBEST position at any time. This can result in the entire swarm converging prematurely "
                    "to Local minima.")
    expander2.image("images/startop.png")

    # generates two global best Particle swarm with bounds and without bounds and displays them on screen
    def generateSwarms():
        # display message while swarms are generating
        with st.spinner('Generating both Particle Swarms'):
            # progress bar displayed
            progressbar = st.progress(0)
            """
            new addition to parameters:
            k: int (less than n_particles), value of the number of neighbours to be considered by the Particle
            p: int (1,2), selects a Minkowski p-norm, 1 is the sum of absolute values, 2 is Euclidean distance
            """
            parameters = {'c1': 0.5, 'c2': 0.3, 'w': 0.9, 'k': 1, 'p': 2}
            # Local Best PSO using ring topology
            swarm = ps.single.LocalBestPSO(n_particles=25, dimensions=2, options=parameters)
            # progress bar updated
            progressbar.progress(10)
            # optimise the swarm for the given amount of iterations on a spherical plain
            cost, pos = swarm.optimize(fx.sphere, iters=165)

            # create mesher within the shape of a sphere
            # used for plotting working results of objective functions
            m = Mesher(func=fx.sphere)
            progressbar.progress(20)
            # create animation of the swarm
            # plot positions on a 2D sphere plain, with a minima of 0,0
            animation = plot_contour(pos_history=swarm.pos_history,
                                 mesher=m,  # surface plot provided
                                 mark=(0, 0),  # minima marked
                                 title="Particle Swarm Animation")

            # Saves the animation to a usable gif file
            animation.save('PSOanimLocal.gif', writer='imagemagick', fps=11)
            progressbar.progress(30)


            # swarm parameters set
            parameters2 = {"c1": 0.5, "c2": 0.8, "w": 0.9}
            swarm2 = ps.single.GlobalBestPSO(n_particles=25, dimensions=2, options=parameters2)
            progressbar.progress(40)
            # optimise the swarm for the given amount of iterations on a spherical plain
            cost, pos = swarm2.optimize(fx.sphere, iters=165)

            # create mesher within the shape of a sphere
            # used for plotting working results of objective functions
            m = Mesher(func=fx.sphere)
            progressbar.progress(60)

            # create animation of the swarm
            # plot positions on a 2D sphere plain, with a minima of 0,0
            animation2 = plot_contour(pos_history=swarm2.pos_history,
                                 mesher=m,  # surface plot provided
                                 mark=(0, 0),  # minima marked
                                 title="Particle Swarm Animation")
            progressbar.progress(80)
            # Saves the animation to a usable gif file
            animation2.save('PSOanimGlobal.gif', writer='imagemagick', fps=11)
            progressbar.progress(90)

            st.info("Swarm one: Global Best - Star Topology")
            st.image(f'PSOanimGlobal.gif')

            st.info("Swarm two: Local Best - Ring topology")
            st.image(f'PSOanimLocal.gif')
            # remove progress bar
            progressbar.empty()

            st.write("Looking at the 'Local Best' swarm above, you can clearly observe that Particle movement is far "
                     "different and many Particles are becoming trapped at their Local Optima. Now, "
                     "this animation has been purposely setup to demonstrate the effect "
                     "the ring topology can have when parameters are set incorrectly. As you have learned earlier "
                     "in the tool, parameter choices are paramount to the success of a PSO algorithm.")

            st.subheader("So what caused this effect?")
            st.write("Previously, Particle Swarms that you have experimented with have consisted of only 3 parameters, "
                     "c1, c2 and Interia (w), whereas the Local Best swarm generated in this instance have accepted "
                     "5 parameters. The new parameters here that have caused effects are 'k' and 'p'. "
                     "You may recognise the 'k' parameter from earlier in this page, as it is the value "
                     "representative of the number of neighbours that a Particle has within its 'ring'.")

            st.info("The parameters for the Local Best swarm were as follows:  \n"
                    "- c1: 0.5  \n"
                    "- c2: 0.3  \n"
                    "- w: 0.9  \n"
                    "- k: 1  \n"
                    "- p: 2 (this new parameter applies Euclidean Distance to calculate distances between "
                    "Particles, so that appropriate neighbours can be set to each Particle.")

            st.write("Above, you can see the value of k, which has been set to 1. This means that each Particle "
                     "only has 1 neighbour at any given time. This is the parameter that has been set 'incorrectly' "
                     "as described previously. As you can see in the swarm animation, when a Particle only has "
                     "one neighbour, Particles easily become lost and lose the ability to move to new positions "
                     "due to having no useful updates to their Velocity from this single neighbour. The final "
                     "result here is premature convergence to multiple local optima across the search space, "
                     "providing very little improvement to the problem function solutions.")

            st.write("Once again, highlighting this is to cement the idea of how important selecting appropriate "
                     "parameters is when adapting PSO algorithms for purpose. Next, we discuss how Particle Swarm "
                     "Optimisation has been applied to real life scenarios and how, for some applications, different "
                     "parameters and topologies have been used and tested to achieve solutions.")



   
    st.title("How does topology effect the Particle Swarms?")
    st.write("Above, we've discussed what Global and Local topology can do to a swarm, but what does this look "
             "like when visualised? Use the 'generate' button below to find out!")
    st.subheader("Local and Global Best swarms")
    # if check box is ticked, the execute
    if st.checkbox("Generate Local and Global Best swarm"):
        generateSwarms()






