from bs4 import BeautifulSoup
import requests
import streamlit as st

def load_scimagojr(q):
    URL = f"https://www.scimagojr.com/journalsearch.php?q={q}"
    resp = requests.get(URL)
    if resp.status_code == 200:
        with open(f"journalsearch_{q}.html", "w", encoding='utf8') as fp:
             fp.write(resp.text)
        soup = BeautifulSoup(resp.text, "html.parser")
   
        return soup, resp.text
    return None, None

st.markdown('<p class="title1">APP KIỂM TRA BÀI BÁO TRONG DANH MỤC SCOPUS</p>', unsafe_allow_html=True)
soup, resp = load_scimagojr('17576385')
st.markdown(resp)
