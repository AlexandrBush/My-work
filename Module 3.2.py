# Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".

def send_email(message: str, recipient: str, sender: str = "university.help@gmail.com"):
    # Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".

    if "@" not in recipient or not recipient.endswith(".com") and not recipient.endswith(
            ".ru") and not recipient.endswith(".net") or "@" not in sender or not sender.endswith(
            ".com") and not sender.endswith(".ru") and not sender.endswith(".net"):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    # Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"

    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")

    # Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."

    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

    # В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."

    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


# Вызовите функцию send_email, передав в неё аргументы.

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')