from pathlib import Path
import streamlit as st
from PIL import Image
header =st.container()

# --- PATH SETTINGS ---
current_dir = Path('__file__').parent if '__file__' in locals() else Path.cwd()
css_file = current_dir / 'styles'/ 'main.css'
resume_file = current_dir / 'assets' / 'CV.pdf'
profile_pic = current_dir / 'assets' / 'profile-pic.png'

# --- General Settings ---
PAGE_TITLE = 'CURRICULUM VITAE  |(Example Format)'
PAGE_ICON = ':wave:'
NAME = 'Andrea'
DESCRIPTION = """Engineer"""
EMAIL = "ABC@gmail.com"
CONTACT_DETAILS= "1234678"
SOCIAL_MEDIA = {
"Twitter": "https://twitter.com/",
"LinkedIn": "https://www.linkedin.com//",
"Facebook":"https://www.facebook.com/",
"Instagram":"https://www.instagram.com/",
    }


#  Load CSS , PDF, & PROFILE PIC
with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
with open(resume_file, 'rb') as pdf_file:
    PDFbytes = pdf_file.read()
profile_pic = Image.open(profile_pic)


# HERO SECTION 
col1 , col2 = st.columns(2, gap='small')
with col1:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(label='Download CV',
                       data=PDFbytes,
                       file_name='resume_file',
                       mime='application/octet-stream')
with col2:
    st.image(profile_pic, width=200)
st.write(' 📧 EMAIL: ', EMAIL)

# -- SOCIAL MEDIA SECTION --
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))
for index , (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    with cols[index]:
        st.markdown(f"""[{platform}]({link})""", unsafe_allow_html=True)


st.write('#')
st.subheader('Awareness of Standards::')
st.write('''
- 🏆TRAINING AND PROFESSIONAL DEVELOPMENT:
Course Name, Venue (Institution, Address), Date
Example:
Epidemiology for Public Health Professionals, Emory University, Atlanta, Georgia, 
USA, 09/25/2006 – 10/27/2006.

''')



st.write('#')
st.subheader('EDUCATION:')
st.write('''
- 👨🏻‍🎓	MSc, London School of Hygiene & Tropical Medicine, Keppel Street, London
 WC1E 7HT, UK, 08/1996 to 06/1998.
''')


st.write('#')
st.subheader('Personal Information')
st.write('''
- Fathers Name 		: 	
- Date of Birth		: 	
- Religion 	        :
- Marital Status 	:
- Nationality 		:	
- Passport 		    :	
''')


