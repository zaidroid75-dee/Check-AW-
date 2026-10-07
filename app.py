import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="AW Checking System - Zaishop", layout="wide")

st.title("🎨 ระบบตรวจสอบและเปรียบเทียบ Artwork (AW Checklist)")
st.write("สำหรับตรวจสอบความถูกต้องของฉลาก บรรจุภัณฑ์ และชิ้นงานพิมพ์")

# แถบเมนูด้านข้างสำหรับเลือกโหมดการทำงาน
menu = st.sidebar.selectbox("เลือกฟังก์ชันการทำงาน", ["เช็คลิสต์ตรวจสอบ (Checklist)", "เปรียบเทียบไฟล์ (Visual Compare)"])

if menu == "เช็คลิสต์ตรวจสอบ (Checklist)":
    st.header("📋 รายการตรวจสอบความถูกต้อง Artwork")
    
    col1, col2 = st.columns(2)
    with col1:
        project_name = st.text_input("ชื่อโปรเจกต์ / ชิ้นงาน", "Banner Soy Protein 30 CAPS")
    with col2:
        checker_name = st.text_input("ผู้ตรวจสอบ", "Jirun Lammalee")

    st.markdown("---")
    
    # หมวดหมู่การเช็ค
    st.subheader("1. ข้อมูลทางกฎหมายและข้อความบนฉลาก")
    c1 = st.checkbox("✅ ตรวจสอบความถูกต้องของชื่อผลิตภัณฑ์และขนาดบรรจุ")
    c2 = st.checkbox("✅ ตรวจสอบเลข อย. (FDA Number)")
    c3 = st.checkbox("✅ ตรวจสอบเครื่องหมายรับรองฮาลาล (Halal Number / Logo)")
    c4 = st.checkbox("✅ ตรวจสอบส่วนประกอบและตารางโภชนาการ (Nutrition Facts)")
    c5 = st.checkbox("✅ ตรวจสอบคำเตือนบังคับตามกฎหมายและขนาดฟอนต์")

    st.subheader("2. องค์ประกอบกราฟิกและบาร์โค้ด")
    c6 = st.checkbox("✅ ตรวจสอบโลโก้แบรนด์ (Brand Logo & Colors)")
    c7 = st.checkbox("✅ ตรวจสอบบาร์โค้ด / QR Code (สแกนทดสอบอ่านค่าจริง)")
    c8 = st.checkbox("✅ ตรวจสอบระยะตัดตก (Bleed) และขอบเขต Die-cut")

    st.markdown("---")
    st.subheader("3. สรุปผลการตรวจสอบ")
    
    status = st.selectbox("ผลการประเมินชิ้นงาน", ["รอตรวจสอบ", "ผ่าน (Approved)", "ไม่ผ่าน / ต้องแก้ไข (Revision Required)"])
    comment = st.text_area("หมายเหตุ หรือ จุดที่ต้องแก้ไขสำหรับ Designer:")

    if st.button("💾 บันทึกและยืนยันผลการตรวจสอบ"):
        if status == "ผ่าน (Approved)":
            st.success("บันทึกข้อมูลสำเร็จ: ชิ้นงานผ่านการตรวจสอบและพร้อมผลิต!")
        else:
            st.warning("บันทึกข้อมูลสำเร็จ: ส่งข้อมูลกลับให้ทีมแก้ไขปรับปรุง Artwork แล้ว")

elif menu == "เปรียบเทียบไฟล์ (Visual Compare)":
    st.header("🔍 เปรียบเทียบความแตกต่างระหว่างไฟล์ AW")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("ไฟล์ต้นฉบับ (Latest Final AW)")
        img1 = st.file_uploader("อัปโหลดไฟล์ภาพต้นฉบับ", type=["png", "jpg", "jpeg"], key="img1")
        if img1:
            st.image(img1, use_container_width=True)
            
    with col_b:
        st.subheader("ไฟล์ตรวจสอบ (Rechecking AW)")
        img2 = st.file_uploader("อัปโหลดไฟล์ภาพที่ต้องการเทียบ", type=["png", "jpg", "jpeg"], key="img2")
        if img2:
            st.image(img2, use_container_width=True)
            
    if img1 and img2:
        st.info("💡 ระบบเปรียบเทียบภาพพร้อมใช้งาน สามารถตรวจสอบจุดที่แตกต่างระหว่างสองไฟล์ได้จากภาพด้านบน")