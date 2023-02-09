class Translate:

    def process_one(self,text):
        if text.lower() == 'да' or text.lower() == 'мужской':
            return 1
        else: return 0

    def process_two(self,predict):
        if predict==['Negative']:
            return 'Поздравляю! Ваши симптомы не совпадают с симптомами диабета. Но, тем не менее не забывайте беречь свое здоровье)'
        else: return 'Ой.. Признаки совпадают.. Но вы не переживайте, все будет хорошо. Главное - это вовремя обратиться к врачу, чего я и Вам советую.'