# STM32F4 / ESP32-S3 - artificial rain
class ArtificialRainSystem:
    def __init__(self):
        self.bombas = "desligado"
        self.valvulas = "desligado"
        self.atomizadores = "desligado"
    
    def ligar_sistema_chuva(self):
        print("Ligando sistema de chuva artificial...")
        self.bombas = "ligado"
        self.valvulas = "ligado"
        self.atomizadores = "ligado"
    
    def desligar_sistema_chuva(self):
        print("Desligando sistema de chuva artificial...")
        self.bombas = "desligado"
        self.valvulas = "desligado"
        self.atomizadores = "desligado"
