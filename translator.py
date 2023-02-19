import gradio as gr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound 
import speech_recognition as sr
import os
import remove

# css_code='div {background-image:url("https://inc42.com/wp-content/uploads/2016/01/india.jpg");repeat 0 0;};}'


translated=""
dest_lang=""

def translate(inp_text,lang):
    global translated
    global dest_lang
    #model
    translator = Translator()
    language={"english":"en",
      "tamil":"ta",
      "telugu":"te",
      "malayalam":"ml",
      "hindi":"hi",
      "kannada":"kn",
      "bengali":"bn",
      "assamese":"as",
      "gujarati":"gu",
      "kashmiri":"ks",
      "marathi":"mr",
      "nepali":"ne",
      "oriya":"or",
      "punjabi":"pa",
      "sanskrit":"sa",
      "urdu":"ur"}
    src_lang=translator.detect(inp_text).lang
    dest_lang=language[lang.lower()]
    translated = str((translator.translate(inp_text,src=src_lang,dest=dest_lang)).text)
    return translated

def audio_translate(inp_audio,src_lang,dest_lang):
   r = sr.Recognizer()
   file_audio=sr.WavFile(inp_audio)
   with file_audio as source:
    audio_text = r.record(source)
    extracted_text=r.recognize_google(audio_text,language=src_lang)
    #model
    translator = Translator()
    language={"english":"en",
      "tamil":"ta",
      "telugu":"te",
      "malayalam":"ml",
      "hindi":"hi",
      "kannada":"kn",
      "bengali":"bn",
      "assamese":"as",
      "gujarati":"gu",
      "kashmiri":"ks",
      "marathi":"mr",
      "nepali":"ne",
      "oriya":"or",
      "punjabi":"pa",
      "sanskrit":"sa",
      "urdu":"ur"}
    dest_lang=language[dest_lang.lower()]
    translated = str((translator.translate(extracted_text,src=src_lang,dest=dest_lang)).text)
    return translated

def translate_voice():
   # remove.func()
   tts = gTTS(text=translated, lang=dest_lang)
   tts.save('audio.mp3')
   playsound('audio.mp3')
   remove.func()
   


with gr.Blocks(title="Translator") as app:
   gr.Markdown("Regional Language Translator")
   with gr.Row().style(equal_height=True):
      with gr.Column():
         
         #text input
         inp_text=gr.Textbox(placeholder="Enter your sentence here...",lines=5,interactive=True)
         inp_lang=gr.Dropdown(["English","Tamil","Telugu","Malayalam","Kannada","Bengali","Hindi","Assamese","Nepali","Oriya","Punjabi","Sanskrit","Urdu","Gujarati","Kashmiri","Marathi"],value="English",show_label=True)
         
         translate_btn=gr.Button(value="Translate").style(full_width=False)

         translated_txt=gr.Textbox(label="Translated Text",placeholder="Translated Version",lines=5)
         hear_btn=gr.Button(value="Hear Me")
         
         
      with gr.Column(scale=1, min_width=600):
         #audio input

         src_lang=gr.Dropdown(["English","Tamil","Telugu","Malayalam","Kannada","Bengali","Hindi","Assamese","Nepali","Oriya","Punjabi","Sankasrit","Urdu","Gujarati","Kashmiri","Marathi"])
         inp_audio=gr.Audio(source="microphone")
         dest_lang=gr.Dropdown(["English","Tamil","Telugu","Malayalam","Kannada","Bengali","Hindi","Assamese","Nepali","Oriya","Punjabi","Sanskrit","Urdu","Gujarati","Kashmiri","Marathi"])
         audio_tran_btn=gr.Button(value="Translate Audio")

         
    
   translate_btn.click(translate,[inp_text,inp_lang],outputs=translated_txt,api_name="Regional Language Translator")
   audio_tran_btn.click(audio_translate,[inp_audio,src_lang,dest_lang])
   hear_btn.click(translate_voice,outputs=translated_txt)

app.launch(share=True)    