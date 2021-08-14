# import Streamlit
import streamlit as st


# create the page as an accessible app function, so that the page can be accessed from the navigation bar
def app():
    st.title('Applications of PSO')

    st.write("Particle Swarm Optimisation aims to improve a problem solution. "
             "In practical uses, this commonly involves minimising costs, times, and other consumptions, "
             "which means that a lot of the applications of PSO are where these factors are prevalent.")

    st.write("Within the 'Processes of PSO' section, we discussed how Confidence Parameters can cause Particles "
             "to become too 'exploitative' or 'explorative'. In real world usage, algorithms can be adapted "
             "using these Parameters to balance these issues and provide benefits to optimisation.")

    st.write("Such examples use what are widely referred to as ‘Modified PSO’ algorithms, which adapt Parameters "
             "to control exactly how exploitative and explorative the particles are. This allows "
             "for more precise applications of PSO, and search space areas to be explored as much as "
             "required for the given objective function.")



    # Transportation Network Design Problem display function
    def tndp():
        st.header("Transportation Network Design Problem (TNDP)")
        st.subheader("What is the Transportation Network Design Problem")
        st.write("TNDP is a programming model that aims to minimize resource usage by determining optimal network "
                 "paths based on nodes in a set. In usage within planning and development, the objective functions to be "
                 "minimized are chosen based on resource constraints to bring benefits to users, such as reduced "
                 "costs and time usage for the operators of such networks.")

        st.subheader("Applying PSO to the TNDP")
        st.write("Canonical PSO, a standard unaltered version of PSO, does not consider budget and simply solves the "
                 "problem by finding the most optimal solution from a given number of iterations. However, with the "
                 "TNDP, there is a constraint for budgeting during optimisation, which ensures that optimisation "
                 "keeps in mind that resources are not infinite. Therefore, PSO must be modified into 'Modified PSO' "
                 "to account for such constraints.")

        st.write("Within such applications of PSO, exist many parameters beyond what has been discussed within "
                 "this tool. When implementing PSO into an already complex problem like this, PSO has to be adapted "
                 "to consider the optimisation of 'travel time functions'. These are functions used within TNDP "
                 "to determine travel time between nodes. These functions have their own parameters that determine "
                 "movements between nodes and construction costs for each travel. While performing optimisation, "
                 "determining successful budget keeping is a key focus in ensuring that when travelling an entire "
                 "network, as little movements are made as possible, in the cheapest way possible.")
        st.write("To put this into perspective, below is network of nodes called 'The Sioux Falls network' that "
                 "has been taken from the source at the bottom of the page. Such source is a research paper that "
                 "experiments with an application of PSO to the TNDP.")
        st.image("images/tndpnodes.jpg")
        st.write("To optimise this problem, PSO was applied to multiple travel time functions to determine "
                 "the most efficient ways of building a transport network between two nodes. Within the source, "
                 "PSO succesfully achieves optimal solutions that are an improvement on resource usage.")

        st.subheader("What was changed from canonical PSO to optimise TNDP?")
        st.write("The application of PSO here is greatly more complex than the examples shown throughout this tool. "
                 "This is because of the considerations that are required when optimising a problem function "
                 "such as the TNDP. For PSO to be applied correctly here, not only were parameters adapted, "
                 "but measures of success had to be considered to ensure that PSO was improving the solution. ")
        st.write("For TNDP, different performance metrics were tracked to ensure that "
                 "improvements were being made. In the source referred to previously, these metrics are optimal "
                 "solution frequency and best objective function values over 50 attempts.")
        st.write("Two particular useful modifications to PSO for TNDP are set ranges for both Inertia weight "
                 "and maximum moving distance to 'guide particles effectively through the search space' [1]. Both "
                 "of these ranges are applied to the optimisation process to ensure that Particles do not become too "
                 "exploratory and to ensure that convergence to an optima is not too fast or slow.")
        st.write("Another adaptation in the application of PSO here revolves around the fact that PSO "
                 "is typically used to solve continuous optimisation problems, while TNDP is a problem of "
                 "combinatorial nature, meaning that elements are selected from from a large pool, without care "
                 "for the order that they are arranged in. In this situation, TNDP denotes its combinatorial "
                 "variables as binary strings, which must be adapted for use in PSO by transforming values "
                 "into readable and presentable numbers and then reverting this where necessary.")

        st.write("As you can see, when adapting PSO to deal with problems such as TNDP, there is a lot of "
                 "complex modifications that must be made so that PSO can effectively optimise the problem, but "
                 "also so that potential solutions can be identified by the algorithm and presented accordingly.")

        st.subheader("Reference used for TNDP")
        st.markdown(""" 
                    Babazadeh, A., Poorzahedy, H. and Nikoosokhan, S. (2011) "Application of particle swarm optimization 
                    to transportation network design problem", Journal of King Saud University, Available at: 
                    https://www.sciencedirect.com/science/article/pii/S1018364711000188 [1] """)



    def multimodal():
        st.header("Multimodal Optimisation")
        st.subheader("What is Multimodal Optimisation")

        st.write("Multimodal Optimisation is a type of optimisation that aims to locate multiple optima in a single "
                 "optimisation run.")
        st.write("Canonical PSO, discussed throughout this tool, aims to return one solution that solves the given "
                 "problem function. However, there are many potential problems that PSO can be applied to that would "
                 "benefit from or require multiple high quality candidate solutions to provide a choice "
                 "of solutions for the user. This could involve the retrieval of local optima from a algorithm "
                 "with these values already predetermined.")

        st.subheader("Adapting PSO to Multimodal Optimisation")
        st.write("Many problems in the real world carry characteristics of Multimodal Optimisation, as many problems "
                 "require multiple solutions, rather than just one. Due to the prevalance of Multimodal problems, "
                 "development of efficient Multimodal Optimisation algorithms is a highly covered subject. Two "
                 "methods of applying PSO to create Multimodal Optimisation algorithms are the 'iterative and "
                 "subpopulation methods' [2]. In iterative Multimodal Optimisation, PSO is applied multiple times "
                 "at once to a problem so that multiple optima can be found. In subpopulation Multimodal Optimisation, "
                 "Particles are split into groups and are given the task of searching the search space at the "
                 "same time to discover optimal solutions.")

        st.subheader("A Multimodel algorithm")
        st.write("One example of PSO being applied to locate multiple optima is within the NichePSO algorithm [2]. "
                 "For this algorithm, PSO is adapted to change behaviour of Particles and to split them into "
                 "sub-groups.")

        st.write("Throughout NichePSO, candidate solutions (Particles) are monitored closely throughout the time "
                 "(Iterations) of the algorithm. If a Particle's level of quality undergoes no changes, it is set to "
                 "become the candidate solution for the problem. This Particle is then taken from the main swarm and "
                 "placed within a new sub-group. As time progresses throughout the algorithm, more particles are taken "
                 "from the main swarm and more sub-groups are created. These sub-groups are then used to find local "
                 "and global optima throughout the search space.")
        st.write("Such application of PSO is very useful for determining multiple quality candidate solutions for "
                 "a problem and they are altered heavily under much research to ensure that all their pitfalls are "
                 "covered. Such a pitfall for NichePSO can be seen as 'a risk of velocity approaching 0'. To "
                 "combat this, each new sub-group of Particles undergoes a iteration of Guaranteed Convergence PSO, "
                 "which is another PSO algorithm that can be implemented inside NichePSO to ensure that Particles converge.")
        st.write("Highly intelligent combinations of PSO algorithms like this one are great examples of why intuitive "
                 "algorithm design can be very beneficial with PSO, as by combining multiple PSO algorithms together, "
                 "highly complex PSO algorithms can be created, which automatically help solve their own drawbacks.")

        st.subheader("Reference used for Multimodal Optimisation")
        st.markdown(""" 
        Ender Özcan, Murat Yılmaz (2007) "Particle Swarms for Multimodal Optimization" . 
        Available at: https://www.researchgate.net/publication/221157358_Particle_Swarms_for_Multimodal_Optimization [2] """)

    # Add a selectbox to the sidebar:
    add_selectbox = st.selectbox(
         'Applications list',
        ('TNDP', 'Multimodal Optimisation')
    )

    if add_selectbox == "TNDP":
        tndp()



    if add_selectbox == "Multimodal Optimisation":
        multimodal()


