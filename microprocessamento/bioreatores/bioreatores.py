# ATmega328 / ESP32 - gestão dos Bioreatores
class BioreactorManagement:
    def __init__(self):
        self.sementes = "desligado"
        self.nutrientes = "desligado"
    
    def liberar_sementes(self):
        print("Liberando sementes...")
        self.sementes = "ligado"
    
    def dosar_nutrientes(self):
        print("Dosando nutrientes...")
        self.nutrientes = "ligado"
