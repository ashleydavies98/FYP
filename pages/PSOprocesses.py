import streamlit as st


# create the page as an accessible app function, so that the page can be accessed from the navigation bar
def app():
    st.title('Processes of PSO')
    st.write("Particle Swarm Optimisation algorithm has many processes "
             "happening all at once. To make these processes simpler, this tool breaks "
             "PSO down into 3 basic processes that explain how PSO starts and finishes, along with "
             "the relevant functionality involved in ensuring the algorithm works as intended.")

    def initialising():
        st.subheader("Initialising")
        st.write("The first stage is to begin the optimisation process. The swarm is provided with its "
                 "parameters as discussed previously and the search space is "
                 "populated with the given amount of Particles. "
                 "The Particles then begin oscillating around the search space according to the velocity "
                 "calculations that are applied with each new Iteration.")

        st.image("images/searchspace.png")

        st.subheader("A programmed example")

        st.write("To give you more understanding of how PSO is initialised, here is a real code example "
                 "of a PSO algorithm's code and the relevant parameters that are passed into it.")

        st.image("images/swarmcode.PNG")

        st.write("This Python code starts with the values of the c1, c2 and inertia confidence parameters being set to "
                 "the 'parameters' variable. ")

        st.write("Next, an instance of the swarm is created and stored within the 'swarm' variable, "
                 "using a function that creates a 'GlobalBestPSO' swarm, which we discussed in the "
                 "introduction. This takes the number of Particles, the swarm dimensions and the "
                 "confidence parameters as its parameters. To reiterate, the GlobalBestPSO function "
                 "means that the swarm is created with a Global Best PSO topology. This topology is "
                 "the standard for canonical PSO and means that all Particles are part of one large "
                 "neighbourhood and can therefore, all communicate with each other.  \n")

        st.write("Once the PSO instance is created, a function called 'optimize' is executed on the swarm, "
                 "which begins the optimisation process for the given amount of Iterations using a sphere "
                 "function. This function provides the swarm with a Global minimum position set at 0,0, which "
                 "is the smallest value of the function and is relatively easy to find. Here, the Particle "
                 "Swarm Optimisation algorithm's Particles attempt to find this position and discover optimal "
                 "'best' positions.")

        with st.form("Processes form"):

            st.write("Previously, we discussed the effect of confidence parameters. Looking at the values of c1, "
                     "c2 in the above image, what will influence Particle movement the most?")
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

    def optimising():
        st.subheader("Optimising")
        st.write("When Particles start following BEST values towards an optimal solution, Particles begin to "
                 "enter a closer proximity to one another, oscillating towards the optima. "
                 "The optima is the solution that is deemed optimal within an entire (global) "
                 "or neighbouring (local) set of candidate solutions (Particles). This global "
                 "and local topology system is discussed and explained in detail further in the 'Types of PSO' section. "
                 "A problem is effectively solved if the given problem reaches a optima that matches "
                 "the value of the original function.")
        st.image("images/optimising.png")

    def convergence():
        st.subheader("Convergence")

        st.write(
            "Converging of Particles towards a optimum. Convergence rate and the possibility of Convergence "
            "is based on swarm parameters and the topology that the algorithm uses.")
        # create a column widget, formatting a section of the page into 2 columns
        column1, column2 = st.beta_columns(2)
        column1.header("Converging Particle Swarm")
        column1.image(f'images/convergence.gif')
        # code for text positioning
        column2.write("  \n")
        column2.write("  \n")
        column2.write("  \n")
        column2.write("  \n")
        column2.write("  \n")
        column2.write("  \n")
        column2.info("The Particles on the left follow GBEST PSO under a strong Social trust parameter,   \n"
                      "which results in them all converging at a similar point in time.")

        st.write("REMEMBER, each 'Particle' represents a potential 'solution'.")
        st.write("Particles can explore in both an exploitative or explorative fashion, "
                 "meaning that they either search around the current solution locally, "
                 "or the entire search space. "
                 "Parameter choices effect how heavily a Particle is exploitative or explorative "
                 "in each Iteration of movement. If a Particle is set with parameters that make it more "
                 "explorative such as a higher inertia value, then the Particles may converge "
                 "too early at a local optimum solution, without "
                 "discovering a potentially more preferable solution in the search space. ")
        st.write("The same goes for ""having too little exploitative behaviour, as the swarm could explore "
                 "too much throughout "
                 "its Iterations, causing Particles to not converge to an optimum before reaching "
                 "the algorithm's stopping condition.")
        st.info("Due to these problems, it is important to ensure that appropriate parameters are selected, "
                "especially for the value of inertia, to ensure that Particles have a good balance of "
                "exploitative and explorative behaviour. To reiterate, this will ensure that Particles do "
                "not converge prematurely to a local optimum, or explore too much too much of "
                "the search space that they do not converge to the Global minima.")
        st.write("Typically, Particles will be more explorative at the initialisation of optimisation "
                 "as the Particles will have larger velocity values that allow them to explore the "
                 "search space more. Further through the Iterations, once velocity slows down and Particles "
                 "begin to converge, they will become more exploitative, as PBEST values for all Particles "
                 "will be in close proximity to each other.")

        st.write("Below are some demonstrations of how Particle Swarm Optimisation is effected when the Inertia "
                 "value is changed.")

        expander1 = st.beta_expander(label='The effect of low inertia - w = 0.5')
        expander1.image(f'PSOW5.gif')
        expander1.write("Particles have low inertia and therefore are not explorative, but entirely "
                        "exploitative. This makes them converge to the Global minima very fast.")
        expander1.info("Minima/Optima: Point of optimal criteria. If a function is optimal when maximised, "
                       "then optima is used, and vice versa.   \n"
                       "The Particle swarms used in this tool aim to find the minima of a sphere function. "
                       "The Global minima is located at 0, 0 for a sphere function, which is why "
                       "the Particles in the animations on screen all converge at 0, 0. "
                       "Ideally, Particles need to be able to roam enough to find the best position possible "
                       "before becoming trapped at the global minima, as they do in the above animation.")

        expander2 = st.beta_expander(label='The effect of medium inertia - w = 0.7')
        expander2.image(f'PSOW7.gif')
        expander2.write("Particles have a slight ability to explore due to the higher inertia, but still "
                        "converge quickly to the Global Minima without much exploration.")

        expander3 = st.beta_expander(label='The effect of high inertia - w = 0.9')
        expander3.image(f'PSOW9.gif')
        expander3.write("Particles have an inertia value of 0.9, which means that they carry "
                        "a lot of momentum when attempting to move to the next optimal location. "
                        "Due to this momentum, they are far more explorative and as you can see "
                        "in the animation, they cover far more of the search space, which allows them "
                        "to discover a wider range of optimal positions.")



    # Add a selectbox to the sidebar:
    add_selectbox = st.selectbox(
        'Choose the process to learn below!',
        ('Choose here!', 'Initialising PSO', 'Optimising', 'Convergence')
    )



    # If an item is selected from the selectbox, display the function content
    if add_selectbox == "Choose here!":
        st.info("Here you can learn about the different components that allow Particle Swarm Optimisation "
                "to function and what role they play in the optimisation process.")

    if add_selectbox == "Initialising PSO":
        initialising()

    if add_selectbox == "Optimising":
        optimising()

    if add_selectbox == "Convergence":
        convergence()
    # inertia value: larger = greater global search. smaller inertia  greater local search ability

