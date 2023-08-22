import streamlit as st

class Skills:
    def __init__(self, title, skills):
        self.title = title
        self.skills = skills

    def display(self):
        st.header(self.title)
        for skill in self.skills:
            st.write(skill["name"])
            st.progress(skill["level"])

skills = Skills("Habilidades", [{"name": "Python", "level": 0.8},
                                {"name": "Java", "level": 0.6},
                                {"name": "Javascript", "level": 0.7}])
skills.display()