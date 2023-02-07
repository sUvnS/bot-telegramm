class Translate:

    def process_one(self,text):
        if text == 'ДА' or text == 'Мужской':
            return 1
        else: return 0

    def process_two(self,predict):
        if predict=='Negative':
            return 'какой-то текст'
        else: return 'другой текст'