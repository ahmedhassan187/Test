import streamlit as st
import time
if 'Flag' not in st.session_state:
    st.session_state.Flag = True
# text_1 = st.text("")
new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">text_1</p>'
text_1 = st.markdown(new_title,unsafe_allow_html=True)
while(True):    
    start_time = time.time()
    end_time = start_time
    st.session_state.Flag = True
    while (end_time -start_time)<99:
        end_time = time.time()
        if st.session_state.Flag:
            text_1.write("Open")
            st.session_state.Flag = False
    start_time = time.time()
    end_time = start_time
    st.session_state.Flag = True
    while (end_time -start_time)<40:
        end_time = time.time()
        if st.session_state.Flag:
            text_1.write("Closed")
            st.session_state.Flag = False