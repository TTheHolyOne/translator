from google_trans_new import google_translator
import sys
import time
'''
Translator made with google_trans_new and google_translator modules
github.com/ttheholyone
ttheholyone.com
TTheHolyOne#1642
'''

print('Holy Translator\n')
input('Press any key to proceed...\n\n')
def googletranslator():
	# Options
	options = int(input('1: Translate\n2: See all LANGUAGES you can translate.\n(Important because you need to know the names to be able to translate..)\n3: Quit\n'))
	translator = google_translator()
	# Select the options
	if options == 1:
		langtgt = input('\n\nWhat language do you want it to translate the text to? \n')
		orgin = input('\n\nWhat is the text you want to translate? \n')
		#translate code
		result = translator.translate(orgin, lang_tgt=langtgt)
		detector = google_translator()
		detect_results = detector.detect(orgin)
		print('\n\nTranslating....\n')
		time.sleep(1)
		#translate output
		print(f'The language you you just translated was: {detect_results}\nAnd translated into {langtgt} is: \n{result}\n')
	elif options == 2:
		language = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'}
		print(language)
	elif options == 3:
		sys.exit()
	else:
		print('\nI\'m not sure what you mean')

googletranslator()

goodbye = input('\n\nWould you like to Quit? (Y/N)')
if goodbye.lower() == 'y':
	sys.quit()
elif goodbye.lower() == 'n':
	googletranslator()
else: 
	print('I\'m not sure what you mean...')

