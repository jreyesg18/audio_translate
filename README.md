# Audio Translate

Este proyecto permite traducir texto desde inglés a otros idiomas y reproducir la traducción en voz utilizando Python. Utiliza la API de Google Translate para la traducción y la biblioteca gTTS para la conversión de texto a voz.

## Requisitos

- Python 3.6 o superior
- pip (para instalar las dependencias)

## Instalación

1. **Clona el repositorio**:
   
bash
   git clone https://github.com/tu-usuario/audio-translate.git
   cd audio-translate

2. **Crea un entorno virtual y actívalo:**
bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
3. **Instala las dependencias:**
   
bash
   pip install deep-translator gtts

## Uso

1. Ejecuta el script main.py:
   '''bash
   python main.py
   
2. Sigue las instrucciones en la consola:
- Introduce el texto en inglés que deseas traducir.
- Indica el idioma al que deseas traducir el texto. (Por ejemplo, es para español, fr para francés, etc.)
El script traducirá el texto y reproducirá la traducción en voz.

## Notas

La reproducción del audio usa afplay en macOS. Asegúrate de que afplay esté disponible en tu sistema.
Si estás en un sistema diferente, como Linux o Windows, puedes necesitar ajustar el comando para reproducir el archivo MP3 (por ejemplo, usar mpg321 en Linux o el reproductor de audio predeterminado en Windows).
Ejemplo
    '''Introduce el texto en inglés que deseas traducir:
    hello
    ¿A qué idioma quieres traducirlo? (es para español, en para inglés, fr para francés, etc.)
    es
    Texto traducido: hola
