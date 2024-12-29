# STM32 / ESP32 - Controle de Voo >> gerencia os motores, estabilizadores, GPS e IMU para a navegação do drone.
class FlightControl:
    def __init__(self):
        self.motores = "desligados"
        self.gps = None
        self.imu = None

    def iniciar_voo(self):
        print("Iniciando voo...")
        self.motores = "ligados"

        self.gps = "ativo"
        self.imu = "ativo"
    
    def parar_voo(self):
        print("Parando voo...")
        self.motores = "desligados"

        self.gps = "desligado"
        self.imu = "desligado"
