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
    st.title('Types of Particle Swarm Optimisation algorithms')

    st.write("On the previous page, we discussed how different parameters can effect PSO algorithms.  \n"
             "Next we will discuss how different types of neighbourhood topologies like star and ring can effect "
             "the results of PSO.")
    st.write("Neighbourhood topology refers to how particles can be grouped into 'neighbourhoods' "
             "that change how they interact with other particles in the swarm. ")
    st.write("Our main focus will be on the differences in using Local best PSO or Global best PSO, which are "
             "commonly ring and star respectively.  \n"
             "As we have discussed before, particle swarm's have a global best value representing "
             "the best position found by the entire swarm, "
             "and local best values for each individual particle.  \n"
             "Using one or the other of these topologies will effect how particles group together and "
             "what they rely on to influence their movement, "
             "similarly to the adjusting of parameters discussed on the previous page.")

    st.subheader("So what's the difference?")
    st.write("The parameters discussed previously effect how particles rely on the positions found by "
             "other particles, being either "
             "they don't rely on the global best value (social) for influence, or their own personal best "
             "position (cognitive).  \n"
             "Whereas, a specific neighbourhood topology will effect how particles group together and rely on "
             "each other "
             "in groups of neighbourhoods, or whether they will be entirely independent. ")
    st.write("If it is still unclear then, in simple terms, a LOCAL topology will cause particles "
             "to rely on those close within their neighbourhood "
             "'neighbourhood'.  Such reliance would also be set by parameters similar to those discussed "
             "previously.  \n"
             "A more GLOBAL centric topology will mean that particles do not interact with "
             "particles local with them, but instead follow after "
             "the particle with the best known position")

    st.title('How does topology really effect the Particle Swarms?')

    # parameters for the local best swarm below
    optionsBounds ={"c1" : 0.5, "c2" : 0.8, "w" : 0.9, "k": 2, "p": 2}

    # generates a localbest particle swarm and displays it on screen
    def generateLocalSwarms():

        optimising = ps.single.LocalBestPSO(n_particles=25, dimensions=2, options=optionsBounds)
        # optimise the swarm for the given amount of iterations on a spherical plain
        cost, pos = optimising.optimize(fx.sphere, iters=165)

        # create mesher within the shape of a sphere
        # used for plotting working results of objective functions
        m = Mesher(func=fx.sphere)

        # create animation of the swarm
        # plot positions on a 2D sphere plain, with a minima of 0,0
        animation = plot_contour(pos_history=optimising.pos_history,
                                 mesher=m,  # surface plot provided
                                 mark=(0, 0), # minima marked
                                 title="Particle Swarm Animation")

        # Saves the animation to a usable gif file
        animation.save('PSOanim.gif', writer='imagemagick', fps=11)

        st.info("Swarm one:")

        """### gif from local file"""
        file_ = open("PSOanim.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src = "data:image/gif;base64,{data_url}" width="750" height="650">',
            unsafe_allow_html=True, )


    st.subheader("Local Best swarms")

    st.write("The local PBEST swarm is generated with bounds. Bounds are set boundaries that the particle positions "
             "cannot exceed. This stops particles from exploring too far in the search space.")

    if st.checkbox("Generate Local Best swarm"):
        generateLocalSwarms()


    # generates two global best particle swarm with bounds and without bounds and displays them on screen
    def generateGlobalBoundsSwarm():

        # Create bounds
        max_bound = 5.12 * np.ones(2)
        min_bound = - max_bound
        bounds = (min_bound, max_bound)

        options ={"c1" : 0.5, "c2" : 0.8, "w" : 0.9}

        optimising = ps.single.GlobalBestPSO(n_particles=25, dimensions=2, options=options, bounds=bounds)
        # optimise the swarm for the given amount of iterations on a spherical plain
        cost, pos = optimising.optimize(fx.sphere, iters=150)


        # create mesher within the shape of a sphere
        # used for plotting working results of objective functions
        m = Mesher(func=fx.sphere)

        # create animation of the swarm
        # plot positions on a 2D sphere plain, with a minima of 0,0
        animation = plot_contour(pos_history=optimising.pos_history,
                                 mesher=m,  # surface plot provided
                                 mark=(0, 0), # minima marked
                                 title="Particle Swarm Animation")

        # Saves the animation to a usable gif file
        animation.save('PSOanimBounds.gif', writer='imagemagick', fps=10)


        st.info("Swarm one: With bounds")

        """### gif from local file"""
        file = open("PSOanimBounds.gif", "rb")
        readfile = file.read()
        data = base64.b64encode(readfile).decode("utf-8")
        file.close()

        #st.info(optimising.mean_pbest_history)
        #st.info(optimising.mean_neighbor_history)
        st.markdown(
            f'<img src = "data:image/gif;base64,{data}" width="750" height="650">',
            unsafe_allow_html=True, )

        #second swarm creation, without bounds

        options2 = {"c1": 0.5, "c2": 0.8, "w": 0.9}

        optimising = ps.single.GlobalBestPSO(n_particles=25, dimensions=2, options=options2)
        # optimise the swarm for the given amount of iterations on a spherical plain
        cost, pos = optimising.optimize(fx.sphere, iters=150)

        # create mesher within the shape of a sphere
        # used for plotting working results of objective functions
        m = Mesher(func=fx.sphere)

        # create animation of the swarm
        # plot positions on a 2D sphere plain, with a minima of 0,0
        animation = plot_contour(pos_history=optimising.pos_history,
                                 mesher=m,  # surface plot provided
                                 mark=(0, 0),  # minima marked
                                 title="Particle Swarm Animation")
        # Saves the animation to a usable gif file
        animation.save('PSOanimNoBounds.gif', writer='imagemagick', fps=10)


        st.info("Swarm two: Without bounds")

        """### gif from local file"""
        file2 = open("PSOanimNoBounds.gif", "rb")
        readfile = file2.read()
        data2 = base64.b64encode(readfile).decode("utf-8")
        file2.close()

        st.markdown(
            f'<img src = "data:image/gif;base64,{data2}" width="750" height="650">',
            unsafe_allow_html=True, )

    st.subheader("Global Best swarms")
    if st.checkbox("Generate Global best swarms"):
        generateGlobalBoundsSwarm()


    st.title("The effect on convergence")
    st.subheader("Local Best topologies")
    st.write("Local topologies cause particles to share position information with a set of particles within "
             "the swarm. These sets can be adapted to create different PSO variants that allow algorithms to "
             "return vastly different convergence results. ")
    st.write("One of the more used and understood variants of local topologies "
             "is the ring topology. Where a particle always has two neighbours. This means that each "
             "particle shares best position information with two other particles at all times. This "
             "can create more exploration, but also many different groupings of particles settling at "
             "local optimums")
    #SHOW EXAMPLE OF RING HERE, MAYBE INCLUDE CONVERGENCE EXAMPLE TOO, OF LOCAL OPTIMUMS?

    st.subheader("Global Best topologies")
    st.write("A Global Topology relies on the best position taken from a single particle in the entire swarm. This can "
             "cause the entire swarm to trapped in a local optimum, where little exploration is achieved as all "
             "particles are following one best known position.")
    #EXAMPLES OF GLOBAL TOP, STAR? IMAGERY, AND POTENTIALLY GENERATED GIF? TRY FIND PYSWARMS STUFF FOR GENERATION


    st.markdown("""A. P. Engelbrecht, "Particle Swarm Optimization: Global Best or Local Best?," 2013 BRICS Congress on Computational Intelligence and 11th Brazilian Congress on Computational Intelligence,
     2013, pp. 124-135, doi: 10.1109/BRICS-CCI-CBIC.2013.31.""")
