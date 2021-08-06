import streamlit as st



def app():
    st.title('Processes of PSO')
    st.write("Even the most basic Particle Swarm Optimisation algorithm has many processes "
             "happening all at once. To make these processes simpler, this tool breaks "
             "PSO down into 3 basic processes that explain how PSO starts and finishes, along with"
             "the relevant functionality involved in ensuring the algorithm works as intended.")

    def initialising():
        st.subheader("Initialising")
        st.write("The first stage is to begin the optimisation process. The swarm is provided with its "
                "parameters as discussed previously and the search space is "
                "populated with the given amount of particles. "
                "The particles then begin oscillating around the search space according to the velocity "
                "calculations that are applied with each new iteration.")
        st.image("searchspace.png")
        st.subheader("A programmed example")
        st.write("To give you more understanding how PSO is initialised, here is a real code example "
                 "of a PSO algorithm's code and the relevant parameters being passed in.")
        st.image("swarmcode.png")
        st.write("This Python code (built using the PySwarms library, acknowledgements found at the end of the tool) "
                 "starts with a dictionary of parameters being created. ")
        st.write("Next, within a callable function, the swarm is created, using a function that creates a "
                 "'GlobalBestPSO' swarm , taking the number of particles, the swarm dimensions and the confidence "
                 "parameters as its parameters. The GlobalBestPSO function means that the swarm is created with a "
                 "Global Best PSO topology. This topology is the standard PSO topology and means that all particles "
                 "can communicate and therefore, use the GBEST value of the entire swarm."
                 "")

    def optimising():
        st.subheader("Optimising")
        st.write("When particles start following BEST values towards an optimal solution, particles begin to "
             "enter a closer proximity to one another, oscillating towards the optima. "
             "The optima is the solution that is deemed optimal "
             "within an entire (global) or neighbouring (local) set of "
             "candidate solutions (particles). This global and local topology system is "
             "discussed and explained in detail further in the tool. "
             "A problem is effectively solved if the given problem reaches a optima that matches the value of "
             "the original function to be optimised.")
        st.image("optimising.png")

    def convergence():
        st.subheader("Convergence")

        st.write(
            "Converging of particles towards a optimum. This is based on the swarm's parameters "
            "and the topology that the algorithm uses")
        st.image("convergence.png")

        st.write("Particles can explore in both a exploitative or exploratory fashion. "
                "Parameter choices effect how heavily a particle is exploitative or exploratory "
                "in each iteration of movement. If a particle is set with parameters that make it slightly "
                "exploratory, then the particles may converge too early at a local optimum solution, without "
                "discovering a potentially more preferable solution in the search space. ")
        st.write("The same goes for ""having too little exploitative behaviour, as the swarm could explore"
                "too much throughout "
                "its iterations, causing particles to not converge to an optimum before reaching "
                "the algorithm's stopping condition.")
        st.info("Due to these problems, it is important to ensure that appropriate parameters are selected "
                "for c1 and c2 to ensure that a particle has a good balance of "
                "exploitative and exploratory behaviour. To reiterate, this will ensure that particles do "
                "not converge prematurely to a local optimum, or explore too much too much of "
                "the search space that they do not converge to the optimum location.")



    # Add a selectbox to the sidebar:
    add_selectbox = st.selectbox(
        'Choose the process to learn below!',
        ('Choose here!', 'Initialising the algorithm', 'Optimising', 'Convergence')
    )



    # If an item is selected from the selectbox, display the function content
    if add_selectbox == "Choose here!":
        st.info("Here you can learn about the different components that allow Particle Swarm Optimisation "
                "to function and what role they play in the optimisation process.")

    if add_selectbox == "Initialising the algorithm":
        initialising()

    if add_selectbox == "Optimising":
        optimising()

    if add_selectbox == "Convergence":
        convergence()
    # inertia value: larger = greater global search. smaller inertia  greater local search ability
