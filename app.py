import streamlit as st
import time
if 'Flag' not in st.session_state:
    st.session_state.Flag = True
start_time = time.time()
end_time = start_time
while (end_time -start_time)<99:
    end_time = time.time()
    if st.session_state.Flag:
        text = st.text("open")
        st.session_state.Flag = False
    