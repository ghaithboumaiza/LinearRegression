#Library imports
import pickle
import streamlit as st
import numpy as np
from datetime import date


#Setting Tit le of App
st.title("Location vélos")

st.text("Saisie les information :")



a = np.asarray( int ( st.text_input("season : 1:spring 2:summer 3:fall 4:winter ") ))
b =np.asarray( int ( st.text_input("mnth") ))
c =np.asarray(  int ( st.text_input("holiday") ))
d =np.asarray(  int ( st.text_input("weekday : 0:Sunday ... 6:Saturday") ))
e =np.asarray( int ( st.text_input("workingday : A binary value indicating whether or not the day")) )
f =np.asarray(  int ( st.text_input("weathersit : 1:clear 2:mist/cloud 3:light rain/snow 4:heavy rain/hail/snow/fog") ))
g =np.asarray( float (  st.text_input(" The temperature in celsius ") ))
h =np.asarray(  float ( st.text_input(" The apparent (feels-like) temperature in celsius") ))
i =np.asarray(  float ( st.text_input("The humidity leve") ))
j =np.asarray(  float ( st.text_input("The windspeed") ))


submit = st.button('Predict')
loaded_model = pickle.load(open('inalized_model.sav', 'rb'))
if submit:
      
        Y_pred = loaded_model.predict([[a,b,c,d,e,f,j,h,i,g ]])
        st.text("Le Nombre de vélos prédecter est")
        st.title(str(int (Y_pred)))
        


