import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser as wb
import datetime
import wikipedia as wk

import speech_recognition as sr

VOZ_ESPANIOL = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
ENGLISH_VOICE = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

#Escuchar microfono y devolver el input de audio como texto
def transform_audio_a_texto():
    recognizer = sr.Recognizer()  # Almacenar el reconocedor en una variable
    mic = sr.Microphone()  # Almacenar el micrófono en una variable

    # Configuración del micrófono
    with mic as source:
        # Tiempo de espera
        recognizer.pause_threshold = 0.8
        # Informar que comenzó a capturar el input de audio
        print("Escuchando...")
        # Ajustar el nivel de ruido ambiental
        recognizer.adjust_for_ambient_noise(source)
        # Guardar lo escuchado en el input
        audio = recognizer.listen(source)

        try:
            # Buscar en Google lo que haya escuchado
            pedido = recognizer.recognize_google(audio, language="es-mx")
            return pedido.lower()
        except sr.UnknownValueError:
            print("No he podido escuchar bien. Repite porfavor")
        except sr.RequestError:
            print("Lo lamento, no pude completar tu pedido :(")
        except Exception as e:
            print(f"Error del sistema: {e}")

def hablar(mensaje,idioma="ESPAÑOL"):
    #Encender pyttsx3
    engine = pyttsx3.init()
    if idioma == 'ESPAÑOL':
        engine.setProperty('voice',VOZ_ESPANIOL)
    else:
        engine.setProperty('voice',ENGLISH_VOICE)

    #Pronunciar mensaje del parametro
    engine.say(mensaje)
    engine.runAndWait()

def pedir_dia():
    dias_semanas = {0:'Lunes',1:'Martes',2:'Miercoles',3:'Jueves',4:'Viernes',5:'Sabado',6:'Domingo'}
    meses = {1:'enero',2:'febrero',3:'marzo',4:'abril',5:'mayo',6:'junio',7:"julio",8:'agosto',9:'septiembre',
             10:'octubre',11:'noviembre',12:'diciembre'}

    dia = datetime.date.today()
    dia_semana = dia.weekday()
    mes = dia.month

    tiempo_actual = datetime.datetime.now().time()
    hora = tiempo_actual.hour
    minutos = tiempo_actual.minute

    return f"Hoy es {dias_semanas.get(dia_semana)} {dia.day} de {meses.get(mes)} de {dia.year}. A las {hora} con {minutos} minutos de la {'tarde' if hora >= 12 else 'mañana'}"

def peticion(pedido):
    if 'abrir youtube' in pedido:
        hablar("Por supuesto. Abriendo Youtube","ESPAÑOL")
        wb.open('https://www.youtube.com')
    elif 'abre navegador' in pedido:
        hablar("Claro!. Estoy en ello")
        wb.open('https://www.google.com')
    elif 'qué día es hoy' in pedido:
        hablar(pedir_dia())
    elif 'busca en wikipedia' in pedido:
        hablar("Claro!. Buscando en wikipedia")
        pedido = pedido.replace('busca en wikipedia','')
        try:
            wk.set_lang('es')
            resultado = wk.summary(pedido,sentences=1)
            hablar(resultado)
        except Exception:
            hablar("Lo lamento. No pude encontrar ninun resultado de los solicitado")
    elif 'busca en internet' in pedido:
        hablar("Por supuesto! Me encuentro investigando")
        pedido = pedido.replace('busca en internet','')
        pywhatkit.search(pedido)
        hablar("Esto fue lo que encontre")
    elif 'reproduce en youtube' in pedido:
        pedido = pedido.replace('reproduce en youtube','')
        try:
            hablar(f"Buena idea. Reproduciendo {pedido}")
            pywhatkit.playonyt(pedido)
        except Exception:
            hablar("Lo lamento, no pude encontrar una reproduccion de lo solicitado")
    elif 'broma' in pedido or 'chiste' in pedido:
        hablar(pyjokes.get_joke('es'))
    elif 'abrir chat gpt' in pedido or 'abre chat gpt' in pedido:
        hablar("Por Supuesto. Abriendo chatgpt")
        wb.open('https://www.chatgpt.com')
    else:
        hablar("Lo lamento. No escuche bien o no pude completar la peticion")

MENSAJE_BIENVENIDA = f"Hola! soy Sabita. Tu asistente virtual!. {pedir_dia()}. en que te puedo ayudar?"

hablar(MENSAJE_BIENVENIDA,"ESPAÑOL")
idioma = str(transform_audio_a_texto()).upper()

while True:
    try:
        pedido = transform_audio_a_texto()
        print(f"Dijiste: {pedido}")
        if 'salir' in pedido or 'adios' in pedido:
            hablar("Hasta Luego!. Si necesitas algo mas solo avisame","ESPAÑOL")
            break
        peticion(pedido)
        continue
    except Exception:
        print("No escuche nada, vuelve a repetir...")