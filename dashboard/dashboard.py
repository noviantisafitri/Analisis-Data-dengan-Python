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

# Dashboard
st.title("📊 Dashboard Peminjaman Sepeda 🚲")
st.markdown("---")

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Peminjaman", f"{day['cnt'].sum():,}")
col2.metric("Pengguna Terdaftar", f"{day['registered'].sum():,}")
col3.metric("Pengguna Casual", f"{day['casual'].sum():,}")

# Tren Peminjaman Sepeda berdasarkan Bulan
st.subheader("📆 Tren Peminjaman Sepeda per Bulan")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=day, x='month', y='cnt', marker='o', ci=None)
plt.xticks(rotation=45)
plt.xlabel("Bulan")
plt.ylabel("Jumlah Peminjaman")
st.pyplot(fig)

# Distribusi Peminjaman Berdasarkan Musim
st.subheader("🌦 Distribusi Peminjaman Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x='season', y='cnt', data=day)
st.pyplot(fig)

# Korelasi Faktor Cuaca terhadap Peminjaman
st.subheader("☀️ Korelasi Faktor Cuaca dan Peminjaman")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(day[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr(), annot=True, cmap='coolwarm', fmt='.2f')
st.pyplot(fig)

# Perbandingan Peminjaman Hari Kerja vs Akhir Pekan
st.subheader("📅 Peminjaman Sepeda: Hari Kerja vs Akhir Pekan")
fig, ax = plt.subplots(figsize=(6, 4))
sns.barplot(x=day['workingday'], y=day['cnt'], ci=None, palette="Set2")
plt.xticks(ticks=[0, 1], labels=["Akhir Pekan", "Hari Kerja"])
st.pyplot(fig)
