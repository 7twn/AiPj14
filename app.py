import streamlit as st
import streamlit.components.v1 as components

# Streamlit 本身是 Python 框架，沒辦法直接「執行」一個純 HTML/JS 檔案，
# 所以這支 app.py 的角色很單純：讀進 stress_dashboard.html 的內容，
# 用 components.html() 把它嵌進 Streamlit 頁面（等於是包一層 iframe）。
# 圖表、儀表板、互動邏輯全部還是原本 HTML 檔案裡的 JavaScript 在跑，
# Streamlit 沒有介入或改寫任何內容。

st.set_page_config(
    page_title="Stress Score 分析儀表板",
    layout="wide",
)

HTML_FILE = "stress_dashboard.html"

with open(HTML_FILE, "r", encoding="utf-8") as f:
    html_content = f.read()

# height 設大一點，並開啟 scrolling，避免報告頁內容被裁切。
# 如果之後內容變更、變長/變短，可以調整這個數字。
components.html(html_content, height=7000, scrolling=True)
