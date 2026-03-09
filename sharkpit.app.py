# -*- coding: utf-8 -*-
import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="SHARKPIT 2026 - S&T Club MECS",
    page_icon="\U0001f988",
    layout="wide"
)

if "queries" not in st.session_state:
    st.session_state.queries = []

# ── IMAGES (base64) ────────────────────────────────────────────────────────────
IMG_HARISHITH = "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"
IMG_ESHWAR    = "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCADIAMgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCxPAjQlSy5ChdncNnk1Qa0PpXTPZ5kY46k1C1lx0ryJ11zM9CNJ8qRzhtSB0qNrc+ldC9mR0FRmyPpU+3H7IwDbnHSo2tfbFdEbI/3aY1l321Ptxqmznjb47U37Oa3mss9qYbL2pquhunYwmhPTHFM8g+lbLWZz0phtCD0q/bInkF8NaNdatr0MNtN9maIea82f9WB3+td/DYW7CTTfDknI/4/tVk5K+wPcnnp0rmdF0aH7Fcale3ckFr/AKny4j88x/uj2rqoNMnutOB1BhpGixjK2yHa7j1Y1SqX0IlGzvcba3Edtv0fwjb+dcN/x8ajJyoPc57mmRqmjyy6boudR8QXIxcXjciLPUk9selWYjdaxCbPRkGl6NGMPckbWkHt/jUdoTtfSvCsW1Txc6k4/Mg9zVqf9f5f5k8tv6/M6qymDxmBp0muLfbHOV/v7QTVuuV0iaGw1FNJ0xTcww75b68Y9WI9e5zXVDmvPrQ5ZabESVmU9VtxdaReW+M+bA6/mpr5skGOD1r6fwCMetfNOsQG11a8gI/1czpj6MavD7tHRh3o0ZzComHOalY8VET2rtRq2NI5pppSaQtVohsKWm5zTgatIzbHr1ooXtRWiIPejaD0qNrQela/lZ7U0we1fNNs9FTiYpsc9qabHvitvyPakMHtU3Y+eJifYfYVE1jntW+YPamfZxnpRdj5omB9g9qjaxx2ro/s3HSmm2FVdheLOYbT/aoZLDHbFdS1spzUT2gPampsOWLK2l2drpscUzRm8vW5hg6rHnv9a1Lq1Rit94gm8xh/qrROg9sd6ks4fKPlWMYErffmPapjDDbTAoDeXp6M3IWuiFRpf1/TOaaXN/X9IpXFtcalB5uqSfYNMX7tupwWHvT1SXUbcQQL/ZmiIPmf7rSD0HoKszWqCVZ9SkNxN/BAvQfhT7q3SVBcaq+I/wDlnap0H4dzWkahk0tLf16f5mbDZm/tGstP/wBB0RM+bcdHm9ce3vW7pF/FfQSeQj+RE/lxyN0kAA5BrPuIGv4hLqDm105PuW6nBYe9SWs0rSrcKBZ6XbqQiEY8ylKSkrf1/wAMTKN1/X9Nm4a8D8e2gtfF+o8YDy+YP+BAGvfAQVBB4NeNfFe3MXiFJscSwKfyJFPDW57EUpWZ54/Wom9aVnqMNlsV6CRrzah1PFPWFmGQKaeM1bsnyStXBXdiajajcr/Z3HajyHHatbC8HFKApHSuhUzlddmVsI6iitGaNTGcDtRQ4tFRqJrU+ifJ9qQw8dKubaNtfLcpt7RlIw0nk81e2Umz2o5R+0ZSMPFIIMkYFXtlKqYaq5Q9qyh9nO7HekNvjjHNaBTn3pXTJz7UWD2rMswD0qM24zzWoYhTfKGemadi1WK6WxMYy3lR+g6mnopRSlrGEz1marAjBOX5x0FOKFx83yp6DvVozc77lWKJY2PkjzZz1kboKa8ccMm983Fwemegq5tYrsjGxPWmBAnES5b+8adwU9SnJAu4T3zb2H3Ih0pssRucT3x2W6cpCO/1q75aRNuI8yU9M0xohu865O5h91KVylP+v8ia0lMsAYxmP0U+navNvi/b/u9OuQOzxn9D/jXogZ4mM0x+9hVQdhXCfF9gNG05e5nbH/fNbUH+8Rml7+h4o5xUYb5qkkU5PFRbSDzXqI0e5MW4p1o+24ApmPlIqFX2ShvSqhuOprE6HqvWl24Y1QXUF24IqQahHx9K61JHnuLLmMrRVUX0fSiq0Ero9vtfiP4eucCSWe3P/TSI4/MZrbtfEWjXoH2fU7Vz6eYAfyNfPkLALzUvmKa8aWCh0Z2WR9IKVcbkIYeoOaXFfOsGo3Vqc291NER3jkIq/D498S2bYTU5JFHaZQ/8xWLwclsx+z7HveOKMc147afFvV48C6srScdyuUP9a3rP4uadJgXem3MJ7mNg4/pWTw9RdBezkei0Yrl7T4h+GbrA/tDySe00bL+vSt211bTr0A2t9bTZ6bJQTWbg1uiXGS3RaxRtp1ANKxI3bz0ox680+inYLjcE9elGOMDgU6ikFxm0L90c+tN2ANk/M1S9uKQcUWC5AybW8xvmfsPSvK/i1f5vNOsWILRRtK+OxY4H6CvU7y6gsbSa7uJAkMSl3c9gK+bfEetS65rl1qEmR5r/ACr/AHVHAH5V04eDcrm1PXUoPIg7VA0iEdBUTuaiLV6SKZYMg68VExUmoSxozmmkK5NlcU5CrVWJNIrEGrSDRl4BaKrebRTVxOMTZBNG8+tM30bxWbNUPLn1ppbPWk3UmahloeMUuRmmCjPNS0UrEoIpyttORwfUVDmlqXEd0a1pr+q2WPs2pXUWOyynH5VuWnxI8RW2A11HOo7TRA/qMGuOpwzWbpp9Aai90enWXxXuiypc6XFITx+5cqfyOav3PxX06MbEtis6jLpJIMD8R1rx65maG1kZSQxG3IPQd6f4etLGZJbnUhIUBxFtwdzHoCO4oWHglzNGTpwcrJHtGnfFDSrm8SC7ie1jfAW4Lbo93oT2rtIbmC5XdBNHKPVHDfyrwG/tNEu9Cd00++glhCoZhhl54DHpwTWNBdSRIgSVkmjG1yjY6dDx7VlKgnrHQUsOr7n05VLUdWsdJt2mvrqKBAP4jyfoOpr5/HiTWEj2DVbwL6ee3+NUJ7mW4bzJpXkc/wATsWP5moVB9SVhlfVnW+NfG8niE/Y7UNDpyHO08NKfVvb0FcM0a09m71JFavNFNIWEaxReZ8wPzjOAB/ntXTGPKrI6FCK0RSeEdaiMIIqwT61Gcj6VqmyXGJCYVxmkEQBNPzyRSE9Kq7J5YjTGp7U3yRmpM00HimmxOMRnlCinmiq5mTyog+0TY/1hpftUw/jP5VJ5Keh/Ok8hPQ/nWmhirjftU/8Af/Sj7XP/AHh+VO+zp70fZ19TU6FXYgvZwOq/lS/b5j2T8qQ2w/vGj7N/tfpSsh3Y8X8oH3UNOGoy90Sofs3+1+lL9mP94UrIfNIm/tGT/nmv504ak/eJfzqv9nb+8KPsz56ilZD5maFpPHfXSW06IFc4G9yAT2GRW9pGpzaJN9gmtI2i3bijgbh7Z/rXL2unT3VykMbRBmbaGkcKo+pPSrOt6ZqOlPCt5DLExQDcwOG+h71MoX9DSFS3TU7q91p5LtWjYQWUwCy24CYkUfjuAzXJa3dW8GqzeVCUVsNtGPp/Squm3l5c3ljA161uiSgCUL9zPU+5rW8d+Fn8Oa6sMc73MM8KzJK4ALZ6/rSVNDnWbdjBOoRn+B6U6hF/dfH0qkYZP7pppif+6aagiOeRr6e0epajbWSMVaeVYwSPU16VqOmXum6P5UsMMhlm8mO2aIMgiC4Uexzz7V5Ppi3aaratao5uBKpj2jJzntXrq+NWtdIJubGSa8CEphc7jj07VnUsjejJtNnm+vRWum3aRqJYnZcvFIB8h9iM5H1rIa8gP8f6UzUby41S/mvLks0srbicdPYe1UjGf7p/Ktow01MJ1Lydi99ph67x+VH2mE5AkWqOw/3T+VN8s/3T+VVyIj2jL/2iEnAlX86Xzo/+ei/nWd5Z9D+VN2e36U+RB7Rml5qYHzr+dFZuz2NFHIhe0Zv/AGY/3hR9nb1FWRRSuKxW+zv6ik8h/QVapccUrjKnkSelJ5L/AN2rtApXHYpeU/8AdNL5bD+E/lV0UtAFDaf7pqe1it2cG6keOPONyrx+J7VYrPUtJLJ8zZBI+Q5I/D/61a0YqT1IqSaWhuSW8EBRYtvlMc7nPOew9K67w1rwutOk8O6jAt2+0rZLIoYP/sHPp1H5elebQXwhP2aUK0TfL7fTB6fSrvmFSgDsQCPKlB+ZT2BP8jW9SEakOUyjJxdzpG8MRR67OEg8vT4ovM5Y43jAZc9QcnpXU6u1p4o0JITGgks4hEkpXe69ORkjg471veH9Lh8R+DPtF9PFFdyLtmeHB2sv94ep4JFeb61a6xoFx5cMzpudh544Vwo3YA7nB7+9ebKnUi0u5306lOabfQ5W6tXtpNr8j1HSq5Fa/wBohu5XVsMD79z3qF7aMFymJEThnUcA+ma7KlFx1jsc0aiejMt55bRTPDI0csfzI6HBU9iKtr4+8Q3Mf2W5vBLHIpjJKYIB4PIqlrEgt7UKqjEhwTnoKxbcE3Eagnlhg0owTjqTKTUtDcwfWmkVdNunoaQ28fpWKNCkB1+lNIq+tvH83Hb1pvkJ/dp3FYoEUmKvGCP+7SGGP+7VXAo4oq4YU/u0UXFY1PLFHlClBpwoAZ5VHk571LS5osMi8k0eVUuaUGlYCHyj6UCMjtU4pTRYZX2H0rLFpbz30sch2yq2RlgA2a281havGUvUkUAb1wCexFaUdJGdTYbqdvCsB8lGaRerBiQMfXrV6zb7JYrPLuWdhwrDp6cVCl1Fp1t8rtLMxOZC5P4VlXOoyTMWlcs1dTaWpidJpPjLVNK1VBY5dJmCS268iXnA/H0rvPiw8FpoWkQqrrMZZJH3/eztXrjvzivEorgpKHBZWBDK6HBUjoRXT+I/FV74vlsWvAokt4BHI6dJGz97HYnjI9awcbz5i1LSxmiRltJpCSB0HPf1qjHfsgXecqv3YwcL9T61edEkaG1RiE3YJ+veibw2+cxXAPsy4/lVykouwlFvYpalqBvljYjaACNo4AP0qDTEMt9Cno2fyq6dAvlVlBiZT/tVe0nR5LWRprgruxhQpz+NROaaHGDuX9ppCDVjyxQYx0rmsdBWAPzfSmkGraovzDHamlF9KLCKu3imkVb2j0prKKdgKhFFWCBRTsIsCnCkAp2OKADPelzSUCmAtLSUooAWiiigYVT1O0N3ZlY/9ah3J9fSrlKuNw+tF7CaucNJMeVIIOeQex71BuLZOa0PECBNVnwMbjn9KzFx610LU53o7FiFlzh0JHqK0oCsZlTtgMv41WtQpQ7mwfpmp2cF1K88bcgcGqW4ixEcXMHHJkFdAOtYEUm/UIMqwCuAOOK36xrbm1LYKKOKUYB5rE1Aj5c0zGBT3aoyaBCp/F9KjJp6/wAX+6aZTASmNzTzTCKAG0UpFFMRZHFOJ4p22kxxVuIDKWjHNLiosAlKDQRSUDHCloFLQA2lX7w+tBoX74+tAHL+Jl/4mOfVQf1NZ8EQZdwBY/StPxJzqCLj/ln/AOzGs+3YA44HFdENkc89ywjzqyhYwPcnpVm7kFvZNtAG0gj65piNtGTjNR3R86Jk45BrR6ECtJMLhJI8FWAP/wBeuoHQE9e+K5TTpRJaqG6p8tdNA++3jb2FY1lombUmS0n40maTPPSuc2A0Ud6M0AKvRv8AdNRmnqfvfQ0ygQ00GjPtTWPNMBpooopAaWKQgVIVxUZ6V0kjMc0uOaUDmnque1ZPcZEV5o21Iy89KQLUPcYAUYp2KMVQEZFCj5h9aeRSAfMPrQBy/iLnUwP+mX/sxrNgBznGa2Nfs7h7p7pFBiWMLnPTk9qyoYM4V5PnPTLYB/KtotJHPJPmJ8Fl6YFDARRszkAYwKJdOJjEqs4Ufe+ckCsoqyyYbJ54zVXuTaxZ02cR3Txt0cfrXWae260A/ukiuLeBg4PA+ldlpcYTTYMDllBOT1NRUfu2NKS1LdJTsUmK5zcT3pDTjTaABerf7pphqRRy30NMPWgBuMU1qeaa1AhlFLxRQBsMoxTCBTTLTC+a6XJWJsPANSDgVAHpS9ZDHseaFNRbqUNU9Rk2RSZFR7qXdTuApxSDG4fUU0mkB+YfWjmAhvkMlrcKvUqcfWuShnYKfLAVT94NhgD9DXYSH74+tcYvDHjkcGrgzOZaEkxypuTAGGPkUBWH4dKyzIEmYDMgXoTxV7Yrqe57Gs2YFbltvBrQyZKXLc+tdlYjbYW4/wCmYrjFGSoruIl2Qxr6KB+lZVDWmPpKKKyNRKDiikoAcnVv900w9ach5P0NMoAQ000401qAGmikJooAs76XdzRRTbEKGpd2aKKEwANS54oop3EAal3UUVJQZoB+YfWiigBG+8frXL6haeTdSyRfOgPzoOozz+VFFaUtzOpsRxAMhccAdQ3BH+NZ1xzdN+FFFbIxexLap5l1Go7sBXa9KKKyqm1PYSkzRRWRoFFFFAAvU/Q02iigQ0mmGiigYhooooEf/9k="
IMG_YASHWANTH = "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"

# ── CONSTANTS ─────────────────────────────────────────────────────────────────
CONTACT_EMAIL  = "scienceclubmecs@gmail.com"
LUMA_IDEATHON  = "https://lu.ma/34izlhhj"
LUMA_MEETUP    = "https://lu.ma/4e3p9fdx"

# ── RENDER HELPER ─────────────────────────────────────────────────────────────
def render(html_str):
    lines = [l for l in html_str.split("\n") if l.strip()]
    st.markdown("\n".join(lines), unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# CSS — Modern Oceanic Minimal Theme
# ══════════════════════════════════════════════════════════════════════════════
CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Inter:wght@300;400;500;600&display=swap');

/* ── RESET / TOKENS ── */
*{box-sizing:border-box;margin:0;padding:0;}
:root{
  --primary:#38BDF8;
  --secondary:#A78BFA;
  --accent:#F472B6;
  --cyan:#22D3EE;
  --bg:#020617;
  --bg2:#0F172A;
  --text:#E2E8F0;
  --text-muted:rgba(226,232,240,0.55);
  --glass:rgba(255,255,255,0.05);
  --glass-border:rgba(255,255,255,0.10);
  --radius:16px;
}

/* ── STREAMLIT CHROME ── */
#MainMenu,footer,header,[data-testid="stHeader"],[data-testid="collapsedControl"]{display:none!important;}
[data-testid="stAppViewContainer"]{background:var(--bg)!important;min-height:100vh;}
[data-testid="stMain"]{background:transparent!important;}
.block-container{padding:0 1rem 5rem 1rem!important;max-width:1100px;margin:0 auto;}
@media(min-width:768px){.block-container{padding:0 2.5rem 5rem 2.5rem!important;}}

/* ── BACKGROUND GRADIENT OVERLAY ── */
[data-testid="stAppViewContainer"]::before{
  content:'';position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none;
  background:
    radial-gradient(ellipse 80% 60% at 20% 0%,rgba(56,189,248,0.12) 0%,transparent 60%),
    radial-gradient(ellipse 60% 50% at 80% 20%,rgba(167,139,250,0.10) 0%,transparent 55%),
    radial-gradient(ellipse 50% 40% at 50% 100%,rgba(34,211,238,0.08) 0%,transparent 60%);
}

/* ── KEYFRAMES ── */
@keyframes gradientShift{
  0%,100%{background-position:0% 50%;}
  50%{background-position:100% 50%;}}
@keyframes fadeUp{
  from{opacity:0;transform:translateY(28px);}
  to{opacity:1;transform:translateY(0);}}
@keyframes float{
  0%,100%{transform:translateY(0);}
  50%{transform:translateY(-18px);}}
@keyframes bubbleRise{
  0%{bottom:-80px;opacity:0;}
  10%{opacity:0.35;}
  85%{opacity:0.15;}
  100%{bottom:105vh;opacity:0;}}
@keyframes swimLeft{0%{left:105%;}100%{left:-20%;}}
@keyframes swimRight{0%{left:-20%;}100%{left:105%;}}
@keyframes pulse{0%,100%{opacity:0.7;}50%{opacity:1;}}

/* ── BUBBLES ── */
.bbl-wrap{position:fixed;width:100%;height:100vh;top:0;left:0;pointer-events:none;z-index:0;overflow:hidden;}
.bbl{position:absolute;border-radius:50%;background:radial-gradient(circle at 35% 35%,rgba(56,189,248,0.3),rgba(14,165,233,0.05));border:1px solid rgba(56,189,248,0.15);animation:bubbleRise linear infinite;}

/* ── SHARK SILHOUETTES ── */
.shark-layer{position:fixed;width:100%;height:100%;top:0;left:0;pointer-events:none;z-index:0;overflow:hidden;}
.shk{position:absolute;opacity:0.04;}
.shk-l{animation:swimLeft linear infinite;}
.shk-r{animation:swimRight linear infinite;}

/* ── SECTIONS ── */
.sp-section{
  background:var(--glass);
  border:1px solid var(--glass-border);
  border-radius:var(--radius);
  backdrop-filter:blur(12px);
  -webkit-backdrop-filter:blur(12px);
  padding:clamp(1.4rem,4vw,2.8rem) clamp(1.2rem,4vw,2.4rem);
  margin:1.6rem 0;
  position:relative;
  overflow:hidden;
  animation:fadeUp 0.7s ease both;
  transition:border-color 0.3s ease,box-shadow 0.3s ease;
  z-index:1;}
.sp-section::before{
  content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,var(--primary),var(--secondary),transparent);
  opacity:0.5;}

/* ── TYPOGRAPHY ── */
.sp-label{
  font-family:'Orbitron',sans-serif;font-size:clamp(9px,1.6vw,11px);
  font-weight:600;letter-spacing:4px;color:var(--primary);
  text-transform:uppercase;margin-bottom:.5rem;opacity:.8;}
.sp-title{
  font-family:'Orbitron',sans-serif;font-weight:900;
  font-size:clamp(22px,5vw,48px);letter-spacing:2px;
  background:linear-gradient(90deg,var(--cyan),var(--primary),var(--secondary),var(--accent),var(--cyan));
  background-size:300% 300%;
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  animation:gradientShift 6s ease infinite;
  margin-bottom:.6rem;line-height:1.2;}
.sp-body{
  font-family:'Inter',sans-serif;font-size:clamp(13px,2vw,15px);
  color:var(--text-muted);line-height:1.85;font-weight:400;}

/* ── HERO ── */
.hero-wrap{
  text-align:center;padding:clamp(3rem,8vw,6rem) 1rem clamp(2.5rem,6vw,4.5rem);
  position:relative;z-index:1;}
.hero-eyebrow{
  font-family:'Inter',sans-serif;font-size:clamp(10px,1.8vw,13px);
  font-weight:500;letter-spacing:5px;color:var(--primary);
  text-transform:uppercase;margin-bottom:1.2rem;opacity:.85;}
.hero-title{
  font-family:'Orbitron',sans-serif;font-weight:900;
  font-size:clamp(54px,14vw,160px);letter-spacing:6px;
  white-space:nowrap;
  background:linear-gradient(90deg,var(--cyan),var(--primary),var(--secondary),var(--accent),var(--cyan));
  background-size:300% 300%;
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  animation:gradientShift 5s ease infinite,float 6s ease-in-out infinite;
  line-height:1;margin-bottom:1rem;}
.hero-tagline{
  font-family:'Inter',sans-serif;font-size:clamp(14px,2.5vw,22px);
  font-weight:300;letter-spacing:3px;color:var(--text);
  margin-bottom:1.4rem;opacity:.9;}
.hero-desc{
  font-family:'Inter',sans-serif;font-size:clamp(12px,1.8vw,14px);
  color:var(--text-muted);max-width:540px;margin:0 auto 2rem;line-height:1.8;}
.hero-cta{
  display:inline-block;
  background:linear-gradient(135deg,var(--cyan),var(--secondary));
  color:#020617;font-family:'Orbitron',sans-serif;font-weight:700;
  font-size:clamp(11px,1.8vw,13px);letter-spacing:3px;
  padding:clamp(12px,2vw,16px) clamp(28px,5vw,48px);
  border-radius:50px;text-decoration:none;
  box-shadow:0 8px 32px rgba(56,189,248,0.30);
  transition:transform 0.3s ease,box-shadow 0.3s ease;}
.hero-cta:hover{transform:translateY(-3px) scale(1.03);box-shadow:0 14px 42px rgba(56,189,248,0.50);text-decoration:none;color:#020617;}

/* ── INFO CHIP ── */
.chip{
  display:inline-block;
  border:1px solid rgba(56,189,248,0.3);border-radius:100px;
  background:rgba(56,189,248,0.07);
  font-family:'Inter',sans-serif;font-size:clamp(10px,1.5vw,12px);
  color:var(--primary);padding:6px 16px;letter-spacing:1.5px;
  margin-bottom:1.2rem;}

/* ── JUDGE CARDS ── */
.jg-grid{display:grid;grid-template-columns:1fr;gap:1.2rem;margin-top:1.6rem;}
@media(min-width:580px){.jg-grid{grid-template-columns:repeat(3,1fr);gap:1.4rem;}}
.jg-card{
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(255,255,255,0.09);
  border-radius:var(--radius);padding:1.4rem 1.2rem;
  text-align:center;
  transition:transform 0.3s ease,border-color 0.3s ease,box-shadow 0.3s ease;
  animation:fadeUp 0.7s ease both;}
.jg-card:hover{transform:translateY(-8px);border-color:rgba(56,189,248,0.35);box-shadow:0 20px 48px rgba(56,189,248,0.12);}
.jg-card:nth-child(1){animation-delay:.1s;}
.jg-card:nth-child(2){animation-delay:.2s;}
.jg-card:nth-child(3){animation-delay:.3s;}
.ph-ring{
  width:clamp(90px,16vw,120px);height:clamp(90px,16vw,120px);
  border-radius:50%;margin:0 auto 1rem;
  background:linear-gradient(135deg,var(--primary),var(--secondary));
  padding:2px;overflow:hidden;}
.ph-ring img{width:100%;height:100%;object-fit:cover;object-position:center top;border-radius:50%;}
.jg-name{
  font-family:'Orbitron',sans-serif;font-size:clamp(12px,2.2vw,15px);
  font-weight:700;color:var(--text);letter-spacing:1.5px;margin-bottom:.3rem;}
.jg-role{
  font-family:'Inter',sans-serif;font-size:clamp(9px,1.5vw,11px);
  color:var(--primary);letter-spacing:2px;margin-bottom:.6rem;font-weight:500;}
.jg-co{
  font-family:'Inter',sans-serif;font-size:clamp(9px,1.4vw,11px);
  color:var(--text-muted);letter-spacing:1px;margin-bottom:.8rem;}
.jg-bio{
  font-family:'Inter',sans-serif;font-size:clamp(11px,1.6vw,12px);
  color:var(--text-muted);line-height:1.7;text-align:left;margin-bottom:1rem;}
.jg-tags{display:flex;flex-wrap:wrap;gap:5px;justify-content:center;margin-bottom:1rem;}
.jg-tag{
  font-family:'Inter',sans-serif;font-size:9px;
  border:1px solid rgba(56,189,248,0.25);border-radius:100px;
  color:var(--primary);padding:3px 9px;letter-spacing:1px;
  background:rgba(56,189,248,0.06);}
.jg-li{
  display:inline-block;font-family:'Inter',sans-serif;font-size:11px;
  font-weight:500;letter-spacing:1.5px;color:var(--primary);
  border:1px solid rgba(56,189,248,0.35);border-radius:100px;
  padding:6px 16px;text-decoration:none;
  transition:background 0.3s ease,color 0.3s ease;}
.jg-li:hover{background:var(--primary);color:#020617;text-decoration:none;}

/* ── REGISTRATION CARDS ── */
.rg-grid{display:grid;grid-template-columns:1fr;gap:1.2rem;margin-top:1.6rem;}
@media(min-width:580px){.rg-grid{grid-template-columns:1fr 1fr;gap:1.4rem;}}
.rg-card{
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(255,255,255,0.09);
  border-radius:var(--radius);padding:1.8rem 1.4rem;
  text-align:center;
  transition:transform 0.3s ease,border-color 0.3s ease,box-shadow 0.3s ease;}
.rg-card:hover{transform:translateY(-6px);}
.rg-card-a{animation:fadeUp .7s ease .1s both;}
.rg-card-a:hover{border-color:rgba(244,114,182,0.4);box-shadow:0 16px 40px rgba(244,114,182,0.1);}
.rg-card-b{animation:fadeUp .7s ease .2s both;}
.rg-card-b:hover{border-color:rgba(56,189,248,0.4);box-shadow:0 16px 40px rgba(56,189,248,0.1);}
.rg-badge-a{display:inline-block;background:rgba(244,114,182,0.12);border:1px solid rgba(244,114,182,0.3);border-radius:100px;color:var(--accent);font-family:'Inter',sans-serif;font-size:9px;letter-spacing:2.5px;padding:4px 14px;margin-bottom:1rem;}
.rg-badge-b{display:inline-block;background:rgba(56,189,248,0.10);border:1px solid rgba(56,189,248,0.3);border-radius:100px;color:var(--primary);font-family:'Inter',sans-serif;font-size:9px;letter-spacing:2.5px;padding:4px 14px;margin-bottom:1rem;}
.rg-icon{font-size:clamp(36px,6vw,50px);display:block;margin-bottom:.8rem;}
.rg-title{font-family:'Orbitron',sans-serif;font-size:clamp(20px,4vw,30px);font-weight:900;color:var(--text);letter-spacing:3px;margin-bottom:.4rem;}
.rg-sub-a{font-family:'Inter',sans-serif;font-size:11px;letter-spacing:2px;color:var(--accent);margin-bottom:.8rem;}
.rg-sub-b{font-family:'Inter',sans-serif;font-size:11px;letter-spacing:2px;color:var(--primary);margin-bottom:.8rem;}
.rg-divider{border:none;border-top:1px solid rgba(255,255,255,0.07);margin:.8rem 0;}
.rg-desc{font-family:'Inter',sans-serif;font-size:clamp(11px,1.6vw,13px);color:var(--text-muted);line-height:1.8;text-align:left;margin-bottom:1.4rem;}
.rg-btn-a{
  display:block;width:100%;
  background:linear-gradient(135deg,var(--accent),#c84b8e);
  color:#fff;font-family:'Orbitron',sans-serif;font-size:12px;
  font-weight:700;letter-spacing:3px;border-radius:50px;padding:13px;
  text-align:center;text-decoration:none;
  box-shadow:0 6px 24px rgba(244,114,182,0.30);
  transition:transform 0.3s,box-shadow 0.3s;}
.rg-btn-a:hover{transform:scale(1.03);box-shadow:0 10px 32px rgba(244,114,182,0.5);text-decoration:none;color:#fff;}
.rg-btn-b{
  display:block;width:100%;
  background:linear-gradient(135deg,var(--cyan),var(--primary));
  color:#020617;font-family:'Orbitron',sans-serif;font-size:12px;
  font-weight:700;letter-spacing:3px;border-radius:50px;padding:13px;
  text-align:center;text-decoration:none;
  box-shadow:0 6px 24px rgba(56,189,248,0.30);
  transition:transform 0.3s,box-shadow 0.3s;}
.rg-btn-b:hover{transform:scale(1.03);box-shadow:0 10px 32px rgba(56,189,248,0.5);text-decoration:none;color:#020617;}
.rg-note{font-family:'Inter',sans-serif;font-size:10px;letter-spacing:2px;color:var(--text-muted);text-align:center;margin-top:.8rem;opacity:.6;}

/* ── TIMELINE ── */
.tl-wrap{position:relative;margin:2rem 0;padding:0 0 1rem;}
.tl-line{position:absolute;left:50%;top:0;bottom:0;width:1px;background:linear-gradient(180deg,var(--primary),var(--secondary));transform:translateX(-50%);}
@media(max-width:599px){.tl-line{left:16px;}}
.tl-row{display:flex;align-items:flex-start;margin-bottom:2.8rem;position:relative;}
.tl-dot{
  width:18px;height:18px;border-radius:50%;
  background:linear-gradient(135deg,var(--primary),var(--secondary));
  flex-shrink:0;position:absolute;left:50%;top:18px;
  transform:translateX(-50%);z-index:2;
  animation:pulse 2s ease-in-out infinite;}
.tl-box{
  width:calc(50% - 26px);
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(255,255,255,0.08);
  border-radius:12px;padding:1.1rem 1.2rem;
  transition:border-color 0.3s,box-shadow 0.3s;}
.tl-box:hover{border-color:rgba(56,189,248,0.3);box-shadow:0 8px 24px rgba(56,189,248,0.1);}
.tl-left .tl-box{margin-right:auto;margin-left:0;text-align:right;}
.tl-right .tl-box{margin-left:auto;margin-right:0;text-align:left;}
@media(max-width:599px){
  .tl-line{left:16px;}
  .tl-dot{left:16px;top:18px;transform:none;}
  .tl-box{width:calc(100% - 44px);margin-left:44px!important;margin-right:0!important;text-align:left!important;}}
.tl-date{font-family:'Inter',sans-serif;font-size:10px;color:var(--primary);letter-spacing:2.5px;font-weight:600;margin-bottom:.3rem;text-transform:uppercase;}
.tl-head{font-family:'Orbitron',sans-serif;font-size:clamp(13px,2.2vw,16px);color:var(--text);letter-spacing:1.5px;margin-bottom:.4rem;font-weight:700;}
.tl-detail{font-family:'Inter',sans-serif;font-size:clamp(11px,1.6vw,13px);color:var(--text-muted);line-height:1.7;}

/* ── GUIDELINES GRID ── */
.gl-grid{display:grid;grid-template-columns:1fr 1fr;gap:.8rem;margin-top:1.4rem;}
@media(min-width:768px){.gl-grid{grid-template-columns:repeat(4,1fr);gap:1rem;}}
.gl-card{
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(255,255,255,0.08);
  border-radius:12px;padding:.9rem 1rem;
  display:flex;align-items:flex-start;gap:10px;
  transition:border-color 0.3s,box-shadow 0.3s;
  animation:fadeUp .6s ease both;}
.gl-card:hover{border-color:rgba(56,189,248,0.3);box-shadow:0 6px 20px rgba(56,189,248,0.1);}
.gl-icon{font-size:18px;flex-shrink:0;margin-top:1px;}
.gl-text{font-family:'Inter',sans-serif;font-size:clamp(11px,1.6vw,13px);color:var(--text-muted);line-height:1.6;}

/* ── BENEFITS ── */
.bn-grid{display:grid;grid-template-columns:1fr;gap:1rem;margin-top:1.4rem;}
@media(min-width:480px){.bn-grid{grid-template-columns:repeat(3,1fr);}}
.bn-card{
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(255,255,255,0.08);
  border-radius:var(--radius);padding:1.4rem 1.2rem;text-align:center;
  transition:transform 0.3s,border-color 0.3s,box-shadow 0.3s;
  animation:fadeUp .7s ease both;}
.bn-card:hover{transform:translateY(-5px);border-color:rgba(167,139,250,0.3);box-shadow:0 12px 32px rgba(167,139,250,0.1);}
.bn-icon{font-size:clamp(28px,5vw,38px);display:block;margin-bottom:.8rem;}
.bn-title{font-family:'Orbitron',sans-serif;font-size:clamp(11px,2vw,14px);font-weight:700;color:var(--text);letter-spacing:2px;margin-bottom:.5rem;}
.bn-desc{font-family:'Inter',sans-serif;font-size:clamp(11px,1.6vw,13px);color:var(--text-muted);line-height:1.7;}

/* ── FORM OVERRIDES ── */
.stTextInput>div>div>input,
.stTextArea>div>div>textarea{
  background:rgba(15,23,42,0.9)!important;
  border:1px solid rgba(56,189,248,0.25)!important;
  border-radius:10px!important;
  color:var(--text)!important;
  font-family:'Inter',sans-serif!important;font-size:14px!important;}
.stTextInput>div>div>input:focus,
.stTextArea>div>div>textarea:focus{
  border-color:var(--primary)!important;
  box-shadow:0 0 0 2px rgba(56,189,248,0.15)!important;}
label[data-baseweb="label"],.stTextInput label,.stTextArea label{
  font-family:'Inter',sans-serif!important;font-size:11px!important;
  font-weight:500!important;letter-spacing:2px!important;
  color:var(--primary)!important;text-transform:uppercase!important;}
.stButton>button{
  font-family:'Orbitron',sans-serif!important;font-size:12px!important;
  font-weight:700!important;letter-spacing:3px!important;
  background:linear-gradient(135deg,var(--cyan),var(--secondary))!important;
  color:#020617!important;border:none!important;
  border-radius:50px!important;padding:12px 36px!important;
  transition:transform 0.3s,box-shadow 0.3s!important;width:100%!important;}
.stButton>button:hover{
  transform:scale(1.04)!important;
  box-shadow:0 8px 28px rgba(56,189,248,0.4)!important;}

/* ── SUCCESS / WARN BOXES ── */
.ok-box{
  border:1px solid rgba(56,189,248,0.4);border-radius:12px;
  background:rgba(56,189,248,0.06);padding:14px 20px;
  font-family:'Inter',sans-serif;font-size:12px;
  color:var(--primary);letter-spacing:1px;margin-top:1rem;line-height:1.6;}
.ok-box a{color:var(--secondary);}

/* ── Q&A THREAD ── */
.qa-item{
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(255,255,255,0.08);
  border-radius:12px;padding:1.2rem 1.4rem;
  margin-bottom:1.2rem;
  transition:border-color 0.3s;}
.qa-item:hover{border-color:rgba(56,189,248,0.25);}
.qa-who{font-family:'Inter',sans-serif;font-size:10px;color:var(--primary);letter-spacing:2.5px;font-weight:600;margin-bottom:.4rem;text-transform:uppercase;}
.qa-q{font-family:'Inter',sans-serif;font-size:clamp(12px,1.8vw,14px);color:var(--text);margin-bottom:.8rem;line-height:1.6;}
.qa-reply{border-left:2px solid var(--primary);padding-left:12px;font-family:'Inter',sans-serif;font-size:clamp(11px,1.6vw,13px);color:var(--text-muted);font-style:italic;line-height:1.6;}
.qa-label{font-family:'Inter',sans-serif;font-size:9px;color:var(--primary);letter-spacing:2.5px;font-weight:600;margin-bottom:.3rem;text-transform:uppercase;}

/* ── FOOTER ── */
.sp-footer{
  text-align:center;padding:3rem 1rem 2rem;
  border-top:1px solid rgba(255,255,255,0.07);
  margin-top:2rem;position:relative;z-index:1;}
.ft-title{font-family:'Orbitron',sans-serif;font-size:clamp(14px,3vw,24px);font-weight:900;letter-spacing:4px;color:var(--text);margin-bottom:.4rem;}
.ft-sub{font-family:'Inter',sans-serif;font-size:11px;letter-spacing:2.5px;color:var(--text-muted);}
.ft-tag{font-family:'Inter',sans-serif;font-size:10px;letter-spacing:4px;color:rgba(226,232,240,0.3);margin-top:.6rem;}
.ft-icons{font-size:18px;letter-spacing:10px;margin-top:.8rem;opacity:.4;}

/* ── TOP BAR ── */
.top-bar{
  font-family:'Orbitron',sans-serif;font-size:clamp(9px,1.5vw,11px);
  font-weight:600;letter-spacing:3px;color:var(--primary);
  padding:.8rem 0;opacity:.8;position:relative;z-index:1;}

/* ── DIVIDER ── */
.sp-divider{
  height:1px;border:none;
  background:linear-gradient(90deg,transparent,rgba(56,189,248,0.3),rgba(167,139,250,0.3),transparent);
  margin:1.5rem 0;}

/* ── COLUMN GAP ── */
[data-testid="stHorizontalBlock"]{gap:.5rem!important;}
</style>"""

st.markdown(CSS, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# BACKGROUND — Bubbles + Shark Silhouettes
# ══════════════════════════════════════════════════════════════════════════════
SHARK_SVG = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 260 100'><ellipse cx='120' cy='50' rx='110' ry='34' fill='none' stroke='white' stroke-width='1.5'/><polygon points='230,50 260,30 260,70' fill='none' stroke='white' stroke-width='1.5'/><polygon points='120,16 102,2 138,2' fill='none' stroke='white' stroke-width='1.5'/><path d='M90,54 Q76,76 56,84 Q82,64 86,54' fill='none' stroke='white' stroke-width='1.5'/><circle cx='196' cy='42' r='3.5' fill='white' opacity='0.7'/></svg>"

render(
    "<div class='bbl-wrap'>"
    "<div class='bbl' style='width:6px;height:6px;left:8%;animation-duration:11s;animation-delay:0s;'></div>"
    "<div class='bbl' style='width:12px;height:12px;left:16%;animation-duration:15s;animation-delay:1.5s;'></div>"
    "<div class='bbl' style='width:5px;height:5px;left:24%;animation-duration:9s;animation-delay:3s;'></div>"
    "<div class='bbl' style='width:18px;height:18px;left:33%;animation-duration:18s;animation-delay:.7s;'></div>"
    "<div class='bbl' style='width:9px;height:9px;left:41%;animation-duration:13s;animation-delay:2s;'></div>"
    "<div class='bbl' style='width:14px;height:14px;left:50%;animation-duration:20s;animation-delay:4.2s;'></div>"
    "<div class='bbl' style='width:7px;height:7px;left:58%;animation-duration:10s;animation-delay:.3s;'></div>"
    "<div class='bbl' style='width:22px;height:22px;left:66%;animation-duration:22s;animation-delay:2.5s;'></div>"
    "<div class='bbl' style='width:10px;height:10px;left:74%;animation-duration:14s;animation-delay:1s;'></div>"
    "<div class='bbl' style='width:28px;height:28px;left:82%;animation-duration:19s;animation-delay:3.5s;'></div>"
    "<div class='bbl' style='width:8px;height:8px;left:90%;animation-duration:12s;animation-delay:.9s;'></div>"
    "<div class='bbl' style='width:16px;height:16px;left:5%;animation-duration:17s;animation-delay:5s;'></div>"
    "</div>"
    "<div class='shark-layer'>"
    "<div class='shk shk-l' style='top:18%;width:240px;animation-duration:30s;animation-delay:0s;'>" + SHARK_SVG + "</div>"
    "<div class='shk shk-r' style='top:42%;width:180px;animation-duration:24s;animation-delay:8s;transform:scaleX(-1);'>" + SHARK_SVG + "</div>"
    "<div class='shk shk-l' style='top:62%;width:300px;animation-duration:36s;animation-delay:16s;'>" + SHARK_SVG + "</div>"
    "<div class='shk shk-r' style='top:78%;width:150px;animation-duration:20s;animation-delay:5s;transform:scaleX(-1);'>" + SHARK_SVG + "</div>"
    "</div>"
)

# ══════════════════════════════════════════════════════════════════════════════
# TOP BAR
# ══════════════════════════════════════════════════════════════════════════════
render("<div class='top-bar'>\U0001f988 &nbsp; S&amp;T CLUB &nbsp;&middot;&nbsp; MATRUSRI ENGINEERING COLLEGE &nbsp;&middot;&nbsp; SHARKPIT 2026</div>")

# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
render(
    "<div class='hero-wrap'>"
    "<div class='hero-eyebrow'>Science &amp; Technology Club &nbsp;&middot;&nbsp; MECS &nbsp;&middot;&nbsp; 2026</div>"
    "<div class='hero-title'>SHARKPIT</div>"
    "<div class='hero-tagline'>Pitch &nbsp;&middot;&nbsp; Innovate &nbsp;&middot;&nbsp; Win</div>"
    "<div class='hero-desc'>The premier startup pitch competition for every B.Tech student at Matrusri Engineering College. Face the Sharks. Defend your idea. Claim the crown.</div>"
    "<a class='hero-cta' href='https://lu.ma/34izlhhj' target='_blank'>REGISTER NOW &rarr;</a>"
    "</div>"
)

# ══════════════════════════════════════════════════════════════════════════════
# ABOUT
# ══════════════════════════════════════════════════════════════════════════════
render(
    "<div class='sp-section'>"
    "<div class='sp-label'>About the Event</div>"
    "<div class='sp-title'>What is SHARKPIT?</div>"
    "<div class='chip'>Open to ALL B.Tech years &nbsp;&middot;&nbsp; Technical &amp; Non-Technical ideas welcome</div>"
    "<div class='sp-body'>SHARKPIT is a high-energy student startup pitch competition and ideathon organised by the S&amp;T Club of MECS. Inspired by investor pitch formats, it challenges students to think like entrepreneurs and defend their ideas before experienced industry founders &mdash; the Sharks.<br/><br/>The event has two parts: a morning casual open meetup for all students, and exclusive evening finals where the top 20 shortlisted teams pitch live before the Sharks. Whether you&rsquo;re technical or non-technical, any B.Tech student with a bold idea can compete.</div>"
    "</div>"
)

# ══════════════════════════════════════════════════════════════════════════════
# WHY PARTICIPATE
# ══════════════════════════════════════════════════════════════════════════════
render(
    "<div class='sp-section'>"
    "<div class='sp-label'>Why Join</div>"
    "<div class='sp-title'>Why Participate?</div>"
    "<div class='bn-grid'>"
    "<div class='bn-card' style='animation-delay:.1s;'>"
    "<span class='bn-icon'>\U0001f4a1</span>"
    "<div class='bn-title'>INNOVATE</div>"
    "<div class='bn-desc'>Turn your raw ideas into structured pitches. Learn to think like a founder and build solutions that matter.</div>"
    "</div>"
    "<div class='bn-card' style='animation-delay:.2s;'>"
    "<span class='bn-icon'>\U0001f91d</span>"
    "<div class='bn-title'>NETWORK</div>"
    "<div class='bn-desc'>Connect with fellow students, industry founders, and mentors who can help shape your entrepreneurial journey.</div>"
    "</div>"
    "<div class='bn-card' style='animation-delay:.3s;'>"
    "<span class='bn-icon'>\U0001f3c6</span>"
    "<div class='bn-title'>EXPOSURE</div>"
    "<div class='bn-desc'>Pitch live before real Shark investors &amp; founders. Gain stage experience and earn certificates recognised by the college.</div>"
    "</div>"
    "</div>"
    "</div>"
)

# ══════════════════════════════════════════════════════════════════════════════
# MEET THE SHARKS
# ══════════════════════════════════════════════════════════════════════════════
render(
    "<div class='sp-section'>"
    "<div class='sp-label'>Jury Panel</div>"
    "<div class='sp-title'>Meet the Sharks</div>"
    "<div class='sp-body' style='margin-bottom:0;'>Three visionary founders. One arena. Zero mercy on weak pitches.</div>"
    "<div class='jg-grid'>"

    # Card 1 — E Sai Eshwar
    "<div class='jg-card'>"
    "<div class='ph-ring'><img src='data:image/jpeg;base64," + IMG_ESHWAR + "' alt='E Sai Eshwar'/></div>"
    "<div class='jg-name'>E SAI ESHWAR</div>"
    "<div class='jg-role'>Founder &middot; Ecosystem Operator</div>"
    "<div class='jg-co'>\U0001f680 Studlyf &nbsp;&middot;&nbsp; Nirvaha &nbsp;&middot;&nbsp; GuideBazaar</div>"
    "<div class='jg-bio'>Operates at the intersection of Applied AI, strategy, and social impact. 12x national hackathon finalist, mentors 600+ students, and has delivered 10+ public speaking sessions on AI &amp; entrepreneurship.</div>"
    "<div class='jg-tags'><span class='jg-tag'>Applied AI</span><span class='jg-tag'>Product</span><span class='jg-tag'>Mentorship</span></div>"
    "<a class='jg-li' href='https://linkedin.com/in/esaieshwar' target='_blank'>\U0001f517 LinkedIn</a>"
    "</div>"

    # Card 2 — Yashwanth Bondapalli
    "<div class='jg-card'>"
    "<div class='ph-ring'><img src='data:image/jpeg;base64," + IMG_YASHWANTH + "' alt='Yashwanth Bondapalli'/></div>"
    "<div class='jg-name'>YASHWANTH BONDAPALLI</div>"
    "<div class='jg-role'>AI &amp; Cybersecurity &middot; Founder</div>"
    "<div class='jg-co'>&#9889; Back to Base XYZ</div>"
    "<div class='jg-bio'>Builds production-grade LLM and RAG systems. Speaker at GitTogether Hyderabad, organised by GitHub India and supported by Microsoft. Combines AI expertise with a security-first mindset.</div>"
    "<div class='jg-tags'><span class='jg-tag'>AI / LLMs</span><span class='jg-tag'>RAG</span><span class='jg-tag'>Cybersecurity</span></div>"
    "<a class='jg-li' href='https://linkedin.com/in/yashwanth-bondapalli-37b6a7255' target='_blank'>\U0001f517 LinkedIn</a>"
    "</div>"

    # Card 3 — Sai Harishith
    "<div class='jg-card'>"
    "<div class='ph-ring'><img src='data:image/jpeg;base64," + IMG_HARISHITH + "' alt='Sai Harishith'/></div>"
    "<div class='jg-name'>SAI HARISHITH</div>"
    "<div class='jg-role'>Founder &amp; Director</div>"
    "<div class='jg-co'>\U0001f6e1\ufe0f ShieldNet Solutions</div>"
    "<div class='jg-bio'>Built ShieldNet Solutions from the ground up — a full-service tech company delivering cybersecurity, web &amp; mobile development, and network administration. Leads with a security-first approach.</div>"
    "<div class='jg-tags'><span class='jg-tag'>Cybersecurity</span><span class='jg-tag'>Web &amp; Mobile</span><span class='jg-tag'>Network</span></div>"
    "<a class='jg-li' href='https://linkedin.com/in/sai-harishith-b37558322' target='_blank'>\U0001f517 LinkedIn</a>"
    "</div>"

    "</div>"
    "</div>"
)

# ══════════════════════════════════════════════════════════════════════════════
# REGISTER NOW
# ══════════════════════════════════════════════════════════════════════════════
render(
    "<div class='sp-section'>"
    "<div class='sp-label'>Registration</div>"
    "<div class='sp-title'>Register Now</div>"
    "<div class='sp-body' style='margin-bottom:1.4rem;'>Click on the following 2 links to register for your preferred session. Participation certificates will be shared online.</div>"
    "<div class='rg-grid'>"

    "<div class='rg-card rg-card-a'>"
    "<span class='rg-badge-a'>IDEATHON REGISTRATION</span>"
    "<span class='rg-icon'>\U0001f988</span>"
    "<div class='rg-title'>IDEATHON</div>"
    "<div class='rg-sub-a'>Evening Pitch Finals</div>"
    "<hr class='rg-divider'/>"
    "<div class='rg-desc'>Register on Luma to compete in the SHARKPIT ideathon. Submit your startup idea and pitch live before our Shark jury on March 17th. Requires idea submission before March 13th and approval via email. Top 20 teams shortlisted.</div>"
    "<a class='rg-btn-a' href='" + LUMA_IDEATHON + "' target='_blank'>REGISTER FOR SESSION &rarr;</a>"
    "<div class='rg-note'>Requires shortlisting &middot; March 17, 2026</div>"
    "</div>"

    "<div class='rg-card rg-card-b'>"
    "<span class='rg-badge-b'>OPEN MEETUP REGISTRATION</span>"
    "<span class='rg-icon'>\U0001f305</span>"
    "<div class='rg-title'>OPEN MEETUP</div>"
    "<div class='rg-sub-b'>Morning Casual Session</div>"
    "<hr class='rg-divider'/>"
    "<div class='rg-desc'>Register on Luma to attend the morning casual session. Come listen to our Shark founders speak, get inspired, and soak in the entrepreneurial energy. Open to every MECS student &mdash; no idea submission or approval needed.</div>"
    "<a class='rg-btn-b' href='" + LUMA_MEETUP + "' target='_blank'>REGISTER FOR SESSION &rarr;</a>"
    "<div class='rg-note'>Open to all &middot; March 17, 2026</div>"
    "</div>"

    "</div>"
    "</div>"
)

# ══════════════════════════════════════════════════════════════════════════════
# EVENT TIMELINE
# ══════════════════════════════════════════════════════════════════════════════
render(
    "<div class='sp-section'>"
    "<div class='sp-label'>Schedule</div>"
    "<div class='sp-title'>Event Timeline</div>"
    "<div class='sp-body' style='margin-bottom:0;'>From raw idea to the Shark Tank &mdash; here&rsquo;s the journey.</div>"
    "<div class='tl-wrap'>"
    "<div class='tl-line'></div>"

    "<div class='tl-row'>"
    "<div class='tl-box tl-left tl-box'>"
    "<div class='tl-date'>March 13, 2026</div>"
    "<div class='tl-head'>\U0001f4a1 Idea Submission Deadline</div>"
    "<div class='tl-detail'>Submit your startup idea before the cutoff. Include a problem statement, proposed solution, and team details. Teams of 1&ndash;4 MECS B.Tech students.</div>"
    "</div>"
    "<div class='tl-dot'></div>"
    "</div>"

    "<div class='tl-row'>"
    "<div class='tl-dot'></div>"
    "<div class='tl-box tl-right tl-box'>"
    "<div class='tl-date'>March 14 &ndash; 16, 2026</div>"
    "<div class='tl-head'>\U0001f4e7 Shortlisting via Email</div>"
    "<div class='tl-detail'>Our panel reviews all submissions and selects the Top 20 teams. Results communicated exclusively via email &mdash; check your inbox!</div>"
    "</div>"
    "</div>"

    "<div class='tl-row'>"
    "<div class='tl-box' style='width:calc(50% - 26px);text-align:right;'>"
    "<div class='tl-date'>March 17, 2026 &mdash; Morning</div>"
    "<div class='tl-head'>\U0001f305 Open Meetup Session</div>"
    "<div class='tl-detail'>All MECS students can attend. Listen to Shark founders speak, get inspired, and network with peers and mentors.</div>"
    "</div>"
    "<div class='tl-dot'></div>"
    "</div>"

    "<div class='tl-row'>"
    "<div class='tl-dot'></div>"
    "<div class='tl-box' style='width:calc(50% - 26px);margin-left:auto;text-align:left;'>"
    "<div class='tl-date'>March 17, 2026 &mdash; Evening</div>"
    "<div class='tl-head'>\U0001f988 Final Pitch Round</div>"
    "<div class='tl-detail'>Top 20 teams pitch live before the Sharks. Defend your idea. Claim your crown. Jury interaction &amp; final presentations.</div>"
    "</div>"
    "</div>"

    "</div>"
    "</div>"
)

# ══════════════════════════════════════════════════════════════════════════════
# PITCH GUIDELINES
# ══════════════════════════════════════════════════════════════════════════════
render(
    "<div class='sp-section'>"
    "<div class='sp-label'>Rules</div>"
    "<div class='sp-title'>Pitch Guidelines</div>"
    "<div class='sp-body' style='margin-bottom:0;'>Follow these rules. The Sharks are watching every second.</div>"
    "<div class='gl-grid'>"
    "<div class='gl-card' style='animation-delay:.05s;'><span class='gl-icon'>&#9201;</span><span class='gl-text'>10 minutes per team for pitching</span></div>"
    "<div class='gl-card' style='animation-delay:.10s;'><span class='gl-icon'>&#128101;</span><span class='gl-text'>Teams of 1 to 4 members</span></div>"
    "<div class='gl-card' style='animation-delay:.15s;'><span class='gl-icon'>&#127919;</span><span class='gl-text'>Cover problem, solution &amp; impact</span></div>"
    "<div class='gl-card' style='animation-delay:.20s;'><span class='gl-icon'>&#127979;</span><span class='gl-text'>Open to all B.Tech years at MECS</span></div>"
    "<div class='gl-card' style='animation-delay:.25s;'><span class='gl-icon'>\U0001f988</span><span class='gl-text'>Top 20 teams advance to finals</span></div>"
    "<div class='gl-card' style='animation-delay:.30s;'><span class='gl-icon'>&#128231;</span><span class='gl-text'>Shortlisting notified via email</span></div>"
    "<div class='gl-card' style='animation-delay:.35s;'><span class='gl-icon'>\U0001f680</span><span class='gl-text'>Original ideas only &mdash; no copying</span></div>"
    "</div>"
    "</div>"
)

# ══════════════════════════════════════════════════════════════════════════════
# ASK A QUERY
# ══════════════════════════════════════════════════════════════════════════════
render(
    "<div class='sp-section'>"
    "<div class='sp-label'>Contact</div>"
    "<div class='sp-title'>Ask a Query</div>"
    "<div class='sp-body'>Have a question about SHARKPIT 2026? Fill the form below &mdash; it will open your email app pre-filled and ready to send to us.</div>"
    "</div>"
)

_, qcol, _ = st.columns([0.3, 5, 0.3])
with qcol:
    q_name  = st.text_input("Your Name",  key="q_name",  placeholder="e.g. Ravi Kumar")
    q_email = st.text_input("Your Email", key="q_email", placeholder="e.g. ravi@student.mecs.edu")
    q_msg   = st.text_area("Your Query",  key="q_msg",   height=110, placeholder="Type your question here...")

    if st.button("\U0001f988  SUBMIT QUERY"):
        if q_name.strip() and q_email.strip() and q_msg.strip():
            subject = urllib.parse.quote(f"SHARKPIT 2026 Query from {q_name.strip()}")
            body    = urllib.parse.quote(
                f"Name: {q_name.strip()}\nEmail: {q_email.strip()}\n\nQuery:\n{q_msg.strip()}"
            )
            mailto  = f"mailto:{CONTACT_EMAIL}?subject={subject}&body={body}"
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

# ══════════════════════════════════════════════════════════════════════════════
# PUBLIC Q&A
# ══════════════════════════════════════════════════════════════════════════════
replied = [q for q in st.session_state.queries if q.get("reply")]
if replied:
    render(
        "<div class='sp-section'>"
        "<div class='sp-label'>Q &amp; A</div>"
        "<div class='sp-title'>Questions &amp; Answers</div>"
    )
    for q in replied:
        render(
            "<div class='qa-item'>"
            f"<div class='qa-who'>&mdash; {q['name']}</div>"
            f"<div class='qa-q'>{q['message']}</div>"
            "<div class='qa-reply'>"
            "<div class='qa-label'>Organiser Reply</div>"
            f"{q['reply']}"
            "</div>"
            "</div>"
        )
    render("</div>")

# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
render(
    "<div class='sp-footer'>"
    "<div class='ft-title'>MATRUSRI ENGINEERING COLLEGE</div>"
    "<div class='ft-sub'>Science &amp; Technology Club &nbsp;&middot;&nbsp; SHARKPIT 2026</div>"
    "<div class='ft-tag'>PITCH &nbsp;&middot;&nbsp; INNOVATE &nbsp;&middot;&nbsp; WIN</div>"
    "<div class='ft-icons'>\U0001f988 \U0001f4a1 \U0001f680</div>"
    "</div>"
)
