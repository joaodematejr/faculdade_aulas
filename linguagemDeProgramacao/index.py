LAGES_FLORIPA = 220
FLORIPA_JOINVILE = 160
JOINVILE_LAGES = 320

HBGASOLINA = 18
CRETAGASOLINA = 11
SANTAFEGASOLINA = 9

HBETANOL = 16
CRETAETANOL = 9
SANTAFEETANOL = 7


VALOR_GASOLINA = 4.50
VALOR_ETANOL = 3.80

cidadeEscolhida = 0
carroEscolhido = 0
carroEscolhidoEtanol = 0

while True:
    cidade = int(input(
        'Primeiro escolha uma cidade : \n [1] - Lages - Florianopolis  \n [2] - Florianopolis - Joinvile \n [3] - Joinvile - Lages \n'))
    if cidade != 0 and cidade <= 3:
        carro = int(input(
            'Agora escolha seu Veiculo : \n [1] - HB20  \n [2] - Creta \n [3] - Santa Fé \n'))
        if carro != 0 and carro <= 3:
            if cidade == 1:
                cidadeEscolhida = LAGES_FLORIPA
            if cidade == 2:
                cidadeEscolhida = FLORIPA_JOINVILE
            if cidade == 3:
                cidadeEscolhida = JOINVILE_LAGES
        if cidadeEscolhida != 0:
            if carro == 1:
                carroEscolhido = HBGASOLINA
                carroEscolhidoEtanol = HBETANOL
            if carro == 2:
                carroEscolhido = CRETAGASOLINA
                carroEscolhidoEtanol = CRETAETANOL
            if carro == 3:
                carroEscolhido = SANTAFEGASOLINA
                carroEscolhidoEtanol = SANTAFEETANOL
        if cidadeEscolhida != 0 and carroEscolhido != 0:

            resultadoGasolina = carroEscolhido * cidadeEscolhida
            resultadoGasolinaEtanol = carroEscolhidoEtanol * cidadeEscolhida
            calcular_gasolina = resultadoGasolina * VALOR_GASOLINA
            calcular_etanol = resultadoGasolinaEtanol * VALOR_ETANOL

            print('O CONSUMO TODAL DE COMBUSTIVEL EM GASOLINA : ',
                  "%.2f" % resultadoGasolina)
            print('O CONSUMO TODAL DE COMBUSTIVEL EM ETANOL : ', "%.2f" %
                  resultadoGasolinaEtanol)
            print('VALOR PAGO PELA GASOLINA É: ', "%.2f" %
                  calcular_gasolina, 'R$')
            print('VALOR PAGO PELA ETANOL É: ', "%.2f" % calcular_etanol, 'R$')
        else:
            print('Veiculo Invalido')
    else:
        print('Opção Invalida')
