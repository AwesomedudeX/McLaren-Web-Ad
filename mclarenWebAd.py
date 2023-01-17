import streamlit as st
import warnings

warnings.filterwarnings("ignore")

sects = ("Homepage", "Facts & Stats", "Under The Hood", "A Look on The Inside", "Pricing & Orders")
sect = st.sidebar.selectbox("Navigate:", sects)
st.sidebar.subheader("Viewing Notes:")
st.sidebar.write(" - Use the navigation box on the left sidebar to go to different parts of the webpage")
st.sidebar.write(" - Click on the 3 lines in the sidebar and select \"Settings\" to change the theme of the page (light/dark mode)")

if sect == "Homepage":
	st.write("Note: This website is not a real website, and was made for a school project. Don't worry about any information being stolen, as none will be saved.")
	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">McLaren MP4-12C</h1>', unsafe_allow_html=True)


if sect == "Facts & Stats":
	pass

if sect == "Under The Hood":
	pass

if sect == "A Look On The Inside":
	pass

if sect == "Pricing & Orders":
	pass
