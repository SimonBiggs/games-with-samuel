import random
import streamlit as st


from . import session


def main():
    state = session.session_state(number=None, guesses=0)

    if state.number is None or st.button("New Number!"):
        state.number = random.randint(0, 100)
        state.guesses = 0

    # st.write(state.number)

    st.write("# Hi Samuel!")

    your_pick = st.number_input("Pick a number", value=0)
    if your_pick == state.number:
        st.write("You Win!")
        st.write(f"You did it in {state.guesses}!")
        st.stop()
    elif your_pick < state.number:
        st.write("Try higher")
    else:
        st.write("Try lower")

    state.guesses += 1

    st.write(f"Number of guesses are {state.guesses}")
