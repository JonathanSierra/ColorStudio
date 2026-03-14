import smtplib
from email.message import EmailMessage
import datetime
import os
# --- 1. CONFIGURACIÓN DEL CORREO ---
correo_envia = "jonathansie42@gmail.com"  # PON AQUÍ TU CORREO DE GMAIL NORMAL
password_app = "mwxoqznghwmpcrjm" # PEGA AQUÍ LAS 16 LETRAS QUE TE DIO GOOGLE
correo_recibe = "jonathansie42@gmail.com" # A DÓNDE QUIERES QUE LLEGUE EL BACKUP
base_de_datos = "color_studio.db" # El archivo que vamos a enviar
# Obtenemos la fecha de hoy para el asunto del correo
fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Iniciando copia de seguridad del {fecha_hoy}...")
# --- 2. PREPARAR EL "SOBRE" (El mensaje) ---
mensaje = EmailMessage()
mensaje['From'] = correo_envia
mensaje['To'] = correo_recibe
mensaje['Subject'] = f"Backup Color Studio - {fecha_hoy}"
mensaje.set_content(
    f"Hola,\n\nAdjunto encontrarás la copia de seguridad automática de la base de datos de Color Studio generada el {fecha_hoy}.\n\nSaludos,\nTu sistema Automático."
)
# --- 3. METER EL ARCHIVO EN EL SOBRE (El adjunto) ---
try:
    with open(base_de_datos, 'rb') as archivo_bd:
        datos_archivo = archivo_bd.read()
        nombre_archivo = os.path.basename(archivo_bd.name)
        
    mensaje.add_attachment(datos_archivo, maintype='application', subtype='octet-stream', filename=nombre_archivo)
    print("Archivo adjuntado correctamente.")
    
except FileNotFoundError:
    print(f"ERROR: No se encontró el archivo '{base_de_datos}'. Asegúrate de que estés ejecutando el script en la misma carpeta.")
    exit() # Detenemos el script si no hay archivo
# --- 4. IR A LA OFICINA DE CORREOS (Enviar por SMTP) ---
try:
    print("Conectando con Gmail...")
    # Nos conectamos al servidor de Gmail de forma segura (SSL en el puerto 465)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
        servidor.login(correo_envia, password_app)
        servidor.send_message(mensaje)
        
    print("¡Copia de seguridad enviada con éxito por correo electrónico!")
except Exception as e:
    print(f"Ocurrió un error al intentar enviar el correo: {e}")