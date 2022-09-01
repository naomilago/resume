from streamlit_lottie import st_lottie
from bokeh.models.widgets import Div
from pathlib import Path
import streamlit as st
from PIL import Image
import requests


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Naomi Lago - CV.pdf"
profile_pic = current_dir / "assets" / "avatar.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Naomi Lago"
PAGE_ICON = './assets/favicon.png'
NAME = "Naomi Lago"
DESCRIPTION = """
Data Science Analyst, assisting and supporting data-driven decision-making.
"""
EMAIL = "info@naomilago.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/naomilago",
    "GitHub": "https://github.com/naomilago",
    "Twitter": "https://twitter.com/naomilago",
}
PROJECTS = {
    "🏆 Pet Paws - A pet donation friendly system": "https://github.com/naomilago/Pet-Paws",
    "🏆 Personal Blog - A personal blog built using Hugo": "https://github.com/naomilago/blog   ",
    "🏆 Lucky Answers - An Android app made with Flutter that aims to answer simple questions": "https://github.com/naomilago/Lucky-Answer",
    "🏆 ExPlan - An Android app made with Flutter that can help you plan your expenses": "https://github.com/naomilago/ExPlan",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

def load_lottie(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

datascience_animation = load_lottie('https://assets10.lottiefiles.com/packages/lf20_qp1q7mct.json')


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

with col2:
    # st.image(profile_pic, width=230)
    st_lottie(datascience_animation)


# --- SOCIAL LINKS ---
st.write("#")   
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 5 years studying technology
- ✔️ Hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Great team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Numpy), SQL, JavaScript (React, React-Native)
- 📊 Data Visulization: PowerBi, MS Excel, Plotly, Streamlit
- 📚 Modeling: Linear Regression
- 🗄️ Databases: Postgres, MongoDB, MySQL
- ☁ Cloud: GCP, AWS, Azure, Linode, Databricks
"""
)


# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Science Analyst | Nestlé**")
st.write("07/2022 - Present")
st.write(
    """
- ► Use of Python to manipulate and prepare data for analysis
- ► Use of Pandas and Plotly to create data visualizations
- ► Use of Streamlit to create interactive web apps
- ► Use of SQL to create and manage databases
- ► Use of Databricks to host and manage Jupyter notebooks
- ► Use of Azure to host and manage cloud services
"""
)

# --- JOB 2
st.write("#")
st.write("🚧", "**UX/UI Designer | Cliqx**")
st.write("01/2018 - 02/2022")
st.write(
    """
- ► Designing and implementing user interfaces for web and mobile apps
- ► Creating wireframes and prototypes for web and mobile apps
- ► Creating mockups for web and mobile apps
- ► Creating user stories and user flows for web and mobile apps
"""
)

# --- JOB 3
st.write("#")
st.write("🚧", "**Help Desk Analyst | Cliqx**")
st.write("04/2015 - 01/2018")
st.write(
    """
- ► Solving customer issues and providing assistance to customers
- ► Assisting customers with software-technical issues
- ► Dealt with APIs, Databases, bot services flows
"""
)


# --- Projects & Accomplishments ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

if st.button('See all projects'):
    js = "window.open('https://projects.naomilago.com')"
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)