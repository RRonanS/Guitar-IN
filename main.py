import pyaudio
import utils
from frequencias import frequencias
import gerenciador

FORMAT = pyaudio.paInt16  # Formato de áudio
CHANNELS = 1              # Número de canais de áudio (mono)
RATE = 44100             # Taxa de amostragem (samples por segundo)
CHUNK = 8192            # Tamanho do buffer de áudio
RECORD_SECONDS = 0.2      # Duração da gravação em segundos
TOLERANCIA = 5           # Tolerancia em Hz de variação de frequencia para as notas

audio = pyaudio.PyAudio()


def list_audio_devices(p):
    """Lista os dispositivos de audio disponíveis"""
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    for i in range(numdevices):
        device_info = p.get_device_info_by_host_api_device_index(0, i)
        print(f"{i}: {device_info['name']}")


list_audio_devices(audio)
try:
    index = int(input('Entre com o id > '))
except KeyboardInterrupt:
    print('encerrado')

# Abra um stream de gravação
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=index)
print("Iniciando...")

frames = []
min_freq, max_freq = utils.get_limiar(frequencias)


def audio_input():
    """Lê a entrada de audio e a armazena"""
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)


print("Capturando som, ctrl+c para encerrar")
try:
    while 1:
        audio_input()

        frequencia = utils.calcular_freq(frames, RATE)
        if frequencia != 0 and min_freq <= frequencia <= max_freq:
            nota = utils.find_note(frequencias, frequencia, TOLERANCIA)
            print("Frequencia dominante:", frequencia)
            print("Nota associada:", nota)
            gerenciador.mapear(gerenciador.dispositivo, nota)
        frames.clear()
except KeyboardInterrupt:
    print('Finalizando...')


# Encerrando o programa
stream.stop_stream()
stream.close()
audio.terminate()