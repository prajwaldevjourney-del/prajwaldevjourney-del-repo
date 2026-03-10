# -*- coding: utf-8 -*-
import streamlit as st

st.set_page_config(page_title="SHARKPIT 2026 - S&T Club MECS", page_icon="\U0001f988", layout="wide")

# ── SESSION STATE ─────────────────────────────────────────────────────────────
if "queries" not in st.session_state:
    st.session_state.queries = []

IMG_HARISHITH = "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"
IMG_ESHWAR    = "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCADIAMgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCxPAjQlSy5ChdncNnk1Qa0PpXTPZ5kY46k1C1lx0ryJ11zM9CNJ8qRzhtSB0qNrc+ldC9mR0FRmyPpU+3H7IwDbnHSo2tfbFdEbI/3aY1l221Ttx+0R/3aY1l221Ttx+0QsrqfmQ/mKb5be9bLWf+zQ1nntTeqJU2jE8pvSnCJuwr/ABFaJsn/ALlA09vSqlUS3I5WZ6V0un2nkQbnHzN0HoKxIYfKtWaVhtLBEUnkn0FdBdl7a2jKglpGCAe/P+FcdauqjsfR5Vg5QXPJHSR3EMEn7vCr3CipZbhZ7MqsasS4IZBjPpmsSwt3eFrmfLSMchSMYz3rXs4tqB2bLDjb/jXHF8x9G0tEzEu9OsbiUefaQs7HliqFv1wRV9fEF9b26WlrbW0ECfL5eFAbHpjAHtVjWI1t7KW5CguqkrnHDdOf1rNs7VJra3lMzeXMDtGcENnnjt0NddBWicVRyfvFdrXUbl5Xup5GEjZMbFsL7cVf8NW2oX2sJpyyfLIWDyLjKqBknHfpXX3mjqmiXCwRuJnj2A8deRnHtXOeHIlQ2twm9JUbJ5GGB4OR6dK6bGXPzWPTLe1gtIjFbRJCh6qqhRUR03TmnM728LSk7vMKZP5msTXfF9npGq21h5sZedl3MGJKjJ5wBzgdcVt2d9ZX0CzW0yyrjkKcj8R2rBHRdGqbWHHEa/lTfs0HaJPyrKl8TaLAB5uqWa56DzQxH4ZpB4r8PkZ/tqwI6H/SF5/WoSfcHJdyS6sbaT70af8BFV0t4FIDQRtj+8orHvfil4Vs5PKi1Brt8E7LWNX59cmq+kfEHwr4ge6W01KSMwQPcMJ4Cmdo5Ud84zWijJq9jN1I32OnQW7gfIuMdhV3R9Bt9W1RLMahHEjAkzLETt47Z9q4KH4seGJJFin+3WzsdoeS3DqCfXBP8hXTWvjvw9dabfapb3ZFhaxb/Pl4ViM/IAeSSMfT1q4RcXqYzqxls7HWXUMWK5S7s7ab/VwRqF/hCDGPyrKuPFnhvy/K/tzT1JBOfPXcMn07UWPjrwtGDnXtPUk5AabqPxFaxV0+WxiqlN7S+8zNQ0+0Vf3drCAvPCDmuVm0XSppT51hbNn+8orqW8R+GJ0J/tyxRDxj7QoJNVhqPhWO4TZr1i2c5b7Qg5/OqUJLqZyrUV9pfecknh/SBJIhsYcIxx2zUy+HdGjcEafEcH+IZrv7vUvC1vY3FzHrum+ZGhYZnBY49gQa4+LxfpTXHkC+BYJ5mVyQRk9vfirShFa2MHiaD2udf8C9Ks9N1K4+y2yxSSWjqSoJJG9c81j2ul2M3h7UWlsobhvtsieZIgJGVOMZ6YzXV+BdR03VrK+bTb2K7WKfY5T+E7QcGp5ofJ8M6kD/wAtb6TOf90VnzJPY1cpOnzQaTR4/d6ZYCQKtjbr7KoFUZLaKGQpBGqqeg28V0d/G7XhcnI6VnPbTBt2x+v9016FJXWp5dWVpMoJC5mQgHOQa1Yoo/vFQSqE5I75FRJC+CSG5HI9K9X0DSfDGgeCbPULaxjlMikmaQBuT6dq5cbXVGKS6s9bJsC8TUlKStGPU+e5drxRBcBG6nB4rb0yWwtL/wAp/NEYJ+UvgFR2BrsNd02PUNVFzawWqwzfMFMajB9MYrzm5ge1v5oFuFZlkwGBB/WvUwuJ9pBSPJxuElQqyp30XQ9LJjjQb5B5ZO4njb9Kq3E0VskZSMLlvl7nPsa5bV7i6jnLiWVVZAMbuD7/SqYvLoXHlmaTqoAxnGe1eqqaS1PBdXUdqVxd6rNtaS5dXU/KoO0D8K6fw5rGo2jmwvZ5Ly3X5Y5mbJjPuehFee3XWNB5eDwOvPat/QhHqF8LK8dVidCV3KSoI9P8K0UVazOWpO50nirw9c3+jzXkVqEeHHnLMh3FeoyD3HrXjJ1LUJFaMysQG2bW4K49fwr6pgtoreJo4dqhlIkCrjdx71876v4J1a31aaK0tHltxK2y4JXG0H2OcetLlV7Iv2j5bHJ3t5dzqFZiD/AHiOvpVDZMUc7mJH97n/AOvXT6r4M8R6dIyyaS86k5HkjzAB9RWKLfVbMbJ7SaLHHzRN/Srmr7GXtEzGzIuArb898fpXSaVb3FvaQXYBEgILMWJCj3qlb6VqV3bGa3tJXQY+YIfT0q/4Xt5X1SK1V/lbO09yPw6U4U7O5nVrXjZHcWsypcmTYhj2lQpXGAe59a0bm5QIXS4iXb0AdvmH+TXMLbtFMqltuMFHX+IdcVqWoJtnf72wDPb+ImuepF9Dr52/dua0bXTqjNMrb14CnA/HjFWXMqRCNWIcdGUYH4VnpcJvUqy4Q5bJwT9K0RKrqhOeE5ZuK5J+6zpgucq28Mk0TGM7P4Tkckf41j/AGSzgkZnC5YkszH196trdi1gdnbO08D1rCur2OdSHmQD+635VFOfYupFrYpajAJfliAJJAQk/eP0rqdK8JNqXh28uZ2LzGRTbRAbVVcfM7eTtB7qK5R5VjlaWVT5cK7jk4YgdvxrsLTxlBDoGpWN5pJYXDgW7wSFfKQr8yFecrkdDnn1rri0kc8k7nr0WiQRiBoknMsK7VWVAVUeoAGKvQ6bCkiM7zs8cjMrlscHHHT2rxlPi1qVksEH9lQS7dsRaS5kUkIB3G0ZzXSw/FqzuLO3M2j3KzL8ssimMb1+h9u9ZuTNlFLc9Bkhjz5kKRl8gbpYfmI9jj/wCv2rGuLHQBq8kMlna/aN+5iyyA7u/AxzXkfiL4hXev3Z8qJLW2RiViVt2T/tNgZ/ACuf8A7QupmLG8n3Ek5LkmqUGxOpb7J9IxR2uy4ggUyLGMCOElt3P0GKqadpS3X+mRiW3jZiVR2G/H0r57g8Q6rBOJY9SupcDH7yZm/maV/FWvPISdYvfqJ2B/LNL2UuhX1hP7J73fRWyS7YrOc25+9LEBtz64P+FUdRtvDF1pI0/7FJbKH3q1srAk9cgnnvXg7+ItYkOW1e9cH/p4cH+dIdb1WTG7Urpj6mVj/WtFSfcTxN+h7Wup6Xb2kNqmqReRCC0UM8hG09cAGt/Q7zRY5p7e0vbWVIyvmRwMCVyOM9ua+aGv7rLfv5HOf4jmmpqF6qkC5lHbAYj+VEqb6CjiX1R9Yw6hpc0sywa/YW0cGFkE0rZjY9j6c9c81oaSBd3UxtzNNB5YzIF2qT6DvXxyL66RcC4mHPO1yP51q6R4x1/SLpZrTU7oMhXIkfeCQc5559qrkcUJVoN3asetfF+Ny+h3TKyKw8ktjj7pr5t0u5aw1GJ0BCJOGye/OT/SvTtS+LFzrOgzabqulRtOyqIriNiobB6MvQ8+ld18LvCvh7XdLiupNMgd/I2+YQeo6d/SuaM2lqd9SCnBOJ4p43+HN94dsf7ahaN7ObHnRRxhRFv4BBJB/TrXlDIynP9K+5NW8H6DPpUunS6VbGFQfLwmwp6Yz/WvmvxX4XvfCWtHTriB1jIHlHyxh0I5DenXH0ropVV0OSrT6o4E5BqQbmA4Jwf896mubdI7kpHHsEfVec1UrsjY2tGs7e5vNkqpKxU7Fd9oB7Z4P8q7Cy8P6RFE8kum208ZBKhFO1vqc+tcL4biJvZDhRlTnIJ7ivRbOZ47cIkVqLZVxkwqevb1rKcW3oJy5LX6nMato1rJqVqn9mW5dU2sYGbYCPbI/lXGwWFuJZmFv5Y5O1WLDP0NemuZLUyXc8Fm7FfmKxKMnp3HNYjNBLayTJFbHCjcDCq49+lcjhJHZGVtjzJ9Ft7dZBFChIQ+WJCWzn8aypNCVWy0KqXJXcJSD9Ogr1CNJJZ1RQBKDltw47V1K+DtFXBbTkbB7c8fma0Uhc7Vj5w07TLmOZrdTtEmf3bqeh+orN1DT3sFjWVFBkJJKjHSvcPH3gGLTtSh1TTmWBJl2SwA4Cs3Uqe1eVeJDJaThJF+bGG4IzXVHR3OWbcXdHJNbu6qqJgKcgE9Ktx2ojOZSSo9ea0dGthdXjRSjaVXPB96mn0y5unaGCFpJNpZUA5P0pl7o1dHhe2g+1sF8+XlFU/dXsMV1MiM0C3Aa3CtkLlGUj61zmnajczaY9pes0RjwGiIPB9VNdpZ3JvtIt5JU/eMoEi4xg9zWFRbG9N36l7TN2xvMghwpxhNpz9a0Y5kZcDgr0NZQGFKr2qeKYcYFcbnruejCmWA+JAD1NSZqAOp5Bpd9VYycWWc0/NQBs04miwuVjjQTUOaM0igDNGaaTzRmkMdmkJppNJmgAYimZzS5zTaYC5ozTc0ZFADs0obFNzRTsId5r/3jSiVx0Y/nTKKdgJhO/94/nThO/wDeNRUUWA0NN1afSdQivbZgskR7jO5e6/iK9S0bxFb6zbieGVSrDDL3U+hr59u9au9Fv4L6zcBlPzKy5WQHXQE6JqSKoHEjrz+ZrhzCLjSvbY9rIKsalbl6o9xr5S+IM9xJ4gd7gMHKjoMA17pY+NbK6TZMrQPjqDkfmK5PxFo+leI7gXM1r5VyCCJEbqRxyO9eHgc0w0abpTdpJ2PucyyzFSrLFUYuSWjt0Pn56kttReAN/FjseldNrnw61TTLhvsTG7t+SjopBx7GufHhLXEdlk0q5X5iPlTPb3FelFxkrXPiakKlN8s1Y0dMmujqkF2yymKZT5a7flGe4rofKkMYaSFW9TXLeHxNHqkCXCMrBdh3ccc4rsJowsrAc+9Qu5LVlqco84s9YSa4kaWGBDxjvmtj+2NKki2mdhkHHyVxmvTBrmSMd8nHtVTTJwFw3bpW0Y2Ryzmldrodjaa9pFvJKz3LFpHLbTGcDPp71Wv8AWdHe6haG5kYeYhI8tuvPvXO2h3WUYC4z/hVmSMMmA2CPpQ0ieZmbN4p0xWIjklfbwCsLkE/lVSfxXYpbzRfvoVZNilV3fMfUdKs3Bwzj0FQPDHNbsnmhGzgbuOP8aytzaHQpNrQ83a6NtqzRzBBjHHB5I7djWdbMklsQMMVB3bjg59Pwra1GBY7ucPu3BiAvbb7j61gzyPaXwjUqUk7A4+UfSt4vQ55rUSCMKxkJ4/hNacpMGnxspDbs5/SoLIJJPtCgnBPFX7y3jFiF3/MM4Pp71pLYyWxjblIGT+la1nf+XGFfHzHBLfSlW0U/wB4A9+9MvPLimCRjdtrGdN3ujpg0kWVeQFiGJBzmmG4cjlzVK3g1G4BKCS2BHaJSf1FW10C+ky0ypHn+JnA/TNcbi0zouWFuZAeXJB9DUq3b92NQjSXibBKknpubAqe30vd1nQY9ASaz5WO6IpZpHHMjfmaYJJP75/Otvd7V/bB6e3/j9L+3D08v8A4+lV7K4uZGN5r/3jSGVv7x/OtnE9wMiUj6g0hDWj5SWRf91qPYhzI5kzn+8f/H6dLdXX2UqssoCp2cnpXR/a5T96TJ7nAqK4C3EZEqB1PUMMilKi+7K5ux+0HzXxH/30aKd5A9KB9MJn/9k="
IMG_YASHWANTH = "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"

def render(html_str):
    lines = [line for line in html_str.split("\n") if line.strip() != ""]
    st.markdown("\n".join(lines), unsafe_allow_html=True)

CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Exo+2:ital,wght@0,300;0,400;0,600;1,300;1,400;1,600&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap');
:root {
  --seafoam:#4ecdc4;--pink:#ff6b9d;--pearl:#e8f4f8;
  --deep:#010d1f;--mid:#0a2540;--bright:#0e4d7b;
  --sand:#f5e6c8;--sand-dark:#d4a96a;
}
*{box-sizing:border-box;}
#MainMenu,footer,header,[data-testid="stHeader"],[data-testid="collapsedControl"]{display:none!important;}
[data-testid="stAppViewContainer"]{
  background:linear-gradient(180deg,#010d1f 0%,#031d38 12%,#0a3055 24%,#0e4d7b 38%,#1a7aad 55%,#a0d8ef 78%,#f5e6c8 100%)!important;
  min-height:100vh;}
[data-testid="stMain"]{background:transparent!important;}
.block-container{padding:0 1rem 4rem 1rem!important;max-width:1200px;margin:0 auto;}
@media(min-width:768px){.block-container{padding:0 2rem 4rem 2rem!important;}}
@keyframes floatBubble{0%{bottom:-120px;opacity:0;transform:translateX(0);}10%{opacity:1;}50%{opacity:0.7;transform:translateX(18px);}90%{opacity:0.3;}100%{bottom:110vh;opacity:0;transform:translateX(-14px);}}
@keyframes swimShark{0%{left:-400px;}100%{left:110%;}}
@keyframes gShift{0%,100%{background-position:0% 50%;}50%{background-position:100% 50%;}}
@keyframes photoPulse{0%,100%{box-shadow:0 0 0 4px #4ecdc4,0 0 20px rgba(78,205,196,0.4);}50%{box-shadow:0 0 0 6px #4ecdc4,0 0 40px rgba(78,205,196,0.7),0 0 60px rgba(255,107,157,0.3);}}
@keyframes lineGlow{0%,100%{opacity:0.6;box-shadow:0 0 6px #4ecdc4;}50%{opacity:1;box-shadow:0 0 16px #4ecdc4,0 0 30px #ff6b9d;}}
@keyframes dotPulse{0%,100%{transform:scale(1);box-shadow:0 0 8px #4ecdc4;}50%{transform:scale(1.15);box-shadow:0 0 20px #4ecdc4,0 0 35px #ff6b9d;}}
@keyframes fadeUp{from{opacity:0;transform:translateY(24px);}to{opacity:1;transform:translateY(0);}}
@keyframes slideInLeft{from{opacity:0;transform:translateX(-60px);}to{opacity:1;transform:translateX(0);}}
@keyframes slideInRight{from{opacity:0;transform:translateX(60px);}to{opacity:1;transform:translateX(0);}}
@keyframes shimmer{0%{background-position:-200% center;}100%{background-position:200% center;}}
.bubbles{position:fixed;width:100%;height:100vh;top:0;left:0;pointer-events:none;z-index:0;overflow:hidden;}
.b{position:absolute;border-radius:50%;background:radial-gradient(circle at 30% 30%,rgba(78,205,196,0.35),rgba(14,77,123,0.15));border:1px solid rgba(78,205,196,0.25);animation:floatBubble linear infinite;}
.sharks-bg{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0;overflow:hidden;}
.shk{position:fixed;opacity:0.07;animation:swimShark linear infinite;}
.coco-l{position:fixed;bottom:0;left:-10px;z-index:1;pointer-events:none;opacity:0.55;}
.coco-r{position:fixed;bottom:0;right:-10px;z-index:1;pointer-events:none;opacity:0.55;transform:scaleX(-1);}
.gs{background:rgba(10,37,64,0.58);border:1px solid rgba(78,205,196,0.22);border-radius:24px;backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);padding:1.8rem 1.2rem;margin:1.5rem 0;position:relative;overflow:hidden;animation:fadeUp 0.8s ease both;}
@media(min-width:768px){.gs{padding:2.5rem 2.8rem;margin:2rem 0;}}
.gs::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,#4ecdc4,transparent);}
.gtitle{font-family:'Bebas Neue',cursive;font-size:clamp(30px,6vw,68px);background:linear-gradient(120deg,#4ecdc4,#e8f4f8,#ff6b9d,#4ecdc4);background-size:300% 300%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:gShift 5s ease infinite;margin:0 0 0.4rem 0;letter-spacing:3px;}
.gsub{font-family:'Space Mono',monospace;color:rgba(232,244,248,0.6);font-size:11px;letter-spacing:2px;margin-bottom:1.5rem;}
@media(min-width:768px){.gsub{font-size:13px;}}
.top-brand{font-family:'Space Mono',monospace;color:#4ecdc4;font-size:clamp(11px,2vw,17px);font-weight:700;letter-spacing:2px;padding:1rem 0;}
.hero{text-align:center;padding:3rem 1rem 3rem 1rem;position:relative;z-index:2;}
@media(min-width:768px){.hero{padding:5rem 1rem 4rem 1rem;}}
.hero-title{font-family:'Bebas Neue',cursive;font-size:clamp(70px,18vw,200px);background:linear-gradient(120deg,#4ecdc4,#e8f4f8,#ff6b9d,#4ecdc4);background-size:300% 300%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:gShift 6s ease infinite;line-height:0.9;letter-spacing:8px;margin:0;}
.hero-sub{font-family:'Space Mono',monospace;color:rgba(232,244,248,0.7);font-size:clamp(9px,2vw,16px);letter-spacing:2px;margin:1.2rem 0 0.8rem 0;}
.hero-tag{font-family:'Exo 2',sans-serif;font-style:italic;font-size:clamp(14px,3vw,26px);color:#4ecdc4;letter-spacing:4px;margin:0;}
.info-banner{border:1px solid rgba(212,169,106,0.6);border-radius:12px;background:rgba(212,169,106,0.08);padding:10px 16px;font-family:'Space Mono',monospace;font-size:11px;color:#f5e6c8;letter-spacing:1px;margin-bottom:1.4rem;}
@media(min-width:768px){.info-banner{padding:14px 22px;font-size:12px;letter-spacing:1.5px;}}
.about-body{font-family:'Exo 2',sans-serif;font-size:14px;color:rgba(232,244,248,0.85);line-height:1.9;}
@media(min-width:768px){.about-body{font-size:15px;}}
/* SHARK CARDS */
.sc-grid{display:grid;grid-template-columns:1fr;gap:1.2rem;margin-top:1.5rem;}
@media(min-width:600px){.sc-grid{grid-template-columns:repeat(3,1fr);gap:1.8rem;}}
.sc{background:rgba(10,37,64,0.7);border:1px solid rgba(78,205,196,0.18);border-radius:20px;padding:1.5rem 1.2rem;text-align:center;transition:all 0.35s ease;cursor:default;position:relative;overflow:hidden;}
@media(min-width:768px){.sc{padding:2rem 1.5rem;}}
.sc:nth-child(1){animation:fadeUp 0.7s ease 0.1s both;}
.sc:nth-child(2){animation:fadeUp 0.7s ease 0.25s both;}
.sc:nth-child(3){animation:fadeUp 0.7s ease 0.4s both;}
.sc:hover{transform:translateY(-8px) scale(1.02);border-color:#4ecdc4;box-shadow:0 24px 60px rgba(78,205,196,0.3);}
@media(min-width:600px){.sc:hover{transform:translateY(-14px) scale(1.02);}}
.photo-wrap{width:110px;height:110px;border-radius:50%;background:linear-gradient(135deg,#4ecdc4,#ff6b9d);display:flex;align-items:center;justify-content:center;margin:0 auto 1rem auto;overflow:hidden;animation:photoPulse 3s ease-in-out infinite;flex-shrink:0;}
@media(min-width:768px){.photo-wrap{width:130px;height:130px;}}
.photo-wrap img{width:100%;height:100%;object-fit:cover;object-position:center top;border-radius:50%;}
.co-badge{font-family:'Space Mono',monospace;font-size:9px;color:#4ecdc4;letter-spacing:1.5px;margin-bottom:0.6rem;opacity:0.85;}
.sc-name{font-family:'Bebas Neue',cursive;font-size:24px;color:#e8f4f8;letter-spacing:3px;margin:0.3rem 0;}
@media(min-width:768px){.sc-name{font-size:28px;}}
.sc-role{font-family:'Space Mono',monospace;font-size:9px;color:#ff6b9d;letter-spacing:1.5px;margin-bottom:1rem;}
.sc-bio{font-family:'Exo 2',sans-serif;font-size:12px;color:rgba(232,244,248,0.78);line-height:1.75;text-align:left;margin-bottom:1rem;}
@media(min-width:768px){.sc-bio{font-size:13px;}}
.sc-tags{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin-bottom:1.2rem;}
.sc-tag{font-family:'Space Mono',monospace;font-size:9px;background:rgba(78,205,196,0.12);border:1px solid rgba(78,205,196,0.3);color:#4ecdc4;border-radius:20px;padding:3px 10px;letter-spacing:1px;}
.li-btn{display:inline-block;font-family:'Bebas Neue',cursive;font-size:14px;letter-spacing:2px;background:linear-gradient(135deg,rgba(78,205,196,0.2),rgba(78,205,196,0.05));border:1px solid rgba(78,205,196,0.4);color:#4ecdc4;border-radius:30px;padding:7px 20px;text-decoration:none;transition:all 0.3s ease;}
.li-btn:hover{background:#4ecdc4;color:#010d1f;text-decoration:none;box-shadow:0 6px 20px rgba(78,205,196,0.5);}
/* REGISTRATION */
.reg-grid{display:grid;grid-template-columns:1fr;gap:1.5rem;margin-top:1.5rem;}
@media(min-width:600px){.reg-grid{grid-template-columns:1fr 1fr;gap:2rem;}}
.reg-card{background:rgba(10,37,64,0.75);border:1px solid rgba(78,205,196,0.18);border-radius:22px;padding:1.8rem 1.4rem;text-align:center;transition:all 0.3s ease;position:relative;overflow:hidden;}
@media(min-width:768px){.reg-card{padding:2.2rem 1.8rem;}}
.reg-card-l{animation:slideInLeft 0.7s ease 0.1s both;}
.reg-card-r{animation:slideInRight 0.7s ease 0.3s both;}
.reg-card-l:hover{transform:translateY(-8px);box-shadow:0 20px 50px rgba(255,107,157,0.22);border-color:#ff6b9d;}
.reg-card-r:hover{transform:translateY(-8px);box-shadow:0 20px 50px rgba(78,205,196,0.22);border-color:#4ecdc4;}
.reg-badge{display:inline-block;font-family:'Space Mono',monospace;font-size:9px;letter-spacing:2px;border-radius:20px;padding:5px 14px;margin-bottom:1rem;}
@media(min-width:768px){.reg-badge{font-size:10px;letter-spacing:3px;padding:6px 18px;}}
.reg-badge-seafoam{background:#4ecdc4;color:#010d1f;}
.reg-badge-pink{background:#ff6b9d;color:white;}
.reg-emoji{font-size:44px;display:block;margin-bottom:12px;}
@media(min-width:768px){.reg-emoji{font-size:54px;}}
.reg-title{font-family:'Bebas Neue',cursive;font-size:32px;color:#e8f4f8;letter-spacing:4px;margin:0.2rem 0;}
@media(min-width:768px){.reg-title{font-size:40px;}}
.reg-subtitle-seafoam{font-family:'Space Mono',monospace;font-size:11px;color:#4ecdc4;letter-spacing:2px;margin-bottom:1rem;}
.reg-subtitle-pink{font-family:'Space Mono',monospace;font-size:11px;color:#ff6b9d;letter-spacing:2px;margin-bottom:1rem;}
.reg-sep-seafoam{border:none;border-top:1px solid rgba(78,205,196,0.25);margin:0.8rem 0;}
.reg-sep-pink{border:none;border-top:1px solid rgba(255,107,157,0.25);margin:0.8rem 0;}
.reg-desc{font-family:'Exo 2',sans-serif;font-size:13px;color:rgba(232,244,248,0.75);line-height:1.8;margin-bottom:1.5rem;text-align:left;}
@media(min-width:768px){.reg-desc{font-size:14px;}}
.reg-btn-pink{display:block;width:100%;background:linear-gradient(135deg,#ff6b9d,#c84b8e);color:white;font-family:'Bebas Neue',cursive;font-size:20px;letter-spacing:4px;border-radius:40px;padding:14px;text-align:center;text-decoration:none;box-shadow:0 8px 28px rgba(255,107,157,0.4);transition:all 0.3s ease;}
.reg-btn-pink:hover{transform:scale(1.04);box-shadow:0 12px 40px rgba(255,107,157,0.65);text-decoration:none;color:white;}
.reg-btn-seafoam{display:block;width:100%;background:linear-gradient(135deg,#4ecdc4,#2eafa7);color:#010d1f;font-family:'Bebas Neue',cursive;font-size:20px;letter-spacing:4px;border-radius:40px;padding:14px;text-align:center;text-decoration:none;box-shadow:0 8px 28px rgba(78,205,196,0.4);transition:all 0.3s ease;}
.reg-btn-seafoam:hover{transform:scale(1.04);box-shadow:0 12px 40px rgba(78,205,196,0.65);text-decoration:none;color:#010d1f;}
.reg-divider{height:2px;border:none;background:linear-gradient(90deg,transparent,#4ecdc4,#ff6b9d,#4ecdc4,transparent);background-size:200% auto;animation:shimmer 3s linear infinite;margin:2rem 0 1rem 0;border-radius:2px;}
.reg-footer-note{font-family:'Space Mono',monospace;font-size:10px;color:rgba(232,244,248,0.4);text-align:center;letter-spacing:2px;}
.reg-instruction{font-family:'Space Mono',monospace;font-size:12px;color:#4ecdc4;text-align:center;letter-spacing:2px;margin-bottom:24px;}
@media(min-width:768px){.reg-instruction{font-size:14px;margin-bottom:32px;}}
/* TIMELINE */
.tl-wrap{position:relative;margin:2rem 0;padding:1rem 0;}
.tl-wrap::before{content:'';position:absolute;left:50%;top:0;bottom:0;width:2px;background:linear-gradient(180deg,#4ecdc4,#ff6b9d);transform:translateX(-50%);animation:lineGlow 2.5s ease-in-out infinite;}
.tl-row{display:flex;align-items:flex-start;margin-bottom:3rem;position:relative;min-height:60px;}
.tl-dot{width:22px;height:22px;border-radius:50%;background:linear-gradient(135deg,#4ecdc4,#ff6b9d);flex-shrink:0;animation:dotPulse 2s ease-in-out infinite;z-index:2;position:absolute;left:50%;top:20px;transform:translateX(-50%);}
.tl-box{width:calc(50% - 28px);background:rgba(10,37,64,0.7);border:1px solid rgba(78,205,196,0.2);border-radius:16px;padding:1.2rem 1.4rem;transition:all 0.3s ease;}
.tl-box:hover{border-color:#4ecdc4;transform:translateY(-3px);box-shadow:0 10px 30px rgba(78,205,196,0.2);}
.tl-left .tl-box{margin-right:auto;margin-left:0;text-align:right;}
.tl-right .tl-box{margin-left:auto;margin-right:0;text-align:left;}
@media(max-width:599px){
  .tl-wrap::before{left:16px;}
  .tl-dot{left:16px;top:18px;transform:none;}
  .tl-box{width:calc(100% - 46px);margin-left:46px!important;margin-right:0!important;text-align:left!important;}
}
.tl-date{font-family:'Space Mono',monospace;font-size:10px;color:#4ecdc4;letter-spacing:3px;margin-bottom:0.4rem;}
.tl-label{font-family:'Bebas Neue',cursive;font-size:20px;color:#e8f4f8;letter-spacing:2px;margin-bottom:0.5rem;}
@media(min-width:600px){.tl-label{font-size:22px;}}
.tl-detail{font-family:'Exo 2',sans-serif;font-size:13px;color:rgba(232,244,248,0.75);line-height:1.7;}
.tl-row:nth-child(1){animation:fadeUp 0.7s ease 0.1s both;}
.tl-row:nth-child(2){animation:fadeUp 0.7s ease 0.3s both;}
.tl-row:nth-child(3){animation:fadeUp 0.7s ease 0.5s both;}
/* PITCH GUIDELINES */
.gg{display:grid;grid-template-columns:1fr 1fr;gap:0.8rem;margin-top:1.5rem;}
@media(min-width:768px){.gg{grid-template-columns:repeat(4,1fr);gap:1rem;}}
.gc{background:rgba(10,37,64,0.65);border:1px solid rgba(78,205,196,0.18);border-radius:14px;padding:0.9rem 0.8rem;transition:all 0.3s ease;font-family:'Exo 2',sans-serif;font-size:12px;color:#e8f4f8;display:flex;gap:8px;align-items:flex-start;}
@media(min-width:768px){.gc{padding:1.1rem 1rem;font-size:13.5px;gap:10px;}}
.gc:hover{border-color:#4ecdc4;transform:translateY(-4px);box-shadow:0 8px 24px rgba(78,205,196,0.2);}
.gc .gicon{font-size:20px;flex-shrink:0;}
@media(min-width:768px){.gc .gicon{font-size:22px;}}
.gc:nth-child(1){animation:fadeUp 0.6s ease 0.05s both;}
.gc:nth-child(2){animation:fadeUp 0.6s ease 0.10s both;}
.gc:nth-child(3){animation:fadeUp 0.6s ease 0.15s both;}
.gc:nth-child(4){animation:fadeUp 0.6s ease 0.20s both;}
.gc:nth-child(5){animation:fadeUp 0.6s ease 0.25s both;}
.gc:nth-child(6){animation:fadeUp 0.6s ease 0.30s both;}
.gc:nth-child(7){animation:fadeUp 0.6s ease 0.35s both;}
.gc:nth-child(8){animation:fadeUp 0.6s ease 0.40s both;}
/* FORM STYLES */
.stTextInput>div>div>input,.stTextArea>div>div>textarea{background:rgba(1,13,31,0.85)!important;border:1px solid rgba(78,205,196,0.4)!important;border-radius:10px!important;color:#e8f4f8!important;font-family:'Exo 2',sans-serif!important;font-size:14px!important;}
.stTextInput>div>div>input:focus,.stTextArea>div>div>textarea:focus{border-color:#4ecdc4!important;box-shadow:0 0 0 2px rgba(78,205,196,0.2)!important;}
label[data-baseweb="label"],.stTextInput label,.stTextArea label{font-family:'Space Mono',monospace!important;font-size:11px!important;color:#4ecdc4!important;letter-spacing:2px!important;}
.stButton>button{font-family:'Bebas Neue',cursive!important;font-size:18px!important;letter-spacing:4px!important;background:linear-gradient(135deg,#4ecdc4,#2eafa7)!important;color:#010d1f!important;border:none!important;border-radius:30px!important;padding:10px 36px!important;transition:all 0.3s ease!important;width:100%;}
@media(min-width:768px){.stButton>button{font-size:20px!important;}}
.stButton>button:hover{transform:scale(1.04)!important;box-shadow:0 8px 24px rgba(78,205,196,0.45)!important;}
.success-box{border:1px solid #4ecdc4;border-radius:12px;background:rgba(78,205,196,0.08);padding:14px 20px;font-family:'Space Mono',monospace;font-size:12px;color:#4ecdc4;letter-spacing:1.5px;margin-top:1rem;}
/* Q&A */
.qt{position:relative;padding:1rem 0 1rem 40px;margin-top:1.5rem;}
@media(min-width:768px){.qt{padding:1rem 0 1rem 52px;}}
.qt::before{content:'';position:absolute;left:16px;top:0;bottom:0;width:2px;background:linear-gradient(180deg,#4ecdc4,#ff6b9d);animation:lineGlow 2.5s ease-in-out infinite;}
@media(min-width:768px){.qt::before{left:22px;}}
.qt-item{display:flex;align-items:flex-start;gap:18px;margin-bottom:2rem;position:relative;animation:fadeUp 0.6s ease both;}
.qt-dot{width:18px;height:18px;border-radius:50%;background:linear-gradient(135deg,#4ecdc4,#ff6b9d);flex-shrink:0;margin-top:4px;position:absolute;left:-28px;animation:dotPulse 2s ease-in-out infinite;}
@media(min-width:768px){.qt-dot{left:-40px;}}
.qt-card{background:rgba(10,37,64,0.65);border:1px solid rgba(78,205,196,0.18);border-radius:14px;padding:1.2rem 1.5rem;flex:1;}
.qt-name{font-family:'Space Mono',monospace;font-size:11px;color:#4ecdc4;letter-spacing:2px;margin-bottom:0.5rem;}
.qt-question{font-family:'Exo 2',sans-serif;font-size:14px;color:#e8f4f8;margin-bottom:0.8rem;line-height:1.6;}
.qt-reply{border-left:3px solid #4ecdc4;padding-left:12px;font-family:'Exo 2',sans-serif;font-size:13px;color:rgba(232,244,248,0.8);font-style:italic;line-height:1.6;}
/* FOOTER */
.beach-footer{background:linear-gradient(180deg,transparent,rgba(245,230,200,0.12),rgba(212,169,106,0.22));border-top:1px solid rgba(212,169,106,0.3);text-align:center;padding:0 1rem 2rem 1rem;margin-top:3rem;position:relative;}
.footer-wave{width:100%;margin-bottom:1.5rem;}
.footer-college{font-family:'Bebas Neue',cursive;font-size:clamp(18px,4vw,42px);color:#d4a96a;letter-spacing:3px;margin:0;}
@media(min-width:768px){.footer-college{letter-spacing:5px;}}
.footer-club{font-family:'Space Mono',monospace;font-size:11px;color:rgba(212,169,106,0.7);letter-spacing:3px;margin:0.3rem 0;}
.footer-tagline{font-family:'Space Mono',monospace;font-size:9px;color:rgba(212,169,106,0.4);letter-spacing:4px;margin:0.2rem 0 1rem 0;}
.footer-emoji{font-size:18px;letter-spacing:6px;margin-top:0.5rem;}
[data-testid="stHorizontalBlock"]{gap:0.5rem!important;}
</style>"""
st.markdown(CSS, unsafe_allow_html=True)

# ── BACKGROUND LAYERS ─────────────────────────────────────────────────────────
SHARK = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 120'><ellipse cx='155' cy='62' rx='140' ry='42' fill='none' stroke='white' stroke-width='2.5'/><polygon points='295,62 320,40 320,84' fill='none' stroke='white' stroke-width='2'/><polygon points='155,20 135,4 175,4' fill='none' stroke='white' stroke-width='2'/><path d='M110,66 Q95,90 70,100 Q100,78 105,66' fill='none' stroke='white' stroke-width='2'/><circle cx='240' cy='54' r='4' fill='white' opacity='0.7'/></svg>"
COCO  = "<svg xmlns='http://www.w3.org/2000/svg' width='120' height='280' viewBox='0 0 120 280'><path d='M60,280 Q55,200 50,150 Q45,100 65,40' fill='none' stroke='#8B6914' stroke-width='10' stroke-linecap='round'/><path d='M65,40 Q20,20 0,50' fill='none' stroke='#2d7a2d' stroke-width='6' stroke-linecap='round'/><path d='M65,40 Q100,10 115,45' fill='none' stroke='#2d7a2d' stroke-width='6' stroke-linecap='round'/><path d='M65,40 Q40,55 30,80' fill='none' stroke='#3a9a3a' stroke-width='5' stroke-linecap='round'/><path d='M65,40 Q90,60 100,82' fill='none' stroke='#3a9a3a' stroke-width='5' stroke-linecap='round'/><path d='M65,40 Q65,65 60,90' fill='none' stroke='#4ab54a' stroke-width='5' stroke-linecap='round'/><circle cx='55' cy='50' r='7' fill='#7a4f00'/><circle cx='75' cy='46' r='6' fill='#7a4f00'/><circle cx='63' cy='58' r='6' fill='#7a4f00'/></svg>"

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
    "<div class='shk' style='top:15%;width:280px;animation-duration:28s;animation-delay:0s;'>" + SHARK + "</div>"
    "<div class='shk' style='top:35%;width:200px;animation-duration:22s;animation-delay:6s;transform:scaleX(-1);'>" + SHARK + "</div>"
    "<div class='shk' style='top:55%;width:340px;animation-duration:34s;animation-delay:12s;'>" + SHARK + "</div>"
    "<div class='shk' style='top:72%;width:160px;animation-duration:20s;animation-delay:4s;transform:scaleX(-1);'>" + SHARK + "</div>"
    "</div>"
    "<div class='coco-l'>" + COCO + "</div>"
    "<div class='coco-r'>" + COCO + "</div>"
)

# ── TOP BAR ───────────────────────────────────────────────────────────────────
render("<div class='top-brand'>\U0001f988 SHARKPIT 2026 &mdash; S&amp;T CLUB MECS</div>")

# ── HERO ──────────────────────────────────────────────────────────────────────
render(
    "<div class='hero'>"
    "<div class='hero-title'>SHARKPIT</div>"
    "<div class='hero-sub'>Science &amp; Technology Club &nbsp;&middot;&nbsp; Matrusri Engineering College</div>"
    "<div class='hero-tag'>\U0001f988 Pitch. Challenge. Win. \U0001f988</div>"
    "</div>"
)

# ── ABOUT THE EVENT ───────────────────────────────────────────────────────────
render(
    "<div class='gs'>"
    "<div class='gtitle'>ABOUT THE EVENT</div>"
    "<div class='info-banner'>Open to all years of B.Tech at Matrusri Engineering College &nbsp;&middot;&nbsp; Organised by the Science &amp; Technology Club</div>"
    "<div class='about-body'>SHARKPIT is a high-energy student startup pitch competition and ideathon organized by the S&amp;T Club of MECS. Inspired by investor pitch formats, it challenges students to think like entrepreneurs and defend their ideas before experienced industry founders &mdash; the Sharks. The event has two parts: a morning casual meetup open to all students, and exclusive evening finals where the top 20 shortlisted teams pitch live before the Sharks.</div>"
    "</div>"
)

# ── MEET THE SHARKS ───────────────────────────────────────────────────────────
render(
    "<div class='gs'>"
    "<div class='gtitle'>MEET THE SHARKS</div>"
    "<div class='gsub'>Three visionary founders. One arena. Zero mercy on weak pitches.</div>"
    "<div class='sc-grid'>"
    # Card 1 – E Sai Eshwar
    "<div class='sc'>"
    "<div class='photo-wrap'><img src='data:image/jpeg;base64," + IMG_ESHWAR + "' alt='E Sai Eshwar'/></div>"
    "<div class='co-badge'>\U0001f680 Studlyf &middot; Nirvaha &middot; GuideBazaar</div>"
    "<div class='sc-name'>E SAI ESHWAR</div>"
    "<div class='sc-role'>Ecosystem &amp; Product Operator &middot; Founder</div>"
    "<div class='sc-bio'>Operates at the intersection of Applied AI, strategy, and social impact. Co-founded Studlyf &mdash; a student ecosystem platform &mdash; and Nirvaha, an AI wellness platform powered by the Bhagavad Gita. 12x national hackathon finalist, mentors 600+ students, and has delivered 10+ public speaking sessions on AI &amp; entrepreneurship.</div>"
    "<div class='sc-tags'>"
    "<span class='sc-tag'>Applied AI</span>"
    "<span class='sc-tag'>Product Strategy</span>"
    "<span class='sc-tag'>Ecosystem</span>"
    "<span class='sc-tag'>Mentorship</span>"
    "</div>"
    "<a class='li-btn' href='https://linkedin.com/in/esaieshwar' target='_blank'>\U0001f517 LinkedIn</a>"
    "</div>"
    # Card 2 – Yashwanth Bondapalli
    "<div class='sc'>"
    "<div class='photo-wrap'><img src='data:image/jpeg;base64," + IMG_YASHWANTH + "' alt='Yashwanth Bondapalli'/></div>"
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
    # Card 3 – Sai Harishith
    "<div class='sc'>"
    "<div class='photo-wrap'><img src='data:image/jpeg;base64," + IMG_HARISHITH + "' alt='Sai Harishith'/></div>"
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
    "</div>"
    "</div>"
)

# ── REGISTER NOW ──────────────────────────────────────────────────────────────
render(
    "<div class='gs'>"
    "<div class='gtitle'>REGISTER NOW</div>"
    "<div class='reg-instruction'>Click on the following 2 links to register for your preferred session</div>"
    "<div class='reg-grid'>"
    "<div class='reg-card reg-card-l'>"
    "<span class='reg-badge reg-badge-seafoam'>IDEATHON REGISTRATION</span>"
    "<span class='reg-emoji'>\U0001f988</span>"
    "<div class='reg-title'>IDEATHON</div>"
    "<div class='reg-subtitle-seafoam'>Evening Pitch Finals</div>"
    "<hr class='reg-sep-seafoam'/>"
    "<div class='reg-desc'>Register through Luma to compete in the SHARKPIT ideathon. Submit your startup idea and pitch live before our Shark jury on March 17th. Requires idea submission before March 13th and approval via email. Top 20 teams shortlisted.</div>"
    "<a class='reg-btn-pink' href='https://luma.com/34izlhhj' target='_blank'>REGISTER ON LUMA \U0001f517</a>"
    "</div>"
    "<div class='reg-card reg-card-r'>"
    "<span class='reg-badge reg-badge-pink'>OPEN MEETUP REGISTRATION</span>"
    "<span class='reg-emoji'>\U0001f305</span>"
    "<div class='reg-title'>OPEN MEETUP</div>"
    "<div class='reg-subtitle-pink'>Morning Casual Session</div>"
    "<hr class='reg-sep-pink'/>"
    "<div class='reg-desc'>Register through Meetup to attend the morning casual session. Come listen to our Shark founders speak, get inspired, and soak in the entrepreneurial energy. Open to every MECS student &mdash; no idea submission or approval needed.</div>"
    "<a class='reg-btn-seafoam' href='https://luma.com/4e3p9fdx' target='_blank'>REGISTER ON MEETUP \U0001f517</a>"
    "</div>"
    "</div>"
    "<hr class='reg-divider'/>"
    "<div class='reg-footer-note'>Both sessions are on March 17, 2026 &nbsp;&middot;&nbsp; Matrusri Engineering College</div>"
    "</div>"
)

# ── EVENT ROADMAP ─────────────────────────────────────────────────────────────
render(
    "<div class='gs'>"
    "<div class='gtitle'>EVENT ROADMAP</div>"
    "<div class='gsub'>From raw idea to the shark tank &mdash; here&#x27;s the journey.</div>"
    "<div class='tl-wrap'>"
    "<div class='tl-row tl-left'>"
    "<div class='tl-box'>"
    "<div class='tl-date'>MARCH 13, 2026</div>"
    "<div class='tl-label'>\U0001f4a1 IDEA SUBMISSION DEADLINE</div>"
    "<div class='tl-detail'>Submit your startup idea before the cutoff. Include a problem statement, proposed solution, and team details. Teams of 1&ndash;4 MECS B.Tech students.</div>"
    "</div>"
    "<div class='tl-dot'></div>"
    "</div>"
    "<div class='tl-row tl-right'>"
    "<div class='tl-dot'></div>"
    "<div class='tl-box'>"
    "<div class='tl-date'>MARCH 14 &ndash; 16, 2026</div>"
    "<div class='tl-label'>\U0001f4e7 SHORTLISTING VIA EMAIL</div>"
    "<div class='tl-detail'>Our panel reviews all submissions and selects the Top 20 teams. Results communicated exclusively via email &mdash; keep an eye on your inbox!</div>"
    "</div>"
    "</div>"
    "<div class='tl-row tl-left'>"
    "<div class='tl-box'>"
    "<div class='tl-date'>MARCH 17, 2026</div>"
    "<div class='tl-label'>\U0001f988 FINAL PITCH ROUND</div>"
    "<div class='tl-detail'>Top 20 teams pitch live before the Sharks. Morning open meetup for all. Evening exclusive finals for shortlisted teams. Defend your idea. Claim your crown.</div>"
    "</div>"
    "<div class='tl-dot'></div>"
    "</div>"
    "</div>"
    "</div>"
)

# ── PITCH GUIDELINES ──────────────────────────────────────────────────────────
render(
    "<div class='gs'>"
    "<div class='gtitle'>PITCH GUIDELINES</div>"
    "<div class='gsub'>Follow these rules. The Sharks are watching every second.</div>"
    "<div class='gg'>"
    "<div class='gc'><span class='gicon'>&#9201;</span><span>10 minutes per team for pitching</span></div>"
    "<div class='gc'><span class='gicon'>&#128101;</span><span>Teams of 1 to 4 members</span></div>"
    "<div class='gc'><span class='gicon'>&#127919;</span><span>Cover problem, solution &amp; impact</span></div>"
    "<div class='gc'><span class='gicon'>&#127979;</span><span>Open to all B.Tech years at MECS</span></div>"
    "<div class='gc'><span class='gicon'>\U0001f988</span><span>Top 20 teams advance to finals</span></div>"
    "<div class='gc'><span class='gicon'>&#128231;</span><span>Shortlisting notified via email</span></div>"
    "<div class='gc'><span class='gicon'>\U0001f680</span><span>Original ideas only &mdash; no copying</span></div>"
    "</div>"
    "</div>"
)

# ── ASK A QUERY ───────────────────────────────────────────────────────────────
render(
    "<div class='gs'>"
    "<div class='gtitle'>ASK A QUERY</div>"
    "<div class='gsub'>Have a question about SHARKPIT 2026? Drop it below &mdash; it will be sent directly to the S&amp;T Club.</div>"
    "</div>"
)
_, qcol, _ = st.columns([0.5, 4, 0.5])
with qcol:
    q_name  = st.text_input("Your Name",  key="q_name",  placeholder="e.g. Ravi Kumar")
    q_email = st.text_input("Your Email", key="q_email", placeholder="e.g. ravi@student.mecs.edu")
    q_msg   = st.text_area("Your Query",  key="q_msg",   height=110, placeholder="Type your question here...")

    if st.button("\U0001f988 SUBMIT QUERY"):
        if q_name.strip() and q_email.strip() and q_msg.strip():
            import urllib.parse
            subject = urllib.parse.quote(f"SHARKPIT 2026 Query from {q_name.strip()}")
            body    = urllib.parse.quote(
                f"Name: {q_name.strip()}\nEmail: {q_email.strip()}\n\nQuery:\n{q_msg.strip()}"
            )
            mailto_link = f"mailto:scienceclubmecs@gmail.com?subject={subject}&body={body}"
            render(
                f"<div class='success-box'>"
                f"&#10003; Your query is ready! "
                f"<a href='{mailto_link}' style='color:#4ecdc4;font-weight:bold;'>"
                f"Click here to send it to scienceclubmecs@gmail.com</a>"
                f"</div>"
            )
        else:
            st.warning("Please fill in all fields before submitting.")

# ── BEACH FOOTER ──────────────────────────────────────────────────────────────
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
