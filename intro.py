import googletrans

translator = googletrans.Translator()

#print(googletrans.LANGUAGES)

message = translator.translate('Love you',dest='hi')

print(message.text)