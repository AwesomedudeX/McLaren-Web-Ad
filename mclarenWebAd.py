import streamlit as st
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(page_title="The McLaren MP4-12C", page_icon="logo.png", layout='wide', initial_sidebar_state='auto')

st.sidebar.subheader("Viewing Notes:")
st.sidebar.write(" - Use the navigation box on the sidebar to go to different parts of the webpage")
st.sidebar.write(" - Click on the 3 lines in the top right and select \"Settings\" to change the theme of the page (light/dark mode)")

sects = ("Homepage", "Facts & Stats", "Under The Hood", "A Look On The Inside", "Pricing & Orders", "Sources")
sect = st.sidebar.radio("Navigate:", sects)

if sect == "Homepage":
	
	st.write("Note: This website is not a real website, and was made for a school project. Don't worry about any information being stolen, as none will be saved.")
	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">McLaren MP4-12C</h1>', unsafe_allow_html=True)
	st.image("McLaren_MP4-12C.webp", caption="Credit: https://cars.mclaren.com/en/legacy/12c")

	st.write("The McLaren MP4-12C is an F1-inspired supercar that was the successor of the Mercedes-Benz SLR McLaren. The SLR was an F1 car that was the result of a collaboration between McLaren and Mercedes. It had the McLaren logo on it, but it wasn't a true McLaren car, which was what the company was looking to develop. McLaren had unveiled the final design for their their MP4-12C model in September 2009, and after Mercedes-Benz sold its 40% stake in 2010 for the SLR, McLaren moved forward with its plans to become a large-scale vehicle manufacturer with their own resources and plans. The result was a RWD beast that rivaled the Lamborghini Gallardo, Porsche 911 Turbo and the Ferrari 458 Italia. The MP4-12C was presented in public a the Goodwood Festival of Speed in July, 2010, with production starting in February the next year. Its key parts were manufactured in McLaren's name by third-party suppliers, with assembly taking place at the McLaren Production Centre (opened November 2011), which was next to the McLaren Technology Centre.")
	st.write("\n(Use the sidebar on the left to navigate the page - click the arrow in the top left to open it)")

if sect == "Facts & Stats":
	
	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">Facts & Stats</h1>', unsafe_allow_html=True)

if sect == "Under The Hood":
	
	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">Under The Hood</h1>', unsafe_allow_html=True)

if sect == "A Look On The Inside":
	
	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">A Look On The Inside</h1>', unsafe_allow_html=True)

	st.image("interior.jpg", caption="https://www.hgreglux.com/used-car/mclaren-mp4-12c-2012-for-sale-7237?is_sold=1")

	st.write("Your 12C is unique to you, and you only. Unleash your imagination with McLaren Special Operations, and come up with your own finish, layout and/or material(s) for your personalized McLaren MP4-12C.")
	
	c1, c2, c3 = st.columns(3)

	with c1:
		e1 = st.expander("Sleek & Optimized Design")
		e1.write("The interior features a sleek layout with our intuitive telematics touchscreen at its core, giving you full control over your ride's entertainment, media and communication. Its IRIS system allows for some of the best onboard navigation available, as well as a custom 7-speaker Meridian Surround Sound experience that will immerse you in your soundtracks more effectively than ever before.")
	
	with c2:
		e2 = st.expander("View Control Panel")
		st.image("panel.jpg", caption="https://www.netcarshow.com/mclaren/2013-mp4-12c_spider/")

	with c3:
		e3 = st.expander("Intake Sound Generator (ISG)")
		e3.write("The Intake Sound Generator (ISG) above the system lets you have some fun by adjusting the amount of sound from the car that comes through to the cabin, from a quiet hum to a powerful growl, displaying the efforts we've taken to give you the looks and performance that you paid for.")

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
