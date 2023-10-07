import uinput
import json
from utils import Fnc_Call

MOUSE_SENSE = 25    # Sensibilidade do mouse
caps_lock = False   # Indica se o caps_lock está ativado ou não

# Configuracao de notas-teclas padrão
teclas = {
    'A0': uinput.KEY_A,
    'A#0/Bb0': uinput.KEY_B,
    'B0': uinput.KEY_C,
    'C1': uinput.KEY_D,
    'C#1/Db1': uinput.KEY_E,
    'D1': uinput.KEY_F,
    'D#1/Eb1': uinput.KEY_G,
    'E1': uinput.KEY_H,
    'F1': uinput.KEY_I,
    'F#1/Gb1': uinput.KEY_J,
    'G1': uinput.KEY_K,
    'G#1/Ab1': uinput.KEY_L,
    'A1': uinput.KEY_M,
    'A#1/Bb1': uinput.KEY_N,
    'B1': uinput.KEY_O,
    'C2': uinput.KEY_P,
    'C#2/Db2': uinput.KEY_Q,
    'D2': uinput.KEY_R,
    'D#2/Eb2': uinput.KEY_S,
    'E2': uinput.KEY_T,
    'F2': uinput.KEY_U,
    'F#2/Gb2': uinput.KEY_V,
    'G2': uinput.KEY_W,
    'G#2/Ab2': uinput.KEY_X,
    'A2': uinput.KEY_Y,
    'A#2/Bb2': uinput.KEY_Z,
    'B2': uinput.KEY_A,
    'C3': uinput.KEY_B,
    'C#3/Db3': uinput.KEY_C,
    'D3': uinput.KEY_D,
    'D#3/Eb3': uinput.KEY_E,
    'E3': uinput.KEY_F,
    'F3': uinput.KEY_G,
    'F#3/Gb3': uinput.KEY_H,
    'A#3/Bb3': uinput.KEY_J,
    'B3': uinput.KEY_CAPSLOCK
}

mouse = {
    'A3': (uinput.REL_X, 1),
    'G3': (uinput.REL_X, -1),
    'C#4/Db4': (uinput.REL_Y, 1),
    'G#3/Ab3': (uinput.REL_Y, -1),
    'C4': (uinput.BTN_LEFT, 1), 
    'D4': (uinput.BTN_RIGHT, 1)
    }

# Inicialização do dispositivo de saída
teclas_keys = list(teclas.values())
mouse_events = [event[0] for event in mouse.values()]
events = teclas_keys + mouse_events

dispositivo = uinput.Device(events)


def mapear(disp, entrada):
    """Dado o dispositivo de saida e uma entrada, mapeia a entrada para um evento"""
    global caps_lock
    if entrada in mouse:
        if mouse[entrada][0] in (uinput.BTN_RIGHT, uinput.BTN_LEFT):
            disp.emit(mouse[entrada][0], mouse[entrada][1])
            disp.emit(mouse[entrada][0], 0)
        else:
            disp.emit(mouse[entrada][0], mouse[entrada][1]*MOUSE_SENSE)
    elif entrada in teclas:
        if isinstance(teclas[entrada], list):
            # Caso seja uma palavra
            for tecla in teclas[entrada]:
                disp.emit_click(tecla)
        elif isinstance(teclas[entrada], Fnc_Call):
            # Caso seja uma chamada de funcao
            teclas[entrada].funcao()
        else:
            # Teclas individuais
            if teclas[entrada] == uinput.KEY_CAPSLOCK:
                if caps_lock:
                    print('Caps-lock OF')
                    caps_lock = False
                else:
                    print('Caps-lock ON')
                    caps_lock = True
            if caps_lock:
                disp.emit_combo([uinput.KEY_CAPSLOCK, teclas[entrada]])
            else:
                disp.emit_click(teclas[entrada])


def load_teclas(arq):
    """Carrega configuracao de teclas de um arquivo json"""
    try:
        with open(arq, 'r') as arquivo_json:
            dados = json.load(arquivo_json)

        if 'teclas' in dados:
            for key in dados['teclas']:
                dados['teclas'][key] = getattr(uinput, dados['teclas'][key])

        if 'mouse' in dados:
            for key in dados['mouse']:
                dados['mouse'][key][0] = getattr(uinput, dados['mouse'][key][0])

        if 'palavras' in dados:
            for key in dados['palavras']:
                palavra = dados['palavras'][key]
                temp = []
                for letra in palavra:
                    temp.append(getattr(uinput, f'KEY_{letra.upper()}'))
                dados['teclas'][key] = temp

        if 'funcoes' in dados:
            for key in dados['funcoes']:
                mod, fun = dados['funcoes'][key].split('.')
                dados['teclas'][key] = Fnc_Call(mod, fun)

        global teclas, mouse, events

        if 'teclas' in dados:
            teclas = dados['teclas']
        if 'mouse' in dados:
            mouse = dados['mouse']
        teclas_keys = list(teclas.values())
        mouse_events = [event[0] for event in mouse.values()]
        events = teclas_keys + mouse_events

    except Exception as E:
        print('Erro ao carregar as teclas do arquivo', arq, '\n ', E)
