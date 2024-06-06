
from googletrans import Translator
from gtts import gTTS
import os

import googletrans
 
 
print(googletrans.LANGUAGES)

# Creating Recogniser() class object

MyText = "hello  My name is India"
get_sentence = 'My name is India'
print(get_sentence)
if 'hello' in MyText:
    
    # Translator method for translation
    translator = Translator()
    
    # short form of english in which
    # you will speak
    from_lang = 'en'
    
    # In which we want to convert, short
    # form of hindi
    to_lang = 'kn'
    print("Phase to be Translated :"+ get_sentence)
            # Using translate() method which require
        # three arguments, 1st the sentence which
        # needs to be translated 2nd source language
        # and 3rd to which we need to translate in
    text_to_translate = translator.translate(get_sentence,
                                                src= from_lang,
                                                dest= to_lang)
        
        # Storing the translated text in text
        # variable
    print(text_to_translate)
    text = text_to_translate.text

        # Using Google-Text-to-Speech ie, gTTS() method
        # to speak the translated text into the
        # destination language which is stored in to_lang.
        # Also, we have given 3rd argument as False because
        # by default it speaks very slowly
    speak = gTTS(text=text, lang=to_lang, slow= False)

        # Using save() method to save the translated
        # speech in capture_voice.mp3
    speak.save("captured_voice.mp3")    
        
        # Using OS module to run the translated voice.
    os.system("start captured_voice.mp3")

    


