import streamlit as st
import pandas as pd

st.markdown('<div style="text-align:left;font-size: 30px;color: white">✨ Xây dựng hệ thống đề xuất dựa trên tương tác </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:left;font-size: 22px;color: orange"> Mô hình được sử dụng: Surprise </div>', unsafe_allow_html=True)
st.image('sp_model.png')
st.divider()
st.markdown(' 1. Dữ liệu sử dụng được lấy từ 3 cột: "ma_khach_hang", "ma_san_pham", "so_sao" của các file: "Khach_hang_full.csv", "San_pham_full.csv", "Danh_gia_full.csv"')
st.image('sp_data_cols.png')
st.markdown(''' 2. Xây dựng các thuật toán:SVD, SVD++, NMF, SlopeOne, KNNBasic, KNNBaseline, KNNWithMeans, KNNWithZScore, CoClustering, BaselineOnly với kỹ thuật cross validate để dự đoán, đánh giá mô hình.
            Kết quả thuật toán KNNBaseline cho ra dự đoán chính xác hơn các thuật toán còn lại => chọn KNNBaseline
            ''')
st.image('sp_crossval_rs.png')
st.markdown(''' 3. Lưu mô hình, triển khai đề xuất. Kết quả đề xuất cho người dùng có id = 1565:
            ''')
st.image('sp_demo.png')