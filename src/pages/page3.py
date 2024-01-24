import streamlit as st
import pandas as pd
import numpy as np

from slide_show import slide_show

st.title("ダッシュボード3")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

slide_show("pages/page1.py")
