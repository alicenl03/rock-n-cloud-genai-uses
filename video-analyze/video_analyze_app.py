
import streamlit as st
import video_analyze_lib as glib

st.set_page_config(layout="wide", page_title="Video Analysis")

st.title("Video Analysis")

col1, col2 = st.columns(2)

prompt_options_dict = {
    "Other": "",
}

prompt_options = list(prompt_options_dict)

image_options_dict = {
    "Other": "house.jpg"
    #Create sample post it picture
}

image_options = list(image_options_dict)


with col1:
    st.subheader("Select an Image")

    image_selection = st.radio("Please choose a picture:", image_options)
    
    if image_selection == 'Other':
        uploaded_file = st.file_uploader("Select an image", type=['png', 'jpg'], label_visibility="collapsed")
    else:
        uploaded_file = None
    
    if uploaded_file and image_selection == 'Other':
        uploaded_image_preview = glib.get_bytesio_from_bytes(uploaded_file.getvalue())
        st.image(uploaded_image_preview)
    #else:
    #    st.image(image_options_dict[image_selection])
    go_button = st.button("Go", type="primary")

    
    

with col2:
    st.subheader("Result")

    if go_button:
        with st.spinner("Processing..."):
            
            if uploaded_file:
                image_bytes = uploaded_file.getvalue()
            else:
                image_bytes = glib.get_bytes_from_file(image_options_dict[image_selection])
            
            response = glib.get_response_from_model(
                image_bytes=image_bytes,
            )
        
        st.write(response)
