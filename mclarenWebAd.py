import streamlit as st
import warnings

warnings.filterwarnings("ignore")

st.sidebar.subheader("Viewing Notes:")
st.sidebar.write(" - Use the navigation box on the left sidebar to go to different parts of the webpage")
st.sidebar.write(" - Click on the 3 lines in the sidebar and select \"Settings\" to change the theme of the page (light/dark mode)")

sects = ("Homepage", "Facts & Stats", "Under The Hood", "A Look On The Inside", "Pricing & Orders", "Sources")
sect = st.sidebar.radio("Navigate:", sects)

if sect == "Homepage":
	
	st.write("Note: This website is not a real website, and was made for a school project. Don't worry about any information being stolen, as none will be saved.")
	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">McLaren MP4-12C</h1>', unsafe_allow_html=True)
	st.image("McLaren_MP4-12C.webp", caption="Credit: https://cars.mclaren.com/en/legacy/12c")

	st.write("The McLaren MP4-12C ")

if sect == "Facts & Stats":
	
	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">Facts & Stats</h1>', unsafe_allow_html=True)

if sect == "Under The Hood":
	
	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">Under The Hood</h1>', unsafe_allow_html=True)

if sect == "A Look On The Inside":
	
	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">A Look On The Inside</h1>', unsafe_allow_html=True)

if sect == "Pricing & Orders":
	
	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">Pricing & Orders</h1>', unsafe_allow_html=True)

if sect == "Sources":
	
	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">Sources:</h1>', unsafe_allow_html=True)
	
	src = (
		"https://cars.mclaren.com/en/legacy/12c",
		"https://supercarnostalgia.com/blog/mclaren-mp4-12c"
	)

	for i in src:
		st.write(f" - {i}")
