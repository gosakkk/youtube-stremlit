import streamlit  as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done !!'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ')


#expander = st.expander('問い合わせ')
#expander.write('問い合わせ1の回答')
#expander = st.expander('問い合わせ')
#expander.write('問い合わせ2の回答')
#expander = st.expander('問い合わせ')
#expander.write('問い合わせ3の回答')

#text = st.text_input('あなたの趣味を教えてください。')
#'あなたの趣味は:', text , 

#condition = st.slider('あなたの今の調子は？', 0, 100, 50)
#'コンデション:', condition

#if st.checkbox('Show Image'):
 #   img = Image.open('sample1.png')
#  st.image(img, caption='おばけ',use_column_width=True)



# df =  pd.DataFrame({
    # '1列目':[1, 2, 3, 4],
    #'2列目':[10, 20, 30, 40]
#})

# st.table(df.style.highlight_max(axis=0))

#df = pd.DataFrame(
#   np.random.rand(100,2)/[50, 50] + [35.69,139.70],
#    columns=['lat', 'lon']  
#　)
# st.map(df)