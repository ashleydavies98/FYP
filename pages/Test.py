import streamlit as st


def app():

    st.title('Tests')

    st.write("You've reached the end of that app. Now that you've learned about Particle Swarm Optimisation, "
             "here are some questions that will test your knowledge based on what has been taught throughout the app.  \n")
    st.write("When you have answered a question, click the submit button at the bottom of its area "
             "to find out if you answered correctly.")
    # Create question form 1
    with st.form("Question form"):

        st.write("What influences particle movement?")
        # Add a question select box
        q1 = st.selectbox(
            'Answer choices',
            ('Pbest', 'Gbest', 'Inertia(w)', 'All of the above')
        )
        submit = st.form_submit_button("Submit")

        if submit:
            if q1 == 'All of the above':
                st.write("Correct!")
            else:
                st.write("Incorrect, try again!")

    # Create question form 2
    with st.form("Question form2"):
        st.write("Which parameter makes the particles rely more on their own Pbest?")

        q2 = st.selectbox(
            'Answer choices',
            ('c2', 'c1', 'Inertia(w)', 'Ebest')
        )

        submit = st.form_submit_button("Submit")

        if submit:
            if q2 == 'c1':
                st.write("Correct!")
            else:
                st.write("Incorrect, try again!")

    # Create question form 3
    with st.form("Question form3"):
        st.write("What is the objective of Particle Swarm Optimisation?")

        q3 = st.selectbox(
            'Answer choices',
            ('To make less choices of optimal solutions', 'To make given problems take less time',
             'Improve/find optimal solutions to a given problem')
        )

        submit = st.form_submit_button("Submit")

        if submit:
            if q3 == 'Improve/find optimal solutions to a given problem':
                st.write("Correct!")
            else:
                st.write("Incorrect, try again!")

    # Create question form 4
    with st.form("Question form4"):
        st.write("A swarm of particles aren't very successful without communication, why is communication "
                 "important between particles?")

        q4 = st.text_area("Insert your answer here.")

        submit = st.form_submit_button("Submit")

        if submit:
            st.info("Correct answer:  \n"
                    "Particle communication is important because of how BEST values are used to find "
                    "optimum solutions. Without particle communication, every particle would be searching "
                    "for their own individual best solution. While this could provide a vast amount "
                    "of possible solutions, there would more than likely be a lack of convergence to "
                    "an appropriate solution and the algorithm would be unsuccessful at optimising. "
                    "Whereas, by communicating with each other, either through reliance on the swarm's "
                    "GBEST or PBESTs from local neighbouring particles, "
                    "there is far more success in optimising the problem and more chance of convergence "
                    "to a optimum in before reaching a stopping condition.")
            st.write("How does your answer compare to the answer above?")

