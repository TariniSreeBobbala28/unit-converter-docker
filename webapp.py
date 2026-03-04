import streamlit as st

# Set page configuration
st.set_page_config(page_title="Unit Converter Pro", layout="centered")

# 1. Custom CSS for Navy Blue BG, Green Button, and Visible Input Text
st.markdown(
    """
    <style>
    /* Main background: Navy Blue */
    .stApp {
        background-color: #000080; 
        color: white;
    }

    /* Fix Input Box: Light background and Black text for visibility */
    div[data-baseweb="input"] {
        background-color: #f0f2f6 !important; 
        border-radius: 5px;
    }
    
    /* Force text inside input to be Black */
    div[data-baseweb="input"] input {
        color: black !important;
        -webkit-text-fill-color: black !important;
    }

    /* Labels and Headers color */
    label, .stMarkdown p {
        color: white !important;
    }

    /* Green Button Styling */
    .stButton>button {
        background-color: #28a745; 
        color: white;
        font-weight: bold;
        width: 100%; 
        border-radius: 10px;
        border: none;
        height: 3em;
        transition: 0.3s;
    }
    
    /* Button Hover Effect */
    .stButton>button:hover {
        background-color: #218838;
        color: white;
        border: 1px solid white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. Application UI and Logic
st.title("🚢 DevOps Unit Converter")
st.write("Convert units instantly within a Docker container.")

# Interactive Dropdown
option = st.selectbox(
    'Select Conversion Type:',
    ('Celsius to Fahrenheit', 'Fahrenheit to Celsius', 'KG to Pounds', 'Pounds to KG', 'KM to Miles', 'Miles to KM')
)

# Numeric Input
val = st.number_input('Enter value to convert:', value=0.0)

# Conversion Logic triggered by the Green Button
if st.button('Convert Now'):
    if option == 'Celsius to Fahrenheit':
        res = (val * 9/5) + 32
        st.success(f"Result: {val:.2f} °C = {res:.2f} °F")
    elif option == 'Fahrenheit to Celsius':
        res = (val - 32) * 5/9
        st.success(f"Result: {val:.2f} °F = {res:.2f} °C")
    elif option == 'KG to Pounds':
        res = val * 2.20462
        st.success(f"Result: {val:.2f} kg = {res:.2f} lbs")
    elif option == 'Pounds to KG':
        res = val / 2.20462
        st.success(f"Result: {val:.2f} lbs = {res:.2f} kg")
    elif option == 'KM to Miles':
        res = val * 0.621371
        st.success(f"Result: {val:.2f} km = {res:.2f} miles")
    elif option == 'Miles to KM':
        res = val / 0.621371
        st.success(f"Result: {val:.2f} miles = {res:.2f} km")