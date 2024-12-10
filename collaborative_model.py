import streamlit as st
import pandas as pd
import numpy as np
np._import_array()
from joblib import dump, load

# Đọc dữ liệu kkhách hàng, sản phẩm, đánh giá
df_users = pd.read_csv('Khach_hang_full.csv')
df_productions = pd.read_csv("San_pham_full.csv")
df = pd.read_csv("Danh_gia_full.csv")
# Hàm lấy thông tin khách hàng theo id
def get_user_info(userid):
    if userid == None:
        return "Không có thông tin khách hàng"
    df_selected = df[(df['ma_khach_hang'] == userid) & (df['so_sao'] >= 3)]
    df_selected = df_selected.set_index('ma_san_pham')
    df_selected = pd.merge(df_selected, df_productions[['ma_san_pham', 'ten_san_pham']], on='ma_san_pham', how='left')
    return df_selected[['ma_khach_hang','so_sao','ma_san_pham', 'ten_san_pham']].sort_values(by=['so_sao'], ascending=False).head(df_selected.shape[0])

# Hàm đề xuất sản phẩm tương tự
def get_recs(userid,model):
    df_rs=df_productions
    if userid == None:
        df_rs = df_rs.sort_values(by=['diem_trung_binh'], ascending=False).head(3)
    else:   
        df_rs['Estimate_Score'] = df['ma_san_pham'].apply(lambda x: model.predict(userid, x).est)
        df_rs=df_rs.sort_values(by=['Estimate_Score'], ascending=False).head(3)
    return df_rs

# Hiển thị đề xuất ra bảng
def display_recommended_products(recommended_products, cols=5):
    for i in range(0, len(recommended_products), cols):
        column_layout  = st.columns(cols)
        for j, col in enumerate(column_layout ):
            if i + j < len(recommended_products):
                product = recommended_products.iloc[i + j]
                with col:         
                    st.write(f'<span style="color: green; font-size: 18px;">🛒  {product['ten_san_pham']}</span>', unsafe_allow_html=True)
        column_layout  = st.columns(cols)
        for j, col in enumerate(column_layout ):
            if i + j < len(recommended_products):
                product = recommended_products.iloc[i + j]
                with col:         
                    st.write(f'<span style="color: greenyellow; font-size: 18px;">💵 vnd {product['gia_ban']}</span>', unsafe_allow_html=True)
                    expander = st.expander(f"Mô tả")
                    product_description = product['mo_ta']
                    truncated_description = ' '.join(product_description.split()[:100]) + '...'
                    expander.write(truncated_description)
                    expander.markdown("Nhấn vào mũi tên để đóng hộp text này.")  

# Load mô hình surprise
model = load('surprise_model.joblib')

# Lấy 10 sản phẩm
random_users = df_users.head(n=10)
st.session_state.random_users = random_users
st.markdown('<div style="text-align:left;font-size: 30px;color: white">✨ Collaborative model </div>', unsafe_allow_html=True)
st.divider()
if 'selected_ma_khach_hang' not in st.session_state:
    st.session_state.selected_ma_khach_hang = None
user_options = [(row['ho_ten'], row['ma_khach_hang']) for index, row in st.session_state.random_users.iterrows()]
container = st.container(border=True)
with container:
    col1, col2, col3 = st.columns([4,1, 3])
    with col1:
        st.markdown('<div class="centered">🔒 Đăng nhập</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('', unsafe_allow_html=True)
    selected_user = col1.selectbox(
        "",
        options=user_options,
        format_func=lambda x: x[0]  
    )
st.session_state.selected_userName = selected_user[0]
st.session_state.selected_ma_khach_hang = selected_user[1]
with col3:
        st.markdown('<div class="centered">❌ Bỏ qua đăng nhập</div>', unsafe_allow_html=True)
        st.markdown('<div class="centered-button-container">', unsafe_allow_html=True)
        if st.button("Tiếp tục tham quan",icon="🚀",type="secondary", use_container_width=True):
            st.session_state.selected_ma_khach_hang=None  
            st.session_state.selected_userName="Khách"       
        st.markdown('</div>', unsafe_allow_html=True)
container = st.container(border=True)
with container:
    st.markdown('<div style="text-align:center;font-size: 25px;color: orange">💁‍♀️ Thông tin khách hàng </div>', unsafe_allow_html=True)
    st.divider()
    col1, col2= st.columns([1,1])
    with col1:
        st.write("✏️ Khách hàng:&nbsp;&nbsp;&nbsp;", f'<span style="color: green; font-size: 20px;">{st.session_state.selected_userName}</span>', unsafe_allow_html=True)
    with col2:
        st.write("✏️ ID:&nbsp;&nbsp;&nbsp;", f'<span style="color: green; font-size: 20px;">{st.session_state.selected_ma_khach_hang}</span>', unsafe_allow_html=True)
    user_info = get_user_info(st.session_state.selected_ma_khach_hang)
    if isinstance(user_info, pd.DataFrame):
        st.dataframe(user_info)
    else:
        st.write("")

container1 = st.container(border=True)
with container1:    
    st.markdown('<div style="text-align:center;font-size: 25px;color: orange"> ✨ Đề xuất sản phẩm</div>', unsafe_allow_html=True)
    st.divider()
    recommendations=get_recs(st.session_state.selected_ma_khach_hang,model)    
    display_recommended_products(recommendations, cols=3)
    st.dataframe(recommendations)

