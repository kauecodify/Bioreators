# NVIDIA Jetson Nano / Qualcomm Snapdragon Flight - comunicação e coordenação
class CommunicationAndCoordination:
    def __init__(self):
        self.drones_na_rede = []
        self.rotas = []

    def adicionar_drone(self, drone_id):
        self.drones_na_rede.append(drone_id)
    
    def definir_rota(self, rota):
        self.rotas.append(rota)
        print(f"Rota definida: {rota}")

    def coordenar_drones(self):
        # coordena a comunicação entre os drones
        print(f"Coordenando {len(self.drones_na_rede)} drones com {len(self.rotas)} rotas.")
