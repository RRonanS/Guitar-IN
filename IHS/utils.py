import numpy as np
from scipy.signal import find_peaks
import json

ATRASO = 100
DIR = 'data/'

def calcular_freq(input, rate, debug=False):
    try:
        sinal = np.frombuffer(b''.join(input), dtype=np.int16)
        
        # Normalização do sinal
        sinal = sinal / np.max(np.abs(sinal))
        
        # Calculando a autocorrelação
        autocorrelacao = np.correlate(sinal, sinal, mode='full')
        
        # Removendo a metade negativa da autocorrelação
        autocorrelacao = autocorrelacao[len(autocorrelacao)//2:]
        
        # Encontrando o primeiro pico após um atraso mínimo, evita picos de alta frequencia
        atraso_minimo = int(rate / ATRASO) 
        picos, _ = find_peaks(autocorrelacao, distance=atraso_minimo)
        
        if len(picos) > 0:
            frequencia_hz = rate / picos[0]
        else:
            frequencia_hz = 0.0
        
        return frequencia_hz
    except Exception:
        if debug:
            print('Falha no processamento do sinal;\n', Exception)
        return 0.0

def find_note(v_freq, freq_dom, tol):
    """Dado o dicionário que associa frequência a nota, a frequência dominante e a tolerância,
    retorna a nota associada se existir ou None."""
    sorted_freqs = sorted(v_freq.keys())

    # Busca binaria nas frequencias
    left, right = 0, len(sorted_freqs) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_freq = sorted_freqs[mid]

        if abs(freq_dom - mid_freq) <= tol:
            return v_freq[mid_freq]

        if freq_dom < mid_freq:
            right = mid - 1
        else:
            left = mid + 1
    return None


def get_limiar(v_freq):
    """Retorna uma tupla de dois itens respectivamente a menor e maior frequencia que represente uma nota"""
    sorted_freqs = sorted(v_freq.keys())
    return sorted_freqs[0], sorted_freqs[len(sorted_freqs)-1]


def inicializar_config():
    """Le e retorna as configurações de inicio"""
    try:
        with open(DIR+'start.json', 'r') as arquivo_json:
            dados = json.load(arquivo_json)
            return dados
    except:
            print('Erro ao ler o arquivo de inicializacao')
            return {
                    "device_index": 0,
                    "ask_device": True,
                    "load_keys": False,
                    "keys_dir": "",
                    "debug": False
                    }


class Fnc_Call:
    """Classe para armazenar a chamada de uma função"""
    def __init__(self, modulo, funcao):
        try:
            modulo = __import__(modulo)
            self.funcao = getattr(modulo, funcao)
        except Exception as E:
            self.funcao = self.NullFunc
    
    def NullFunc():
        return None
