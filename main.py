from deep_translator import GoogleTranslator
from gtts import gTTS
import os


def translate_text(text, dest_lang='es'):
    try:
        translator = GoogleTranslator(target=dest_lang)
        translation = translator.translate(text)
        return translation
    except Exception as e:
        return f"Error en la traducción: {e}"


def speak_text(text, lang='es'):
    try:
        tts = gTTS(text, lang=lang)
        audio_file = "translated.mp3"
        tts.save(audio_file)
        os.system(f"afplay {audio_file}")  # Usa afplay en lugar de mpg321
    except Exception as e:
        print(f"Error al reproducir el texto: {e}")


def main():
    print("Introduce el texto en inglés que deseas traducir:")
    text = input()
    print("¿A qué idioma quieres traducirlo? (es para español, en para inglés, fr para francés, etc.)")
    dest_lang = input()

    # Validación simple del idioma
    if dest_lang not in ['es', 'en', 'fr', 'de', 'it']:
        print("Idioma no soportado.")
        return

    # Llamada a la función de traducción
    translated_text = translate_text(text, dest_lang)
    print(f"Texto traducido: {translated_text}")

    # Reproducción de la traducción en voz
    speak_text(translated_text, lang=dest_lang)


if __name__ == "__main__":
    main()
