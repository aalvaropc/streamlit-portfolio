import streamlit as st

class AboutMe:
    def __init__(self, title, about, img):
        self.title = title
        self.about = about
        self.img = img

    def display(self):
        col1, col2 = st.columns(2)
        with col1:
            st.title(self.title)
            st.info(self.about)
            
            st.write('<a href="https://github.com/aalvaropc">💻 Github</a>', unsafe_allow_html=True)
            st.write('<a href="https://www.linkedin.com/in/aalvarop-pe/">🔗 LinkedIn</a>', unsafe_allow_html=True)
            st.write('<a href="mailto:aalvaropc@gmail.com">📨 Gmail</a>', unsafe_allow_html=True)
        with col2:
            st.image(self.img, width=560)
            
descripcion = """
Soy un programador Python Junior con una pasión por aprender y crear soluciones eficientes y escalables. 
Tengo experiencia en desarrollo de aplicaciones web con Django y Flask, 
y he trabajado en proyectos que incluyen tanto el front-end como el back-end. 
Me encanta trabajar en equipo y estoy constantemente buscando nuevos desafíos y oportunidades de crecimiento. 
"""
about = AboutMe("Alvaro Peña", descripcion, "img/profile/alvaro.jpg")
about.display()