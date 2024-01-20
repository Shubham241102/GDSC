import streamlit as st
st.title('Demo App')
st.write('Demo APP')

with st.sidebar:
  st.write('This Is Sidebar')
col1,col2=st.columns(2)
with col1:
  a= st.number_input('enter a value' , value=10)
with col2:
  b=st.text_input('enter a text')
  c=st.selectbox(label ='choose' , options=[1,2,3])
sub=st.button(label='Khatam')
if sub:
  st.balloons()
  st.write(a)
  st.write(b)
print(a)


