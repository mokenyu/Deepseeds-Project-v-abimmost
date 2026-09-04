import streamlit as st


## FORMS

import time

st.sidebar.title("SIDEBAR")

model_choice = st.sidebar.selectbox("Choose model", ["Gemini", "LLama", "Chatgpt"])
temperature = st.sidebar.slider("Creativity", 0.0, 1.0, 0.6)
page = st.sidebar.radio("Go To", ["Home", "Display Test", "Streamlit Flow, Images & Markdown", "Form", "Tabs", "Columns", "Container", "Expander", "Empty"])

if page == "Home":
    st.header("Welcome home")
    st.image("C:/Users/gwe/Pictures/Wall-p/5929327825758829361_121.jpg", use_container_width=True)

if page == "Form":
    st.header("FORMS")

    with st.form(key="key_data"):
        username = st.text_input(label="Username *")
        email = st.text_input(label="Email *")
        prompt = st.text_area(label="Provide your instructions *")
        submit = st.form_submit_button(label="Submit")
        
        if submit:
            if not username or not email or not prompt:
                st.error("Enter all required info")
            else:
                progress = st.progress(0)

                for i in range(100):
                    time.sleep(0.01) # Simulate computation
                    progress.progress(i+1)
                time.sleep(0.4)
                st.balloons()
                st.success("Submitted Succesfully")
                # st.write(f"My data is:{email}")

if page == "Display Test":
    ## STREAMLIT TEST

    st.header("Display Test")
    st.title("Hello bod")

    st.write("Sharp sentinel")
    st.subheader("Uptymos Prrr")

    st.write({
        "the way": "up",
        "phone num": 3.14,
        "ip": 1,
        "added": 3*5
    })

if page == "Streamlit Flow, Images & Markdown":
    ## STREAMLIT FLOW

    st.header("Streamlit Flow, Images & Markdown")

    print("run")
    pressed = st.button("Stangle")

    print(pressed)

    from profile import markdown_code

    st.title("WELCOME")
    st.header("WELCOME")
    st.header("WELCOME")
    st.image("C:/Users/atsim/Videos/Captures/Screenshot 7_6_2025 6_07_22 PM.png", caption="Welcome to the app", use_column_width=True)

    uploaded_image = st.file_uploader("Upload an image", type=["png","jpeg","jpg"])

    if uploaded_image:
        st.image(uploaded_image, caption = "Uploaded image!", use_column_width=True)

    st.markdown("---")  # Horizontal line divider

    st.markdown(markdown_code)

if page == "Tabs":
    ## TABS
    #Separates content into different pages without navigating
    
    st.header("Tabs")

    tab1, tab2 = st.tabs(["Prompt", "Output"])

    with tab1:
        proompt=st.text_area("Enter your prompt")
    with tab2:
        st.write(proompt)

if page == "Columns":
    ## COLUMNS
    # Place elements side by side(e.g. inputs on the left and output on the right)
    
    st.header("Columns")

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Enter your name")
        email = st.text_input("Enter your email")
    with col2:
        st.text(name)
        st.text(email)

if page == "Container":
    ## CONTAINER
    # Goup related elements and allow for updates within the group

    st.header("Container")

    container = st.container(border=True)

    container.write("Generated Text Area")
    btn = container.button("Generate Text")

if page == "Expander":
    ## EXPANDER
    # Hide/Show details on demand - useful for advanced settings or explanations.
    st.header("Expander")

    with st.expander("Advanced Options"):
        st.slider("Max tokens", 100, 1000)
        st.checkbox("Stream output")

if page == "Empty":
    ## EMPTY
    # Reserve a space for contents that updates later (e.g. dynamic result areas)
    st.header("Empty")

    placeholder = st.empty()

    if st.button("Generate"):
        placeholder.write("Generating...")
        time.sleep(2)
        # Simulate generation
        placeholder.write("Done! Here's the result")


# ## GENAI APP
# # Simple GenAI app that combines layouts

# import streamlit as st

# st.title("GenAI Prompt Generator")

# # Sidebar Settings
# st.sidebar.title("Settings")
# temp = st.sidebar.slider("Creativity (Temperature)", 0.0, 1.0, 0.5)

# # Tabs
# tab1, tab2 = st.tabs(["Prompt", "Output"])

# with tab1:
#     prompt = st.text_area("Enter your prompt")

# with tab2:
#     st.write("**AI Output:**")
#     if st.button("Generate"):
#         st.success(f"response from model (temp={temp}) for: {prompt}")