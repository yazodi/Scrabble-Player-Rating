
import streamlit as st
import joblib
import numpy as np

# Başlık
st.title("📊 Scrabble Oyuncu Derecesi Tahmin Uygulaması")

# Modeli yükle
model = joblib.load("model.pkl")

# Kullanıcıdan giriş verilerini al
st.header("🎮 Oyun Bilgilerini Girin")

player1_score = st.number_input("Player 1 Skoru", min_value=0, value=400)
player2_score = st.number_input("Player 2 Skoru", min_value=0, value=380)
player1_is_winner = st.selectbox("Player 1 Kazandı mı?", [True, False])
player1_vs_bot = st.selectbox("Rakip bot mu?", [True, False])

# Özellikleri hazırla
score_diff = player1_score - player2_score
features = np.array([[player1_score, player2_score, score_diff, int(player1_is_winner), int(player1_vs_bot)]])

# Tahmin
if st.button("Tahmin Et"):
    prediction = model.predict(features)[0]
    st.success(f"Tahmin Edilen Player 1 Rating: {int(prediction)}")
