import streamlit as st

class Projects:
    def __init__(self, title, projects):
        self.title = title
        self.projects = projects

    def display(self):
        st.title(self.title) 
        col1, _, col2 = st.columns([1.5, 0.5, 1.5])
        col = col1
        for project, details in self.projects.items():
            with col:
                st.subheader(project)
                st.image(details["img"], caption=project, use_column_width=True)
                st.markdown("[Source code]({})".format(details["link"]))
            col = col2 if col == col1 else col1
        
projects = Projects("Proyectos", {
                "Discord bot": {"img": "img/proyectos/discord.jpg", "link": "https://github.com/aalvaropc/proyectos_python/blob/main/Automatizaci%C3%B3n/discord_bot.py"},
                "Clasificador archivos": {"img": "img/proyectos/clasificador_archivos.jpg", "link": "https://github.com/aalvaropc/proyectos_python/blob/main/Automatizaci%C3%B3n/clasificador_archivos.py"},
                "Compresor imagenes": {"img": "img/proyectos/compresor.png", "link": "https://github.com/aalvaropc/proyectos_python/blob/main/Automatizaci%C3%B3n/compresor_img.py"},
                "Productos falabella": {"img": "img/proyectos/falabella.jpg", "link": "https://github.com/aalvaropc/proyectos_python/blob/main/WebScrapping/selenium_2.py"},
                "Precio bitcoin": {"img": "img/proyectos/precio_bitcoin.jpg", "link": "https://github.com/aalvaropc/proyectos_python/blob/main/WebScrapping/selenium_1.py"},
                "Descargar videos": {"img": "img/proyectos/descargar_videos.png", "link": "https://github.com/aalvaropc/proyectos_python/blob/main/Automatizaci%C3%B3n/descargar_videos.py"},
                })
projects.display()