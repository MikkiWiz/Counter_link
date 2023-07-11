# Сокращение ссылок с помощью Битли

[TODO: При отправке ссылки, программа возвращает короткую ссылку. Если отправлять короткую ссылку, то программа возвращает количество переходов по Битлинку]

### Как установить 

Python3 должен быть уже установлен
Затем используйте 'pip' для установки зависимостей:

```
$ pip install -r requirements.txt
```

Рекомендуется использовать [virtual/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

### Переменные окружения

Создайте файл с расширением ".env" в том же каталоге, где находится ваша программа.

Откройте файл ".env" и добавьте следующую переменную окружения:

```
BITLY_SECRET_KEY=<ваш_токен_Bitly>
```
Здесь <ваш_токен_Bitly> должен быть заменен на ваш собственный токен Bitly. Токен Bitly можно получить, зарегистрировавшись на сайте Bitly и создав OAuth-токен в настройках вашей учетной записи.

Пример заполнения файла ".env":

```
BITLY_SECRET_KEY=abcdefgh12345678
```
Сохраните файл ".env".

Теперь ваше окружение настроено для работы с программой. При запуске программы она будет использовать значение токена Bitly из переменной окружения "BITLY_SECRET_KEY" для выполнения запросов к API Bitly.

### Пример запуска скрипта
Для сокращения ссылки:
```
$ python main.py https://vk.com/
```
Для подсчета переходов:
```
$ python main.py https://bit.ly/3JCRlA7
```

### Цель проекта

Код написан в образователльных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
