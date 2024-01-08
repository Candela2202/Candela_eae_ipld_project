import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Candela Portfolio",
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.header("Introduction to Programming Languages for Data")
    st.write("###")
    st.write("***Final Project - Dec 2023***")
    st.write("**Author:** Candela")
    st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


# ----- Top title -----
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Candela</h1></div>""", unsafe_allow_html=True)  # TODO: Add your name


# ----- Profile image file -----
profile_image_file_path = "me.JPG"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
current_role = "Industrial Fashion Designer and Data Analytics Máster Student at EAE"   # TODO: Change this

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
- 🧑‍💻 I am a Industrial Fashion Designer and Data Analytics Máster Student at EAE.

- My previous studies are Fashion Industrial Desing in Politécnica Madrid University and a Máster in Markenting Online in The Power Bussiness School.

- ❤️ When I was 3 years old I started dancing and now Im already doing ballet for more than 18 years.

- 🤖 My personal proyect and wish is develop a new Fashion Design Brand.

- 🏂 One of my hobbies is Fashion Blogging

- 📫 How to reach me: [Email](candeladam02@hotmail.com)
         [LinKedin](www.linkedin.com/in/candeladamas)
         

- 🏠 Im from the South of Spain: [Granada](https://www.google.com/search?q=Granada&rlz=1C5CHFA_enES1028ES1062&oq=Granada&aqs=chrome..69i57j46i131i433i512j0i131i433i512j0i131i433i512i650j46i433i512j0i131i433i512i650j0i433i512j46i175i199i512j0i131i433i512j0i271.1324j1j9&sourceid=chrome&ie=UTF-8), Andalucía. I curretly reside in [Barcelona](https://www.google.com/search?q=Barcelona+city&sca_esv=591519426&rlz=1C5CHFA_enES1028ES1062&ei=RNR9ZduQEcedkdUP89q-gAE&ved=0ahUKEwjbwruBtJSDAxXHTqQEHXOtDxAQ4dUDCBA&uact=5&oq=Barcelona+city&gs_lp=Egxnd3Mtd2l6LXNlcnAiDkJhcmNlbG9uYSBjaXR5Mg4QLhivARjHARiABBiOBTIOEC4YgAQYxwEYrwEYjgUyCBAuGIAEGLEDMg4QLhiABBjHARivARiOBTIOEC4YgAQYxwEYrwEYjgUyDhAuGIAEGMcBGK8BGI4FMgUQABiABDIREC4YrwEYxwEYgAQYmAUYmwUyBRAAGIAEMhEQLhiABBjHARivARiYBRibBTIdEC4YrwEYxwEYgAQYjgUYlwUY3AQY3gQY4ATYAQNIlQ1Q9gJYoApwAXgBkAEAmAHSAaABkAWqAQUwLjQuMbgBA8gBAPgBAcICChAAGEcY1gQYsAPCAg0QABiABBiKBRhDGLADwgIOEAAY5AIY1gQYsAPYAQHCAhMQLhiABBiKBRhDGMgDGLAD2AECwgIQEAAYgAQYigUYQxixAxiDAcICDRAAGIAEGIoFGEMYsQPCAgoQABiABBiKBRhDwgIQEC4YgAQYigUYQxixAxiDAcICChAuGIAEGIoFGEPCAggQABiABBixA8ICDhAAGIAEGIoFGLEDGIMBwgIHEC4YgAQYCsICCBAuGLEDGIAEwgIXEC4YsQMYgAQYlwUY3AQY3gQY4ATYAQPiAwQYACBBiAYBkAYTugYGCAEQARgJugYGCAIQARgIugYGCAMQARgU&sclient=gws-wiz-serp).
""")

# Feel free to add other points like your Linkedin, Github, Social Media, etc.
