import streamlit as st
import time
import os

# -----------------------------------------------------------------------------
# 1. CONFIGURATION & CSS DESIGN
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="For You ❤️",
    page_icon="🌹",
    layout="centered"
)

# Custom CSS for Dark Romantic Theme
st.markdown("""
    <style>
    /* Dark Background (Deep Red/Burgundy) */
    .stApp {
        background-color: #2b0505;
        background-image: linear-gradient(to bottom, #2b0505, #4a0a10);
        color: #ffccd5; /* Light pink text default */
    }
    
    /* Title Styling */
    h1 {
        color: #ff4d6d; /* Brighter pink for headers */
        font-family: 'Helvetica Neue', sans-serif;
        text-align: center;
        font-weight: bold;
        text-shadow: 2px 2px 4px #000000;
    }
    
    /* Subheaders */
    h2, h3, p {
        color: #ffe6ea !important; /* Very light pink/white for readability */
        text-align: center;
    }

    /* Buttons */
    div.stButton > button {
        width: 100%;
        border-radius: 25px;
        height: 60px;
        font-size: 20px;
        font-weight: bold;
        background-color: #590d22;
        color: white;
        border: 2px solid #800f2f; /* Darker border instead of white */
        box-shadow: 0px 4px 6px rgba(0,0,0,0.5);
        transition: transform 0.2s;
    }
    
    /* Button Hover */
    div.stButton > button:hover {
        transform: scale(1.05);
        background-color: #800f2f;
        border-color: #ff4d6d;
        color: white;
    }
    
    /* Secondary Button (No) specific styling if needed, currently global */

    /* Image Styling - Removed White Border */
    img {
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        /* No border property here to avoid the white frame */
    }

    /* Toast/Error styling adjustment for visibility */
    div[data-baseweb="toast"] {
        background-color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. SESSION STATE
# -----------------------------------------------------------------------------
if 'stage' not in st.session_state:
    st.session_state.stage = 'asking'

# -----------------------------------------------------------------------------
# 3. MAIN CONTENT
# -----------------------------------------------------------------------------

st.title("A very important question... 💌")
st.write("") 

# --- IMAGE SECTION ---
# Looks for 'us.jpg' in the root folder.
image_filename = "us.png"

if os.path.exists(image_filename):
    st.image(image_filename, caption="Us ❤️", use_container_width=True)
else:
    # Fallback if you haven't put the image in the folder yet
    st.warning("⚠️ Image not found. Please place a file named 'us.jpg' in the app folder.")
    # Placeholder to keep the layout
    st.image(
        "https://images.unsplash.com/photo-1518199266791-5375a83190b7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
        caption="Example Image (Place 'us.jpg' in folder)",
        use_container_width=True
    )

st.write("---") 

# -----------------------------------------------------------------------------
# 4. QUESTION & LOGIC
# -----------------------------------------------------------------------------

if st.session_state.stage == 'asking':
    st.header("Will you be my Valentine? 🌹")
    st.write("")
    
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        # YES BUTTON
        if st.button("YES! ❤️ 😍", type="primary"):
            st.session_state.stage = 'accepted'
            st.rerun()
        
        # NO BUTTON
        if st.button("No... 🤔"):
            st.toast("⚠️ Wrong answer! Please try again.", icon="❌")
            st.error("Oops! Wrong button. Try again!")

# -----------------------------------------------------------------------------
# 5. SUCCESS SCREEN
# -----------------------------------------------------------------------------
elif st.session_state.stage == 'accepted':
    st.balloons()
    time.sleep(1)
    st.snow()
    
    st.success("Yay! I'm so happy! 🥂💑")
    
    st.markdown("""
        <h3 style='text-align: center;'>You are the best! ❤️</h3>
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            <img src="https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif" width="300" style="border-radius: 10px;">
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("Back to start"):
        st.session_state.stage = 'asking'
        st.rerun()