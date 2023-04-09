import streamlit as st
import pandas as pd
from PIL import Image

data=pd.read_csv('final_data.csv')
#st.markdown('# COMPTYRE \n ## Compare the Tyres here!!!!! \n ### find your perfect one')

veh=data['Car Model'].unique()

#img1=Image.open('Screenshot from 2023-04-09 22-37-14.png')
img2=Image.open('img5.png')

st.image(img1)
st.image(img2)

option = st.selectbox(' #### Which is your car?',veh)

'You selected: ', option

ev=data[data['Car Model']==option]
ev=ev[['Brand','Price','Features','Product Name']]
ev=ev.sort_values(by='Price', ascending=True)
    
    
    
st.dataframe(ev)

with st.sidebar:
    st.write('# DEVELOPER')
    st.markdown('#### [Saifudheen N](https://www.linkedin.com/in/saifudheen-nouphal-2b33a5144/)')
    st.write('##### MSc Data Science \n Department of Futures Studies')
    
    
# st.dataframe(data.groupby(['Faculty']).sum()['Point'].reset_index().sort_values(by='Point', ascending=False))

