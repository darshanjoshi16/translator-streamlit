#Implementation of Translator in Python programming
# Author: Darshan Joshi
#Github:darshanjoshi16

#importing the streamlit library which is useful for creating web applications
import streamlit as st

#importing the google translator library which will be helpful to translate functionality
import googletrans

#creating the initiation of translator class from library
translator = googletrans.Translator()

#creating this function will traverse the whole library as per dictionary  
#compare the destination language with the available language in the library 
# return the key related to that language
def gt_key(val):
    for key,value in googletrans.LANGUAGES.items():
        if(val == value):
            return key
    return "key does not exist"


#streamlit part of implementation

#Markdown allows the corporated part of HTML and creation of the page  
st.markdown('<style> body{background-color: Blue;} </style>',unsafe_allow_html=True)

#using the selectbox property of streamlit and giving all available options in tuple for source language
srcoption=st.selectbox('Select Source Language',tuple(googletrans.LANGUAGES.values()))

#input text property to inputting the source text you want to translate
text=st.text_area('Input the text')

#using the selectbox property of streamlit and giving all available options in tuple for desired language
destoption=st.selectbox('Select Destination Language',tuple(googletrans.LANGUAGES.values()))

#translating the source text to desired language using googletrans library's initiated variable
translated = translator.translate(text,dest=gt_key(destoption))

#printing the output in the web application
st.write(translated.text)