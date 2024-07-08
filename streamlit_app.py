from bs4 import BeautifulSoup
import requests
import streamlit as st
import streamlit.components.v1 as components

def load_scimagojr(q):
    # URL = f"https://www.scimagojr.com/journalsearch.php?q={q}"
    URL = 'https://www.khoahocdulieu.vn'
    st.write(URL)
    resp = requests.get(URL)
    st.write(resp.status_code)
    #st.write(resp.text)
    if resp.status_code == 200:
        st.write(resp.text)
       
        with open(f"journalsearch_{q}.html", "w", encoding='utf8') as fp:
             fp.write(resp.text)
        soup = BeautifulSoup(resp.text, "html.parser")
   
        return soup, resp.text
    return None, None

st.markdown('<p class="title1">APP KIỂM TRA BÀI BÁO TRONG DANH MỤC SCOPUS</p>', unsafe_allow_html=True)
soup, resp = load_scimagojr('17576385')
#st.markdown(resp)
components.iframe("https://www.scimagojr.com/journalsearch.php?q=21100774786&tip=sid&clean=0", height=1000)
