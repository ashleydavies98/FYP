# import framework
import streamlit as st


# create the page as an accessible app function, so that the page can be accessed from the navigation bar
def app():
    st.title('Components of PSO')
    st.write("As just discussed, the variant of PSO mainly covered in this tool is the Position/Velocity "
             "update algorithm. In this variant, particle positions and Velocity both influence each "
             "other between iterations.   \n The velocity value for each particle is calculated "
             "from multiple components and parameters that are attributed to Particles and the "
             "algorithm's Search Space.")

    st.subheader("The components")

    # function for the 'components' teaching block
    def components():
        st.subheader("Particle Components")
        st.image("images/components.png")
        st.write("As you can see above, 3 main components influence Velocity for Position/Velocity update PSO, "
                 "Next, we discuss exactly HOW those 3 components are used to cause a change in Velocity "
                 "and therefore a change in particle position between Iterations.")

    # function for the 'confidence parameters' teaching block
    def confidence():
        st.subheader("Confidence parameters")
        st.write("Particle Swarm Optimisation is a very adaptable Swarm Intelligence algorithm that can be "
                 "adapted for many "
                 "different uses.")

        st.write("This is because Velocity in Position/Velocity "
                 "PSO is calculated from 3 Parameters, which control the "
                 "influence of the 3 components just discussed. "
                 "These parameters can be adapted to cause a component to "
                 "give more influence on Velocity and provide different results "
                 "with each new optimisation attempt. ")

        st.write("To put it simply, in PSO the influence of each component on "
                 "Particle movement is only as much as "
                 "the Parameters allow them to be. These Parameters are known as Confidence or Trust Parameters. ")

        st.subheader("What are confidence parameters?")

        st.write("Confidence parameters are used within the calculation of Velocity to "
                 "control the influence of PBEST values "
                 "and the entire swarm's GBEST value.")
        st.write("The equation for calculating Velocity is shown using the expander below.")

        expander = st.beta_expander(label='Equation for Velocity')

        expander.info("Velocity  \n = Current motion(w) + Particle memory(c1) + swarm influence (c2)  \n"
                      "- w is the inertia value applied to the swarm that creates a drifting effect. It helps "
                      "particles explore the search space further by creating a "
                      "resistance against changes in Velocity.  \n"
                      "- c1, or cognitive influence, refers to how much a particle "
                      "relies on its own PBEST value for influencing its Velocity.  \n"
                      "- c2, or social influence, refers to how much a particle relies "
                      "on the GBEST of the entire swarm for influencing its Velocity.")

        st.write("As you can see, Confidence Parameters c1 and c2 refer to the influence of PBEST "
                 "AND GBEST respectively. This influence is controlled simply by setting the value "
                 "of either c1 or c2 higher than the other. ")

        st.info("A higher c1 value will cause each particle's movement to be influenced MORE "
                "by their own PBEST positions, rather than the GBEST values.  \n "
                "  \n"
                "As long as the values of c1 and c2 are above 0, "
                "the particles within the swarm will still use both PBEST and GBEST for their Velocity "
                "calculations. However, a higher value "
                "in one of the confidence parameters will see the particles lean more towards that respective "
                "component than the other.")

    # function for the 'components' teaching block
    def searchPara():
        st.subheader("Search Space Parameters")

        st.write("While each particle has its own variables and components, the search space "
                 "also has parameters, which are: Number of iterations(n) and Number of particles. The search "
                 "space also has another variable, which is Time(t).")
        st.info("-Number of iterations: The number of iterations that the algorithm will go through. With each "
                "iteration, the algorithm will try to improve the problems solution further.  \n"
                "  \n"
                "-Number of particles: The number of particles to be placed within the search space.  \n"
                "  \n"
                "-Time: A variable containing The current iteration of the algorithm. Time is tracked "
                "to determine what positions particles are in "
                "at particular points throughout optimisation and is incremented at each new iteration.")

        st.write("More iterations mean more Velocity updates and therefore, further optimisation. However by "
                 "increasing iterations, you are making the computation times of the algorithm longer and "
                 "this could result in wasted performance as it may not be necessary. Also, "
                 "if too little iterations are allowed, then PSO may "
                 "not arrive at a optimal solution before completing.  \n"
                 "  \n"
                 "When selecting parameters for the search space and "
                 "particles and their components, it is important to consider what values should be "
                 "input to achieve a satisfactory optimisation result, but without wasting resources. "
                 "This will be cover later in the tool.")





    # Add a selectbox to the sidebar:
    add_selectbox = st.selectbox(
        'Select a tab from the box below to learn about the components and their effects.',
        ('Choose here!', 'Particle Components', 'Confidence Parameters' , 'Search Space parameters')
    )

    # If an item is selected from the selectbox, display the function content

    if add_selectbox == "Particle Components":
        components()

    if add_selectbox == "Confidence Parameters":
        confidence()

    if add_selectbox == "Search Space parameters":
        searchPara()


