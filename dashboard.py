import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load Dataset
day = pd.read_csv("day.csv")

# Konversi tanggal
day['dteday'] = pd.to_datetime(day['dteday'])

# Mapping nama bulan dan musim
day['month'] = day['dteday'].dt.month_name()
day['season'] = day['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})

# Sidebar untuk filter interaktif
st.sidebar.header("🔍 Filter Data")
start_date = st.sidebar.date_input("Mulai Tanggal", day['dteday'].min())
end_date = st.sidebar.date_input("Sampai Tanggal", day['dteday'].max())
selected_season = st.sidebar.multiselect("Pilih Musim", day['season'].unique(), default=day['season'].unique())

# Filter dataset berdasarkan input pengguna
filtered_data = day[(day['dteday'] >= pd.to_datetime(start_date)) & 
                    (day['dteday'] <= pd.to_datetime(end_date)) & 
                    (day['season'].isin(selected_season))]

# Dashboard
st.title("Dashboard Peminjaman Sepeda 🚲")
st.markdown("---")

# Pilihan Select Box
option = st.selectbox("Pilih Tampilan:", ["Visualisasi Data", "Hasil Binning"])

if option == "Visualisasi Data":
    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Peminjaman", f"{filtered_data['cnt'].sum():,}")
    col2.metric("Pengguna Terdaftar", f"{filtered_data['registered'].sum():,}")
    col3.metric("Pengguna Casual", f"{filtered_data['casual'].sum():,}")

    # Histogram Peminjaman
    st.subheader("📊 Distribusi Peminjaman Sepeda")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(filtered_data['cnt'], bins=30, kde=True)
    plt.title("Distribusi Peminjaman Sepeda")
    st.pyplot(fig)

    # Distribusi Peminjaman Berdasarkan Musim
    st.subheader("🌦 Distribusi Peminjaman Berdasarkan Musim")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(x=filtered_data['season'])
    plt.title("Distribusi Peminjaman Berdasarkan Musim")
    st.pyplot(fig)

    # Scatter Plot Suhu vs Peminjaman
    st.subheader("🌡 Hubungan Suhu dengan Peminjaman Sepeda")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(x=filtered_data['temp'], y=filtered_data['cnt'])
    plt.title("Hubungan Suhu dengan Jumlah Peminjaman")
    st.pyplot(fig)

    # Rata-rata Peminjaman Sepeda per Bulan
    st.subheader("📆 Rata-rata Peminjaman Sepeda per Bulan")
    monthly_trend = filtered_data.groupby('month')['cnt'].mean().sort_values()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=monthly_trend.index, y=monthly_trend.values)
    plt.xticks(rotation=45)
    plt.title("Rata-rata Peminjaman Sepeda per Bulan")
    st.pyplot(fig)

    # Tren Peminjaman Sepeda berdasarkan Bulan
    st.subheader("📆 Tren Peminjaman Sepeda per Bulan")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=day, x='mnth', y='cnt', ci=None, marker='o')
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Peminjaman')
    plt.title('Tren Peminjaman Sepeda Berdasarkan Bulan')
    st.pyplot(fig)

    # Distribusi Peminjaman Berdasarkan Musim
    st.subheader("🌦 Distribusi Peminjaman Berdasarkan Musim")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x='season', y='cnt', data=filtered_data)
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Peminjaman')
    plt.title('Distribusi Peminjaman Sepeda Berdasarkan Musim')
    st.pyplot(fig)

    # Korelasi Antara Faktor Cuaca dan Peminjaman
    st.subheader("🔗 Korelasi Antara Faktor Cuaca dan Peminjaman Sepeda")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(day[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Korelasi Antara Faktor Cuaca dan Peminjaman Sepeda')
    st.pyplot(fig)

    # Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan
    st.subheader("📅 Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x='workingday', y='cnt', data=filtered_data)
    plt.xticks([0, 1], ['Akhir Pekan', 'Hari Kerja'])
    plt.xlabel('Hari')
    plt.ylabel('Jumlah Peminjaman')
    plt.title('Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan')
    st.pyplot(fig)

elif option == "Hasil Binning":
    st.subheader("📊 Hasil Binning Peminjaman Sepeda dan Faktor Cuaca")

    # Binning untuk Jumlah Peminjaman
    filtered_data['cnt_category'] = pd.cut(filtered_data['cnt'], bins=[0, 2000, 4000, filtered_data['cnt'].max()], 
                                           labels=['Rendah', 'Sedang', 'Tinggi'])

    # Binning untuk Suhu
    filtered_data['temp_category'] = pd.cut(filtered_data['temp'], bins=[0, 0.3, 0.6, 1], 
                                            labels=['Dingin', 'Normal', 'Panas'])

    # Binning untuk Kelembaban
    filtered_data['hum_category'] = pd.cut(filtered_data['hum'], bins=[0, 0.4, 0.7, 1], 
                                           labels=['Rendah', 'Sedang', 'Tinggi'])

    # Menampilkan hasil
    st.dataframe(filtered_data[['cnt', 'cnt_category', 'temp', 'temp_category', 'hum', 'hum_category']].head(20))
    # Visualisasi Binning: Bar Chart Peminjaman per Kategori
    st.subheader("📊 Distribusi Peminjaman Berdasarkan Kategori")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='cnt_category', data=filtered_data, palette="Set2")
    plt.xlabel("Kategori Jumlah Peminjaman")
    plt.ylabel("Frekuensi")
    st.pyplot(fig)

    # Visualisasi Binning: Heatmap Hubungan Faktor Cuaca dan Peminjaman
    st.subheader("🔥 Korelasi antara Faktor Cuaca dan Peminjaman")
    pivot_table = filtered_data.pivot_table(index="temp_category", columns="hum_category", values="cnt", aggfunc="mean")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(pivot_table, annot=True, cmap="coolwarm", fmt=".0f")
    plt.xlabel("Kategori Kelembaban")
    plt.ylabel("Kategori Suhu")
    st.pyplot(fig)

else :
    st.subheader("Silahkan pilih filternya terlebih dahulu")