import random

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
           'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
           'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
           'Перспективы не очень хорошие', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как тебя зовут?\n')
print(f"Привет, {name}, что ты хочешь узнать?")
while True:
    input('Введите вопрос: ')
    print(random.choice(answers))
    if input('Хочешь узнать ещё что-нибудь? (д = да, н = нет)\n') == 'н':
        print('Возвращайся если возникнут вопросы!')
        break
    else:
        continue