import streamlit as st
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(page_title="The McLaren MP4-12C", page_icon="logo.png", layout='wide', initial_sidebar_state='expanded')

st.sidebar.subheader("Viewing Notes:")
st.sidebar.write(" - Use the navigation box on the sidebar to go to different parts of the webpage")
st.sidebar.write(" - Click on the 3 lines in the top right and select \"Settings\" to change the theme of the page (light/dark mode)")

sects = ("Homepage", "Facts & Stats", "Interior Design", "Exterior Design", "Sources")
sect = st.sidebar.radio("Navigate:", sects)

if sect == "Homepage":
	
	st.write("Note: This website is not a real website, and was made for a school project. Don't worry about any information being stolen, as none will be saved.")
	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">McLaren MP4-12C</h1>', unsafe_allow_html=True)
	st.image("McLaren_MP4-12C.webp", caption="Credit: https://cars.mclaren.com/en/legacy/12c")

	st.write("The McLaren MP4-12C is an F1-inspired supercar that was the successor of the Mercedes-Benz SLR McLaren. The SLR was an F1 car that was the result of a collaboration between McLaren and Mercedes. It had the McLaren logo on it, but it wasn't a true McLaren car, which was what the company was looking to develop. McLaren had unveiled the final design for their their MP4-12C model in September 2009, and after Mercedes-Benz sold its 40% stake in 2010 for the SLR, McLaren moved forward with its plans to become a large-scale vehicle manufacturer with their own resources and plans. The result was a RWD beast that rivaled the Lamborghini Gallardo, Porsche 911 Turbo and the Ferrari 458 Italia. The MP4-12C was presented in public a the Goodwood Festival of Speed in July, 2010, with production starting in February the next year. Its key parts were manufactured in McLaren's name by third-party suppliers, with assembly taking place at the McLaren Production Centre (opened November 2011), which was next to the McLaren Technology Centre.")
	st.write("\n(Use the sidebar on the left to navigate the page - click the arrow in the top left to open it)")

if sect == "Facts & Stats":
	
	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">Facts & Stats</h1>', unsafe_allow_html=True)

	c1, c2 = st.columns(2)

	with c1:
		e1 = st.expander("General Performance")
		e1.image("aerodynamics.jpg", caption="https://www.v12-gt.com/les-dernieres-news-du-monde-automobile-de-luxe/l-echos-des-constructeurs-d-automobiles/McLaren-MP4-12C2")
		gpdf = pd.DataFrame(index=["1", "2", "3", "4", "5", "6"], columns=["Statistic", "Value"], data=[["Top Speed", "33kph (207mph)"], ["Acceleration: 0-100kph (62mph)", "3.1 sec."], ["Acceleration: 0-200kph (124mph)", "8.8 sec."], ["Maximum Power Output", "625PS (616bhp)"], ["Maximum Torque", "600Nm (443lbft)"], ["Efficiency (EU WLTP)", "279g/km"]])
		e1.dataframe(gpdf)
	
	with c2:
		e2 = st.expander("Body & Weight")
		e2.image("body.jpg", caption="https://www.journauto.com/blog/2010/09/04/preview-2012-mclaren-mp4-12c/")
		bwdf = pd.DataFrame(index=["1", "2", "3", "4"], columns=["Statistic   ", "Value"], data=[["Body Type", "Coupé"], ["Number of Doors", "2"], ["Dry Weight (Lightest)", "1341kg (2956lb)"], ["DIN Kerb Weight", "1474kg (3249lbs)"]])
		e2.dataframe(bwdf)

	c3, c4 = st.columns(2)

	with c3:
		e3 = st.expander("Engine")
		e3.image("engine.jpg", caption="https://www.caranddriver.com/reviews/a22042645/2012-mclaren-mp4-12c-tech-trickledown/")
		edf = pd.DataFrame(index=["1", "2", "3"], columns=["Statistic   ", "Value"], data=[["Engine Capacity", "3799cc"], ["Engine Type", "V8, 4.0L"], ["Technology", "Twin Turbochargers, Dry Sump System"]])
		e3.dataframe(edf)

	with c4:
		e4 = st.expander("Braking")
		e4.image("brakes.jpg", caption="http://mp4-12c.over-blog.com/pages/Wheels-tyres-and-brakes-4755907.html")
		bdf = pd.DataFrame(index=["1", "2"], columns=["Statistic   ", "Value"], data=[["Braking: 100-0kph (62-0mph)", "30.7m (101ft)"], ["Braking: 200-0kph (124-0mph)", "123.5m (405ft)"]])
		e4.dataframe(bdf)

	e5 = st.expander("Rating")
	rdf = pd.DataFrame(index=["1", "2", "3", "4", "5", "6"], columns=["Section   ", "Rating"], data=[["Comfort", "4.3"], ["Interior Design", "4.6"], ["Performance", "5"], ["Value For The Money", "4.6"], ["Exterior Styling", "4.9"], ["Reliability", "4.6"]])
	e5.write("(https://www.cars.com/research/mclaren-mp4_12c-2012/)")
	e5.dataframe(rdf)

if sect == "Interior Design":
	
	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">A Look On The Inside</h1>', unsafe_allow_html=True)

	st.image("interior.jpg", caption="https://www.hgreglux.com/used-car/mclaren-mp4-12c-2012-for-sale-7237?is_sold=1")

	st.write("Your 12C is unique to you, and you only. Unleash your imagination with McLaren Special Operations, and come up with your own finish, layout and/or material(s) for your personalized McLaren MP4-12C.")
	
	c1, c2, c3 = st.columns(3)

	with c1:
		e1 = st.expander("Sleek & Optimized Design")
		e1.write("The interior features a sleek layout with our intuitive telematics touchscreen at its core, giving you full control over your ride's entertainment, media and communication. Its IRIS system allows for some of the best onboard navigation available, as well as a custom 7-speaker Meridian Surround Sound experience that will immerse you in your soundtracks more effectively than ever before.")
	
	with c2:
		e2 = st.expander("View Control Panel")
		e2.image("panel.jpg", caption="https://www.netcarshow.com/mclaren/2013-mp4-12c_spider/")

	with c3:
		e3 = st.expander("Intake Sound Generator (ISG)")
		e3.write("The Intake Sound Generator (ISG) above the system lets you have some fun by adjusting the amount of sound from the car that comes through to the cabin, from a quiet hum to a powerful growl, displaying the efforts we've taken to give you the looks and performance that you paid for.")

	st.write("The 12C's interior is built for comfort and performance. No matter what you expect, the cabin on this supercar will give you comfort and convenience as you cruise in your custom-built MP4-12C.")

if sect == "Exterior Design":
	
	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">Exterior Design</h1>', unsafe_allow_html=True)

	st.write("The 12C is the first street car since our iconic F1, and so we've made sure this extraordinary supercar is engineered to perfection. Every curve, line, part and surface in the 12C's design is there for a reason, and that is to give you our best performance and thrill as you ride in this exotic masterpiece.")

	c1, c2 = st.columns(2)

	with c1:
		e1 = st.expander("Iconic Doors")
		e1.subheader("Iconic Doors")
		e1.image("doors.jpg", "https://cars.mclaren.com/en/legacy/12c/design")
		e1.write("Our iconic dihedral doors - first seen on our F1 model - are lighter and more aerodynamic than regular doors. They are also more practical - they have only 1 hinge, which doesn't need as much room to open while making it much easier to enter and exit the cabin.")

	with c2:
		e2 = st.expander("Spoiler Airbrakes")
		e2.subheader("Spoiler Airbrakes")
		e2.image("airbrakes.jpg", "https://kumparan.com/kumparanoto/mengenal-fitur-air-brake-spoiler-yang-ada-pada-mclaren-mp4-12c-1tLuIWa3jLS")
		e2.write("The 12C's spoiler airbrakes are designed to make braking as efficient as possible while maximizing its aerodynamics. The spoiler is designed to stay aligned with the car while driving, and flip up when you hit the brakes, creating drag that slows down your car more quickly. It's a simple feature that's effective, looks nice, and comes with no compromise in terms of performance.")

	c3, c4 = st.columns(2)

	with c3:
		e3 = st.expander("Extraordinary Finish")
		e3.subheader("Spoiler Airbrakes")
		e3.image("finish.jpg", caption="https://en.wikipedia.org/wiki/McLaren_12C")
		e3.write("Our 3-stage Formula 1™-inspired paint technology is mixed and painted by hand for perfection, ensuring that the colour, tint, lustre and smooth finish of the 12C's paint job is absolutely flawless. It also minimizes the paint weight as much as possible. A lot of our Special and Elite paint jobs use a higher level of metallic and perlescent content. Using our exclusive pignents and a greater holographic effect, these highly-crafted paint finishes pay tribute to the car's aerodynamic design by bringing out every line, curve and contour of the body.")


	with c4:
		e4 = st.expander("Fast & Light")
		e4.subheader("Fast & Light")
		e4.image("wheels.jpg", caption="https://www.mclarenboston.com/2012-mclaren-mp4-12c-c-335/")
		e4.write("Reducing a car's wheel weight is more impactful than trying to reduce weight in any other part of the car, so we optimize every single detail of our wheels. We reduce mass as much as possible, while enhancing the strength and performance of our wheels. Our specialist Pirelli tires come with rims with a 5 and 10-spoke design, as well as a range of marvelous finishes like Diamond Cut and Stealth.")

if sect == "Sources":
	
	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">Sources:</h1>', unsafe_allow_html=True)
	
	src = (
		"https://cars.mclaren.com/en/legacy/12c",
		"https://supercarnostalgia.com/blog/mclaren-mp4-12c"
	)

	for i in src:
		st.write(f" - {i}")
