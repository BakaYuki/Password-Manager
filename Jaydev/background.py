from dbconn import *
import base64


background_image_path = "images/locknobg.jpg"
st.markdown(
f"""
<style>
    body {{
        background-image: url("data:image/jpeg;base64,{base64.b64encode(open(background_image_path, "rb").read()).decode()}"); /* Using base64 encoding to embed image */
        background-size: cover;
    }}
</style>
""",
unsafe_allow_html=True,
)