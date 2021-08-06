import streamlit as st



def app():
    st.title('Applications of PSO')

    st.write("Particle Swarm Optimisation is all about improving a problem solution to be a higher quality. "
             "In practical uses, this commonly involves minimising costs, times, and other consumptions. "
             "This means that a lot of the applications of PSO are where these factors are prevalent.")

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



