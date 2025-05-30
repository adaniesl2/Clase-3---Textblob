import streamlit as st
from textblob import TextBlob
from googletrans import Translator
from PIL import Image

translator = Translator()
st.title('El Juicio')

st.subheader("Serperior te va a juzgar dependiendo de lo que digas. Espero que le dejes una buena impresión")
image = Image.open('Serperior.png')
st.image(image, width=350)

with st.sidebar:
               st.subheader("¿Qué toma en cuenta?")
               ("""
                Serperior toma en cuenta la polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
                Lo valora entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
                
               El otro factor que toma en cuenta es la subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
               (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.

                 """
               ) 


with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:

        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        #blob = TextBlob(text1)
       
        
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x >= 0.5:
            st.write( 'Es un sentimiento Positivo 😊')
        elif x <= -0.5:
            st.write( 'Es un sentimiento Negativo 😔')
        else:
            st.write( 'Es un sentimiento Neutral 😐')

with st.expander('Corrección en inglés'):
       text2 = st.text_area('Escribe por favor: ',key='4')
       if text2:
          blob2=TextBlob(text2)
          st.write((blob2.correct())) 
