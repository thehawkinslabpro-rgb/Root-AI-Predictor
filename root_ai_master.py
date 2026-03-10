import streamlit as st
import pandas as pd
import numpy as np
import time
import random

# --- CONFIGURAZIONE DASHBOARD ---
st.set_page_config(page_title="Root-AI Control Panel", layout="wide")
st.title("🌳 Root-AI: Dashboard della Saturazione")

# --- LOGICA CORE (La tua formula) ---
def calcola_p(E, N, S, C, T):
    # P = ((E * N) + S) / (C + T)
    # Usiamo pesi ottimizzati dall'ultima calibrazione
    weights = {"E": 1.0, "N": 1.2, "S": 1.8, "C": 1.0, "T": 1.1}
    num = (E * weights["E"] * N * weights["N"]) + (S * weights["S"])
    den = (C * weights["C"]) + (T * weights["T"])
    return num / den

# --- SIDEBAR PER INPUT LIVE ---
st.sidebar.header("Dati Partita Live")
match_name = st.sidebar.text_input("Partita", "Inter vs Juventus")
s_val = st.sidebar.slider("Saturazione (S)", 0.0, 10.0, 5.0)
c_val = st.sidebar.slider("Resistenza (C)", 0.0, 10.0, 5.0)

# --- AREA PRINCIPALE ---
col1, col2 = st.columns(2)

with col1:
    p_attuale = calcola_p(8, 7, s_val, c_val, 2) # E, N, T simulati o fissi
    st.metric(label="PRESSIONE RADICE (P)", value=f"{p_attuale:.2f}", delta=f"{p_attuale-7:.2f}")
    
    # Progress Bar della Saturazione
    st.write("Livello di Saturazione Critica")
    st.progress(min(p_attuale / 12, 1.0)) # Normalizzato per la barra

with col2:
    st.subheader("Verdetto AI")
    if p_attuale > 9.0:
        st.error("🔥 PUNTO DI ROTTURA! Alta probabilità di Gol/Corner")
    elif p_attuale > 7.5:
        st.warning("⚠️ ACCUMULO: La radice sta avvolgendo l'area")
    else:
        st.success("❄️ STASI: Sistema in equilibrio")

# --- GRAFICO STORICO (Simulato) ---
st.divider()
st.subheader("Andamento Pressione ultimi 30 minuti")
chart_data = pd.DataFrame(np.random.randn(30, 1) * 0.5 + p_attuale, columns=['Pressione'])
st.line_chart(chart_data)

# --- TABELLA ULTIMI 100 RISULTATI ---
st.subheader("Archivio Risultati (Ultime 100 Partite)")
# Qui l'AI caricherebbe il file CSV che abbiamo discusso
df_history = pd.DataFrame({
    'Partita': ['Milan-Roma', 'PSG-OM', 'City-Liverpool'] * 33 + ['Inter-Juve'],
    'Pressione Max': [8.9, 9.2, 7.5] * 33 + [p_attuale],
    'Esito': ['Vinta', 'Vinta', 'Persa (Stasi)'] * 33 + ['In Corso']
})
st.table(df_history.head(10))
