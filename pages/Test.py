import streamlit as st

# create the page as an accessible app function, so that the page can be accessed from the navigation bar
def app():

    st.title('Tests')

    st.write("You've reached the end of that app. Now that you've learned about Particle Swarm Optimisation, "
             "here are some questions that will test your knowledge based on what has been taught throughout the app.  \n")
    st.write("When you have answered a question, click the submit button at the bottom of its area "
             "to find out if you answered correctly.")
    # Create question form 1
    with st.form("Question form 1"):

        st.write("What influences particle movement?")
        # Add a question select box
        q1 = st.selectbox(
            'Answer choices',
            ('PBEST', 'GBEST', 'Inertia(w)', 'All of the above')
        )
        submit = st.form_submit_button("Submit")

        if submit:
            if q1 == 'All of the above':
                st.info("Correct!")
            else:
                st.info("Incorrect, try again!")

    # Create question form 2
    with st.form("Question form 2"):
        st.write("Which parameter makes the particles rely more on their own Pbest?")

        q2 = st.selectbox(
            'Answer choices',
            ('c2', 'c1', 'Inertia(w)', 'Ebest')
        )

        submit = st.form_submit_button("Submit")

        if submit:
            if q2 == 'c1':
                st.info("Correct!")
            else:
                st.info("Incorrect, try again!")

    # Create question form 3                             POTENTIALLY SUBJECTIVE?
    with st.form("Question form 3"):
        st.write("What is the objective of Particle Swarm Optimisation?")

        q3 = st.selectbox(
            'Answer choices',
            ('To make less choices of optimal solutions',
             'To make given problems take less time',
             'Improve/find optimal solutions to a given problem',
             'Potentially, all of the above')
        )

        submit = st.form_submit_button("Submit")

        if submit:
            if q3 == 'Potentially, all of the above':
                st.info("Correct! While PSO is used to improve solutions to a problems, throughout the tool "
                         "we've discovered how PSO can be applied to many problems to provide more specifically "
                         "optimal solutions and to potentially save resources, such as time.")
            else:
                st.info("Incorrect, try again!")

    # Create question form 4
    with st.form("Question form 4"):
        st.write("A swarm of particles aren't very successful without communication, why is communication "
                 "important between particles?")

        q4 = st.text_area("Insert your answer here.")

        submit = st.form_submit_button("Submit")

        if submit:
            st.write("How does your answer compare to the correct answer below?")
            st.info("Correct answer:  \n"
                    "Particle communication is important because of how BEST values are used to find "
                    "optimum solutions. Without particle communication, every particle would be searching "
                    "for their own individual best solution. While this could provide a vast amount "
                    "of possible solutions, there would more than likely be a lack of convergence to "
                    "an appropriate solution and convergence to many local optimas. "
                    "Whereas, by communicating with each other, either through reliance on the swarm's "
                    "GBEST or PBESTs from local neighbouring particles, there is far more success in "
                    "optimising the problem and more chance of convergence to a optimum in before "
                    "reaching a stopping condition.")

    with st.form("Question form 5"):

        st.write("When discussing Local Best Types of Particle Swarm Optimisation, which parameter was causing the "
                 "Particles to converge at many local minima?")
        # Add a question select box
        q5 = st.selectbox(
            'Answer choices',
            ('Number of neighbours (k)',
             'The value of c1',
             'Inertia being too low',
             'The use of Euclidean Distance (p=2)')
        )
        submit = st.form_submit_button("Submit")

        if submit:
            if q5 == 'Number of neighbours (k)':
                st.info("Correct! Particles, in this swarm are attempting to update their velocity and move between "
                        "Iterations using their own PBEST, along with their neighbour's PBEST. In this case, "
                        "they only have one neighbour at a time and therefore, movements are slow "
                        "and imprecise and some Particles get trapped at non-beneficial positions "
                        "in the search space, meaning that they never converge to the Global Minima "
                        "of the sphere function.")
            else:
                st.info("Incorrect, try again!")

    with st.form("Question form 6"):
        st.write("How does Inertia effect convergence speed?")

        q6 = st.selectbox(
            'Answer choices',
            ('Lower inertia causes faster convergence',
             'Higher inertia causes faster convergence',
             'Inertia is not a parameter that effects convergence')
        )

        submit = st.form_submit_button("Submit")

        if submit:
            if q6 == 'Higher inertia causes faster convergence':
                st.info("Correct! Inertia effects how quickly Particles Converge.")
            else:
                st.info("Incorrect, try again!")


    with st.form("Question form 7"):
        st.write("How does Mutlimodal PSO differ from Canonical PSO?")

        q7 = st.selectbox(
            'Answer choices',
            ('Multimodal PSO does not use inertia',
             'Multimodal PSO aims to locate multiple optima',
             'Multimodal PSO converges faster',
             'Multimodal PSO returns one potential solution')
        )

        submit = st.form_submit_button("Submit")

        if submit:
            if q7 == 'Multimodal PSO aims to locate multiple optima':
                st.info("Correct! Multimodal PSO is used to find multiple optima locations within "
                         "one run of optimisation.")
            else:
                st.info("Incorrect, try again!")