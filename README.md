# 📊 Bike Sharing Dashboard 🚲

Dashboard ini menampilkan analisis data peminjaman sepeda menggunakan Streamlit.

---

## 🚀 Setup Environment

### **1️⃣ Menggunakan Anaconda**
```sh
conda create --name bike-sharing python=3.9
conda activate bike-sharing
pip install -r requirements.txt
```

### **2️⃣ Menggunakan Shell/Terminal**
```sh
# Buat direktori proyek
mkdir dashboard
cd dashboard

# Setup environment menggunakan pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```

---

## ▶️ Menjalankan Aplikasi
```sh
streamlit run dashboard.py
```

Aplikasi akan berjalan di **http://localhost:8501** secara default.

---

## 📦 Struktur Direktori
```
/bike_sharing_dashboard
├── dashboard.py         # File utama Streamlit
├── requirements.txt     # Daftar library yang dibutuhkan
├── day.csv              # Dataset peminjaman sepeda
├── README.md            # Dokumentasi proyek
```

---

## 📌 Fitur Dashboard
✅ Visualisasi tren peminjaman sepeda per bulan 📆  
✅ Analisis distribusi peminjaman berdasarkan musim 🌦  
✅ Korelasi faktor cuaca terhadap peminjaman ☀️  
✅ Perbandingan peminjaman di hari kerja vs akhir pekan 📅  
✅ Binning untuk mengelompokkan jumlah peminjaman dan faktor cuaca 📊  

---

## 🌍 Deploy ke Streamlit Cloud
1. **Push project ke GitHub**
2. **Buka [Streamlit Cloud](https://share.streamlit.io/)**
3. **Deploy dengan memilih repository GitHub**
4. **Aplikasi akan tersedia di URL publik** ✨

---

📌 **Dikembangkan oleh Novianti Safitri**
