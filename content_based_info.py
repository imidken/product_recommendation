import streamlit as st
import pandas as pd

st.markdown('<div style="text-align:left;font-size: 30px;color: white">✨ Xây dựng hệ thống đề xuất dựa trên nội dung </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:left;font-size: 22px;color: orange"> Mô hình được sử dụng: Cosine Similarity </div>', unsafe_allow_html=True)
st.image('cs_formula.png')
st.divider()
st.markdown(' 1. Dữ liệu sử dụng được lấy từ các cột: "phan_loai", "gia_ban", "mô tả", "diem_trung_binh" của các file: "Khach_hang_full.csv", "San_pham_full.csv", "Danh_gia_full.csv"')
st.image('cs_data_cols.png')
st.markdown(''' 2. Tiền xử lý dữ liệu đối với các cột văn bản, bao gồm:
            ''')
st.markdown('''> - Chuyển thành viết thường''')
st.markdown('''> - Loại bỏ xuống dòng và dấu câu''')
st.markdown('''> - Xử lý các dấu cách, khoảng trắng''')
st.markdown('''> - Word tokenize''')
st.markdown('''> - Xử lý từ phủ định''')
st.markdown('''> - Xóa stopwords''')
st.markdown('''> - Kết hợp 2 cột văn bản: phan_loai và mo_ta thành cột content''')
st.markdown('''> - Loại bỏ xuống dòng''')
st.markdown(''' 3. Tiền xử lý dữ liệu đối với các cột số => chuẩn hóa''')

st.markdown(''' 4. Kết hợp vector văn bản và vector số thành vector duy nhất bằng hstack''')

st.markdown(''' 5. Xây dựng mô hình Cosine Similarity''')

st.markdown(''' 6. Lưu mô hình, triển khai đề xuất. Kết quả đề xuất cho sản phẩm có id = 422204999:
            ''')
st.image('cs_demo.png')
st.image('cs_demo_heatmap.png')