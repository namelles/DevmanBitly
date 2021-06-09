# Обрезка ссылок с помошью Битли

[TODO: Получение коротких ссылок с помощью API сервиса Битли. Получение количества переходов по ссылкам ]

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить

Токен необходимый для аутентификации/авторизации в API Billy должен быть  размещен в переменной окружения BITLY_TOKEN. 
Передача аргумента в командной строке. Пример:
```
python main.py -url https://google.com
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).