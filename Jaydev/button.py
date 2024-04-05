import streamlit as st

st.markdown(
    """
    <style>
    .element-container:has(style){
        display: none;
    }
    #button-after {
        display: none;
    }
    .element-container:has(#button-after) {
        display: none;
        
    }
    .element-container:has(#button-after) + div button {
        border-padding-top: 10px;
        border:none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.button("button1")
st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
if st.button("My Button"):
    st.write("Button clicked")
st.button("button2")

st.button(r"$\textsf{\Large Enter text here}$")