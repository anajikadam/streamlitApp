# app.py
import streamlit as st

def main():
    st.title("Simple Streamlit App")
    
    # Add text
    st.text("Welcome to my Streamlit app!")

    # Add a slider
    number = st.slider("Select a number", 0, 100, 50)
    

    # Add a button
    if st.button("Check Selected Number"):
        st.write("You selected:", number)
        # st.success("Button clicked!")

    # Add a checkbox
    if st.checkbox("Show data"):
        st.write("Here is some data:")
        st.dataframe({"Column 1": [1, 2, 3], "Column 2": [4, 5, 6]})

if __name__ == "__main__":
    main()


