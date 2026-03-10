import torch
import torch.nn as nn
import torch.optim as optim
import time
import random

# ==========================================
# 1. IL CUORE: LOGICA TEORIA DELLA RADICE
# ==========================================
class RootEngine:
    def __init__(self):
        # Pesi iniziali calibrati (E, N, S, C, T)
        self.weights = torch.tensor([1.0, 1.2, 1.8, 1.0, 1.1], requires_grad=True)
        self.optimizer = optim.SGD([self.weights], lr=0.01)

    def calculate_p(self, E, N, S, C, T):
        """
        Formula di Marco: P = ((E * N) + S) / (C + T)
        """
        w = self.weights
        numerator = (E * w[0] * N * w[1]) + (S * w[2])
        denominator = (C * w[3]) + (T * w[4])
        return numerator / denominator

# ==========================================
# 2. IL CERVELLO: AI CHE IMPARA (LOSS FUNCTION)
# ==========================================
    def update_ai(self, predicted_p, actual_outcome):
        """
        L'AI confronta la pressione calcolata con l'evento reale.
        Se P era alto ma non c'è stato il gol, ricalibra i pesi.
        """
        self.optimizer.zero_grad()
        # Se c'è stato un gol/corner (1.0), la perdita è la distanza da P
        target = torch.tensor(float(actual_outcome))
        loss = torch.abs(predicted_p - target)
        loss.backward()
        self.optimizer.step()
        return loss.item()

# ==========================================
# 3. IL MOTORE: SIMULATORE LIVE & SCRAPER
# ==========================================
def get_match_nutrients():
    """Simula l'arrivo di dati real-time dai campi"""
    return {
        "E": random.uniform(6, 10),  # Evento Radice (Energia iniziale)
        "N": random.uniform(5, 9),   # Nutrienti (Possesso trequarti)
        "S": random.uniform(7, 10),  # Saturazione (Attacchi continui)
        "C": random.uniform(4, 8),   # Contro-Evento (Resistenza)
        "T": random.uniform(1, 4)    # Tempo di Adattamento (Reattività)
    }

# ==========================================
# 4. IL DEPLOY: ESECUZIONE TOTALE
# ==========================================
def start_root_system():
    print("🚀 SISTEMA ROOT-AI ATTIVO")
    print("Teoria della Radice di Marco: Causalità Adattiva v2.0")
    print("-" * 50)
    
    engine = RootEngine()
    
    try:
        while True:
            # 1. Prendi i nutrienti live
            data = get_match_nutrients()
            
            # 2. Calcola la Pressione P
            p_val = engine.calculate_p(data['E'], data['N'], data['S'], data['C'], data['T'])
            
            # 3. Determina il segnale
            print(f"DEBUG | P: {p_val.item():.2f} | Sat: {data['S']:.2f} | Res: {data['C']:.2f}")
            
            if p_val > 9.0:
                print("🔥 [ALERTA CRITICA] Punto di Rottura Identificato! Probabile GOL/CORNER.")
            elif p_val > 7.5:
                print("⚠️ [ACCUMULO] Pressione in aumento. Monitorare ramificazione.")
            
            # 4. Simulazione Feedback AI (In un caso reale avviene dopo l'evento)
            # Se P > 9, simuliamo che l'evento sia accaduto (1.0) per allenare l'AI
            if p_val > 9.0:
                loss = engine.update_ai(p_val, 1.0)
                print(f"🧠 AI: Apprendimento completato (Loss: {loss:.4f})")
            
            print("-" * 30)
            time.sleep(5) # Aggiornamento ogni 5 secondi per il test
            
    except KeyboardInterrupt:
        print("\n🛑 Sistema interrotto dall'utente.")

if __name__ == "__main__":
    start_root_system()
