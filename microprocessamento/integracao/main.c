int main() {
    // inicializa todos os módulos
    FlightControl flight = {0, 0, 0};
    EnvironmentalSensors sensors = {0, 0, 0, 0};
    BioreactorManagement bioreactor = {0, 0};
    ArtificialRainSystem rain_system = {0, 0, 0};
    CommunicationAndCoordination comm = {{"Drone1"}, 1};
    MachineLearning ml = {0};

    // exemplo de interação entre os sistemas
    printf("iniciando sistema...\n");

    // inicia o voo
    iniciar_voo(&flight);

    // lê sensores ambientais
    ler_sensores(&sensors);

    // libera sementes e dosa nutrientes
    liberar_sementes(&bioreactor);
    dosar_nutrientes(&bioreactor);

    // liga sistema de chuva artificial
    ligar_chuva(&rain_system);

    // adiciona drones à rede e define rotas
    adicionar_drone(&comm, "Drone2");
    definir_rota(&comm, "Rota Norte");

    // treina modelo de ml e analisa imagens
    treinar_modelo(&ml);
    analisar_imagens(&ml, "imagem_de_area_degradada.jpg");

    // desliga o sistema de chuva
    desligar_chuva(&rain_system);

    // para o voo
    parar_voo(&flight);

    printf("sistema finalizado.\n");

    return 0;
}
