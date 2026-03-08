import streamlit as st
import datetime

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="SHARKPIT 2026 — Matrusri Engineering College",
    page_icon="🦈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
#  SESSION STATE
# ─────────────────────────────────────────────
if "organiser_logged_in" not in st.session_state:
    st.session_state.organiser_logged_in = False
if "show_login_modal" not in st.session_state:
    st.session_state.show_login_modal = False
if "queries" not in st.session_state:
    st.session_state.queries = []  # list of dicts {name, email, message, reply}
if "query_submitted" not in st.session_state:
    st.session_state.query_submitted = False

ORGANISER_USERNAME = "sharkpit_admin"
ORGANISER_PASSWORD = "MEC@2026"

# ─────────────────────────────────────────────
#  MEGA CSS — OCEANIC THEME
# ─────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Exo+2:ital,wght@0,300;0,600;0,800;1,300&family=Space+Mono:wght@400;700&display=swap');

/* ── CSS Variables ── */
:root {
  --ocean-deep:    #010d1f;
  --ocean-mid:     #0a2540;
  --ocean-bright:  #0e4d7b;
  --ocean-light:   #1a91d1;
  --seafoam:       #4ecdc4;
  --electric-pink: #ff6b9d;
  --pearl:         #e8f4f8;
  --sand:          #f5e6c8;
  --sand-dark:     #d4a96a;
  --gold:          #ffd700;
  --bubble-white:  rgba(255,255,255,0.15);
  --card-bg:       rgba(10, 37, 64, 0.82);
  --glass:         rgba(255,255,255,0.06);
}

/* ── Reset & Base ── */
* { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"],
[data-testid="stMain"], .main {
  min-height: 100vh;
  background: transparent !important;
}

[data-testid="stAppViewContainer"] {
  background: linear-gradient(
    180deg,
    #010d1f 0%,
    #031d38 18%,
    #0a3055 35%,
    #0e4d7b 55%,
    #1a7aad 72%,
    #a0d8ef 88%,
    #f5e6c8 100%
  ) !important;
  position: relative;
  overflow-x: hidden;
  font-family: 'Exo 2', sans-serif;
}

/* ── BUBBLES ── */
.bubbles-layer {
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  pointer-events: none;
  z-index: 0;
  overflow: hidden;
}

.bubble {
  position: absolute;
  bottom: -120px;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.45), rgba(100,210,255,0.08));
  border: 1px solid rgba(255,255,255,0.25);
  animation: floatBubble linear infinite;
}

.bubble:nth-child(1)  { width:18px;  height:18px;  left:4%;   animation-duration:14s; animation-delay:0s;   }
.bubble:nth-child(2)  { width:32px;  height:32px;  left:12%;  animation-duration:18s; animation-delay:2s;   }
.bubble:nth-child(3)  { width:12px;  height:12px;  left:22%;  animation-duration:11s; animation-delay:4s;   }
.bubble:nth-child(4)  { width:24px;  height:24px;  left:33%;  animation-duration:16s; animation-delay:1s;   }
.bubble:nth-child(5)  { width:8px;   height:8px;   left:44%;  animation-duration:9s;  animation-delay:3s;   }
.bubble:nth-child(6)  { width:40px;  height:40px;  left:55%;  animation-duration:20s; animation-delay:0.5s; }
.bubble:nth-child(7)  { width:16px;  height:16px;  left:64%;  animation-duration:13s; animation-delay:5s;   }
.bubble:nth-child(8)  { width:28px;  height:28px;  left:74%;  animation-duration:17s; animation-delay:2.5s; }
.bubble:nth-child(9)  { width:10px;  height:10px;  left:82%;  animation-duration:10s; animation-delay:1.5s; }
.bubble:nth-child(10) { width:22px;  height:22px;  left:91%;  animation-duration:15s; animation-delay:3.5s; }
.bubble:nth-child(11) { width:36px;  height:36px;  left:8%;   animation-duration:22s; animation-delay:6s;   }
.bubble:nth-child(12) { width:14px;  height:14px;  left:48%;  animation-duration:12s; animation-delay:7s;   }
.bubble:nth-child(13) { width:20px;  height:20px;  left:70%;  animation-duration:19s; animation-delay:0.8s; }
.bubble:nth-child(14) { width:6px;   height:6px;   left:26%;  animation-duration:8s;  animation-delay:4.5s; }
.bubble:nth-child(15) { width:30px;  height:30px;  left:87%;  animation-duration:21s; animation-delay:2.2s; }

@keyframes floatBubble {
  0%   { transform: translateY(0) translateX(0) scale(1);   opacity: 0;   }
  5%   { opacity: 1; }
  50%  { transform: translateY(-45vh) translateX(15px) scale(1.05); }
  95%  { opacity: 0.7; }
  100% { transform: translateY(-105vh) translateX(-10px) scale(0.95); opacity: 0; }
}

/* ── SHARK SILHOUETTES ── */
.shark-layer {
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  pointer-events: none;
  z-index: 0;
  overflow: hidden;
}

.shark-svg {
  position: absolute;
  opacity: 0.06;
  animation: swimShark linear infinite;
  filter: blur(1.5px);
}

.shark-svg:nth-child(1) { top: 15%; width: 280px; animation-duration: 30s; animation-delay: 0s; }
.shark-svg:nth-child(2) { top: 38%; width: 180px; animation-duration: 24s; animation-delay: 8s; }
.shark-svg:nth-child(3) { top: 62%; width: 340px; animation-duration: 36s; animation-delay: 4s; transform: scaleX(-1); }
.shark-svg:nth-child(4) { top: 80%; width: 140px; animation-duration: 20s; animation-delay: 14s; }

@keyframes swimShark {
  0%   { left: -400px; }
  100% { left: 110%;   }
}

/* ── COCONUT TREES ── */
.coconut-left, .coconut-right {
  position: fixed;
  bottom: 0;
  z-index: 1;
  pointer-events: none;
  width: 140px;
}
.coconut-left  { left: 0; }
.coconut-right { right: 0; transform: scaleX(-1); }

/* ── CONTENT LAYER ── */
[data-testid="stMainBlockContainer"] {
  position: relative;
  z-index: 2;
  padding-bottom: 0 !important;
}

/* ── HIDE STREAMLIT CHROME ── */
#MainMenu, footer, header, [data-testid="stHeader"],
[data-testid="collapsedControl"] { display: none !important; }
[data-testid="stSidebar"] { display: none; }

/* ── TOP BAR ── */
.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 32px 0 32px;
  position: relative;
  z-index: 10;
}

.top-bar-brand {
  font-family: 'Space Mono', monospace;
  color: var(--seafoam);
  font-size: 13px;
  letter-spacing: 3px;
  text-transform: uppercase;
  opacity: 0.8;
}

.organiser-btn {
  background: linear-gradient(135deg, rgba(78,205,196,0.15), rgba(255,107,157,0.15));
  border: 1px solid var(--seafoam);
  color: var(--seafoam);
  padding: 8px 20px;
  border-radius: 30px;
  font-family: 'Space Mono', monospace;
  font-size: 12px;
  letter-spacing: 2px;
  cursor: pointer;
  text-transform: uppercase;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
}
.organiser-btn:hover {
  background: var(--seafoam);
  color: var(--ocean-deep);
  box-shadow: 0 0 20px rgba(78,205,196,0.4);
}

/* ── HERO ── */
.hero {
  text-align: center;
  padding: 60px 20px 30px;
  position: relative;
}

.hero-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(90px, 18vw, 200px);
  line-height: 0.9;
  letter-spacing: 8px;
  background: linear-gradient(
    135deg,
    var(--seafoam) 0%,
    var(--pearl) 30%,
    var(--electric-pink) 60%,
    var(--seafoam) 100%
  );
  background-size: 300% 300%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: gradientShift 5s ease infinite;
  text-shadow: none;
  filter: drop-shadow(0 0 40px rgba(78,205,196,0.3));
}

@keyframes gradientShift {
  0%   { background-position: 0% 50%; }
  50%  { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.hero-subtitle {
  font-family: 'Space Mono', monospace;
  font-size: clamp(12px, 2.2vw, 18px);
  letter-spacing: 5px;
  color: var(--pearl);
  opacity: 0.75;
  margin-top: 8px;
  text-transform: uppercase;
}

.hero-tagline {
  font-family: 'Exo 2', sans-serif;
  font-style: italic;
  font-size: clamp(14px, 2.5vw, 20px);
  color: var(--seafoam);
  margin-top: 16px;
  letter-spacing: 2px;
  opacity: 0.9;
}

.wave-divider {
  width: 100%;
  overflow: hidden;
  line-height: 0;
  margin-top: 20px;
}

/* ── GLASS SECTIONS ── */
.glass-section {
  background: rgba(10, 37, 64, 0.55);
  border: 1px solid rgba(78,205,196,0.2);
  border-radius: 24px;
  padding: 48px 48px;
  margin: 24px auto;
  max-width: 1100px;
  backdrop-filter: blur(12px);
  box-shadow: 0 8px 60px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.08);
  position: relative;
  overflow: hidden;
}

.glass-section::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--seafoam), transparent);
}

.section-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(36px, 5vw, 60px);
  letter-spacing: 4px;
  text-align: center;
  background: linear-gradient(135deg, var(--seafoam), var(--pearl), var(--electric-pink));
  background-size: 200% 200%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: gradientShift 6s ease infinite;
  margin-bottom: 32px;
}

.body-text {
  font-family: 'Exo 2', sans-serif;
  font-size: 16px;
  line-height: 1.9;
  color: rgba(232, 244, 248, 0.88);
  max-width: 850px;
  margin: 0 auto;
  text-align: center;
}

/* ── JURY CARDS ── */
.sharks-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 28px;
  margin-top: 40px;
}

.shark-card {
  background: linear-gradient(
    145deg,
    rgba(14, 77, 123, 0.7),
    rgba(10, 37, 64, 0.9)
  );
  border: 1px solid rgba(78,205,196,0.3);
  border-radius: 20px;
  padding: 36px 28px;
  text-align: center;
  backdrop-filter: blur(16px);
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  position: relative;
  overflow: hidden;
  box-shadow: 0 10px 40px rgba(0,0,0,0.4);
}

.shark-card::before {
  content: '';
  position: absolute;
  top: -50%; left: -50%;
  width: 200%; height: 200%;
  background: radial-gradient(circle at 50% 50%, rgba(78,205,196,0.06), transparent 60%);
  opacity: 0;
  transition: opacity 0.4s;
}

.shark-card:hover {
  transform: translateY(-12px) scale(1.02);
  border-color: var(--seafoam);
  box-shadow: 0 20px 60px rgba(78,205,196,0.25), 0 0 0 1px rgba(78,205,196,0.3);
}

.shark-card:hover::before { opacity: 1; }

.shark-avatar {
  width: 90px; height: 90px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--seafoam), var(--electric-pink));
  margin: 0 auto 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 36px;
  box-shadow: 0 0 30px rgba(78,205,196,0.4);
  position: relative;
}

.shark-avatar::after {
  content: '';
  position: absolute;
  inset: -3px;
  border-radius: 50%;
  border: 2px solid transparent;
  background: linear-gradient(135deg, var(--seafoam), var(--electric-pink)) border-box;
  -webkit-mask: linear-gradient(#fff 0 0) padding-box, linear-gradient(#fff 0 0);
  mask: linear-gradient(#fff 0 0) padding-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: destination-out;
  mask-composite: exclude;
}

.shark-name {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 26px;
  letter-spacing: 3px;
  color: var(--pearl);
  margin-bottom: 8px;
}

.shark-title {
  font-family: 'Space Mono', monospace;
  font-size: 11px;
  color: var(--seafoam);
  letter-spacing: 2px;
  text-transform: uppercase;
  margin-bottom: 6px;
  line-height: 1.7;
}

.shark-company {
  font-family: 'Exo 2', sans-serif;
  font-size: 13px;
  color: rgba(232,244,248,0.6);
  margin-bottom: 24px;
  font-style: italic;
}

.linkedin-btn {
  display: inline-block;
  background: linear-gradient(135deg, rgba(10,102,194,0.3), rgba(10,102,194,0.6));
  border: 1px solid rgba(10,102,194,0.7);
  color: #88b8f0;
  padding: 10px 24px;
  border-radius: 30px;
  text-decoration: none;
  font-family: 'Space Mono', monospace;
  font-size: 11px;
  letter-spacing: 2px;
  text-transform: uppercase;
  transition: all 0.3s ease;
  cursor: pointer;
}

.linkedin-btn:hover {
  background: rgba(10,102,194,0.8);
  color: white;
  box-shadow: 0 0 20px rgba(10,102,194,0.4);
  text-decoration: none;
}

/* ── REGISTRATION SECTION ── */
.reg-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 28px;
  margin-top: 32px;
}

@media (max-width: 700px) { .reg-grid { grid-template-columns: 1fr; } }

.reg-card {
  background: linear-gradient(145deg, rgba(78,205,196,0.08), rgba(255,107,157,0.05));
  border: 1px solid rgba(78,205,196,0.25);
  border-radius: 20px;
  padding: 36px 28px;
  text-align: center;
  position: relative;
  overflow: hidden;
  transition: all 0.3s ease;
}

.reg-card:hover {
  border-color: var(--seafoam);
  box-shadow: 0 12px 40px rgba(78,205,196,0.15);
  transform: translateY(-4px);
}

.reg-badge {
  display: inline-block;
  background: linear-gradient(135deg, var(--seafoam), var(--ocean-bright));
  color: var(--ocean-deep);
  font-family: 'Space Mono', monospace;
  font-size: 10px;
  letter-spacing: 3px;
  text-transform: uppercase;
  padding: 5px 16px;
  border-radius: 20px;
  margin-bottom: 16px;
  font-weight: 700;
}

.reg-badge.evening {
  background: linear-gradient(135deg, var(--electric-pink), #c84b8e);
  color: white;
}

.reg-session-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 32px;
  letter-spacing: 3px;
  color: var(--pearl);
  margin-bottom: 12px;
}

.reg-desc {
  font-family: 'Exo 2', sans-serif;
  font-size: 14px;
  color: rgba(232,244,248,0.7);
  line-height: 1.7;
  margin-bottom: 24px;
}

.reg-btn {
  display: inline-block;
  padding: 14px 32px;
  border-radius: 40px;
  font-family: 'Bebas Neue', sans-serif;
  font-size: 18px;
  letter-spacing: 3px;
  text-decoration: none;
  text-transform: uppercase;
  transition: all 0.3s ease;
  cursor: pointer;
  border: none;
  width: 100%;
}

.reg-btn.morning {
  background: linear-gradient(135deg, var(--seafoam), #2eafa7);
  color: var(--ocean-deep);
  box-shadow: 0 8px 24px rgba(78,205,196,0.3);
}

.reg-btn.morning:hover {
  box-shadow: 0 12px 40px rgba(78,205,196,0.5);
  transform: scale(1.02);
  color: var(--ocean-deep);
  text-decoration: none;
}

.reg-btn.evening {
  background: linear-gradient(135deg, var(--electric-pink), #c84b8e);
  color: white;
  box-shadow: 0 8px 24px rgba(255,107,157,0.3);
}

.reg-btn.evening:hover {
  box-shadow: 0 12px 40px rgba(255,107,157,0.5);
  transform: scale(1.02);
  color: white;
  text-decoration: none;
}

/* ── TIMELINE ── */
.timeline {
  position: relative;
  max-width: 700px;
  margin: 40px auto 0;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 50%;
  top: 0; bottom: 0;
  width: 2px;
  background: linear-gradient(180deg, var(--seafoam), var(--electric-pink));
  transform: translateX(-50%);
}

.timeline-item {
  display: flex;
  align-items: flex-start;
  margin-bottom: 48px;
  position: relative;
}

.timeline-item:nth-child(odd)  { flex-direction: row-reverse; }
.timeline-item:nth-child(even) { flex-direction: row; }

.timeline-content {
  width: calc(50% - 36px);
  background: linear-gradient(145deg, rgba(14,77,123,0.6), rgba(10,37,64,0.8));
  border: 1px solid rgba(78,205,196,0.2);
  border-radius: 16px;
  padding: 22px 24px;
  position: relative;
  backdrop-filter: blur(8px);
  transition: all 0.3s ease;
}

.timeline-content:hover {
  border-color: var(--seafoam);
  box-shadow: 0 8px 32px rgba(78,205,196,0.15);
}

.timeline-dot {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  width: 20px; height: 20px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--seafoam), var(--electric-pink));
  box-shadow: 0 0 20px rgba(78,205,196,0.6);
  flex-shrink: 0;
  z-index: 1;
  top: 20px;
}

.timeline-date {
  font-family: 'Space Mono', monospace;
  font-size: 12px;
  color: var(--seafoam);
  letter-spacing: 2px;
  margin-bottom: 6px;
}

.timeline-label {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 22px;
  letter-spacing: 2px;
  color: var(--pearl);
  margin-bottom: 8px;
}

.timeline-detail {
  font-family: 'Exo 2', sans-serif;
  font-size: 13px;
  color: rgba(232,244,248,0.65);
  line-height: 1.6;
}

/* ── GUIDELINES ── */
.guidelines-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-top: 32px;
}

.guideline-chip {
  background: linear-gradient(145deg, rgba(78,205,196,0.1), rgba(10,77,123,0.4));
  border: 1px solid rgba(78,205,196,0.25);
  border-radius: 14px;
  padding: 20px;
  text-align: center;
  transition: all 0.3s ease;
}

.guideline-chip:hover {
  border-color: var(--seafoam);
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(78,205,196,0.15);
}

.guideline-icon { font-size: 28px; margin-bottom: 10px; }

.guideline-text {
  font-family: 'Exo 2', sans-serif;
  font-size: 13px;
  color: rgba(232,244,248,0.85);
  line-height: 1.5;
}

/* ── QUERY SECTION ── */
.query-form-wrap {
  max-width: 650px;
  margin: 0 auto;
}

/* ── Streamlit input overrides ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
  background: rgba(10,37,64,0.7) !important;
  border: 1px solid rgba(78,205,196,0.3) !important;
  border-radius: 12px !important;
  color: var(--pearl) !important;
  font-family: 'Exo 2', sans-serif !important;
  font-size: 14px !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
  border-color: var(--seafoam) !important;
  box-shadow: 0 0 16px rgba(78,205,196,0.2) !important;
}

label[data-testid="stWidgetLabel"] > div > p {
  color: rgba(232,244,248,0.8) !important;
  font-family: 'Space Mono', monospace !important;
  font-size: 12px !important;
  letter-spacing: 1px !important;
}

.stButton > button {
  background: linear-gradient(135deg, var(--seafoam), #2eafa7) !important;
  color: var(--ocean-deep) !important;
  border: none !important;
  border-radius: 30px !important;
  font-family: 'Bebas Neue', sans-serif !important;
  font-size: 18px !important;
  letter-spacing: 3px !important;
  padding: 12px 36px !important;
  width: 100% !important;
  cursor: pointer !important;
  transition: all 0.3s ease !important;
  box-shadow: 0 8px 24px rgba(78,205,196,0.3) !important;
}

.stButton > button:hover {
  box-shadow: 0 12px 40px rgba(78,205,196,0.5) !important;
  transform: scale(1.02) !important;
}

/* ── Query Cards (Organiser View) ── */
.query-card {
  background: rgba(10,37,64,0.7);
  border: 1px solid rgba(78,205,196,0.2);
  border-radius: 14px;
  padding: 20px 24px;
  margin-bottom: 16px;
}

.query-from {
  font-family: 'Space Mono', monospace;
  font-size: 12px;
  color: var(--seafoam);
  margin-bottom: 6px;
}

.query-msg {
  font-family: 'Exo 2', sans-serif;
  font-size: 14px;
  color: var(--pearl);
  margin-bottom: 12px;
}

.query-reply {
  background: rgba(78,205,196,0.08);
  border-left: 3px solid var(--seafoam);
  padding: 10px 14px;
  border-radius: 0 8px 8px 0;
  font-family: 'Exo 2', sans-serif;
  font-size: 13px;
  color: rgba(232,244,248,0.8);
  margin-top: 10px;
}

/* ── BEACH FOOTER ── */
.beach-footer {
  margin-top: 60px;
  position: relative;
  text-align: center;
  padding: 60px 20px 40px;
  background: linear-gradient(180deg, transparent, rgba(245,230,200,0.15) 40%, rgba(212,169,106,0.25) 100%);
}

.footer-waves {
  margin-bottom: 20px;
}

.footer-text {
  font-family: 'Space Mono', monospace;
  font-size: 12px;
  color: rgba(212,169,106,0.8);
  letter-spacing: 3px;
  text-transform: uppercase;
}

.footer-mec {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 20px;
  letter-spacing: 5px;
  color: var(--sand-dark);
  margin: 8px 0;
}

/* ── SUCCESS MSG ── */
.success-box {
  background: linear-gradient(135deg, rgba(78,205,196,0.15), rgba(78,205,196,0.05));
  border: 1px solid var(--seafoam);
  border-radius: 14px;
  padding: 20px 28px;
  text-align: center;
  font-family: 'Exo 2', sans-serif;
  color: var(--seafoam);
  font-size: 15px;
  margin-top: 16px;
}

/* ── INFO BANNER ── */
.info-banner {
  display: flex;
  align-items: center;
  gap: 16px;
  background: rgba(255,215,0,0.08);
  border: 1px solid rgba(255,215,0,0.25);
  border-radius: 14px;
  padding: 16px 24px;
  margin-bottom: 24px;
}

.info-banner-icon { font-size: 22px; }

.info-banner-text {
  font-family: 'Exo 2', sans-serif;
  font-size: 13px;
  color: rgba(255,215,0,0.85);
  line-height: 1.6;
}

/* ── LOGGED-IN BADGE ── */
.logged-in-badge {
  background: linear-gradient(135deg, rgba(78,205,196,0.2), rgba(78,205,196,0.05));
  border: 1px solid var(--seafoam);
  color: var(--seafoam);
  padding: 8px 18px;
  border-radius: 30px;
  font-family: 'Space Mono', monospace;
  font-size: 11px;
  letter-spacing: 2px;
}

.logout-link {
  background: none;
  border: none;
  color: rgba(255,107,157,0.7);
  font-family: 'Space Mono', monospace;
  font-size: 10px;
  letter-spacing: 1px;
  cursor: pointer;
  text-decoration: underline;
  margin-left: 12px;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  BACKGROUND LAYERS (Bubbles + Sharks)
# ─────────────────────────────────────────────

SHARK_SVG = """
<svg viewBox="0 0 200 80" xmlns="http://www.w3.org/2000/svg" fill="white">
  <!-- body -->
  <ellipse cx="100" cy="45" rx="85" ry="22" />
  <!-- tail -->
  <polygon points="15,45 0,20 0,70" />
  <!-- dorsal fin -->
  <polygon points="100,23 115,5 130,23" />
  <!-- pectoral fin -->
  <polygon points="80,55 60,75 95,55" />
  <!-- mouth detail -->
  <path d="M180,45 Q190,38 195,45" stroke="rgba(0,0,0,0.5)" stroke-width="2" fill="none"/>
  <!-- eye -->
  <circle cx="175" cy="40" r="3" fill="rgba(0,0,0,0.7)"/>
</svg>
"""

st.markdown(f"""
<div class="bubbles-layer">
  {''.join(['<div class="bubble"></div>' for _ in range(15)])}
</div>
<div class="shark-layer">
  {''.join([f'<div class="shark-svg">{SHARK_SVG}</div>' for _ in range(4)])}
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  COCONUT TREES (SVG)
# ─────────────────────────────────────────────
COCONUT_SVG = """
<svg viewBox="0 0 120 280" xmlns="http://www.w3.org/2000/svg">
  <!-- trunk -->
  <path d="M55,280 Q45,220 50,170 Q48,120 58,70" stroke="#8B6914" stroke-width="10" fill="none" stroke-linecap="round"/>
  <!-- fronds -->
  <path d="M58,70 Q100,30 130,20" stroke="#2d6a2d" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M58,70 Q90,55 110,80" stroke="#2d8c2d" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M58,70 Q20,30 -10,45" stroke="#3a7c3a" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M58,70 Q30,55 10,80" stroke="#2d6a2d" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M58,70 Q60,20 55,0" stroke="#3a8c3a" stroke-width="5" fill="none" stroke-linecap="round"/>
  <!-- leaf tips -->
  <ellipse cx="130" cy="20" rx="10" ry="5" fill="#2d6a2d" transform="rotate(-20,130,20)"/>
  <ellipse cx="110" cy="80" rx="9" ry="4" fill="#2d8c2d" transform="rotate(10,110,80)"/>
  <ellipse cx="-10" cy="45" rx="10" ry="5" fill="#3a7c3a" transform="rotate(20,-10,45)"/>
  <ellipse cx="10" cy="80" rx="9" ry="4" fill="#2d6a2d" transform="rotate(-15,10,80)"/>
  <ellipse cx="55" cy="0" rx="6" ry="10" fill="#3a8c3a"/>
  <!-- coconuts -->
  <circle cx="62" cy="72" r="6" fill="#8B6914"/>
  <circle cx="54" cy="75" r="5" fill="#7a5c10"/>
</svg>
"""

st.markdown(f"""
<div class="coconut-left">{COCONUT_SVG}</div>
<div class="coconut-right">{COCONUT_SVG}</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  TOP BAR
# ─────────────────────────────────────────────
top_left, top_right = st.columns([3, 1])

with top_left:
    st.markdown('<div class="top-bar-brand">🦈 SHARKPIT — S&T CLUB MECS</div>', unsafe_allow_html=True)

with top_right:
    if st.session_state.organiser_logged_in:
        st.markdown('<div style="text-align:right;padding-top:8px;">'
                    '<span class="logged-in-badge">✓ ORGANISER</span></div>', unsafe_allow_html=True)
        if st.button("Logout", key="logout_btn"):
            st.session_state.organiser_logged_in = False
            st.rerun()
    else:
        if st.button("🔐  ORGANISER LOGIN", key="org_login_trigger"):
            st.session_state.show_login_modal = True

# ─────────────────────────────────────────────
#  ORGANISER LOGIN MODAL
# ─────────────────────────────────────────────
if st.session_state.show_login_modal and not st.session_state.organiser_logged_in:
    st.markdown("""
    <div class="glass-section" style="max-width:480px;margin:0 auto;">
      <div class="section-title" style="font-size:36px;">ORGANISER LOGIN</div>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        col_center = st.columns([1, 3, 1])[1]
        with col_center:
            u = st.text_input("Username", key="org_user", placeholder="Enter username")
            p = st.text_input("Password", type="password", key="org_pass", placeholder="Enter password")
            login_col, cancel_col = st.columns(2)
            with login_col:
                if st.button("LOGIN", key="do_login"):
                    if u == ORGANISER_USERNAME and p == ORGANISER_PASSWORD:
                        st.session_state.organiser_logged_in = True
                        st.session_state.show_login_modal = False
                        st.success("✓ Access granted. Welcome, Organiser!")
                        st.rerun()
                    else:
                        st.error("Invalid credentials. Try again.")
            with cancel_col:
                if st.button("CANCEL", key="cancel_login"):
                    st.session_state.show_login_modal = False
                    st.rerun()

# ─────────────────────────────────────────────
#  HERO
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-title">SHARKPIT</div>
  <div class="hero-subtitle">Science &amp; Technology Club &nbsp;·&nbsp; Matrusri Engineering College</div>
  <div class="hero-tagline">🦈 &nbsp; Pitch. Challenge. Win. &nbsp; 🦈</div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  ABOUT THE EVENT
# ─────────────────────────────────────────────
st.markdown("""
<div class="glass-section">
  <div class="section-title">ABOUT THE EVENT</div>

  <div class="info-banner">
    <span class="info-banner-icon">🎓</span>
    <span class="info-banner-text">
      Open to <strong>all years of B.Tech</strong> students at Matrusri Engineering College &nbsp;·&nbsp;
      Organized by the <strong>Science &amp; Technology Club</strong>
    </span>
  </div>

  <p class="body-text">
    <strong style="color:#4ecdc4;">SHARKPIT</strong> is a high-energy student startup pitch competition and ideathon
    organized by the Science &amp; Technology Club of Matrusri Engineering College (MECS). Inspired by the iconic
    format of investor pitch events, SHARKPIT challenges students to think like entrepreneurs, build
    real-world solutions, and defend their ideas in front of experienced industry founders.
    <br><br>
    Whether you're a solo visionary or a passionate team, this is your arena to transform a raw idea into
    a compelling pitch. Present your concept, tackle tough questions from our expert jury — the Sharks —
    and compete for recognition, mentorship, and bragging rights as Matrusri's boldest builders.
    <br><br>
    The event unfolds in two electrifying parts: a <strong style="color:#ff6b9d;">morning ideathon session</strong>
    open to all curious minds, and an <strong style="color:#4ecdc4;">exclusive evening finals</strong> where the
    top 20 shortlisted teams battle it out before live juries. Are you ready to take the plunge?
  </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  MEET THE SHARKS (Jury)
# ─────────────────────────────────────────────
st.markdown("""
<div class="glass-section">
  <div class="section-title">MEET THE SHARKS</div>
  <p class="body-text" style="margin-bottom:0;">
    Three visionary founders. One arena. Zero mercy.
  </p>

  <div class="sharks-grid">

    <div class="shark-card">
      <div class="shark-avatar">🦈</div>
      <div class="shark-name">E SAI ESHWAR</div>
      <div class="shark-title">Founder &amp; CEO</div>
      <div class="shark-company">Studlyf · Nirvaha Wellness<br>Techstars Facilitator</div>
      <a class="linkedin-btn"
         href="https://linkedin.com/in/esaieshwar"
         target="_blank" rel="noopener noreferrer">
        🔗 &nbsp; Visit Profile
      </a>
    </div>

    <div class="shark-card">
      <div class="shark-avatar">🌊</div>
      <div class="shark-name">YASHWANTH BONDAPALLI</div>
      <div class="shark-title">Founder</div>
      <div class="shark-company">Back2Base Community<br>AI Developer &amp; Entrepreneur</div>
      <a class="linkedin-btn"
         href="https://linkedin.com/in/yashwanth-bondapalli-37b6a7255"
         target="_blank" rel="noopener noreferrer">
        🔗 &nbsp; Visit Profile
      </a>
    </div>

    <div class="shark-card">
      <div class="shark-avatar">🛡️</div>
      <div class="shark-name">SAI HARISHITH</div>
      <div class="shark-title">Founder &amp; CEO</div>
      <div class="shark-company">Shieldnet Solutions<br>Cybersecurity Entrepreneur</div>
      <a class="linkedin-btn"
         href="https://linkedin.com/in/sai-harishith-b37558322"
         target="_blank" rel="noopener noreferrer">
        🔗 &nbsp; Visit Profile
      </a>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  REGISTRATION
# ─────────────────────────────────────────────
st.markdown("""
<div class="glass-section">
  <div class="section-title">REGISTER NOW</div>
  <p class="body-text">
    Two ways to be part of SHARKPIT 2026. Choose your session below.
  </p>

  <div class="reg-grid">

    <div class="reg-card">
      <div class="reg-badge">MORNING SESSION</div>
      <div class="reg-session-title">CASUAL MEETUP</div>
      <p class="reg-desc">
        🌅 Come listen, learn, and get inspired. The morning session is a <strong>casual, open meetup</strong>
        where all MECS students can walk in, hear from our Shark founders, and soak in the
        entrepreneurial energy. No pitching required — just curiosity and passion.
        <br><br>
        <em>Open to everyone. No approval needed.</em>
      </p>
      <a class="reg-btn morning"
         href="https://your-morning-registration-link.com"
         target="_blank" rel="noopener noreferrer">
        Register — Morning
      </a>
    </div>

    <div class="reg-card">
      <div class="reg-badge evening">EVENING SESSION</div>
      <div class="reg-session-title">PITCH FINALS</div>
      <p class="reg-desc">
        🌆 The main event. The <strong>exclusive evening finals</strong> are for teams who submitted
        their ideas and got shortlisted — the Top 20 teams pitch live before the Sharks.
        Registration requires approval. Submit your idea before March 13th to be considered.
        <br><br>
        <em>Requires idea submission &amp; approval.</em>
      </p>
      <a class="reg-btn evening"
         href="https://lu.ma/sharkpit2026"
         target="_blank" rel="noopener noreferrer">
        Register — Evening (Luma)
      </a>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  EVENT PLAN / TIMELINE
# ─────────────────────────────────────────────
st.markdown("""
<div class="glass-section">
  <div class="section-title">EVENT ROADMAP</div>
  <p class="body-text">From raw idea to the shark tank — here's how it goes.</p>

  <div class="timeline">

    <div class="timeline-item">
      <div class="timeline-content">
        <div class="timeline-date">MARCH 13, 2026</div>
        <div class="timeline-label">💡 IDEA SUBMISSION</div>
        <div class="timeline-detail">
          Submit your startup idea or innovation concept before the deadline.
          Include a brief description, problem statement, and proposed solution.
          Teams of 1–4 members are welcome.
        </div>
      </div>
      <div class="timeline-dot"></div>
      <div style="width:calc(50% - 36px);"></div>
    </div>

    <div class="timeline-item">
      <div style="width:calc(50% - 36px);"></div>
      <div class="timeline-dot"></div>
      <div class="timeline-content">
        <div class="timeline-date">MARCH 14 – 16, 2026</div>
        <div class="timeline-label">📧 SHORTLISTING</div>
        <div class="timeline-detail">
          Our panel will review all submissions and select the <strong>Top 20 teams</strong>.
          Results will be communicated <strong>via email</strong>. Keep an eye on your inbox!
        </div>
      </div>
    </div>

    <div class="timeline-item">
      <div class="timeline-content">
        <div class="timeline-date">MARCH 17, 2026</div>
        <div class="timeline-label">🦈 FINAL PITCH ROUND</div>
        <div class="timeline-detail">
          The Top 20 shortlisted teams present live before our Shark juries.
          Defend your idea, answer the hard questions, and compete for the crown!
          Morning session open to all; evening finals for shortlisted teams only.
        </div>
      </div>
      <div class="timeline-dot"></div>
      <div style="width:calc(50% - 36px);"></div>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  GUIDELINES
# ─────────────────────────────────────────────
st.markdown("""
<div class="glass-section">
  <div class="section-title">PITCH GUIDELINES</div>
  <p class="body-text">
    Follow these rules to keep the finals smooth, fair, and electric.
  </p>

  <div class="guidelines-grid">
    <div class="guideline-chip">
      <div class="guideline-icon">⏱️</div>
      <div class="guideline-text"><strong>10 minutes</strong> per team for pitching</div>
    </div>
    <div class="guideline-chip">
      <div class="guideline-icon">📊</div>
      <div class="guideline-text">PPT must be <strong>max 7 slides</strong></div>
    </div>
    <div class="guideline-chip">
      <div class="guideline-icon">👥</div>
      <div class="guideline-text">Teams of <strong>1 to 4 members</strong></div>
    </div>
    <div class="guideline-chip">
      <div class="guideline-icon">🎯</div>
      <div class="guideline-text">Focus on <strong>problem, solution &amp; impact</strong></div>
    </div>
    <div class="guideline-chip">
      <div class="guideline-icon">🏫</div>
      <div class="guideline-text">Open to <strong>all B.Tech years</strong> at MECS</div>
    </div>
    <div class="guideline-chip">
      <div class="guideline-icon">🦈</div>
      <div class="guideline-text"><strong>Top 20 teams</strong> advance to finals</div>
    </div>
    <div class="guideline-chip">
      <div class="guideline-icon">📧</div>
      <div class="guideline-text">Shortlisting notified <strong>via email</strong></div>
    </div>
    <div class="guideline-chip">
      <div class="guideline-icon">🚀</div>
      <div class="guideline-text">Original ideas only — <strong>no copying</strong></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  ASK QUERIES SECTION
# ─────────────────────────────────────────────
st.markdown("""
<div class="glass-section">
  <div class="section-title">ASK A QUERY</div>
  <p class="body-text">
    Got questions about registrations, eligibility, or the pitch format?
    Drop your query below and our organising team will get back to you!
  </p>
</div>
""", unsafe_allow_html=True)

with st.container():
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        q_name  = st.text_input("Your Name", placeholder="e.g. Ravi Kumar", key="q_name")
        q_email = st.text_input("Your Email", placeholder="e.g. ravi@mec.ac.in", key="q_email")
        q_msg   = st.text_area("Your Query", placeholder="Type your question here…",
                               height=120, key="q_msg")
        if st.button("🦈  SUBMIT QUERY", key="submit_query"):
            if q_name.strip() and q_email.strip() and q_msg.strip():
                st.session_state.queries.append({
                    "name": q_name.strip(),
                    "email": q_email.strip(),
                    "message": q_msg.strip(),
                    "reply": None
                })
                st.markdown("""
                <div class="success-box">
                  ✅ Query submitted! Our organising team will reply to you shortly.
                </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("Please fill in all fields before submitting.")

# ─────────────────────────────────────────────
#  ORGANISER DASHBOARD — REPLY TO QUERIES
# ─────────────────────────────────────────────
if st.session_state.organiser_logged_in:
    st.markdown("""
    <div class="glass-section" style="border-color:rgba(78,205,196,0.5);">
      <div class="section-title" style="font-size:40px;">🛠️ ORGANISER PANEL</div>
      <p class="body-text">Manage and reply to student queries below.</p>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.queries:
        st.info("No queries received yet.")
    else:
        for i, q in enumerate(st.session_state.queries):
            with st.expander(f"🗨️  {q['name']}  ·  {q['email']}", expanded=False):
                st.markdown(f"""
                <div class="query-card">
                  <div class="query-from">From: {q['name']} &lt;{q['email']}&gt;</div>
                  <div class="query-msg">{q['message']}</div>
                  {f'<div class="query-reply"><strong>Reply:</strong> {q["reply"]}</div>' if q["reply"] else ''}
                </div>
                """, unsafe_allow_html=True)
                reply_text = st.text_area(
                    "Write a reply",
                    value=q["reply"] or "",
                    key=f"reply_{i}",
                    height=100
                )
                if st.button("Send Reply", key=f"send_reply_{i}"):
                    st.session_state.queries[i]["reply"] = reply_text
                    st.success("Reply saved!")
                    st.rerun()

# ─────────────────────────────────────────────
#  BEACH FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div class="beach-footer">
  <!-- wave SVG -->
  <svg viewBox="0 0 1200 60" xmlns="http://www.w3.org/2000/svg"
       style="width:100%;max-height:60px;margin-bottom:24px;">
    <path d="M0,30 Q150,0 300,30 Q450,60 600,30 Q750,0 900,30 Q1050,60 1200,30 L1200,60 L0,60 Z"
          fill="rgba(212,169,106,0.3)"/>
    <path d="M0,40 Q200,10 400,40 Q600,70 800,40 Q1000,10 1200,40 L1200,60 L0,60 Z"
          fill="rgba(212,169,106,0.5)"/>
    <path d="M0,50 Q300,30 600,50 Q900,70 1200,50 L1200,60 L0,60 Z"
          fill="rgba(212,169,106,0.7)"/>
  </svg>

  <div class="footer-mec">MATRUSRI ENGINEERING COLLEGE</div>
  <div class="footer-text">Science &amp; Technology Club &nbsp;·&nbsp; SHARKPIT 2026</div>
  <div style="margin-top:12px;font-family:'Space Mono',monospace;font-size:10px;
              color:rgba(212,169,106,0.5);letter-spacing:2px;">
    PITCH · CHALLENGE · WIN
  </div>

  <!-- decorative shells -->
  <div style="font-size:22px;margin-top:18px;letter-spacing:12px;opacity:0.5;">
    🐚 🦀 🐚 🌴 🐚 🦀 🐚
  </div>
</div>
""", unsafe_allow_html=True)
