import numpy as np


def calcular_freq(input, rate):
    """Dado um audio input e o rate retorna a frequencia dominante do audio"""
    try:
        sinal = np.frombuffer(b''.join(input), dtype=np.int16)
        stft = np.abs(np.fft.fft(sinal))
        frequencia_dominante = np.argmax(stft)
        frequencia_hz = frequencia_dominante * rate / len(sinal)
        return frequencia_hz
    except:
        print('Erro')
        return 0


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
