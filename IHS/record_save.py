import pyaudio
import wave

# Configurações de gravação
FORMAT = pyaudio.paInt16  # Formato de áudio
CHANNELS = 1              # Número de canais de áudio (mono)
RATE = 44100              # Taxa de amostragem (samples por segundo)
CHUNK = 1024              # Tamanho do buffer de áudio
RECORD_SECONDS = 5       # Duração da gravação em segundos
OUTPUT_FILENAME = "output.wav"

# Inicialize o objeto PyAudio
audio = pyaudio.PyAudio()

# Abra um stream de gravação
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Gravando...")

frames = []

# Capture áudio em chunks e armazene em 'frames'
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Gravação concluída.")

# Encerrando o stream e o objeto PyAudio
stream.stop_stream()
stream.close()
audio.terminate()

# Salve os frames como um arquivo WAV
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print(f"Áudio salvo como {OUTPUT_FILENAME}")
