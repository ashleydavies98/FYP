import streamlit as st


# create the page as an accessible app
def app():
    st.title('Components of PSO')
    st.write("As just discussed, the variant of PSO we cover within this tool is the position/velocity algorithm. "
             "In this variant, particle positions are influenced by velocity, which is created "
             "from a few key components.")


    st.subheader("The components")
    st.write("This page discussed these components and exactly how they can effect the optimisation process "
             "of Particle Swarm Optimisation algorithms.")


    # function for the variables teaching area
    def variables():
        st.subheader("Components")

        st.image("variables.png")

        st.write("The above image shows the components of a PSO algorithm. Velocity is made up " 
                 "of the 3 components in the image and these drive the movement of the particle.")


        st.write("Now that you have learned the components that create velocity for canonical PSO, "
                 "next we discuss how "
                 "those 3 components are used to cause a change in velocity based on parameters set for the swarm.")

    # function for the confidence teaching area
    def confidence():
        st.subheader("Confidence parameters")

        #st.image("canonical.png")
        st.write("Particle Swarm Optimisation is a very adaptable Swarm Intelligence algorithm that can be "
                 "adapted for many "
                 "different purposes.")

        st.write("This is because, movement in position/velocity "
                 "PSO is determined from 3 main parameters, which control the "
                 "influence of the components discussed previously. "
                 "These parameters can be adapted to cause one component to "
                 "give more influence on velocity and provide different results with each new algorithm execution. ")

        st.write("To simplify, in a PSO algorithm, the influence of each component on the "
                 "particle's movement is only as much as "
                 "the parameters allow them to be. These parameters are known as confidence parameters. ")

        st.subheader("What are confidence parameters?")

        st.write("Confidence parameters are used within the calculation of velocity to "
                 "tell the particles whether to rely more on their PBEST or the entire "
                 "swarm's GBEST for influencing their velocity value.  \n"
                 "The way velocity is calculated is shown using the equation below.")

        st.info("Velocity  \n = Current motion(w) + Particle memory(c1) + swarm influence (c2)  \n"
                "- w is the inertia value applied to the swarm that creates a drifting effect. It helps "
                "particles explore the search space further.  \n"
                "- c1, or cognitive influence, refers to how much a particle relies on its own PBEST value "
                "for influencing its velocity.  \n"
                "- c2, or social influence, refers to how much a particle relies on the GBEST of the entire "
                "swarm for influencing its velocity")

        st.write("As you can see, c1 and c2 refer to the influence of PBEST AND GBEST respectively. "
                 "This influence is controlled by setting "
                 "the value of either c1 or c2 higher than the other. ")

        st.info("For example, A higher c1 value will cause each particle's movement to be influenced MORE "
                 "by their own PBEST positions, rather than the GBEST values.  \n "
                 "  \n"
                 "As long as the values of c1 and c2 are above 0, "
                 "the particles within the swarm will still use both PBEST and GBEST for their velocity "
                 "calculations. However, a higher value "
                 "in one of the confidence parameters will see the particles lean more towards that "
                 "component than the other.")

    # Add a selectbox to the sidebar:
    add_selectbox = st.selectbox(
        'Choose a component to learn about below!',
        ('Choose here!', 'Components', 'Confidence Parameters')
    )

    # If an item is selected from the selectbox, display the function content
    if add_selectbox == "Choose here!":
        st.info("Here you can learn about the different components that allow Particle Swarm Optimisation "
                "to function and what role they play in the optimisation process.")

    if add_selectbox == "Components":
        variables()

    if add_selectbox == "Confidence Parameters":
        confidence()

