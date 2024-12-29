# Raspberry Pi Pico / Arduino Due - sensores ambientais
class EnvironmentalSensors:
    def __init__(self):
        self.umidade = 0
        self.temperatura = 0
        self.vento = 0
        self.solo = 0
    
    def ler_sensores(self):
        self.umidade = 75
        self.temperatura = 25
        self.vento = 10
        self.solo = 50
    
    def ajustar_dispersao(self):
        print(f"Ajustando dispersão: Umidade: {self.umidade}, Temperatura: {self.temperatura}, Vento: {self.vento}, Solo: {self.solo}")
