# -*- coding: utf-8 -*-
import streamlit as st
import urllib.parse
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sp_images import IMG_HARISHITH, IMG_ESHWAR, IMG_YASHWANTH

st.set_page_config(
    page_title="SHARKPIT 2026 - S&T Club MECS",
    page_icon="\U0001f988",
    layout="wide"
)

if "queries" not in st.session_state:
    st.session_state.queries = []

CONTACT_EMAIL = "scienceclubmecs@gmail.com"
LUMA_IDEATHON = "https://lu.ma/34izlhhj"
LUMA_MEETUP   = "https://lu.ma/4e3p9fdx"

def render(html_str):
    lines = [l for l in html_str.split("\n") if l.strip()]
    st.markdown("\n".join(lines), unsafe_allow_html=True)

CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Inter:wght@300;400;500;600&display=swap');

*{box-sizing:border-box;margin:0;padding:0;}
:root{
  --p:#38BDF8;--s:#A78BFA;--ac:#F472B6;--cy:#22D3EE;
  --bg:#020617;--tx:#E2E8F0;--txm:rgba(226,232,240,0.62);
  --gl:rgba(255,255,255,0.04);--gb:rgba(255,255,255,0.09);--r:16px;}

#MainMenu,footer,header,[data-testid="stHeader"],[data-testid="collapsedControl"]{display:none!important;}
[data-testid="stAppViewContainer"]{background:var(--bg)!important;min-height:100vh;}
[data-testid="stMain"]{background:transparent!important;}
.block-container{padding:0 1rem 5rem!important;max-width:1100px;margin:0 auto;}
@media(min-width:768px){.block-container{padding:0 2.5rem 5rem!important;}}

[data-testid="stAppViewContainer"]::before{
  content:'';position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none;
  background:
    radial-gradient(ellipse 80% 55% at 15% 0%,rgba(56,189,248,0.13) 0%,transparent 60%),
    radial-gradient(ellipse 60% 45% at 85% 15%,rgba(167,139,250,0.11) 0%,transparent 55%),
    radial-gradient(ellipse 50% 40% at 50% 100%,rgba(34,211,238,0.08) 0%,transparent 60%);}

@keyframes gS{0%,100%{background-position:0% 50%;}50%{background-position:100% 50%;}}
@keyframes fU{from{opacity:0;transform:translateY(22px);}to{opacity:1;transform:translateY(0);}}
@keyframes flt{0%,100%{transform:translateY(0);}50%{transform:translateY(-15px);}}
@keyframes bR{0%{bottom:-80px;opacity:0;}10%{opacity:0.28;}85%{opacity:0.1;}100%{bottom:105vh;opacity:0;}}
@keyframes sL{0%{left:105%;}100%{left:-25%;}}
@keyframes sR{0%{left:-25%;}100%{left:105%;}}
@keyframes pd{0%,100%{opacity:.7;transform:translateX(-50%) scale(1);}50%{opacity:1;transform:translateX(-50%) scale(1.35);}}

.bbl-wrap{position:fixed;width:100%;height:100vh;top:0;left:0;pointer-events:none;z-index:0;overflow:hidden;}
.bbl{position:absolute;border-radius:50%;
  background:radial-gradient(circle at 35% 35%,rgba(56,189,248,0.22),rgba(14,165,233,0.03));
  border:1px solid rgba(56,189,248,0.11);animation:bR linear infinite;}
.shk-wrap{position:fixed;width:100%;height:100%;top:0;left:0;pointer-events:none;z-index:0;overflow:hidden;}
.shk{position:absolute;opacity:0.033;}
.shk-l{animation:sL linear infinite;}
.shk-r{animation:sR linear infinite;}

.sp-sec{background:var(--gl);border:1px solid var(--gb);border-radius:var(--r);
  backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);
  padding:clamp(1.4rem,4vw,2.6rem) clamp(1.2rem,4vw,2.4rem);
  margin:1.5rem 0;position:relative;overflow:hidden;animation:fU .7s ease both;z-index:1;
  transition:border-color .3s,box-shadow .3s;}
.sp-sec::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,var(--p),var(--s),transparent);opacity:0.4;}

.sp-lbl{font-family:'Orbitron',sans-serif;font-size:clamp(9px,1.5vw,11px);font-weight:600;
  letter-spacing:4px;color:var(--p);text-transform:uppercase;margin-bottom:.4rem;opacity:.8;}
.sp-ttl{font-family:'Orbitron',sans-serif;font-weight:900;font-size:clamp(22px,5vw,44px);
  letter-spacing:2px;
  background:linear-gradient(90deg,var(--cy),var(--p),var(--s),var(--ac),var(--cy));
  background-size:300% 300%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;animation:gS 6s ease infinite;margin-bottom:.7rem;line-height:1.2;}
.sp-bod{font-family:'Inter',sans-serif;font-size:clamp(13px,1.9vw,15px);color:var(--txm);line-height:1.85;}

.top-bar{font-family:'Orbitron',sans-serif;font-size:clamp(9px,1.4vw,11px);font-weight:600;
  letter-spacing:3px;color:var(--p);padding:.8rem 0;opacity:.72;position:relative;z-index:1;}

.hw{text-align:center;padding:clamp(2.5rem,7vw,5.5rem) 1rem clamp(2rem,5vw,4rem);position:relative;z-index:1;}
.h-eye{font-family:'Inter',sans-serif;font-size:clamp(10px,1.7vw,12px);font-weight:500;
  letter-spacing:5px;color:var(--p);text-transform:uppercase;margin-bottom:1rem;opacity:.85;}
.h-ttl{font-family:'Orbitron',sans-serif;font-weight:900;
  font-size:clamp(52px,13vw,145px);letter-spacing:6px;white-space:nowrap;
  background:linear-gradient(90deg,var(--cy),var(--p),var(--s),var(--ac),var(--cy));
  background-size:300% 300%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;animation:gS 5s ease infinite,flt 6s ease-in-out infinite;
  line-height:1;margin-bottom:.9rem;}
.h-tag{font-family:'Inter',sans-serif;font-size:clamp(13px,2.4vw,20px);font-weight:300;
  letter-spacing:3px;color:var(--tx);margin-bottom:1.2rem;opacity:.9;}
.h-dsc{font-family:'Inter',sans-serif;font-size:clamp(12px,1.7vw,14px);
  color:var(--txm);max-width:520px;margin:0 auto;line-height:1.8;}

.chip{display:inline-block;border:1px solid rgba(56,189,248,0.3);border-radius:100px;
  background:rgba(56,189,248,0.07);font-family:'Inter',sans-serif;
  font-size:clamp(9px,1.4vw,11px);color:var(--p);padding:5px 15px;
  letter-spacing:1.5px;margin-bottom:1.1rem;}

.bn-grid{display:grid;grid-template-columns:1fr;gap:1rem;margin-top:1.4rem;}
@media(min-width:480px){.bn-grid{grid-template-columns:repeat(3,1fr);}}
.bn-c{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);
  border-radius:var(--r);padding:1.3rem 1.1rem;text-align:center;
  transition:transform .3s,border-color .3s,box-shadow .3s;animation:fU .7s ease both;}
.bn-c:hover{transform:translateY(-5px);border-color:rgba(167,139,250,0.3);
  box-shadow:0 12px 32px rgba(167,139,250,0.1);}
.bn-ico{font-size:clamp(26px,4.5vw,36px);display:block;margin-bottom:.7rem;}
.bn-ttl{font-family:'Orbitron',sans-serif;font-size:clamp(11px,1.9vw,13px);
  font-weight:700;color:var(--tx);letter-spacing:2px;margin-bottom:.4rem;}
.bn-dsc{font-family:'Inter',sans-serif;font-size:clamp(11px,1.5vw,13px);color:var(--txm);line-height:1.7;}

.jg-grid{display:grid;grid-template-columns:1fr;gap:1.3rem;margin-top:1.6rem;}
@media(min-width:600px){.jg-grid{grid-template-columns:repeat(3,1fr);gap:1.4rem;}}
.jg-c{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.09);
  border-radius:var(--r);padding:1.5rem 1.2rem;text-align:center;
  transition:transform .3s,border-color .3s,box-shadow .3s;animation:fU .7s ease both;}
.jg-c:hover{transform:translateY(-8px);border-color:rgba(56,189,248,0.35);
  box-shadow:0 20px 50px rgba(56,189,248,0.12);}
.jg-c:nth-child(1){animation-delay:.1s;}.jg-c:nth-child(2){animation-delay:.2s;}.jg-c:nth-child(3){animation-delay:.3s;}
.ph{width:clamp(90px,15vw,116px);height:clamp(90px,15vw,116px);border-radius:50%;
  margin:0 auto 1rem;
  background:linear-gradient(135deg,var(--p),var(--s));
  padding:2.5px;overflow:hidden;}
.ph img{width:100%;height:100%;object-fit:cover;object-position:center top;border-radius:50%;}
.jg-nm{font-family:'Orbitron',sans-serif;font-size:clamp(11px,2vw,14px);font-weight:700;
  color:var(--tx);letter-spacing:1.5px;margin-bottom:.3rem;}
.jg-rl{font-family:'Inter',sans-serif;font-size:clamp(9px,1.4vw,11px);color:var(--p);
  letter-spacing:1.8px;margin-bottom:.3rem;font-weight:600;}
.jg-co{font-family:'Inter',sans-serif;font-size:clamp(9px,1.3vw,11px);
  color:var(--txm);letter-spacing:1px;margin-bottom:.7rem;}
.jg-bio{font-family:'Inter',sans-serif;font-size:clamp(11px,1.5vw,12.5px);
  color:var(--txm);line-height:1.7;text-align:left;margin-bottom:.9rem;}
.jg-tags{display:flex;flex-wrap:wrap;gap:5px;justify-content:center;margin-bottom:.9rem;}
.jg-tag{font-family:'Inter',sans-serif;font-size:9px;
  border:1px solid rgba(56,189,248,0.25);border-radius:100px;
  color:var(--p);padding:3px 9px;letter-spacing:1px;background:rgba(56,189,248,0.06);}
.jg-li{display:inline-block;font-family:'Inter',sans-serif;font-size:11px;
  font-weight:600;letter-spacing:1.5px;color:var(--p);
  border:1px solid rgba(56,189,248,0.35);border-radius:100px;
  padding:6px 18px;text-decoration:none;transition:background .3s,color .3s;}
.jg-li:hover{background:var(--p);color:#020617;text-decoration:none;}

.rg-grid{display:grid;grid-template-columns:1fr;gap:1.2rem;margin-top:1.5rem;}
@media(min-width:580px){.rg-grid{grid-template-columns:1fr 1fr;gap:1.4rem;}}
.rg-c{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.09);
  border-radius:var(--r);padding:1.8rem 1.4rem;text-align:center;
  transition:transform .3s,border-color .3s,box-shadow .3s;}
.rg-c:hover{transform:translateY(-5px);}
.rg-ca{animation:fU .7s ease .1s both;}
.rg-ca:hover{border-color:rgba(244,114,182,0.4);box-shadow:0 14px 40px rgba(244,114,182,0.1);}
.rg-cb{animation:fU .7s ease .2s both;}
.rg-cb:hover{border-color:rgba(56,189,248,0.4);box-shadow:0 14px 40px rgba(56,189,248,0.1);}
.rg-ba{display:inline-block;background:rgba(244,114,182,0.1);
  border:1px solid rgba(244,114,182,0.3);border-radius:100px;color:var(--ac);
  font-family:'Inter',sans-serif;font-size:9px;letter-spacing:2.5px;padding:4px 14px;margin-bottom:.9rem;}
.rg-bb{display:inline-block;background:rgba(56,189,248,0.08);
  border:1px solid rgba(56,189,248,0.3);border-radius:100px;color:var(--p);
  font-family:'Inter',sans-serif;font-size:9px;letter-spacing:2.5px;padding:4px 14px;margin-bottom:.9rem;}
.rg-ico{font-size:clamp(34px,5.5vw,46px);display:block;margin-bottom:.7rem;}
.rg-ttl{font-family:'Orbitron',sans-serif;font-size:clamp(18px,3.5vw,28px);
  font-weight:900;color:var(--tx);letter-spacing:3px;margin-bottom:.35rem;}
.rg-sa{font-family:'Inter',sans-serif;font-size:11px;letter-spacing:2px;color:var(--ac);margin-bottom:.7rem;}
.rg-sb{font-family:'Inter',sans-serif;font-size:11px;letter-spacing:2px;color:var(--p);margin-bottom:.7rem;}
.rg-hr{border:none;border-top:1px solid rgba(255,255,255,0.07);margin:.7rem 0;}
.rg-dsc{font-family:'Inter',sans-serif;font-size:clamp(11px,1.5vw,13px);
  color:var(--txm);line-height:1.8;text-align:left;margin-bottom:1.3rem;}
.rg-ba-btn{display:block;width:100%;
  background:linear-gradient(135deg,var(--ac),#c84b8e);
  color:#fff;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;
  letter-spacing:3px;border-radius:50px;padding:13px;text-align:center;text-decoration:none;
  box-shadow:0 6px 24px rgba(244,114,182,0.28);transition:transform .3s,box-shadow .3s;}
.rg-ba-btn:hover{transform:scale(1.03);box-shadow:0 10px 32px rgba(244,114,182,0.5);
  text-decoration:none;color:#fff;}
.rg-bb-btn{display:block;width:100%;
  background:linear-gradient(135deg,var(--cy),var(--p));
  color:#020617;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;
  letter-spacing:3px;border-radius:50px;padding:13px;text-align:center;text-decoration:none;
  box-shadow:0 6px 24px rgba(56,189,248,0.28);transition:transform .3s,box-shadow .3s;}
.rg-bb-btn:hover{transform:scale(1.03);box-shadow:0 10px 32px rgba(56,189,248,0.5);
  text-decoration:none;color:#020617;}
.rg-nt{font-family:'Inter',sans-serif;font-size:10px;letter-spacing:1.8px;
  color:var(--txm);text-align:center;margin-top:.6rem;opacity:.5;}

/* ── TIMELINE ────────────────────────────────────────────────────────────── */
.tl-outer{position:relative;padding:2.5rem 0 1rem;margin-top:1.5rem;}
.tl-spine{
  position:absolute;left:50%;top:0;bottom:0;width:2px;
  background:linear-gradient(180deg,transparent 0%,var(--p) 10%,var(--s) 90%,transparent 100%);
  transform:translateX(-50%);border-radius:2px;}
@media(max-width:599px){.tl-spine{left:18px;transform:none;}}

.tl-row{display:flex;align-items:flex-start;position:relative;margin-bottom:3.2rem;}

.tl-dot{
  position:absolute;left:50%;top:18px;
  width:16px;height:16px;border-radius:50%;
  background:linear-gradient(135deg,var(--p),var(--s));
  transform:translateX(-50%);z-index:3;
  box-shadow:0 0 14px rgba(56,189,248,0.55);
  animation:pd 2.4s ease-in-out infinite;}
@media(max-width:599px){.tl-dot{left:18px;transform:none;top:18px;}}

.tl-box{
  width:calc(50% - 28px);
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(255,255,255,0.08);
  border-radius:12px;padding:1rem 1.15rem;
  transition:border-color .3s,box-shadow .3s;
  animation:fU .65s ease both;}
.tl-box:hover{border-color:rgba(56,189,248,0.3);box-shadow:0 8px 24px rgba(56,189,248,0.1);}

/* LEFT: box aligned left of the spine */
.tl-L{justify-content:flex-start;}
.tl-L .tl-box{text-align:right;margin-left:0;margin-right:auto;}

/* RIGHT: box aligned right of the spine */
.tl-R{justify-content:flex-end;}
.tl-R .tl-box{text-align:left;margin-right:0;margin-left:auto;}

/* Mobile: all items stack left */
@media(max-width:599px){
  .tl-L,.tl-R{justify-content:flex-start;}
  .tl-L .tl-box,.tl-R .tl-box{
    width:calc(100% - 46px)!important;
    margin-left:46px!important;
    margin-right:0!important;
    text-align:left!important;}}

.tl-dt{font-family:'Inter',sans-serif;font-size:10px;color:var(--p);
  letter-spacing:2.5px;font-weight:600;margin-bottom:.25rem;text-transform:uppercase;}
.tl-hd{font-family:'Orbitron',sans-serif;font-size:clamp(12px,2vw,15px);
  color:var(--tx);letter-spacing:1.2px;margin-bottom:.35rem;font-weight:700;}
.tl-dd{font-family:'Inter',sans-serif;font-size:clamp(11px,1.5vw,13px);
  color:var(--txm);line-height:1.7;}
/* ───────────────────────────────────────────────────────────────────────── */

.gl-grid{display:grid;grid-template-columns:1fr 1fr;gap:.8rem;margin-top:1.4rem;}
@media(min-width:768px){.gl-grid{grid-template-columns:repeat(4,1fr);gap:1rem;}}
.gl-c{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);
  border-radius:12px;padding:.9rem 1rem;display:flex;align-items:flex-start;gap:10px;
  transition:border-color .3s,box-shadow .3s;animation:fU .6s ease both;}
.gl-c:hover{border-color:rgba(56,189,248,0.3);box-shadow:0 6px 20px rgba(56,189,248,0.08);}
.gl-ico{font-size:18px;flex-shrink:0;margin-top:1px;}
.gl-tx{font-family:'Inter',sans-serif;font-size:clamp(11px,1.5vw,13px);color:var(--txm);line-height:1.6;}

.stTextInput>div>div>input,.stTextArea>div>div>textarea{
  background:rgba(10,18,40,0.92)!important;border:1px solid rgba(56,189,248,0.22)!important;
  border-radius:10px!important;color:var(--tx)!important;
  font-family:'Inter',sans-serif!important;font-size:14px!important;}
.stTextInput>div>div>input:focus,.stTextArea>div>div>textarea:focus{
  border-color:var(--p)!important;box-shadow:0 0 0 2px rgba(56,189,248,0.12)!important;}
label[data-baseweb="label"],.stTextInput label,.stTextArea label{
  font-family:'Inter',sans-serif!important;font-size:11px!important;
  font-weight:600!important;letter-spacing:2px!important;
  color:var(--p)!important;text-transform:uppercase!important;}
.stButton>button{
  font-family:'Orbitron',sans-serif!important;font-size:12px!important;
  font-weight:700!important;letter-spacing:3px!important;
  background:linear-gradient(135deg,var(--cy),var(--s))!important;
  color:#020617!important;border:none!important;border-radius:50px!important;
  padding:12px 36px!important;transition:transform .3s,box-shadow .3s!important;width:100%!important;}
.stButton>button:hover{transform:scale(1.04)!important;
  box-shadow:0 8px 28px rgba(56,189,248,0.4)!important;}

.ok-box{border:1px solid rgba(56,189,248,0.4);border-radius:12px;
  background:rgba(56,189,248,0.06);padding:14px 18px;font-family:'Inter',sans-serif;
  font-size:12px;color:var(--p);letter-spacing:1px;margin-top:1rem;line-height:1.6;}
.ok-box a{color:var(--s);}
.qa-item{background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);
  border-radius:12px;padding:1.1rem 1.3rem;margin-bottom:1.1rem;transition:border-color .3s;}
.qa-item:hover{border-color:rgba(56,189,248,0.22);}
.qa-who{font-family:'Inter',sans-serif;font-size:10px;color:var(--p);
  letter-spacing:2.5px;font-weight:600;margin-bottom:.35rem;text-transform:uppercase;}
.qa-q{font-family:'Inter',sans-serif;font-size:clamp(12px,1.7vw,14px);
  color:var(--tx);margin-bottom:.75rem;line-height:1.6;}
.qa-rep{border-left:2px solid var(--p);padding-left:12px;font-family:'Inter',sans-serif;
  font-size:clamp(11px,1.5vw,13px);color:var(--txm);font-style:italic;line-height:1.6;}
.qa-lbl{font-family:'Inter',sans-serif;font-size:9px;color:var(--p);
  letter-spacing:2.5px;font-weight:600;margin-bottom:.25rem;text-transform:uppercase;}

.sp-ft{text-align:center;padding:2.8rem 1rem 2rem;
  border-top:1px solid rgba(255,255,255,0.07);margin-top:2rem;position:relative;z-index:1;}
.ft-ttl{font-family:'Orbitron',sans-serif;font-size:clamp(13px,2.8vw,22px);
  font-weight:900;letter-spacing:4px;color:var(--tx);margin-bottom:.4rem;}
.ft-sb{font-family:'Inter',sans-serif;font-size:11px;letter-spacing:2.5px;color:var(--txm);}
.ft-tg{font-family:'Inter',sans-serif;font-size:10px;letter-spacing:4px;
  color:rgba(226,232,240,0.27);margin-top:.5rem;}
.ft-ic{font-size:16px;letter-spacing:10px;margin-top:.7rem;opacity:.32;}

[data-testid="stHorizontalBlock"]{gap:.5rem!important;}
</style>"""

st.markdown(CSS, unsafe_allow_html=True)

# ── SHARK SVG ──────────────────────────────────────────────────────────────────
SV = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 260 100'>"
      "<ellipse cx='120' cy='50' rx='110' ry='33' fill='none' stroke='white' stroke-width='1.5'/>"
      "<polygon points='230,50 260,28 260,72' fill='none' stroke='white' stroke-width='1.5'/>"
      "<polygon points='120,17 102,2 138,2' fill='none' stroke='white' stroke-width='1.5'/>"
      "<path d='M90,54 Q76,77 56,85 Q82,65 86,54' fill='none' stroke='white' stroke-width='1.5'/>"
      "<circle cx='196' cy='42' r='3.5' fill='white' opacity='0.6'/>"
      "</svg>")

# ── BACKGROUND ELEMENTS ────────────────────────────────────────────────────────
render(
    "<div class='bbl-wrap'>"
    "<div class='bbl' style='width:6px;height:6px;left:7%;animation-duration:11s;animation-delay:0s;'></div>"
    "<div class='bbl' style='width:14px;height:14px;left:15%;animation-duration:16s;animation-delay:2s;'></div>"
    "<div class='bbl' style='width:5px;height:5px;left:23%;animation-duration:9s;animation-delay:4s;'></div>"
    "<div class='bbl' style='width:20px;height:20px;left:32%;animation-duration:19s;animation-delay:.8s;'></div>"
    "<div class='bbl' style='width:9px;height:9px;left:40%;animation-duration:13s;animation-delay:2.5s;'></div>"
    "<div class='bbl' style='width:15px;height:15px;left:50%;animation-duration:21s;animation-delay:5s;'></div>"
    "<div class='bbl' style='width:7px;height:7px;left:58%;animation-duration:10s;animation-delay:.4s;'></div>"
    "<div class='bbl' style='width:24px;height:24px;left:67%;animation-duration:23s;animation-delay:3s;'></div>"
    "<div class='bbl' style='width:10px;height:10px;left:75%;animation-duration:14s;animation-delay:1.2s;'></div>"
    "<div class='bbl' style='width:30px;height:30px;left:83%;animation-duration:20s;animation-delay:4s;'></div>"
    "<div class='bbl' style='width:8px;height:8px;left:91%;animation-duration:12s;animation-delay:1s;'></div>"
    "<div class='bbl' style='width:18px;height:18px;left:4%;animation-duration:18s;animation-delay:6s;'></div>"
    "</div>"
    "<div class='shk-wrap'>"
    f"<div class='shk shk-l' style='top:15%;width:220px;animation-duration:32s;animation-delay:0s;'>{SV}</div>"
    f"<div class='shk shk-r' style='top:38%;width:170px;animation-duration:25s;animation-delay:9s;transform:scaleX(-1);'>{SV}</div>"
    f"<div class='shk shk-l' style='top:60%;width:280px;animation-duration:38s;animation-delay:18s;'>{SV}</div>"
    f"<div class='shk shk-r' style='top:80%;width:140px;animation-duration:21s;animation-delay:6s;transform:scaleX(-1);'>{SV}</div>"
    "</div>"
)

# ── TOP BAR ───────────────────────────────────────────────────────────────────
render(
    "<div class='top-bar'>"
    "\U0001f988 &nbsp; S&amp;T CLUB &nbsp;&middot;&nbsp; MATRUSRI ENGINEERING COLLEGE &nbsp;&middot;&nbsp; SHARKPIT 2026"
    "</div>"
)

# ── HERO  (no CTA button — registration section below handles it) ─────────────
render(
    "<div class='hw'>"
    "<div class='h-eye'>Science &amp; Technology Club &nbsp;&middot;&nbsp; MECS &nbsp;&middot;&nbsp; 2026</div>"
    "<div class='h-ttl'>SHARKPIT</div>"
    "<div class='h-tag'>Pitch &nbsp;&middot;&nbsp; Innovate &nbsp;&middot;&nbsp; Win</div>"
    "<div class='h-dsc'>The premier startup pitch competition for every B.Tech student at Matrusri Engineering College. Face the Sharks. Defend your idea. Claim the crown.</div>"
    "</div>"
)

# ── ABOUT ──────────────────────────────────────────────────────────────────────
render(
    "<div class='sp-sec'>"
    "<div class='sp-lbl'>About the Event</div>"
    "<div class='sp-ttl'>What is SHARKPIT?</div>"
    "<div class='chip'>Open to ALL B.Tech years &nbsp;&middot;&nbsp; Technical &amp; Non-Technical ideas welcome</div>"
    "<div class='sp-bod'>SHARKPIT is a high-energy student startup pitch competition and ideathon organised by the S&amp;T Club of MECS. Inspired by investor pitch formats, it challenges students to think like entrepreneurs and defend their ideas before experienced industry founders &mdash; the Sharks.<br/><br/>"
    "The event has two parts: a morning casual open meetup for all students, and exclusive evening finals where the top 20 shortlisted teams pitch live before the Sharks. Whether you&rsquo;re technical or non-technical, any B.Tech student with a bold idea can compete.</div>"
    "</div>"
)

# ── WHY PARTICIPATE ────────────────────────────────────────────────────────────
render(
    "<div class='sp-sec'>"
    "<div class='sp-lbl'>Why Join</div>"
    "<div class='sp-ttl'>Why Participate?</div>"
    "<div class='bn-grid'>"
    "<div class='bn-c' style='animation-delay:.1s;'><span class='bn-ico'>\U0001f4a1</span>"
    "<div class='bn-ttl'>INNOVATE</div>"
    "<div class='bn-dsc'>Turn raw ideas into structured pitches. Think like a founder and build solutions that matter.</div></div>"
    "<div class='bn-c' style='animation-delay:.2s;'><span class='bn-ico'>\U0001f91d</span>"
    "<div class='bn-ttl'>NETWORK</div>"
    "<div class='bn-dsc'>Connect with students, founders, and mentors who can shape your entrepreneurial journey.</div></div>"
    "<div class='bn-c' style='animation-delay:.3s;'><span class='bn-ico'>\U0001f3c6</span>"
    "<div class='bn-ttl'>EXPOSURE</div>"
    "<div class='bn-dsc'>Pitch live before real Shark investors &amp; founders. Earn certificates recognised by the college.</div></div>"
    "</div></div>"
)

# ── MEET THE SHARKS ────────────────────────────────────────────────────────────
# Image 1 = Sai Harishith  (IMG_HARISHITH) — white shirt, glasses, tile background
# Image 2 = E Sai Eshwar   (IMG_ESHWAR)    — navy suit, speaking on stage
# Image 3 = Yashwanth      (IMG_YASHWANTH) — Back to Base event, dark blue shirt
render(
    "<div class='sp-sec'>"
    "<div class='sp-lbl'>Jury Panel</div>"
    "<div class='sp-ttl'>Meet the Sharks</div>"
    "<div class='sp-bod' style='margin-bottom:.5rem;'>Three visionary founders. One arena. Zero mercy on weak pitches.</div>"
    "<div class='jg-grid'>"

    # Card 1 — E Sai Eshwar
    "<div class='jg-c'>"
    f"<div class='ph'><img src='data:image/jpeg;base64,{IMG_ESHWAR}' alt='E Sai Eshwar'/></div>"
    "<div class='jg-nm'>E SAI ESHWAR</div>"
    "<div class='jg-rl'>Founder &middot; Ecosystem Operator</div>"
    "<div class='jg-co'>\U0001f680 Studlyf &nbsp;&middot;&nbsp; Nirvaha &nbsp;&middot;&nbsp; GuideBazaar</div>"
    "<div class='jg-bio'>Operates at the intersection of Applied AI, strategy, and social impact. 12x national hackathon finalist, mentors 600+ students, and has delivered 10+ public speaking sessions on AI &amp; entrepreneurship.</div>"
    "<div class='jg-tags'><span class='jg-tag'>Applied AI</span><span class='jg-tag'>Product</span><span class='jg-tag'>Mentorship</span></div>"
    "<a class='jg-li' href='https://linkedin.com/in/esaieshwar' target='_blank'>\U0001f517 LinkedIn</a>"
    "</div>"

    # Card 2 — Yashwanth Bondapalli
    "<div class='jg-c'>"
    f"<div class='ph'><img src='data:image/jpeg;base64,{IMG_YASHWANTH}' alt='Yashwanth Bondapalli'/></div>"
    "<div class='jg-nm'>YASHWANTH BONDAPALLI</div>"
    "<div class='jg-rl'>AI &amp; Cybersecurity &middot; Founder</div>"
    "<div class='jg-co'>&#9889; Back to Base XYZ</div>"
    "<div class='jg-bio'>Builds production-grade LLM and RAG systems. Speaker at GitTogether Hyderabad, organised by GitHub India and supported by Microsoft. AI expertise with a security-first mindset.</div>"
    "<div class='jg-tags'><span class='jg-tag'>AI / LLMs</span><span class='jg-tag'>RAG</span><span class='jg-tag'>Cybersecurity</span></div>"
    "<a class='jg-li' href='https://linkedin.com/in/yashwanth-bondapalli-37b6a7255' target='_blank'>\U0001f517 LinkedIn</a>"
    "</div>"

    # Card 3 — Sai Harishith
    "<div class='jg-c'>"
    f"<div class='ph'><img src='data:image/jpeg;base64,{IMG_HARISHITH}' alt='Sai Harishith'/></div>"
    "<div class='jg-nm'>SAI HARISHITH</div>"
    "<div class='jg-rl'>Founder &amp; Director</div>"
    "<div class='jg-co'>\U0001f6e1\ufe0f ShieldNet Solutions</div>"
    "<div class='jg-bio'>Built ShieldNet Solutions from the ground up &mdash; a full-service tech company delivering cybersecurity, web &amp; mobile development, and network administration. Leads with a security-first approach.</div>"
    "<div class='jg-tags'><span class='jg-tag'>Cybersecurity</span><span class='jg-tag'>Web &amp; Mobile</span><span class='jg-tag'>Network</span></div>"
    "<a class='jg-li' href='https://linkedin.com/in/sai-harishith-b37558322' target='_blank'>\U0001f517 LinkedIn</a>"
    "</div>"

    "</div></div>"
)

# ── REGISTER NOW ───────────────────────────────────────────────────────────────
render(
    "<div class='sp-sec'>"
    "<div class='sp-lbl'>Registration</div>"
    "<div class='sp-ttl'>Register Now</div>"
    "<div class='sp-bod' style='margin-bottom:1.3rem;'>Click the link for your preferred session. Participation certificates will be shared online after the event.</div>"
    "<div class='rg-grid'>"

    "<div class='rg-c rg-ca'>"
    "<span class='rg-ba'>IDEATHON REGISTRATION</span>"
    "<span class='rg-ico'>\U0001f988</span>"
    "<div class='rg-ttl'>IDEATHON</div>"
    "<div class='rg-sa'>Evening Pitch Finals</div>"
    "<hr class='rg-hr'/>"
    "<div class='rg-dsc'>Register on Luma to compete in the SHARKPIT ideathon. Submit your startup idea and pitch live before our Shark jury on March 17th. Requires idea submission before March 13th and approval via email. Top 20 teams shortlisted.</div>"
    f"<a class='rg-ba-btn' href='{LUMA_IDEATHON}' target='_blank'>REGISTER FOR SESSION &rarr;</a>"
    "<div class='rg-nt'>Requires shortlisting &middot; March 17, 2026</div>"
    "</div>"

    "<div class='rg-c rg-cb'>"
    "<span class='rg-bb'>OPEN MEETUP REGISTRATION</span>"
    "<span class='rg-ico'>\U0001f305</span>"
    "<div class='rg-ttl'>OPEN MEETUP</div>"
    "<div class='rg-sb'>Morning Casual Session</div>"
    "<hr class='rg-hr'/>"
    "<div class='rg-dsc'>Register on Luma to attend the morning casual session. Listen to Shark founders speak, get inspired, and soak in the entrepreneurial energy. Open to every MECS student &mdash; no idea submission needed.</div>"
    f"<a class='rg-bb-btn' href='{LUMA_MEETUP}' target='_blank'>REGISTER FOR SESSION &rarr;</a>"
    "<div class='rg-nt'>Open to all &middot; March 17, 2026</div>"
    "</div>"

    "</div></div>"
)

# ── EVENT ROADMAP ──────────────────────────────────────────────────────────────
# Layout: L1 left, L2 right, L3 left, L4 right (spine in centre)
render(
    "<div class='sp-sec'>"
    "<div class='sp-lbl'>Schedule</div>"
    "<div class='sp-ttl'>Event Roadmap</div>"
    "<div class='sp-bod' style='margin-bottom:0;'>Your journey from raw idea to the Shark Tank.</div>"

    "<div class='tl-outer'>"
    "<div class='tl-spine'></div>"

    # Row 1 — LEFT
    "<div class='tl-row tl-L'>"
    "<div class='tl-box' style='animation-delay:.05s;'>"
    "<div class='tl-dt'>March 13, 2026</div>"
    "<div class='tl-hd'>\U0001f4a1 Idea Submission Deadline</div>"
    "<div class='tl-dd'>Submit your startup idea before the cutoff. Include a problem statement, proposed solution, and team details. Teams of 1&ndash;4 MECS B.Tech students.</div>"
    "</div>"
    "<div class='tl-dot'></div>"
    "</div>"

    # Row 2 — RIGHT
    "<div class='tl-row tl-R'>"
    "<div class='tl-dot'></div>"
    "<div class='tl-box' style='animation-delay:.15s;'>"
    "<div class='tl-dt'>March 14 &ndash; 16, 2026</div>"
    "<div class='tl-hd'>\U0001f4e7 Shortlisting via Email</div>"
    "<div class='tl-dd'>Panel reviews all submissions and selects Top 20 teams. Results communicated exclusively via email &mdash; check your inbox!</div>"
    "</div>"
    "</div>"

    # Row 3 — LEFT
    "<div class='tl-row tl-L'>"
    "<div class='tl-box' style='animation-delay:.25s;'>"
    "<div class='tl-dt'>March 17, 2026 &mdash; Morning</div>"
    "<div class='tl-hd'>\U0001f305 Open Meetup Session</div>"
    "<div class='tl-dd'>All MECS students attend. Listen to Shark founders speak, get inspired, and network with peers and mentors.</div>"
    "</div>"
    "<div class='tl-dot'></div>"
    "</div>"

    # Row 4 — RIGHT (last item)
    "<div class='tl-row tl-R'>"
    "<div class='tl-dot'></div>"
    "<div class='tl-box' style='animation-delay:.35s;'>"
    "<div class='tl-dt'>March 17, 2026 &mdash; Evening</div>"
    "<div class='tl-hd'>\U0001f988 Final Pitch Round</div>"
    "<div class='tl-dd'>Top 20 teams pitch live before the Sharks. Defend your idea. Claim your crown. Jury interaction &amp; final presentations.</div>"
    "</div>"
    "</div>"

    "</div>"  # tl-outer
    "</div>"  # sp-sec
)

# ── PITCH GUIDELINES ───────────────────────────────────────────────────────────
render(
    "<div class='sp-sec'>"
    "<div class='sp-lbl'>Rules</div>"
    "<div class='sp-ttl'>Pitch Guidelines</div>"
    "<div class='sp-bod' style='margin-bottom:0;'>Follow these rules. The Sharks are watching every second.</div>"
    "<div class='gl-grid'>"
    "<div class='gl-c' style='animation-delay:.05s;'><span class='gl-ico'>&#9201;</span>"
    "<span class='gl-tx'>10 minutes per team for pitching</span></div>"
    "<div class='gl-c' style='animation-delay:.10s;'><span class='gl-ico'>&#128101;</span>"
    "<span class='gl-tx'>Teams of 1 to 4 members</span></div>"
    "<div class='gl-c' style='animation-delay:.15s;'><span class='gl-ico'>&#127919;</span>"
    "<span class='gl-tx'>Cover problem, solution &amp; impact</span></div>"
    "<div class='gl-c' style='animation-delay:.20s;'><span class='gl-ico'>&#127979;</span>"
    "<span class='gl-tx'>Open to all B.Tech years at MECS</span></div>"
    "<div class='gl-c' style='animation-delay:.25s;'><span class='gl-ico'>\U0001f988</span>"
    "<span class='gl-tx'>Top 20 teams advance to finals</span></div>"
    "<div class='gl-c' style='animation-delay:.30s;'><span class='gl-ico'>&#128231;</span>"
    "<span class='gl-tx'>Shortlisting notified via email</span></div>"
    "<div class='gl-c' style='animation-delay:.35s;'><span class='gl-ico'>\U0001f680</span>"
    "<span class='gl-tx'>Original ideas only &mdash; no copying</span></div>"
    "</div></div>"
)

# ── ASK A QUERY ────────────────────────────────────────────────────────────────
render(
    "<div class='sp-sec'>"
    "<div class='sp-lbl'>Contact</div>"
    "<div class='sp-ttl'>Ask a Query</div>"
    "<div class='sp-bod'>Have a question about SHARKPIT 2026? Fill the form below &mdash; it opens your email app pre-filled and ready to send.</div>"
    "</div>"
)

_, qcol, _ = st.columns([0.3, 5, 0.3])
with qcol:
    q_name  = st.text_input("Your Name",  key="q_name",  placeholder="e.g. Ravi Kumar")
    q_email = st.text_input("Your Email", key="q_email", placeholder="e.g. ravi@student.mecs.edu")
    q_msg   = st.text_area("Your Query",  key="q_msg",   height=110,
                            placeholder="Type your question here...")
    if st.button("\U0001f988  SUBMIT QUERY"):
        if q_name.strip() and q_email.strip() and q_msg.strip():
            subj   = urllib.parse.quote(f"SHARKPIT 2026 Query from {q_name.strip()}")
            body   = urllib.parse.quote(
                f"Name: {q_name.strip()}\nEmail: {q_email.strip()}\n\nQuery:\n{q_msg.strip()}"
            )
            mailto = f"mailto:{CONTACT_EMAIL}?subject={subj}&body={body}"
            st.session_state.queries.append({
                "name": q_name.strip(), "email": q_email.strip(),
                "message": q_msg.strip(), "reply": None
            })
            render(
                f"<div class='ok-box'>"
                f"&#10003; &nbsp; Query ready! &nbsp;"
                f"<a href='{mailto}' target='_blank'>Click here to open your email app and send it</a>"
                f" &mdash; addressed to {CONTACT_EMAIL}."
                f"</div>"
            )
        else:
            st.warning("Please fill in all fields before submitting.")

# ── PUBLIC Q&A ─────────────────────────────────────────────────────────────────
replied = [q for q in st.session_state.queries if q.get("reply")]
if replied:
    render(
        "<div class='sp-sec'>"
        "<div class='sp-lbl'>Q &amp; A</div>"
        "<div class='sp-ttl'>Questions &amp; Answers</div>"
    )
    for q in replied:
        render(
            "<div class='qa-item'>"
            f"<div class='qa-who'>&mdash; {q['name']}</div>"
            f"<div class='qa-q'>{q['message']}</div>"
            "<div class='qa-rep'>"
            "<div class='qa-lbl'>Organiser Reply</div>"
            f"{q['reply']}"
            "</div></div>"
        )
    render("</div>")

# ── FOOTER ─────────────────────────────────────────────────────────────────────
render(
    "<div class='sp-ft'>"
    "<div class='ft-ttl'>MATRUSRI ENGINEERING COLLEGE</div>"
    "<div class='ft-sb'>Science &amp; Technology Club &nbsp;&middot;&nbsp; SHARKPIT 2026</div>"
    "<div class='ft-tg'>PITCH &nbsp;&middot;&nbsp; INNOVATE &nbsp;&middot;&nbsp; WIN</div>"
    "<div class='ft-ic'>\U0001f988 \U0001f4a1 \U0001f680</div>"
    "</div>"
)
