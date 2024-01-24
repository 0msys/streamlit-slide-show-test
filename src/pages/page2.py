import streamlit as st
import pandas as pd
import numpy as np

from slide_show import slide_show

st.title("ダッシュボード2")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)

slide_show("pages/page3.py")
