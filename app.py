import streamlit as st
import google.generativeai as genai
import random

# ตั้งค่าหน้าจอ
st.set_page_config(page_title="TikTok 8-Sec Pro + Trend Finder", page_icon="💰")

# ใส่ API Key ของคุณ
genai.configure(api_key="AIzaSyAHr1OWBYjJtXynAQ5eDoin7M13qyp8AGU")

st.markdown("<h1 style='text-align: center; color: #FF0050;'>💰 TikTok Trend & Script</h1>", unsafe_allow_html=True)

# --- ฟังก์ชันสุ่มสินค้าเทรนด์ ---
trend_products = [
    {"name": "กระบอกน้ำเก็บความเย็น 2 ลิตร", "img": "https://images.unsplash.com/photo-1602143399827-bd95967c7c40?w=500"},
    {"name": "ไฟแต่งห้อง RGB อัจฉริยะ", "img": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=500"},
    {"name": "เครื่องดูดฝุ่นไร้สายพกพา", "img": "https://images.unsplash.com/photo-1558317374-067fb5f30001?w=500"},
    {"name": "สเปรย์ฉีดผ้าหอมไม่ต้องซัก", "img": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=500"},
    {"name": "กล้องวงจรปิดจิ๋วไร้สาย", "img": "https://images.unsplash.com/photo-1557862921-37829c790f19?w=500"}
]

with st.sidebar:
    st.header("🔍 ค้นหาไอเดีย")
    if st.button("🎲 สุ่มสินค้าขายดีวันนี้"):
        chosen = random.choice(trend_products)
        st.session_state.product_name = chosen["name"]
        st.image(chosen["img"], caption=f"ตัวอย่างสินค้า: {chosen['name']}")
        st.success(f"ลองทำคลิป: {chosen['name']} ดูสิ!")

# --- ส่วนหลักของแอป ---
if 'product_name' not in st.session_state:
    st.session_state.product_name = ""

product_name = st.text_input("📦 ชื่อสินค้าที่จะทำสคริปต์:", value=st.session_state.product_name)

tone = st.selectbox("🎭 เลือกแนวการพากย์:", ["สาวหวานขี้ป้ายยา", "ดุดันไม่เกรงใจใคร", "ตลกกวนๆ", "หรูหราดูแพง"])

if st.button("✨ เสกสคริปต์และวิเคราะห์"):
    if product_name:
        with st.spinner('กำลังใช้ AI วิเคราะห์จุดขาย...'):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"วิเคราะห์จุดขาย, เขียนสคริปต์ TikTok 8 วินาที (Hook, Content, CTA), และแคปชันพร้อมแฮชแท็ก สำหรับสินค้า: {product_name} ในโทน: {tone}"
            response = model.generate_content(prompt)
            
            st.subheader("🎯 วิเคราะห์และสคริปต์")
            st.write(response.text)
    else:
        st.warning("กรุณาใส่ชื่อสินค้าก่อนครับ")
