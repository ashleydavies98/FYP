# import Streamlit
import streamlit as st


# create the page as an accessible app function, so that the page can be accessed from the navigation bar
def app():
    st.title('Applications of PSO')

    st.write("Particle Swarm Optimisation improves or solves a problem solution. "
             "In practical uses, this commonly involves minimising costs, times, and other consumptions, "
             "which means that a lot of the applications of PSO are where these factors are prevalent.")

    st.write("Within the 'Processes of PSO' section, we discussed how Confidence Parameters can cause Particles "
             "to become too 'exploitative' or 'explorative'. In real world usage, algorithms can be adapted "
             "using these Parameters to balance these issues and provide benefits to optimisation.")

    st.write("Such examples use what is widely referred to as ‘Modified PSO’ algorithms, which adapt Parameters "
             "to control exactly how exploitative and explorative the particles are. This allows "
             "for more precise applications of PSO, and search space areas to be explored as much as "
             "required for the given objective function.")

    # Add a selectbox to the sidebar:
    add_selectbox = st.selectbox(
        'Applications list',
        ('TNDP', 'HSP', '', '')
    )

    # Transportation Network Design Problem display function
    def tndp():
        st.header("Transportation Network Design Problem")
        st.write("Objectives get minimised from a choice of project resource constraints. Canonical PSO, "
                 "a standard unaltered version of PSO, does not consider budget and simply solves the problem by "
                 "finding the most optimal solution from a given number of iterations. However, with the TNDP, "
                 "there is a constraint for budgeting during optimisation, which is considered when iterating through "
                 "different iterations. ")

    # Heating System Planning function
    def hsp():
        st.header("Heating System Planning")
        st.write("PSO is modified into “modified PSO” and used to make sustainable investment decision into the "
                 "heating systems throughout the country, which in this case is China. The use of PSO provides data "
                 "to improve general decision making about the advancement of systems for the relevant administrations "
                 "that have authority to provide such systems.")

        st.write("Most notable examples of applications for Particle Swarm Optimisation come from systems that require "
                 "predictions, forecasts, and estimation. This means that anything with data can be used in some way to "
                 "provide forecasting. This makes PSO is so useful and important in modern systems, as it allows for "
                 "important predictions to be made, which allows for streamlined recommendations for organisations in "
                 "their choices. Allowing them to save money, time and be more efficient. For the heating system planning "
                 "problem, this is very appropriate as it is a simple system, but with a complex layout and distribution.")

        st.write("HSP focuses on placing and using heating systems in the most sustainable and efficient way possible, this "
                 "is partly due to “building energy consumption accounting for 21.5% of 20.9% of social total energy consumption” [1]")

        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")

        st.markdown(""" 
            Source: HSP
            Rong-Jiang-ma, Nan-Yang Yu, Jun-Yi Hu,- Application of Particle Swarm Optimization Algorithm in the Heating System Planning Problem 
            (2013). Available at: https://www.researchgate.net/publication/255736712_Application_of_Particle_Swarm_Optimization_Algorithm_in_the_Heating_System_Planning_Problem.""")

    # ADD MORE APPLICATIONS, I SAY THERE'S PLENTY IN THE REPORT, DO IT!

    if add_selectbox == "TNDP":
        tndp()

    if add_selectbox == "HSP":
        hsp()



