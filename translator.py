from translate import Translator

translator = Translator('es')

text = input('Enter text to translate to Spanish: ')

translation = translator.translate(text)

print('\n' + translation)
