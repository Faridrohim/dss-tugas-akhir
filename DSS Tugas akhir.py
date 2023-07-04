import streamlit as st

# Data sintetis laptop (contoh)
laptops = [
    {'brand': 'Lenovo', 'kebutuhan': 'Gaming', 'ram': 8, 'storage': 256, 'price': 700},
    {'brand': 'HP', 'kebutuhan': 'Multimedia', 'ram': 16, 'storage': 512, 'price': 1200},
    {'brand': 'Dell', 'kebutuhan': 'Kantor', 'ram': 16, 'storage': 512, 'price': 1500},
    {'brand': 'Asus', 'kebutuhan': 'Gaming', 'ram': 8, 'storage': 512, 'price': 1000},
    {'brand': 'Acer', 'kebutuhan': 'Multimedia', 'ram': 12, 'storage': 256, 'price': 800}
]

# Fungsi untuk menghitung nilai WP
def calculate_wp(laptops, weights):
    scores = []
    for laptop in laptops:
        score = (
            weights['kebutuhan'] * (laptop['kebutuhan'] == kebutuhan) +
            weights['ram'] * (laptop['ram'] == ram) +
            weights['storage'] * (laptop['storage'] == storage) +
            weights['price'] * (laptop['price'] == price)
        )
        scores.append(score)
    return scores

# Tampilan web menggunakan Streamlit
st.title("Sistem Rekomendasi Laptop")

# Input pengguna untuk spesifikasi laptop
kebutuhan = st.selectbox("Pilih Kebutuhan Anda", ['Gaming', 'Multimedia', 'Kantor'])
ram = st.slider("Pilih RAM (GB)", 4, 32, 8, step=4)
storage = st.slider("Pilih Storage (GB)", 128, 1024, 256, step=128)
price = st.slider("Pilih Harga (IDR)", 5000000, 20000000, 10000000, step=1000000)

weights = {'kebutuhan': 0.4, 'ram': 0.3, 'storage': 0.2, 'price': 0.1}

# Tombol untuk memunculkan laptop yang direkomendasikan
if st.button("Rekomendasikan"):
    # Menghitung nilai WP untuk setiap laptop
    laptop_scores = calculate_wp(laptops, weights)

    # Mendapatkan indeks laptop dengan nilai tertinggi
    max_score_index = laptop_scores.index(max(laptop_scores))

    # Menampilkan laptop yang direkomendasikan
    st.subheader("Laptop yang Direkomendasikan:")
    st.write("Merek:", laptops[max_score_index]['brand'])
    st.write("Kebutuhan:", laptops[max_score_index]['kebutuhan'])
    st.write("RAM:", laptops[max_score_index]['ram'], "GB")
    st.write("Storage:", laptops[max_score_index]['storage'], "GB")
    st.write("Harga:", "IDR", laptops[max_score_index]['price'])
