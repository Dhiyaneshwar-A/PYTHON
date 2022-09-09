import pywhatkit as pw
txt="""Hi this is text to handwriting convertor
Welcome"""
pw.text_to_handwriting(txt,"hwsample.png",rgb=[0,0,250])
print(" END ")