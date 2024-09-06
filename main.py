import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time 

st.title('streamlit入門')
st.write('プレグレスバーの表示')
'Start'

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

'Done!!'

left_column,reight_column=st.columns(2)

button=left_column.button('右カラムに文字を表示')
if button:
    reight_column.write('ここの右カラム')

expander1=st.expander('問い合わせ1')
expander1.write('問い合わせの回答1')
expander2=st.expander('問い合わせ2')
expander2.write('問い合わせの回答2')
expander3=st.expander('問い合わせ3')
expander3.write('問い合わせの回答3')
#oprion=st.text_input('あなたの趣味を教えてください。')
#condistion=st.slider('あなたの調子は？',0,100,50)

#'あなたの趣味は',oprion,'です。'
#'コンディション：',condistion
