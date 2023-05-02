class Translate:

    def process_one(self,text):
        if text.lower() == 'да' or text.lower() == 'мужской':
            return 1
        else: return 0

    def process_two(self,predict):
        if predict==['Negative']:
            return 'Поздравляю! Ваши симптомы не совпадают с симптомами диабета. Но, тем не менее не забывайте беречь свое здоровье)'
        else: return 'Ой.. Признаки совпадают.. Советую Вам обратиться к врачу-специалисту. Но вы не переживайте, всё будет хорошо!'

    def process_three(self,text):
        if text.lower() == 'да':
            return 1
        if text.lower() == 'нет':
            return 2
        else: return 3

    def process_four(self,predict_c):
        if predict_c==0:
            return 'Поздравляю! Ваши симптомы не совпадают с симптомами covid-19. Но, тем не менее не забывайте беречь свое здоровье)'
        else:
            return 'Ой.. Признаки совпадают.. Советую Вам обратиться к врачу-специалисту. Но вы не переживайте, всё будет хорошо!'