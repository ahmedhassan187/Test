import streamlit as st
import time
start_time = time.time()
end_time = start_time
while (end_time -start_time)<99:
    end_time = time.time()
    text = st.text("open")
    