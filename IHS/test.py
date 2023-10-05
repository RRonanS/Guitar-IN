# Arquivo para gerar testes do gerenciador sem ter uma guitarra
import utils
import gerenciador
from time import sleep

DADOS_INCIALI = utils.inicializar_config()
DEBUG = DADOS_INCIALI['debug']
NOTAS_TESTE = ['E2', 'A2'] # Modifique com as notas que deseja testar o mapeamento

gerenciador.load_teclas('data/funcoes.json') # Carregue o json que deseja usar como base

sleep(1) # Sleep necessário para funcionar corretamente(Dar tempo de istanciar o dispositivo)
for nota in NOTAS_TESTE:
    gerenciador.mapear(gerenciador.dispositivo, nota)
