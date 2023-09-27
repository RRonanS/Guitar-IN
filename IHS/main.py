import pyaudio
import threading
import utils
from frequencias import frequencias

FORMAT = pyaudio.paInt16  # Formato de áudio
CHANNELS = 1              # Número de canais de áudio (mono)
RATE = 44100             # Taxa de amostragem (samples por segundo)
CHUNK = 2048              # Tamanho do buffer de áudio
RECORD_SECONDS = 0.1      # Duração da gravação em segundos
TOLERANCIA = 5           # Tolerancia em Hz de variação de frequencia para as notas

audio = pyaudio.PyAudio()

# Abra um stream de gravação
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Iniciando...")

frames = []
min_freq, max_freq = utils.get_limiar(frequencias)


def audio_input():
    """Lê a entrada de audio e a armazena"""
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)


print("Capturando som")
while 1:
    t_in = threading.Thread(target=audio_input)
    t_in.start()
    t_in.join()

    frequencia = utils.calcular_freq(frames, RATE)
    if frequencia != 0 and min_freq <= frequencia <= max_freq:
        print("Frequencia dominante:", frequencia)
        print("Nota associada:", utils.find_note(frequencias, frequencia, TOLERANCIA))
    frames.clear()


# Encerrando o programa
stream.stop_stream()
stream.close()
audio.terminate()
