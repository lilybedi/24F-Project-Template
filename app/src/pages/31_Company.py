import streamlit as st

#
# Information needed on load
#


student_info, website_links = st.columns(2)

# Custom CSS portion
st.markdown(
    """
    <style>
    .second {
        background-color: #aaaaaa; 
        display: inline-block;
        margin: 0; 

    }
    </style>
    """,
    unsafe_allow_html=True,
)

with student_info:
    image, stats = st.columns(2)
    
    with image:
      st.markdown('<div class="second"> Image </div>', unsafe_allow_html=True)
      st.image('./assets/logo.png')
    with stats:
      st.write()
      st.markdown('<div class="second"> Stats </div>', unsafe_allow_html=True)


with website_links:
# Contains the "Links to Websites" page, where the resumes may be viewed and
# re-viewed

    st.write("Links to Websites")

    resumes = st.expander(label="Resumes")
    #
    # Data should come in [ResumeNames] as a list
    # and [ResumeFiles] as a list, where item ResumeName[0]
    # corresponds with [ResumeFile[0]]
    #

    # Delete when done - Sample Data
    resume_names = ["Programming Resume", "Data Science Resume"]
    resume_files = ["google.com", "yahoo.com"]
    # Stop deleting

    for i in range (0,len(resume_files)):
      try:
        url = resume_files[i]
        name = resume_names[i]
      except IndexError:
         st.write("Resume link or name not provided")
      resumes.markdown(f"[{name}]({url})") 






