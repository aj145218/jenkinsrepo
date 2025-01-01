import streamlit as st
import pandas as pd

data = {
    'Task':['Extract','Transform', 'Load'],
    'Status':['Completed','InProgress', 'Pending']

    }
df=pd.DataFrame(data)
st.write('Etl Pipeline Execution status')
st.write(df)