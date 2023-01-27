import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import webbrowser
import datetime
import wikipedia
import pyjokes

#ESTO VA A ESCUCHAR NUESTRO MICROFONO Y DEVOLVER EL AUDIO COMO TEXTO
def transformar_audio_en_texto():
    
    #almacenar recognizer en variable
    r = sr.Recognizer()
    
    #configurar el microfono
    with sr.Microphone() as origen:
    
    #tiempo de espera
        r.pause_threshold = 0.8 
        
    #informar que comenzo la grabacion
        print("Ya puedes hablar")
    
    #guardar lo que escuche como audio
        audio = r.listen(origen)
    
        try:
        #buscar en google
            pedido = r.recognize_google(audio,language="es-AR")
        
        #prueba de que pudo ingresar
            print("Dijiste: " + pedido)
        #devolver pedido
            return pedido
    
    #en caso que no comprenda el audio
        except sr.UnknownValueError:
        #prueba de que no comprendio el audio
            print("Ups, no entendi lo que has dicho")
            #Devolver error 
            return "sigo esperando"
        
        except sr.RequestError:
            #prueba de que no comprendio el audio
            print("Ups, no hay servicio")
            #Devolver error 
            return "sigo esperando"
        
        #error inesperado
        except:
            print("Algo a salido mal")
            return "sigo esperando"

# OPCIONES DE VOZ
id1= "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
id2= "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        
# FUNCION PARA QUE EL ASISTENTE PUEDA SER ESCUCHADO 
def hablar(mensaje):
    
    #ENCENDER EL MOTOR DE PYTTSX3
    motor = pyttsx3.init()
    motor.setProperty("voice", id1)
    #PRONUNCIAR MENSAJE
    motor.say(mensaje)
    motor.runAndWait()

#INFORMAR EL DIA DE LA SEMANA
def pedir_dia():
    #crear variable con dato de hoy
    dia = datetime.date.today()
    print(dia)
    
    #crear variable para el dia de semana
    dia_semana = dia.weekday()
    print(dia_semana)
    
    #diccionario con nombres de dias
    calendario = {0: "Lunes",
                  1: "Martes",
                  2: "Miércoles",
                  3: "Jueves",
                  4: "Viernes",
                  5: "Sábado",
                  6: "Domingo"}
    
    # decir el dia de la semana
    hablar(f"hoy es {calendario[dia_semana]}")
    
# INFORMAR QUE HORA ES
def pedir_hora():
    #variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f"En este momento son las {hora.hour} horas con {hora.minute} y {hora.second} segundos"
    print(hora)
    
    #decir la hora
    hablar(hora)
    
# FUNCION PARA SALUDO INICIAL
def saludo_inicial():
    hora=datetime.datetime.now()
    if hora.hour < 6 or hora.hour >= 20:
        momento="Buenas noches"
    elif hora.hour >= 6 and hora.hour < 13:
        momento= "Buenos días"
    else:
        momento = "Buenas noches"
    
    hablar(f"{momento}, soy Helena tu asistente personal. Por favor, dime en que puedo ayudarte")
    
# FUNCION CENTRAL DEL ASISTENTE
def pedir_cosas():
    #ACTIVAR EL SALUDO INICIAL
    saludo_inicial()
    
    #variable de corte
    comenzar = True
    
    #LOOP CENTRAL
    while comenzar:
        
        #ACTIVAR EL MICRO Y GUARDAR EL PEDIDO EN UN STRING
        pedido = transformar_audio_en_texto().lower()
        hora = datetime.datetime.now()
            
        if "abrir youtube" in pedido:
            hablar("Con gusto, estoy abriendo youtube")
            webbrowser.open("https://www.youtube.com/")
            continue
        elif "abrir navegador" in pedido:
            hablar("Claro, estoy en eso")
            webbrowser.open("https://www.google.com")
            continue
        elif "qué día es hoy" in pedido:
            pedir_dia()
            continue
        elif "qué hora es" in pedido:
            pedir_hora()
            continue
        elif "te gusta gran hermano" in pedido:
            hablar("Me encanta gran hermano y espero que este fin de semana se vaya Ariel")
            continue
        elif "busca en wikipedia" in pedido:
            hablar("Claro, ya mismo lo estoy buscando")
            pedido = pedido.replace("busca en wikipedia","")
            wikipedia.set_lang("es")
            resultado= wikipedia.summary(pedido, sentences=1)
            hablar("Wikipedia dice lo siguiente:")
            hablar(resultado)
            continue
        elif "busca en internet" in pedido:
            hablar("Ya mismo me pongo a buscarlo")
            pedido= pedido.replace("busca en internet","")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
        elif "contame un chiste" in pedido:
            hablar(pyjokes.get_joke("es"))
            hablar("qué te ha parecido? estuvo bueno o malísimo?")      
        elif "malísimo" in pedido:
            hablar("Lo lamento, todavia no comprendo del todo el sentido del humor de los humanos")
            continue
        elif "reproducir" in pedido:
            hablar("buena idea, ya comienzo a reproducirlo")
            pywhatkit.playonyt(pedido)
            continue
        elif "adiós" in pedido:
            hablar("Gracias por confiarme tus consultas, cualquier otra cosa, me avisas")
            break
pedir_cosas()