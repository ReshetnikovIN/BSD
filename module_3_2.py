def send_email(message, recipient, sender = "university.help@gmail.ru"):
    if (recipient.find('@') == -1) or not((recipient.find('.ru') != -1) or (recipient.find('.com') != -1)\
            or (recipient.find('.net') != -1)) or not((sender.find('.ru') != -1) or (sender.find('.com') != -1)\
            or (sender.find('.net') != -1)):
#        print(sender.find('.com'), sender.find('.ru'), sender.find('.com') == -1, sender.find('.ru') == -1, (sender.find('.com') == -1) or (sender.find('.ru') == -1))
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    else:
        if (sender == "university.help@gmail.ru"):
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')