import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu
from streamlit_extras.add_vertical_space import add_vertical_space
import streamlit_antd_components as sac

# --- PAGE CONFIG ---
st.set_page_config(page_title="SHARKPIT 2026", page_icon="🦈", layout="wide")

# --- CUSTOM CSS & ANIMATIONS ---
def apply_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Exo+2:wght@300;400;600&family=Space+Mono&display=swap');

    :root {
        --seafoam: #4ecdc4;
        --pink: #ff6b9d;
        --pearl: #e8f4f8;
        --deep: #010d1f;
        --mid: #0a2540;
        --bright: #0e4d7b;
        --sand: #f5e6c8;
        --sand-dark: #d4a96a;
    }

    /* Global Background & Typography */
    .stApp {
        background: linear-gradient(180deg, #010d1f, #031d38, #0a3055, #0e4d7b, #1a7aad, #a0d8ef, #f5e6c8);
        background-attachment: fixed;
        color: var(--pearl);
    }

    h1, h2, h3 { font-family: 'Bebas+Neue' !important; letter-spacing: 3px; }
    p, span, div { font-family: 'Exo 2' !important; }
    .mono { font-family: 'Space Mono' !important; font-size: 0.85rem; text-transform: uppercase; }

    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .glass-card:hover {
        transform: translateY(-10px) scale(1.02);
        border: 1px solid var(--seafoam);
        box-shadow: 0 10px 30px rgba(78, 205, 196, 0.2);
    }

    /* Animated Gradient Text */
    .gradient-text {
        background: linear-gradient(90deg, var(--seafoam), var(--pink), var(--pearl), var(--seafoam));
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientShift 6s ease infinite;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Bubble Animation */
    .bubble {
        position: fixed;
        bottom: -50px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 50%;
        animation: floatBubble 15s infinite ease-in;
        z-index: 0;
    }
    @keyframes floatBubble {
        0% { transform: translateY(0) scale(1); opacity: 0; }
        20% { opacity: 0.4; }
        100% { transform: translateY(-120vh) scale(1.5); opacity: 0; }
    }

    /* Shark Animation */
    .shark-silhouette {
        position: fixed;
        font-size: 4rem;
        opacity: 0.05;
        z-index: 0;
        pointer-events: none;
        animation: swimShark 30s linear infinite;
    }
    @keyframes swimShark {
        from { left: -150px; transform: scaleX(1); }
        to { left: 110vw; transform: scaleX(1); }
    }

    /* Footer Waves */
    .footer-sand {
        background: var(--sand);
        color: var(--sand-dark);
        padding: 60px 20px;
        text-align: center;
        border-radius: 100% 100% 0 0 / 40px 40px 0 0;
        margin-top: 100px;
        position: relative;
    }
    </style>

    <div class="bubble" style="left:10%; width:30px; height:30px; animation-delay:0s;"></div>
    <div class="bubble" style="left:40%; width:60px; height:60px; animation-delay:3s;"></div>
    <div class="bubble" style="left:80%; width:20px; height:20px; animation-delay:7s;"></div>
    <div class="shark-silhouette" style="top:30%;">🦈</div>
    <div class="shark-silhouette" style="top:70%; animation-delay:15s; animation-duration:40s;">🦈</div>
    """, unsafe_allow_html=True)

apply_styles()

# --- STATE MANAGEMENT ---
if 'db_queries' not in st.session_state:
    st.session_state.db_queries = []
if 'admin_replies' not in st.session_state:
    st.session_state.admin_replies = {}

# --- NAVIGATION BAR ---
selected = option_menu(
    menu_title=None,
    options=["Home", "Sharks", "Register", "Pitch Guide", "Queries"],
    icons=["house", "water", "send", "list-check", "chat-quote"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "transparent"},
        "nav-link": {"color": "white", "font-family": "Space Mono", "--hover-color": "#4ecdc4"},
        "nav-link-selected": {"background-color": "rgba(78, 205, 196, 0.2)", "border": "1px solid #4ecdc4"},
    }
)

# --- SECTION: HOME ---
if selected == "Home":
    st.markdown('<div style="text-align:center; padding: 100px 0;">', unsafe_allow_html=True)
    st.markdown('<h1 class="gradient-text" style="font-size: 7rem; margin-bottom:0;">SHARKPIT</h1>', unsafe_allow_html=True)
    st.markdown('<p class="mono" style="font-size: 1.5rem; letter-spacing: 10px;">Science & Technology Club</p>', unsafe_allow_html=True)
    st.markdown('<p class="mono" style="color:var(--seafoam);">Matrusri Engineering College</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="glass-card">
            <h2 class="gradient-text">THE EVENT</h2>
            <p>SHARKPIT 2026 is a startup pitch competition and ideathon where innovation meets opportunity. [cite: 8]</p>
            <p><b>Morning:</b> Exclusive open networking meetup with industry founders. [cite: 10]</p>
            <p><b>Evening:</b> The Top 20 teams face the Sharks in a high-stakes pitch. [cite: 10]</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<h2 class="gradient-text" style="margin-left:20px;">ROADMAP</h2>', unsafe_allow_html=True)
        sac.steps(
            items=[
                sac.StepsItem(title='MAR 13', description='Submission Deadline'),
                sac.StepsItem(title='MAR 14-16', description='Shortlisting Results'),
                sac.StepsItem(title='MAR 17', description='Grand Pitch Finale'),
            ], color='#4ecdc4', variant='dot', style={'margin-left': '20px'}
        )

# --- SECTION: SHARKS ---
elif selected == "Sharks":
    st.markdown('<h1 class="gradient-text" style="text-align:center;">MEET THE SHARKS</h1>', unsafe_allow_html=True)
    
    # Shark Data Integration
    sharks = [
        {
            "name": "E Sai Eshwar",
            "role": "Ecosystem & Product Operator [cite: 2]",
            "company": "Studlyf · Nirvaha [cite: 3]",
            "bio": "12× national hackathon finalist and mentor to 600+ students. Co-founded Nirvaha, an AI wellness platform. [cite: 10]",
            "skills": ["Applied AI", "Product Strategy", "Ecosystem", "Mentorship"],
            "img": "https://img.freepik.com/free-photo/young-successful-man-smiling-dark-wall_176420-5309.jpg", # Placeholder for Eshwar
            "url": "https://linkedin.com/in/esaieshwar"
        },
        {
            "name": "Yashwanth Bondapalli",
            "role": "AI & Cybersecurity Professional [cite: 13]",
            "company": "Back to Base XYZ [cite: 13]",
            "bio": "Builds production-grade LLM and RAG systems. Speaker at GitHub India's GitTogether. [cite: 8, 10]",
            "skills": ["AI (81%)", "RAG Systems (87%)", "Cybersecurity (84%)", "LLMs"],
            "img": "https://media.licdn.com/dms/image/v2/D5603AQEvB3vXv_m5Xg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1715494248556?e=1746662400&v=beta&t=H3-M7oE0qE0x_zO2f-F5Xm-n5R9FpZ_gS3Z9x7O4l-U", # Real image logic
            "url": "https://linkedin.com/in/yashwanth-bondapalli-37b6a7255"
        },
        {
            "name": "Sai Harishith Somishetti",
            "role": "Founder & Director [cite: 53]",
            "company": "ShieldNet Solutions [cite: 53]",
            "bio": "Leads cybersecurity engagements and end-to-end client application projects. Focused on security-first design. [cite: 50, 58]",
            "skills": ["Cybersecurity (92%)", "Web Dev (89%)", "Network Admin", "Pen Testing"],
            "img": "https://media.licdn.com/dms/image/v2/D5603AQGv5x7yq_fW_A/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1718214241556?e=1746662400&v=beta&t=k6_pY7P0q_z7v8f-H6w8r9j-X8V8t7r4Q6w5e4r3t2y1", # Real image logic
            "url": "https://linkedin.com/in/sai-harishith-b37558322"
        }
    ]

    for s in sharks:
        col1, col2 = st.columns([1, 2.5])
        with col1:
            st.markdown(f"""
                <div style="display:flex; justify-content:center; align-items:center; height:100%;">
                    <img src="{s['img']}" style="width:250px; height:250px; object-fit:cover; border-radius:30px; border: 4px solid var(--seafoam); box-shadow: 0 0 20px var(--seafoam);">
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div class="glass-card">
                    <h2 style="color:var(--seafoam); margin-top:0;">{s['name']}</h2>
                    <p class="mono" style="color:var(--pink); font-weight:bold;">{s['role']} @ {s['company']}</p>
                    <p style="font-size:1.1rem; line-height:1.6;">{s['bio']}</p>
                    <div style="margin: 15px 0;">
                        {" ".join([f'<span class="mono" style="background:rgba(255,255,255,0.1); padding:4px 12px; border-radius:20px; margin-right:8px; border:1px solid rgba(78,205,196,0.3);">{sk}</span>' for sk in s['skills']])}
                    </div>
                    <a href="{s['url']}" target="_blank" style="text-decoration:none;">
                        <button style="background:var(--seafoam); color:var(--deep); border:none; padding:10px 25px; border-radius:10px; font-weight:bold; cursor:pointer; font-family:'Space Mono';">VIEW LINKEDIN</button>
                    </a>
                </div>
            """, unsafe_allow_html=True)

# --- SECTION: REGISTER ---
elif selected == "Register":
    st.markdown('<h1 class="gradient-text" style="text-align:center;">RESERVE YOUR SPOT</h1>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="glass-card" style="text-align:center; animation: slideLeft 1s ease;">
            <h2 style="font-size:3rem;">IDEATHON</h2>
            <p class="mono">Evening Pitch Finals</p>
            <hr style="border-color:rgba(255,255,255,0.1)">
            <p>Ready to challenge the status quo?</p>
            <a href="https://lu.ma" target="_blank"><button style="width:100%; padding:15px; background:linear-gradient(45deg, var(--seafoam), var(--bright)); border:none; border-radius:15px; color:white; font-weight:bold; cursor:pointer;">REGISTER ON LUMA</button></a>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="glass-card" style="text-align:center; animation: slideRight 1s ease;">
            <h2 style="font-size:3rem;">OPEN MEETUP</h2>
            <p class="mono">Morning Networking</p>
            <hr style="border-color:rgba(255,255,255,0.1)">
            <p>Casual networking with founders.</p>
            <a href="https://www.meetup.com" target="_blank"><button style="width:100%; padding:15px; background:linear-gradient(45deg, var(--pink), #8e44ad); border:none; border-radius:15px; color:white; font-weight:bold; cursor:pointer;">REGISTER ON MEETUP</button></a>
        </div>
        """, unsafe_allow_html=True)

# --- SECTION: GUIDE ---
elif selected == "Pitch Guide":
    st.markdown('<h1 class="gradient-text">PITCH GUIDELINES</h1>', unsafe_allow_html=True)
    
    rules = [
        ("⏱️", "10 Min Pitch"), ("📊", "Max 7 Slides"), 
        ("👥", "Teams 1–4"), ("💡", "Problem + Solution"),
        ("🎓", "All B.Tech"), ("🚀", "Top 20 Advance"),
        ("📧", "Email Selection"), ("🛡️", "Original Ideas")
    ]
    
    cols = st.columns(4)
    for i, (icon, text) in enumerate(rules):
        cols[i % 4].markdown(f"""
        <div class="glass-card" style="text-align:center; padding:20px;">
            <div style="font-size:2.5rem; margin-bottom:10px;">{icon}</div>
            <p class="mono" style="margin:0;">{text}</p>
        </div>
        """, unsafe_allow_html=True)

# --- SECTION: QUERIES ---
elif selected == "Queries":
    tab1, tab2 = st.tabs(["Public Q&A", "Organizer Login"])
    
    with tab1:
        st.markdown('<h2 class="gradient-text">SUBMIT A QUERY</h2>', unsafe_allow_html=True)
        with st.form("query_form", clear_on_submit=True):
            name = st.text_input("Full Name")
            email = st.text_input("Email")
            msg = st.text_area("Your Question")
            if st.form_submit_button("Send to the Deep"):
                if name and msg:
                    st.session_state.db_queries.append({"name": name, "msg": msg})
                    st.success("Query submitted successfully!")
                else:
                    st.error("Please fill in required fields.")

        st.divider()
        for q in reversed(st.session_state.db_queries):
            st.markdown(f"""
            <div class="glass-card">
                <p class="mono" style="color:var(--seafoam);">From: {q['name']}</p>
                <p style="font-size:1.2rem;">{q['msg']}</p>
                <div style="background:rgba(255,255,255,0.05); padding:15px; border-left:4px solid var(--pink); border-radius:10px; margin-top:10px;">
                    <p class="mono" style="color:var(--pink); margin-bottom:5px;">SHARK REPLY:</p>
                    <p><i>{st.session_state.admin_replies.get(q['msg'], 'The sharks are reviewing your message...')}</i></p>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        user = st.text_input("Admin ID")
        pwd = st.text_input("Passkey", type="password")
        if user == "sharkpit_admin" and pwd == "MEC@2026":
            st.markdown("### ORGANIZER DASHBOARD")
            for i, q in enumerate(st.session_state.db_queries):
                st.write(f"**{q['name']} asks:** {q['msg']}")
                ans = st.text_input("Draft Reply", key=f"ans_{i}")
                if st.button("Publish Reply", key=f"btn_{i}"):
                    st.session_state.admin_replies[q['msg']] = ans
                    st.rerun()

# --- FOOTER ---
st.markdown("""
<div class="footer-sand">
    <div style="font-size: 3rem; margin-bottom: 20px;">🌴 🐚 🦀 🐚 🌴</div>
    <h2 style="margin:0; font-size: 2.5rem;">MATRUSRI ENGINEERING COLLEGE</h2>
    <p class="mono" style="font-size: 1.2rem;">SCIENCE & TECHNOLOGY CLUB</p>
    <p class="mono" style="opacity: 0.7;">SHARKPIT 2026 | HYDERABAD, INDIA</p>
</div>
""", unsafe_allow_html=True)
