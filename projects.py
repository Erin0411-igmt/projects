'''
Erin Courtemanche
7/5/2025
Erin's Portfolio Website
Description: This project creates a python-based website that acts a data analytics
and computer information systems portfolio for Erin Courtemanche
'''

#Imports
import streamlit as st
import os
from pathlib import Path
from PIL import Image
import fitz
import base64
import io
from io import BytesIO

#python -m streamlit run "C:\Users\eacou\OneDrive - Bentley University\[1] Portfolio\Portfolio Page\portfolio.py"

#Website Tab
st.set_page_config(
    page_title="Erin Courtemanche's Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

#Title Formatting
def title_template(text, font_size=75, color= "#333333", center=True):
    align = 'center' if center else 'left'
    st.markdown(f"""
    <h2 style = 'text-align: {align};
        color: {color};
        font-size: {font_size}px;
        margin-botton: 15px;'>
        {text}
        </h2>
        """, unsafe_allow_html=True)

#Navigation Bar Set up
st.sidebar.markdown("**Erin Courtemanche**")
st.sidebar.markdown("*Data Analytics & CIS Student*")
st.sidebar.markdown("---")

st.sidebar.markdown("Navigate")
page_select = st.sidebar.radio("Navigate to:", ["About Me", "Resume", "Projects", "View Source Code"])

#Navigation Bar Quick Links
st.sidebar.markdown("---")
st.sidebar.markdown("## 🔗 Quick Links")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/erin-courtemanche-4744a72b4/)")
st.sidebar.markdown("[My Data Website](https://erin0411-igmt-nuclear-streamlit-fbbdhv.streamlit.app/)")

base_path = Path(__file__).parent
pdf_path = base_path / "Erin_Courtemanche_Resume(2026).pdf"

with open(pdf_path, "rb") as f:
    st.sidebar.download_button(
        "📥 Download Resume",
        f,
        file_name="Erin_Courtemanche_Resume(2026).pdf",
        mime="application/pdf"
    )

#About Me Page
if page_select == "About Me":
    title_template("About Me")

    st.title("Education")
    st.write("🎓 I'm currently a Junior at Bentley University pursuing double majors in Data Analytics and Computer Information Systems")
    st.write("🧠 I'm also pursuing double minors in Business Administration and Artificial Intelligence")
    st.write("✏️ I'm a member of Bentley's Advanced Standing in Business Analytics, which is an excellerated Master's degree for business analytics. I hope to finish my masters by 2028")

    st.title("Goals")
    st.write("🌱 I strive to always expand my knowledge and skillset by exploring new tools, technologies, and challenges that push me foward")
    st.write("✨ I aim to work at a company where I'm genuinely excited to show up each day -- a place that values creativity, curiosity, and collaboration")
    st.write("🚀 I'm committed to developing myself not just as a professional, but as a person -- improving how I communicate, connect with others, and contribute to a team")

    st.title("Fun Facts")
    st.write("🥋 I have 3 black belts in Shaolin Kempo and have taught martial arts for 4 years!")
    st.write("🎭 I love live theater, but I didn't become a 'theater kid' until college")
    st.write("🐶 I have a Shnorkie named Loki; I've attached a photo of him for your viewing pleasure")

    #Loki Picture
    base_path = Path(__file__).parent
    image_path = base_path / "loki.jpg"
    image = Image.open(image_path)

    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    encoded = base64.b64encode(buffered.getvalue()).decode()

    #Image Border
    st.markdown(
        f"""
        <div style="border: 4px solid #D4AF37; border-radius: 12px; padding: 10px; display: inline-block;">
            <img src="data:image/jpeg;base64,{encoded}" width="700" />
            <p style="text-align: center; font-weight: bold; margin-top: 8px;">Loki Courtemanche</p>
        </div>
        """,
        unsafe_allow_html=True
    )

#Resume Page
if page_select == "Resume":
    pdf_path = Path(__file__).parent / "Erin_Courtemanche_Resume(2026).pdf"

    doc = fitz.open(pdf_path)
    page = doc.load_page(0)

    zoom = 2
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    image = Image.open(io.BytesIO(pix.tobytes("png")))

    st.image(image, caption="Erin Courtemanche Resume Preview", use_column_width=True)

#Project Portfolio
if page_select == "Projects":
    title_template("Projects")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    #MA214 Data Project
    st.title("💼 Business Startup Time Data Project (Freshman Year)")
    st.write("The following data analysis was conducted using a World Bank database containing information on business startups from over 188 individuals. The goal of the analysis was to determine"
             " whether there is any correlation between the average time it takes to start a business and other factors in the dataset, such as gender and continent. All necessary testing was performed"
             " using R Script.")

    #ST625 Data Project
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.title("🎟️ Theater Ticket Sales Data Project (Sophomore Year)")
    st.write("The following data analysis was conducted using a database containing information from Broadway theaters, including weekly gross ticket sales, show titles, average ticket prices,"
             " and more. The goal of the analysis was to explore the relationship between weekly ticket sales and factors such as the type of show playing, the top ticket price, and"
             " whether the show included a preview performance.")

    #Nuclear Website
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.title("💣 Nuclear Database Website (Sophomore Year)")
    st.write("This website was built using python and features an interactive database detailing every nuclear explosion that took place between 1945 and 1998. The dataset includes"
             " each explosion's location, purpose, deployment method, yield (in kilotons), and other relevant information. This site is interactive, so feel free to explore the data "
             " and visualizations. ")
    st.markdown("*Note: The site may have to be 'woken up' and may take a few extra seconds to load.*")
    st.markdown(
        '<a href="https://erin0411-igmt-nuclear-streamlit-fbbdhv.streamlit.app/" target="_blank">Visit My Data Website</a>',
        unsafe_allow_html=True)

#View Source Code
if page_select == "View Source Code":
    with open(os.path.abspath(__file__), "r", encoding = "utf-8") as f:
        source_code = f.read()
    st.code(source_code, language = "python")