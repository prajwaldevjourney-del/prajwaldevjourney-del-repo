# -*- coding: utf-8 -*-
import streamlit as st
import urllib.parse
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orig_images import IMG_HARISHITH, IMG_ESHWAR, IMG_YASHWANTH

st.set_page_config(
    page_title="SHARKPIT 2026 - S&T Club MECS",
    page_icon="\U0001f988",
    layout="wide"
)

# ── SESSION STATE ──────────────────────────────────────────────────────────────
if "organiser_logged_in" not in st.session_state:
    st.session_state.organiser_logged_in = False
if "show_login_modal" not in st.session_state:
    st.session_state.show_login_modal = False
if "queries" not in st.session_state:
    st.session_state.queries = []

ORGANISER_USERNAME = "sharkpit_admin"
ORGANISER_PASSWORD = "MEC@2026"
CONTACT_EMAIL      = "scienceclubmecs@gmail.com"
LUMA_IDEATHON      = "https://lu.ma/34izlhhj"
LUMA_MEETUP        = "https://lu.ma/4e3p9fdx"

def render(html_str):
    lines = [l for l in html_str.split("\n") if l.strip()]
    st.markdown("\n".join(lines), unsafe_allow_html=True)

# ── CSS ────────────────────────────────────────────────────────────────────────
CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Exo+2:ital,wght@0,300;0,400;0,600;1,300;1,400;1,600&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap');
:root{
  --seafoam:#4ecdc4;--pink:#ff6b9d;--pearl:#e8f4f8;
  --deep:#010d1f;--mid:#0a2540;--bright:#0e4d7b;
  --sand:#f5e6c8;--sand-dark:#d4a96a;}

#MainMenu,footer,header,[data-testid="stHeader"],[data-testid="collapsedControl"]{display:none!important;}
[data-testid="stAppViewContainer"]{
  background:linear-gradient(180deg,#010d1f 0%,#031d38 12%,#0a3055 24%,#0e4d7b 38%,#1a7aad 55%,#a0d8ef 78%,#f5e6c8 100%)!important;
  min-height:100vh;}
[data-testid="stMain"]{background:transparent!important;}
.block-container{padding:0 1rem 4rem!important;max-width:1100px;margin:0 auto;}
@media(min-width:768px){.block-container{padding:0 2rem 4rem!important;}}

@keyframes floatBubble{
  0%{bottom:-120px;opacity:0;transform:translateX(0);}
  10%{opacity:1;}50%{opacity:0.7;transform:translateX(18px);}
  90%{opacity:0.3;}100%{bottom:110vh;opacity:0;transform:translateX(-14px);}}
@keyframes swimShark{0%{left:-400px;}100%{left:110%;}}
@keyframes gShift{0%,100%{background-position:0% 50%;}50%{background-position:100% 50%;}}
@keyframes photoPulse{
  0%,100%{box-shadow:0 0 0 3px #4ecdc4,0 0 18px rgba(78,205,196,0.4);}
  50%{box-shadow:0 0 0 5px #4ecdc4,0 0 36px rgba(78,205,196,0.7),0 0 54px rgba(255,107,157,0.25);}}
@keyframes lineGlow{
  0%,100%{opacity:0.6;box-shadow:0 0 6px #4ecdc4;}
  50%{opacity:1;box-shadow:0 0 16px #4ecdc4,0 0 30px #ff6b9d;}}
@keyframes dotPulse{
  0%,100%{transform:scale(1);box-shadow:0 0 8px #4ecdc4;}
  50%{transform:scale(1.18);box-shadow:0 0 22px #4ecdc4,0 0 38px #ff6b9d;}}
@keyframes fadeUp{from{opacity:0;transform:translateY(24px);}to{opacity:1;transform:translateY(0);}}
@keyframes slideInLeft{from{opacity:0;transform:translateX(-50px);}to{opacity:1;transform:translateX(0);}}
@keyframes slideInRight{from{opacity:0;transform:translateX(50px);}to{opacity:1;transform:translateX(0);}}
@keyframes shimmer{0%{background-position:-200% center;}100%{background-position:200% center;}}

/* BUBBLES */
.bubbles{position:fixed;width:100%;height:100vh;top:0;left:0;pointer-events:none;z-index:0;overflow:hidden;}
.b{position:absolute;border-radius:50%;
  background:radial-gradient(circle at 30% 30%,rgba(78,205,196,0.35),rgba(14,77,123,0.15));
  border:1px solid rgba(78,205,196,0.25);animation:floatBubble linear infinite;}
.sharks-bg{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0;overflow:hidden;}
.shk{position:fixed;opacity:0.07;animation:swimShark linear infinite;}
.coco-l{position:fixed;bottom:0;left:-10px;z-index:1;pointer-events:none;opacity:0.5;}
.coco-r{position:fixed;bottom:0;right:-10px;z-index:1;pointer-events:none;opacity:0.5;transform:scaleX(-1);}

/* GLASS CARD */
.gs{background:rgba(10,37,64,0.58);border:1px solid rgba(78,205,196,0.22);border-radius:24px;
  backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);
  padding:clamp(1.4rem,4vw,2.5rem) clamp(1.2rem,4vw,2.8rem);
  margin:2rem 0;position:relative;overflow:hidden;animation:fadeUp 0.8s ease both;}
.gs::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,#4ecdc4,transparent);}

.gtitle{font-family:'Bebas Neue',cursive;font-size:clamp(34px,6vw,68px);
  background:linear-gradient(120deg,#4ecdc4,#e8f4f8,#ff6b9d,#4ecdc4);
  background-size:300% 300%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;animation:gShift 5s ease infinite;margin:0 0 0.4rem 0;letter-spacing:3px;}
.gsub{font-family:'Space Mono',monospace;color:rgba(232,244,248,0.6);font-size:clamp(11px,1.5vw,13px);
  letter-spacing:2px;margin-bottom:2rem;}
.top-brand{font-family:'Space Mono',monospace;color:#4ecdc4;font-size:clamp(11px,1.8vw,17px);
  font-weight:700;letter-spacing:2px;padding:1rem 0;}
.org-badge{font-family:'Space Mono',monospace;background:rgba(78,205,196,0.15);
  border:1px solid #4ecdc4;color:#4ecdc4;border-radius:20px;padding:4px 14px;font-size:11px;letter-spacing:2px;}

/* HERO */
.hero{text-align:center;padding:clamp(3rem,7vw,5rem) 1rem clamp(2.5rem,5vw,4rem);position:relative;z-index:2;}
.hero-title{font-family:'Bebas Neue',cursive;
  font-size:clamp(80px,17vw,200px);
  background:linear-gradient(120deg,#4ecdc4,#e8f4f8,#ff6b9d,#4ecdc4);
  background-size:300% 300%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;animation:gShift 6s ease infinite;line-height:0.9;letter-spacing:8px;margin:0;}
.hero-sub{font-family:'Space Mono',monospace;color:rgba(232,244,248,0.7);
  font-size:clamp(10px,1.8vw,16px);letter-spacing:3px;margin:1.2rem 0 0.8rem;}
.hero-tag{font-family:'Exo 2',sans-serif;font-style:italic;
  font-size:clamp(14px,2.5vw,26px);color:#4ecdc4;letter-spacing:4px;margin:0;}

.info-banner{border:1px solid rgba(212,169,106,0.6);border-radius:12px;
  background:rgba(212,169,106,0.08);padding:12px 20px;font-family:'Space Mono',monospace;
  font-size:clamp(10px,1.4vw,12px);color:#f5e6c8;letter-spacing:1.5px;margin-bottom:1.4rem;}
.about-body{font-family:'Exo 2',sans-serif;font-size:clamp(13px,1.7vw,15px);
  color:rgba(232,244,248,0.85);line-height:1.9;}

/* ── SHARK CARDS ── */
.sc-grid{display:grid;grid-template-columns:1fr;gap:1.5rem;margin-top:2rem;}
@media(min-width:600px){.sc-grid{grid-template-columns:repeat(3,1fr);gap:1.8rem;}}
.sc{background:rgba(10,37,64,0.7);border:1px solid rgba(78,205,196,0.18);border-radius:20px;
  padding:clamp(1.3rem,3vw,2rem) clamp(1rem,2.5vw,1.5rem);text-align:center;
  transition:all 0.35s ease;cursor:default;position:relative;overflow:hidden;}
.sc:nth-child(1){animation:fadeUp 0.7s ease 0.1s both;}
.sc:nth-child(2){animation:fadeUp 0.7s ease 0.25s both;}
.sc:nth-child(3){animation:fadeUp 0.7s ease 0.4s both;}
.sc:hover{transform:translateY(-12px) scale(1.02);border-color:#4ecdc4;
  box-shadow:0 22px 56px rgba(78,205,196,0.28);}

/* PHOTO RING */
.photo-ring{width:clamp(90px,14vw,120px);height:clamp(90px,14vw,120px);border-radius:50%;
  background:linear-gradient(135deg,#4ecdc4,#ff6b9d);
  display:flex;align-items:center;justify-content:center;
  margin:0 auto 1rem;padding:3px;overflow:hidden;
  animation:photoPulse 3s ease-in-out infinite;}
.photo-ring img{width:100%;height:100%;object-fit:cover;object-position:center top;border-radius:50%;}

.co-badge{font-family:'Space Mono',monospace;font-size:9px;color:#4ecdc4;
  letter-spacing:1.5px;margin-bottom:0.6rem;opacity:.85;}
.sc-name{font-family:'Bebas Neue',cursive;font-size:clamp(20px,3vw,28px);
  color:#e8f4f8;letter-spacing:3px;margin:0.3rem 0;}
.sc-role{font-family:'Space Mono',monospace;font-size:9px;color:#ff6b9d;
  letter-spacing:1.5px;margin-bottom:1rem;}
.sc-bio{font-family:'Exo 2',sans-serif;font-size:clamp(12px,1.5vw,13px);
  color:rgba(232,244,248,0.78);line-height:1.75;text-align:left;margin-bottom:1rem;}
.sc-tags{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin-bottom:1.2rem;}
.sc-tag{font-family:'Space Mono',monospace;font-size:9px;background:rgba(78,205,196,0.12);
  border:1px solid rgba(78,205,196,0.3);color:#4ecdc4;border-radius:20px;
  padding:3px 10px;letter-spacing:1px;}
.li-btn{display:inline-block;font-family:'Bebas Neue',cursive;font-size:14px;letter-spacing:2px;
  background:linear-gradient(135deg,rgba(78,205,196,0.2),rgba(78,205,196,0.05));
  border:1px solid rgba(78,205,196,0.4);color:#4ecdc4;border-radius:30px;
  padding:7px 20px;text-decoration:none;transition:all 0.3s ease;}
.li-btn:hover{background:#4ecdc4;color:#010d1f;text-decoration:none;
  box-shadow:0 6px 20px rgba(78,205,196,0.5);}

/* REGISTRATION */
.reg-grid{display:grid;grid-template-columns:1fr;gap:1.5rem;margin-top:1.5rem;}
@media(min-width:580px){.reg-grid{grid-template-columns:1fr 1fr;gap:2rem;}}
.reg-card{background:rgba(10,37,64,0.75);border:1px solid rgba(78,205,196,0.18);
  border-radius:22px;padding:clamp(1.5rem,3vw,2.2rem) clamp(1.2rem,2.5vw,1.8rem);
  text-align:center;transition:all 0.3s ease;position:relative;overflow:hidden;}
.reg-card-l{animation:slideInLeft 0.7s ease 0.1s both;}
.reg-card-r{animation:slideInRight 0.7s ease 0.3s both;}
.reg-card-l:hover{transform:translateY(-8px);box-shadow:0 20px 50px rgba(255,107,157,0.22);border-color:#ff6b9d;}
.reg-card-r:hover{transform:translateY(-8px);box-shadow:0 20px 50px rgba(78,205,196,0.22);border-color:#4ecdc4;}
.reg-badge{display:inline-block;font-family:'Space Mono',monospace;font-size:9px;
  letter-spacing:3px;border-radius:20px;padding:5px 16px;margin-bottom:1.1rem;}
.rb-sf{background:#4ecdc4;color:#010d1f;}
.rb-pk{background:#ff6b9d;color:white;}
.reg-emoji{font-size:clamp(40px,6vw,54px);display:block;margin-bottom:12px;}
.reg-title{font-family:'Bebas Neue',cursive;font-size:clamp(28px,4.5vw,40px);
  color:#e8f4f8;letter-spacing:4px;margin:0.2rem 0;}
.reg-sub-sf{font-family:'Space Mono',monospace;font-size:11px;color:#4ecdc4;
  letter-spacing:3px;margin-bottom:1rem;}
.reg-sub-pk{font-family:'Space Mono',monospace;font-size:11px;color:#ff6b9d;
  letter-spacing:3px;margin-bottom:1rem;}
.reg-sep-sf{border:none;border-top:1px solid rgba(78,205,196,0.25);margin:.8rem 0;}
.reg-sep-pk{border:none;border-top:1px solid rgba(255,107,157,0.25);margin:.8rem 0;}
.reg-desc{font-family:'Exo 2',sans-serif;font-size:clamp(12px,1.5vw,14px);
  color:rgba(232,244,248,0.75);line-height:1.8;margin-bottom:1.5rem;text-align:left;}
.reg-btn-pk{display:block;width:100%;
  background:linear-gradient(135deg,#ff6b9d,#c84b8e);color:white;
  font-family:'Bebas Neue',cursive;font-size:clamp(16px,2.5vw,22px);letter-spacing:4px;
  border-radius:40px;padding:14px;text-align:center;text-decoration:none;
  box-shadow:0 8px 28px rgba(255,107,157,0.4);transition:all 0.3s ease;}
.reg-btn-pk:hover{transform:scale(1.04);box-shadow:0 12px 40px rgba(255,107,157,0.65);
  text-decoration:none;color:white;}
.reg-btn-sf{display:block;width:100%;
  background:linear-gradient(135deg,#4ecdc4,#2eafa7);color:#010d1f;
  font-family:'Bebas Neue',cursive;font-size:clamp(16px,2.5vw,22px);letter-spacing:4px;
  border-radius:40px;padding:14px;text-align:center;text-decoration:none;
  box-shadow:0 8px 28px rgba(78,205,196,0.4);transition:all 0.3s ease;}
.reg-btn-sf:hover{transform:scale(1.04);box-shadow:0 12px 40px rgba(78,205,196,0.65);
  text-decoration:none;color:#010d1f;}
.reg-divider{height:2px;border:none;
  background:linear-gradient(90deg,transparent,#4ecdc4,#ff6b9d,#4ecdc4,transparent);
  background-size:200% auto;animation:shimmer 3s linear infinite;margin:2rem 0 1rem;border-radius:2px;}
.reg-footer-note{font-family:'Space Mono',monospace;font-size:11px;
  color:rgba(232,244,248,0.4);text-align:center;letter-spacing:2px;}
.reg-instruction{font-family:'Space Mono',monospace;font-size:clamp(11px,1.6vw,14px);
  color:#4ecdc4;text-align:center;letter-spacing:2px;margin-bottom:28px;}

/* ── TIMELINE ─────────────────────────────────────────────────────────────── */
.tl-outer{position:relative;margin:2rem 0;padding:1rem 0;}

/* Central vertical spine */
.tl-spine{
  position:absolute;
  left:50%;top:0;bottom:0;
  width:2px;
  background:linear-gradient(180deg,#4ecdc4,#ff6b9d);
  transform:translateX(-50%);
  animation:lineGlow 2.5s ease-in-out infinite;}
@media(max-width:599px){
  .tl-spine{left:20px;transform:none;}}

/* Each row */
.tl-row{
  display:flex;
  align-items:flex-start;
  position:relative;
  margin-bottom:2.8rem;}

/* Dot always at spine centre */
.tl-dot{
  position:absolute;
  left:50%;top:20px;
  width:22px;height:22px;border-radius:50%;
  background:linear-gradient(135deg,#4ecdc4,#ff6b9d);
  transform:translateX(-50%);
  flex-shrink:0;z-index:2;
  animation:dotPulse 2s ease-in-out infinite;}
@media(max-width:599px){
  .tl-dot{left:20px;transform:none;top:18px;}}

/* Box occupies half-width on either side */
.tl-box{
  width:calc(50% - 32px);
  background:rgba(10,37,64,0.7);
  border:1px solid rgba(78,205,196,0.2);
  border-radius:16px;
  padding:clamp(.9rem,2.5vw,1.4rem) clamp(1rem,2.5vw,1.8rem);
  transition:all 0.3s ease;}
.tl-box:hover{border-color:#4ecdc4;transform:translateY(-3px);
  box-shadow:0 10px 30px rgba(78,205,196,0.2);}

/* LEFT row: box on left, dot in centre */
.tl-L{justify-content:flex-start;}
.tl-L .tl-box{text-align:right;margin-left:0;margin-right:auto;}

/* RIGHT row: dot in centre, box on right */
.tl-R{justify-content:flex-end;}
.tl-R .tl-box{text-align:left;margin-right:0;margin-left:auto;}

/* Mobile: all collapse left */
@media(max-width:599px){
  .tl-L,.tl-R{justify-content:flex-start;}
  .tl-L .tl-box,.tl-R .tl-box{
    width:calc(100% - 50px)!important;
    margin-left:50px!important;margin-right:0!important;
    text-align:left!important;}}

.tl-date{font-family:'Space Mono',monospace;font-size:10px;color:#4ecdc4;
  letter-spacing:3px;margin-bottom:.4rem;}
.tl-label{font-family:'Bebas Neue',cursive;font-size:clamp(16px,2.5vw,22px);
  color:#e8f4f8;letter-spacing:2px;margin-bottom:.5rem;}
.tl-detail{font-family:'Exo 2',sans-serif;font-size:clamp(12px,1.5vw,13.5px);
  color:rgba(232,244,248,0.75);line-height:1.7;}

.tl-row:nth-child(1){animation:fadeUp 0.7s ease 0.1s both;}
.tl-row:nth-child(2){animation:fadeUp 0.7s ease 0.3s both;}
.tl-row:nth-child(3){animation:fadeUp 0.7s ease 0.5s both;}
.tl-row:nth-child(4){animation:fadeUp 0.7s ease 0.7s both;}
/* ─────────────────────────────────────────────────────────────────────────── */

/* GUIDELINES */
.gg{display:grid;grid-template-columns:repeat(2,1fr);gap:1rem;margin-top:1.5rem;}
@media(min-width:768px){.gg{grid-template-columns:repeat(4,1fr);}}
.gc{background:rgba(10,37,64,0.65);border:1px solid rgba(78,205,196,0.18);
  border-radius:14px;padding:1.1rem 1rem;transition:all 0.3s ease;
  font-family:'Exo 2',sans-serif;font-size:clamp(12px,1.5vw,13.5px);
  color:#e8f4f8;display:flex;gap:10px;align-items:flex-start;}
.gc:hover{border-color:#4ecdc4;transform:translateY(-4px);
  box-shadow:0 8px 24px rgba(78,205,196,0.2);}
.gicon{font-size:20px;flex-shrink:0;}

/* FORM */
.stTextInput>div>div>input,.stTextArea>div>div>textarea{
  background:rgba(1,13,31,0.85)!important;border:1px solid rgba(78,205,196,0.4)!important;
  border-radius:10px!important;color:#e8f4f8!important;
  font-family:'Exo 2',sans-serif!important;font-size:14px!important;}
.stTextInput>div>div>input:focus,.stTextArea>div>div>textarea:focus{
  border-color:#4ecdc4!important;box-shadow:0 0 0 2px rgba(78,205,196,0.2)!important;}
label[data-baseweb="label"],.stTextInput label,.stTextArea label{
  font-family:'Space Mono',monospace!important;font-size:11px!important;
  color:#4ecdc4!important;letter-spacing:2px!important;}
.stButton>button{
  font-family:'Bebas Neue',cursive!important;font-size:18px!important;
  letter-spacing:4px!important;
  background:linear-gradient(135deg,#4ecdc4,#2eafa7)!important;
  color:#010d1f!important;border:none!important;border-radius:30px!important;
  padding:10px 36px!important;transition:all 0.3s ease!important;width:100%!important;}
.stButton>button:hover{transform:scale(1.04)!important;
  box-shadow:0 8px 24px rgba(78,205,196,0.45)!important;}
.success-box{border:1px solid #4ecdc4;border-radius:12px;
  background:rgba(78,205,196,0.08);padding:14px 20px;
  font-family:'Space Mono',monospace;font-size:12px;color:#4ecdc4;
  letter-spacing:1.5px;margin-top:1rem;}
.success-box a{color:#ff6b9d;}

/* Q&A */
.qt{position:relative;padding:1rem 0 1rem 52px;margin-top:1.5rem;}
.qt::before{content:'';position:absolute;left:22px;top:0;bottom:0;width:2px;
  background:linear-gradient(180deg,#4ecdc4,#ff6b9d);animation:lineGlow 2.5s ease-in-out infinite;}
.qt-item{display:flex;align-items:flex-start;gap:18px;margin-bottom:2rem;
  position:relative;animation:fadeUp 0.6s ease both;}
.qt-dot{width:18px;height:18px;border-radius:50%;
  background:linear-gradient(135deg,#4ecdc4,#ff6b9d);
  flex-shrink:0;margin-top:4px;position:absolute;left:-40px;
  animation:dotPulse 2s ease-in-out infinite;}
.qt-card{background:rgba(10,37,64,0.65);border:1px solid rgba(78,205,196,0.18);
  border-radius:14px;padding:1.2rem 1.5rem;flex:1;}
.qt-name{font-family:'Space Mono',monospace;font-size:11px;color:#4ecdc4;
  letter-spacing:2px;margin-bottom:.5rem;}
.qt-question{font-family:'Exo 2',sans-serif;font-size:14px;color:#e8f4f8;
  margin-bottom:.8rem;line-height:1.6;}
.qt-reply{border-left:3px solid #4ecdc4;padding-left:12px;
  font-family:'Exo 2',sans-serif;font-size:13px;
  color:rgba(232,244,248,0.8);font-style:italic;line-height:1.6;}

/* LOGIN */
.login-wrap{background:rgba(10,37,64,0.85);border:1px solid rgba(78,205,196,0.3);
  border-radius:20px;padding:2rem 2.5rem;margin:1rem 0 2rem;}
.login-title{font-family:'Bebas Neue',cursive;font-size:30px;color:#4ecdc4;
  letter-spacing:4px;margin-bottom:1.2rem;}

/* FOOTER */
.beach-footer{
  background:linear-gradient(180deg,transparent,rgba(245,230,200,0.12),rgba(212,169,106,0.22));
  border-top:1px solid rgba(212,169,106,0.3);text-align:center;
  padding:0 1rem 2rem;margin-top:3rem;position:relative;}
.footer-wave{width:100%;margin-bottom:1.5rem;}
.footer-college{font-family:'Bebas Neue',cursive;font-size:clamp(18px,4vw,42px);
  color:#d4a96a;letter-spacing:5px;margin:0;}
.footer-club{font-family:'Space Mono',monospace;font-size:12px;
  color:rgba(212,169,106,0.7);letter-spacing:3px;margin:.3rem 0;}
.footer-tagline{font-family:'Space Mono',monospace;font-size:9px;
  color:rgba(212,169,106,0.4);letter-spacing:4px;margin:.2rem 0 1rem;}
.footer-emoji{font-size:18px;letter-spacing:8px;margin-top:.5rem;}

[data-testid="stHorizontalBlock"]{gap:.5rem!important;}
</style>"""

st.markdown(CSS, unsafe_allow_html=True)

# ── BACKGROUND SVGs ────────────────────────────────────────────────────────────
SHARK = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 120'>"
         "<ellipse cx='155' cy='62' rx='140' ry='42' fill='none' stroke='white' stroke-width='2.5'/>"
         "<polygon points='295,62 320,40 320,84' fill='none' stroke='white' stroke-width='2'/>"
         "<polygon points='155,20 135,4 175,4' fill='none' stroke='white' stroke-width='2'/>"
         "<path d='M110,66 Q95,90 70,100 Q100,78 105,66' fill='none' stroke='white' stroke-width='2'/>"
         "<circle cx='240' cy='54' r='4' fill='white' opacity='0.7'/></svg>")
COCO = ("<svg xmlns='http://www.w3.org/2000/svg' width='120' height='280' viewBox='0 0 120 280'>"
        "<path d='M60,280 Q55,200 50,150 Q45,100 65,40' fill='none' stroke='#8B6914' stroke-width='10' stroke-linecap='round'/>"
        "<path d='M65,40 Q20,20 0,50' fill='none' stroke='#2d7a2d' stroke-width='6' stroke-linecap='round'/>"
        "<path d='M65,40 Q100,10 115,45' fill='none' stroke='#2d7a2d' stroke-width='6' stroke-linecap='round'/>"
        "<path d='M65,40 Q40,55 30,80' fill='none' stroke='#3a9a3a' stroke-width='5' stroke-linecap='round'/>"
        "<path d='M65,40 Q90,60 100,82' fill='none' stroke='#3a9a3a' stroke-width='5' stroke-linecap='round'/>"
        "<path d='M65,40 Q65,65 60,90' fill='none' stroke='#4ab54a' stroke-width='5' stroke-linecap='round'/>"
        "<circle cx='55' cy='50' r='7' fill='#7a4f00'/>"
        "<circle cx='75' cy='46' r='6' fill='#7a4f00'/>"
        "<circle cx='63' cy='58' r='6' fill='#7a4f00'/></svg>")

render(
    "<div class='bubbles'>"
    "<div class='b' style='width:8px;height:8px;left:5%;animation-duration:12s;animation-delay:0s;bottom:-120px;'></div>"
    "<div class='b' style='width:14px;height:14px;left:12%;animation-duration:16s;animation-delay:1.5s;bottom:-120px;'></div>"
    "<div class='b' style='width:6px;height:6px;left:20%;animation-duration:10s;animation-delay:3s;bottom:-120px;'></div>"
    "<div class='b' style='width:22px;height:22px;left:28%;animation-duration:18s;animation-delay:0.8s;bottom:-120px;'></div>"
    "<div class='b' style='width:10px;height:10px;left:35%;animation-duration:14s;animation-delay:2s;bottom:-120px;'></div>"
    "<div class='b' style='width:18px;height:18px;left:43%;animation-duration:20s;animation-delay:4s;bottom:-120px;'></div>"
    "<div class='b' style='width:7px;height:7px;left:52%;animation-duration:11s;animation-delay:1s;bottom:-120px;'></div>"
    "<div class='b' style='width:30px;height:30px;left:60%;animation-duration:22s;animation-delay:2.5s;bottom:-120px;'></div>"
    "<div class='b' style='width:12px;height:12px;left:68%;animation-duration:15s;animation-delay:0.3s;bottom:-120px;'></div>"
    "<div class='b' style='width:40px;height:40px;left:75%;animation-duration:19s;animation-delay:3.5s;bottom:-120px;'></div>"
    "<div class='b' style='width:9px;height:9px;left:82%;animation-duration:13s;animation-delay:1.2s;bottom:-120px;'></div>"
    "<div class='b' style='width:16px;height:16px;left:88%;animation-duration:17s;animation-delay:0.6s;bottom:-120px;'></div>"
    "<div class='b' style='width:25px;height:25px;left:93%;animation-duration:21s;animation-delay:4.5s;bottom:-120px;'></div>"
    "<div class='b' style='width:11px;height:11px;left:8%;animation-duration:9s;animation-delay:2.8s;bottom:-120px;'></div>"
    "<div class='b' style='width:20px;height:20px;left:48%;animation-duration:16s;animation-delay:5s;bottom:-120px;'></div>"
    "</div>"
    "<div class='sharks-bg'>"
    f"<div class='shk' style='top:15%;width:280px;animation-duration:28s;animation-delay:0s;'>{SHARK}</div>"
    f"<div class='shk' style='top:35%;width:200px;animation-duration:22s;animation-delay:6s;transform:scaleX(-1);'>{SHARK}</div>"
    f"<div class='shk' style='top:55%;width:340px;animation-duration:34s;animation-delay:12s;'>{SHARK}</div>"
    f"<div class='shk' style='top:72%;width:160px;animation-duration:20s;animation-delay:4s;transform:scaleX(-1);'>{SHARK}</div>"
    "</div>"
    f"<div class='coco-l'>{COCO}</div>"
    f"<div class='coco-r'>{COCO}</div>"
)

# ── TOP BAR ───────────────────────────────────────────────────────────────────
col_l, col_r = st.columns([3, 1])
with col_l:
    render("<div class='top-brand'>\U0001f988 SHARKPIT 2026 &mdash; S&amp;T CLUB MECS</div>")
with col_r:
    if not st.session_state.organiser_logged_in:
        if st.button("\U0001f510 ORGANISER LOGIN"):
            st.session_state.show_login_modal = True
            st.rerun()
    else:
        render("<span class='org-badge'>&#10003; ORGANISER</span>")
        if st.button("Logout"):
            st.session_state.organiser_logged_in = False
            st.session_state.show_login_modal = False
            st.rerun()

# ── LOGIN MODAL ────────────────────────────────────────────────────────────────
if st.session_state.show_login_modal and not st.session_state.organiser_logged_in:
    render("<div class='login-wrap'><div class='login-title'>\U0001f510 ORGANISER LOGIN</div></div>")
    _, lc2, _ = st.columns([1, 2, 1])
    with lc2:
        uname = st.text_input("Username", key="login_user", placeholder="sharkpit_admin")
        upass = st.text_input("Password", type="password", key="login_pass")
        b1, b2 = st.columns(2)
        with b1:
            if st.button("LOGIN"):
                if uname == ORGANISER_USERNAME and upass == ORGANISER_PASSWORD:
                    st.session_state.organiser_logged_in = True
                    st.session_state.show_login_modal = False
                    st.rerun()
                else:
                    st.error("Invalid credentials.")
        with b2:
            if st.button("CANCEL"):
                st.session_state.show_login_modal = False
                st.rerun()

# ── HERO ──────────────────────────────────────────────────────────────────────
render(
    "<div class='hero'>"
    "<div class='hero-title'>SHARKPIT</div>"
    "<div class='hero-sub'>Science &amp; Technology Club &nbsp;&middot;&nbsp; Matrusri Engineering College</div>"
    "<div class='hero-tag'>\U0001f988 Pitch. Challenge. Win. \U0001f988</div>"
    "</div>"
)

# ── ABOUT ──────────────────────────────────────────────────────────────────────
render(
    "<div class='gs'>"
    "<div class='gtitle'>ABOUT THE EVENT</div>"
    "<div class='info-banner'>Open to all years of B.Tech at Matrusri Engineering College &nbsp;&middot;&nbsp; Organised by the Science &amp; Technology Club</div>"
    "<div class='about-body'>SHARKPIT is a high-energy student startup pitch competition and ideathon organized by the S&amp;T Club of MECS. Inspired by investor pitch formats, it challenges students to think like entrepreneurs and defend their ideas before experienced industry founders &mdash; the Sharks. The event has two parts: a morning casual meetup open to all students, and exclusive evening finals where the top 20 shortlisted teams pitch live before the Sharks.</div>"
    "</div>"
)

# ── MEET THE SHARKS ────────────────────────────────────────────────────────────
# Image 1 = Sai Harishith (white shirt, glasses) → IMG_HARISHITH
# Image 2 = E Sai Eshwar  (navy suit, on stage)  → IMG_ESHWAR
# Image 3 = Yashwanth     (Back to Base event)    → IMG_YASHWANTH
render(
    "<div class='gs'>"
    "<div class='gtitle'>MEET THE SHARKS</div>"
    "<div class='gsub'>Three visionary founders. One arena. Zero mercy on weak pitches.</div>"
    "<div class='sc-grid'>"

    # Card 1 — E Sai Eshwar
    "<div class='sc'>"
    f"<div class='photo-ring'><img src='data:image/jpeg;base64,{IMG_ESHWAR}' alt='E Sai Eshwar'/></div>"
    "<div class='co-badge'>\U0001f680 Studlyf &middot; Nirvaha &middot; GuideBazaar</div>"
    "<div class='sc-name'>E SAI ESHWAR</div>"
    "<div class='sc-role'>Ecosystem &amp; Product Operator &middot; Founder</div>"
    "<div class='sc-bio'>Operates at the intersection of Applied AI, strategy, and social impact. Co-founded Studlyf &mdash; a student ecosystem platform &mdash; and Nirvaha, an AI wellness platform. 12x national hackathon finalist, mentors 600+ students, and has delivered 10+ public speaking sessions on AI &amp; entrepreneurship.</div>"
    "<div class='sc-tags'>"
    "<span class='sc-tag'>Applied AI</span>"
    "<span class='sc-tag'>Product Strategy</span>"
    "<span class='sc-tag'>Ecosystem</span>"
    "<span class='sc-tag'>Mentorship</span>"
    "</div>"
    "<a class='li-btn' href='https://linkedin.com/in/esaieshwar' target='_blank'>\U0001f517 LinkedIn</a>"
    "</div>"

    # Card 2 — Yashwanth Bondapalli
    "<div class='sc'>"
    f"<div class='photo-ring'><img src='data:image/jpeg;base64,{IMG_YASHWANTH}' alt='Yashwanth Bondapalli'/></div>"
    "<div class='co-badge'>&#9889; Back to Base XYZ</div>"
    "<div class='sc-name'>YASHWANTH BONDAPALLI</div>"
    "<div class='sc-role'>AI &amp; Cybersecurity Professional &middot; Founder</div>"
    "<div class='sc-bio'>Works at the intersection of Artificial Intelligence and Cybersecurity, building production-grade LLM and RAG systems. Speaker at GitTogether Hyderabad &mdash; organised by GitHub India and supported by Microsoft. Combines AI expertise with a security-first mindset in every system he builds.</div>"
    "<div class='sc-tags'>"
    "<span class='sc-tag'>AI / LLMs</span>"
    "<span class='sc-tag'>RAG Systems</span>"
    "<span class='sc-tag'>Cybersecurity</span>"
    "<span class='sc-tag'>Open Source</span>"
    "</div>"
    "<a class='li-btn' href='https://linkedin.com/in/yashwanth-bondapalli-37b6a7255' target='_blank'>\U0001f517 LinkedIn</a>"
    "</div>"

    # Card 3 — Sai Harishith
    "<div class='sc'>"
    f"<div class='photo-ring'><img src='data:image/jpeg;base64,{IMG_HARISHITH}' alt='Sai Harishith'/></div>"
    "<div class='co-badge'>\U0001f6e1\ufe0f ShieldNet Solutions</div>"
    "<div class='sc-name'>SAI HARISHITH</div>"
    "<div class='sc-role'>Founder &amp; Director &middot; ShieldNet Solutions</div>"
    "<div class='sc-bio'>Built ShieldNet Solutions from the ground up into a full-service tech company delivering cybersecurity, web &amp; mobile development, and network administration. Leads with a security-first approach. Actively offers student internship programmes across Hyderabad engineering colleges.</div>"
    "<div class='sc-tags'>"
    "<span class='sc-tag'>Cybersecurity</span>"
    "<span class='sc-tag'>Web &amp; Mobile</span>"
    "<span class='sc-tag'>Network Admin</span>"
    "<span class='sc-tag'>Pen Testing</span>"
    "</div>"
    "<a class='li-btn' href='https://linkedin.com/in/sai-harishith-b37558322' target='_blank'>\U0001f517 LinkedIn</a>"
    "</div>"

    "</div></div>"
)

# ── REGISTER NOW ───────────────────────────────────────────────────────────────
render(
    "<div class='gs'>"
    "<div class='gtitle'>REGISTER NOW</div>"
    "<div class='reg-instruction'>Click on the following links to register for your preferred session</div>"
    "<div class='reg-grid'>"

    # Ideathon card (pink)
    "<div class='reg-card reg-card-l'>"
    "<span class='reg-badge rb-sf'>IDEATHON REGISTRATION</span>"
    "<span class='reg-emoji'>\U0001f988</span>"
    "<div class='reg-title'>IDEATHON</div>"
    "<div class='reg-sub-sf'>Evening Pitch Finals</div>"
    "<hr class='reg-sep-sf'/>"
    "<div class='reg-desc'>Register through Luma to compete in the SHARKPIT ideathon. Submit your startup idea and pitch live before our Shark jury on March 17th. Requires idea submission before March 13th and approval via email. Top 20 teams shortlisted.</div>"
    f"<a class='reg-btn-pk' href='{LUMA_IDEATHON}' target='_blank'>REGISTER FOR SESSION \U0001f517</a>"
    "</div>"

    # Open Meetup card (seafoam)
    "<div class='reg-card reg-card-r'>"
    "<span class='reg-badge rb-pk'>OPEN MEETUP REGISTRATION</span>"
    "<span class='reg-emoji'>\U0001f305</span>"
    "<div class='reg-title'>OPEN MEETUP</div>"
    "<div class='reg-sub-pk'>Morning Casual Session</div>"
    "<hr class='reg-sep-pk'/>"
    "<div class='reg-desc'>Register through Luma to attend the morning casual session. Come listen to our Shark founders speak, get inspired, and soak in the entrepreneurial energy. Open to every MECS student &mdash; no idea submission or approval needed.</div>"
    f"<a class='reg-btn-sf' href='{LUMA_MEETUP}' target='_blank'>REGISTER FOR SESSION \U0001f517</a>"
    "</div>"

    "</div>"
    "<hr class='reg-divider'/>"
    "<div class='reg-footer-note'>Both sessions are on March 17, 2026 &nbsp;&middot;&nbsp; Matrusri Engineering College</div>"
    "</div>"
)

# ── EVENT ROADMAP (alternating L / R, spine centred) ──────────────────────────
render(
    "<div class='gs'>"
    "<div class='gtitle'>EVENT ROADMAP</div>"
    "<div class='gsub'>From raw idea to the shark tank &mdash; here&#x27;s the journey.</div>"

    "<div class='tl-outer'>"
    "<div class='tl-spine'></div>"

    # Row 1 — LEFT
    "<div class='tl-row tl-L'>"
    "<div class='tl-box'>"
    "<div class='tl-date'>MARCH 13, 2026</div>"
    "<div class='tl-label'>\U0001f4a1 IDEA SUBMISSION DEADLINE</div>"
    "<div class='tl-detail'>Submit your startup idea before the cutoff. Include a problem statement, proposed solution, and team details. Teams of 1&ndash;4 MECS B.Tech students.</div>"
    "</div>"
    "<div class='tl-dot'></div>"
    "</div>"

    # Row 2 — RIGHT
    "<div class='tl-row tl-R'>"
    "<div class='tl-dot'></div>"
    "<div class='tl-box'>"
    "<div class='tl-date'>MARCH 14 &ndash; 16, 2026</div>"
    "<div class='tl-label'>\U0001f4e7 SHORTLISTING VIA EMAIL</div>"
    "<div class='tl-detail'>Our panel reviews all submissions and selects the Top 20 teams. Results communicated exclusively via email &mdash; keep an eye on your inbox!</div>"
    "</div>"
    "</div>"

    # Row 3 — LEFT
    "<div class='tl-row tl-L'>"
    "<div class='tl-box'>"
    "<div class='tl-date'>MARCH 17, 2026 &mdash; MORNING</div>"
    "<div class='tl-label'>\U0001f305 OPEN MEETUP SESSION</div>"
    "<div class='tl-detail'>All MECS students attend. Listen to Shark founders speak, get inspired, and network with fellow students and mentors.</div>"
    "</div>"
    "<div class='tl-dot'></div>"
    "</div>"

    # Row 4 — RIGHT (last item)
    "<div class='tl-row tl-R'>"
    "<div class='tl-dot'></div>"
    "<div class='tl-box'>"
    "<div class='tl-date'>MARCH 17, 2026 &mdash; EVENING</div>"
    "<div class='tl-label'>\U0001f988 FINAL PITCH ROUND</div>"
    "<div class='tl-detail'>Top 20 shortlisted teams pitch live before the Sharks. Defend your idea. Claim your crown. Jury interaction &amp; exclusive finals.</div>"
    "</div>"
    "</div>"

    "</div>"  # tl-outer
    "</div>"  # gs
)

# ── PITCH GUIDELINES ───────────────────────────────────────────────────────────
render(
    "<div class='gs'>"
    "<div class='gtitle'>PITCH GUIDELINES</div>"
    "<div class='gsub'>Follow these rules. The Sharks are watching every second.</div>"
    "<div class='gg'>"
    "<div class='gc'><span class='gicon'>&#9201;</span><span>10 minutes per team for pitching</span></div>"
    "<div class='gc'><span class='gicon'>&#128202;</span><span>PPT must be max 7 slides</span></div>"
    "<div class='gc'><span class='gicon'>&#128101;</span><span>Teams of 1 to 4 members</span></div>"
    "<div class='gc'><span class='gicon'>&#127919;</span><span>Cover problem, solution &amp; impact</span></div>"
    "<div class='gc'><span class='gicon'>&#127979;</span><span>Open to all B.Tech years at MECS</span></div>"
    "<div class='gc'><span class='gicon'>\U0001f988</span><span>Top 20 teams advance to finals</span></div>"
    "<div class='gc'><span class='gicon'>&#128231;</span><span>Shortlisting notified via email</span></div>"
    "<div class='gc'><span class='gicon'>\U0001f680</span><span>Original ideas only &mdash; no copying</span></div>"
    "</div>"
    "</div>"
)

# ── ASK A QUERY → mailto ───────────────────────────────────────────────────────
render(
    "<div class='gs'>"
    "<div class='gtitle'>ASK A QUERY</div>"
    "<div class='gsub'>Have a question about SHARKPIT 2026? Fill the form below &mdash; it opens your email app pre-filled and ready to send.</div>"
    "</div>"
)
_, qcol, _ = st.columns([1, 4, 1])
with qcol:
    q_name  = st.text_input("Your Name",  key="q_name",  placeholder="e.g. Ravi Kumar")
    q_email = st.text_input("Your Email", key="q_email", placeholder="e.g. ravi@student.mecs.edu")
    q_msg   = st.text_area("Your Query",  key="q_msg",   height=110, placeholder="Type your question here...")
    if st.button("\U0001f988 SUBMIT QUERY"):
        if q_name.strip() and q_email.strip() and q_msg.strip():
            subj   = urllib.parse.quote(f"SHARKPIT 2026 Query from {q_name.strip()}")
            body   = urllib.parse.quote(
                f"Name: {q_name.strip()}\nEmail: {q_email.strip()}\n\nQuery:\n{q_msg.strip()}"
            )
            mailto = f"mailto:{CONTACT_EMAIL}?subject={subj}&body={body}"
            st.session_state.queries.append({
                "name": q_name.strip(),
                "email": q_email.strip(),
                "message": q_msg.strip(),
                "reply": None
            })
            render(
                f"<div class='success-box'>"
                f"&#10003; &nbsp; Query ready! &nbsp;"
                f"<a href='{mailto}' target='_blank'>Click here to open your email app and send it</a>"
                f" &mdash; addressed to {CONTACT_EMAIL}."
                f"</div>"
            )
        else:
            st.warning("Please fill in all fields before submitting.")

# ── PUBLIC Q&A ─────────────────────────────────────────────────────────────────
replied = [q for q in st.session_state.queries if q["reply"] is not None]
if replied:
    items_html = ""
    for i, q in enumerate(replied):
        delay = round(0.1 + i * 0.15, 2)
        items_html += (
            f"<div class='qt-item' style='animation-delay:{delay}s;'>"
            "<div class='qt-dot'></div>"
            "<div class='qt-card'>"
            f"<div class='qt-name'>— {q['name']}</div>"
            f"<div class='qt-question'>{q['message']}</div>"
            "<div class='qt-reply'>"
            "<strong style='color:#4ecdc4;font-family:Space Mono,monospace;font-size:10px;letter-spacing:2px;'>ORGANISER REPLY</strong><br/>"
            f"{q['reply']}"
            "</div>"
            "</div></div>"
        )
    render(
        "<div class='gs'>"
        "<div class='gtitle'>Q &amp; A</div>"
        "<div class='qt'>" + items_html + "</div>"
        "</div>"
    )

# ── ORGANISER PANEL ───────────────────────────────────────────────────────────
if st.session_state.organiser_logged_in:
    render(
        "<div class='gs'>"
        "<div class='gtitle'>\U0001f6e0\ufe0f ORGANISER PANEL</div>"
        "<div class='gsub'>Manage student queries and post public replies.</div>"
        "</div>"
    )
    if not st.session_state.queries:
        st.info("No queries received yet.")
    else:
        for idx, q in enumerate(st.session_state.queries):
            with st.expander(f"{q['name']}  |  {q['email']}"):
                st.markdown(
                    "<div style='font-family:Exo 2,sans-serif;font-size:14px;"
                    f"color:#e8f4f8;margin-bottom:.8rem;'>{q['message']}</div>",
                    unsafe_allow_html=True
                )
                if q["reply"]:
                    st.markdown(
                        "<div style='border-left:3px solid #4ecdc4;padding-left:12px;"
                        "font-family:Exo 2,sans-serif;font-size:13px;"
                        f"color:rgba(232,244,248,0.8);font-style:italic;'>{q['reply']}</div>",
                        unsafe_allow_html=True
                    )
                reply_text = st.text_area(
                    "Write / Edit Reply",
                    value=q["reply"] if q["reply"] else "",
                    key=f"reply_{idx}",
                    height=90
                )
                if st.button("Send Reply", key=f"send_{idx}"):
                    st.session_state.queries[idx]["reply"] = reply_text.strip()
                    st.rerun()

# ── FOOTER ─────────────────────────────────────────────────────────────────────
render(
    "<div class='beach-footer'>"
    "<svg class='footer-wave' viewBox='0 0 1440 80' xmlns='http://www.w3.org/2000/svg' preserveAspectRatio='none'>"
    "<path d='M0,40 Q180,10 360,40 Q540,70 720,40 Q900,10 1080,40 Q1260,70 1440,40 L1440,80 L0,80 Z' fill='rgba(212,169,106,0.15)'/>"
    "<path d='M0,50 Q200,20 400,50 Q600,80 800,50 Q1000,20 1200,50 Q1320,65 1440,50 L1440,80 L0,80 Z' fill='rgba(212,169,106,0.3)'/>"
    "<path d='M0,60 Q160,40 320,60 Q480,80 640,60 Q800,40 960,60 Q1120,80 1280,60 Q1380,50 1440,60 L1440,80 L0,80 Z' fill='rgba(212,169,106,0.5)'/>"
    "</svg>"
    "<div class='footer-college'>MATRUSRI ENGINEERING COLLEGE</div>"
    "<div class='footer-club'>Science &amp; Technology Club &nbsp;&middot;&nbsp; SHARKPIT 2026</div>"
    "<div class='footer-tagline'>PITCH &middot; CHALLENGE &middot; WIN</div>"
    "<div class='footer-emoji'>\U0001f41a \U0001f980 \U0001f41a \U0001f334 \U0001f41a \U0001f980 \U0001f41a</div>"
    "</div>"
)
