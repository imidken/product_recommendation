import streamlit as st
import pandas as pd
from joblib import dump, load

# Hàm đề xuất sản phẩm tương tự
def get_recs_cont(df, sp_id, cosine_sim, nums=3):
    matching_indices = df.index[df['ma_san_pham'] == sp_id].tolist()
    if not matching_indices:
        print(f"No product found with ID: {sp_id}")
        return pd.DataFrame()  
    idx = matching_indices[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:nums+1]
    product_indices = [i[0] for i in sim_scores]
    return df.iloc[product_indices]

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
                    # st.write(f'<span style="color: green; font-size: 18px;">🛒  {product['ten_san_pham']}</span>', unsafe_allow_html=True)
                    st.write(f'<span style="color: greenyellow; font-size: 18px;">💵 vnd {product['gia_ban']}</span>', unsafe_allow_html=True)
                    expander = st.expander(f"Mô tả")
                    product_description = product['mo_ta']
                    truncated_description = ' '.join(product_description.split()[:100]) + '...'
                    expander.write(truncated_description)
                    expander.markdown("Nhấn vào mũi tên để đóng hộp text này.")  


# Đọc dữ liệu sản phẩm
df_products = pd.read_csv('San_pham_full.csv')
# Lấy 10 sản phẩm
random_products = df_products.head(n=10)
st.session_state.random_products = random_products

# Load mô hình cosin_sim
model = load('cosinesim.joblib')


st.markdown('<div style="text-align:left;font-size: 30px;color: white">✨ Content based model </div>', unsafe_allow_html=True)
st.divider()
st.write(f'<span style="color: white; font-size: 25px;">🛒 Danh sách sản phẩm</span>', unsafe_allow_html=True)

# Kiểm tra xem 'selected_ma_san_pham' đã có trong session_state hay chưa
if 'selected_ma_san_pham' not in st.session_state:
    st.session_state.selected_ma_san_pham = None
product_options = [(row['ten_san_pham'], row['ma_san_pham']) for index, row in st.session_state.random_products.iterrows()]
st.session_state.random_products
container = st.container(border=True)
with container:
    st.markdown('<div style="text-align:center;font-size: 25px;color: orange">🛒 Chọn sản phẩm</div>', unsafe_allow_html=True)
    selected_product = st.selectbox(
        "",
        options=product_options,
        format_func=lambda x: x[0]  
    )
# Hiển thị sản phẩm đã chọn
container1 = st.container(border=True)
with container1:
    st.markdown('<div style="text-align:center;font-size: 25px;color: orange">🛒 Thông tin sản phẩm đã chọn </div>', unsafe_allow_html=True)
# Cập nhật session_state dựa trên lựa chọn hiện tại
    st.session_state.selected_ma_san_pham = selected_product[1]
    if st.session_state.selected_ma_san_pham:
        selected_product = df_products[df_products['ma_san_pham'] == st.session_state.selected_ma_san_pham]
        if not selected_product.empty:
            st.write(f'<span style="color: white; font-size: 18px;">🏷️ Tên sản phẩm:</span>', unsafe_allow_html=True)
            st.write(f'<span style="color: green; font-size: 30px;">{selected_product['ten_san_pham'].values[0]}</span>', unsafe_allow_html=True)            
            st.write("💳 ID sản phẩm: ",f'<span style="color: lime; font-size: 17px;">{st.session_state.selected_ma_san_pham}</span>', unsafe_allow_html=True)
            st.divider()
            product_description = selected_product['mo_ta'].values[0]
            truncated_description = ' '.join(product_description.split()[:100])
            st.write(f'<span style="color: white; font-size: 18px;">ⓘ Thông tin:</span>', unsafe_allow_html=True)
            st.write(truncated_description, '...')
            st.divider()
            st.write(f'<span style="color: white; font-size: 22px;">🛒 Các sản phẩm đề xuất liên quan:</span>', unsafe_allow_html=True)
            recommendations = get_recs_cont(df_products, st.session_state.selected_ma_san_pham, model, nums=3) 
            display_recommended_products(recommendations, cols=3)
        else:
            st.write(f"Không tìm thấy sản phẩm với ID: {st.session_state.selected_ma_san_pham}")









