import streamlit as st

st.set_page_config(page_title="SHARKPIT", layout="wide")

# -----------------------------
# CUSTOM CSS THEME
# -----------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Background Ocean Gradient */
.stApp {
    background: linear-gradient(to bottom,#c9f2ff,#e6fbff,#ffffff);
}

/* Bubbles Animation */
.bubbles {
    position: fixed;
    width: 100%;
    height: 100%;
    z-index:-1;
    overflow:hidden;
}

.bubbles span{
    position:absolute;
    bottom:-150px;
    width:20px;
    height:20px;
    background:rgba(255,255,255,0.6);
    border-radius:50%;
    animation:rise 20s infinite;
}

@keyframes rise{
    0%{transform:translateY(0);}
    100%{transform:translateY(-1200px);}
}

/* Title */
.title{
    text-align:center;
    font-size:90px;
    font-weight:900;
    color:#003b4f;
}

/* Subtitle */
.subtitle{
    text-align:center;
    font-size:28px;
    font-weight:600;
    color:#0077a6;
}

/* Paragraph */
.desc{
    text-align:center;
    font-size:20px;
    color:#003b4f;
    padding:20px 80px;
}

/* Shark Card */
.card{
    background:white;
    border-radius:18px;
    padding:25px;
    box-shadow:0px 10px 30px rgba(0,0,0,0.1);
    text-align:center;
    transition:0.3s;
}

.card:hover{
    transform:translateY(-8px);
}

.card img{
    width:160px;
    height:160px;
    border-radius:100px;
    object-fit:cover;
}

.name{
    font-size:22px;
    font-weight:700;
    margin-top:10px;
    color:#003b4f;
}

.role{
    font-size:16px;
    color:#0077a6;
}

.btn{
    margin-top:10px;
    padding:8px 18px;
    border-radius:10px;
    background:#0099cc;
    color:white;
    text-decoration:none;
}

/* Section Title */
.section{
    font-size:50px;
    text-align:center;
    font-weight:800;
    color:#003b4f;
    margin-top:60px;
}

/* Roadmap */
.roadmap{
    text-align:center;
    font-size:20px;
    padding:25px;
    background:white;
    border-radius:15px;
    box-shadow:0px 5px 20px rgba(0,0,0,0.1);
}

/* Footer sand */
.footer{
    margin-top:80px;
    padding:40px;
    background:#f7e7b4;
    text-align:center;
    border-radius:20px 20px 0 0;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO SECTION
# -----------------------------
st.markdown('<div class="title">SHARKPIT</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">By SCIENCE AND TECH CLUB – MECS</div>', unsafe_allow_html=True)

st.markdown("""
<div class="desc">
SHARKPIT is a startup pitching and innovation platform organised by the Science and Technology Club of Matrusri Engineering College.
The event invites students from all years of B.Tech to present their innovative ideas, startup concepts, and technical projects
to a panel of experienced founders and entrepreneurs.

Participants will get the opportunity to pitch their ideas, receive valuable feedback from industry leaders, and showcase their
creativity and entrepreneurial mindset. The event aims to inspire students to transform their ideas into impactful solutions
while learning the fundamentals of startup pitching and problem solving.

The competition culminates with shortlisted teams presenting their ideas in front of the jury panel where the best concepts,
innovative thinking and practical solutions will be recognized.
</div>
""", unsafe_allow_html=True)

# -----------------------------
# SHARKS SECTION
# -----------------------------
st.markdown('<div class="section">Meet Our Sharks</div>', unsafe_allow_html=True)

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="card">
        <img src="sai_eshwar.png">
        <div class="name">E Sai Eshwar</div>
        <div class="role">Founder – Studlyf & Nirvaha Wellness</div>
        <a class="btn" href="https://linkedin.com/in/esaieshwar" target="_blank">Visit Profile</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <img src="yashwanth_bondapalli.png">
        <div class="name">Yashwanth Bondapalli</div>
        <div class="role">Founder – Back2Base</div>
        <a class="btn" href="https://linkedin.com/in/yashwanth-bondapalli-37b6a7255" target="_blank">Visit Profile</a>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <img src="sai_harishith.png">
        <div class="name">Sai Harishith</div>
        <div class="role">Founder – ShieldNet Solutions</div>
        <a class="btn" href="https://linkedin.com/in/sai-harishith-b37558322" target="_blank">Visit Profile</a>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# REGISTRATION
# -----------------------------
st.markdown('<div class="section">Registration</div>', unsafe_allow_html=True)

st.markdown("""
### Morning Session – Casual Founder Meetup
Anyone can attend this session and listen to founders sharing their journey.

🔗 https://luma.com/4e3p9fdx

### Evening Session – SharkPit Pitching Round
This registration requires approval for pitching ideas.

🔗 https://luma.com/34izlhhj
""")

# -----------------------------
# EVENT ROADMAP
# -----------------------------
st.markdown('<div class="section">Event Roadmap</div>', unsafe_allow_html=True)

c1,c2 = st.columns(2)

with c1:
    st.markdown('<div class="roadmap"><b>13 March</b><br>Idea Submission Deadline</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="roadmap"><b>Shortlisting</b><br>Selected Teams Notified via Email</div>', unsafe_allow_html=True)

c3,c4 = st.columns(2)

with c3:
    st.markdown('<div class="roadmap"><b>17 March</b><br>Final Round Pitching in front of Jury (Top 20 Teams)</div>', unsafe_allow_html=True)

# -----------------------------
# GUIDELINES
# -----------------------------
st.markdown('<div class="section">Guidelines</div>', unsafe_allow_html=True)

st.markdown("""
• Each team will be given **10 minutes** to pitch their idea.  
• The **presentation should not exceed 7 slides**.  
• Clearly explain **problem statement, solution, market opportunity and implementation**.  
• Teams should maintain clarity and concise storytelling during their pitch.  
• Judges will evaluate based on **innovation, feasibility, impact and presentation quality**.
""")

# -----------------------------
# QUERY BUTTON
# -----------------------------
st.markdown('<div class="section">Have Questions?</div>', unsafe_allow_html=True)

st.markdown("""
<a href="mailto:scienceclubmecs@gmail.com?subject=SHARKPIT Query" target="_blank">
<button style="
padding:12px 25px;
font-size:18px;
background:#0099cc;
color:white;
border:none;
border-radius:10px;">
Ask Queries
</button>
</a>
""", unsafe_allow_html=True)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
<div class="footer">
Open to all years of B.Tech – Matrusri Engineering College
</div>
""", unsafe_allow_html=True)
