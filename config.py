# Токен бота, string
token = "7384956038:AAEDPmcF3GiGNAhvz4Ajp7XEyp8f1zjE-GI"
# id админа в integer
admin = 300404908

# Настройка работы через проксю
REQUEST_KWARGS={
    'proxy_url': 'socks5://localhost:9050',
}

# Префиксы, нужны если человек перешел по ссылке вида t.me/bot?start=libgen, чтобы сразу перекинуть юзера на нужную менюшку
prefix_start_in_lg = "/start libgen"
prefix_start_in_ch = "/start channel"
prefix_offer_book = "/start offer_book"

# что это?
offer_book_command = "offer_book"

# Стартовое сообщение, выдается после простого /start без указаний меню
start_message = '''
Ой, привет тебе :)

Я - бот канала @bzd_channel

<b>Умею:</b>
1) Искать книги по программированию на канале
2) Искать совершенно любые книги на Library Genesis
3) Исполняю роль предложки для книг
'''

# Кнопки меню, нужны для самих названий и в коллбеках менюшек
back_button = "🔙 Назад"
search_in_ch_button = "🔍 Поиск по каналу 🔎"
search_in_lg_button = "🔍 Поиск по LibGen 🔎"
offer_book_button = "🤝 Предложить книгу 🤝"
help_in_fts3_button = "❓ Как делать сложные запросы ❓"
get_all_statistics_button = "Статистика бота"
add_post_button = "Добавить книгу"
delete_post_button = "Удалить книгу"

# Юзерское главное меню
start_reply_markup = [[search_in_ch_button, search_in_lg_button],[offer_book_button],[get_all_statistics_button]]

# Админское главное меню
start_admin_reply_markup = \
    [
        [search_in_ch_button, search_in_lg_button],
        [offer_book_button],
        [add_post_button, delete_post_button],
        [get_all_statistics_button]
    ]

add_book_message = "Начинай пересылать файлы, фото, видео и текст с каналов которые нужно добавить в базу"
delete_post_message = "Начинай пересылать файлы, фото, видео и текст которые нужно удалить из базы, либо отправь id канала и номер поста в формате channel_id/post_id.\n\nОСТОРОЖНО, будет удалено сразу, без вопросов, не косяч"

# Кнопки меню в поиске по LG
into_lg_search_reply_markup = [[help_in_fts3_button],[back_button]]

# Стартовое сообщение предложки
start_in_offer_book_msg = """У тебя есть книга которой нет на канале и ты хочешь ей поделиться? Кидай :) Всё анонимно! Спасибо :)

Поддерживаемые типы файлов:
<code>    .zip
    .pdf
    .epub</code>
    
<a href='https://t.me/joinchat/AAAAAFBfTfCQVbxixZ1_HQ'>ССЫЛКА НА ПРЕДЛОЖКУ</a>"""

# Допустимые расширения для файлов предложки
offer_book_extension = [".pdf", ".zip", ".epub"]
# Допустимые mime типы для предложки
offer_book_mime_type = ["application/zip", "application/pdf", "application/epub+zip", "application/epub"]
# ID предложки куда бот складывает файлы
offer_book_channel_chat_id = -1001348423152

# Сообщение при поиске на канале
start_in_channel_msg = '''Какая книга тебе нужна? Напиши :-)

Если ты пишешь слово не полностью - не забывай использовать *, например запрос <b>'тестирова*'</b> будет находить и <b>'тестирование'</b> и <b>'тестированию'</b>

Если хочешь искать еще лучше - <b>кнопка помощи снизу :-)</b>
'''

# Сообщение при поиске по LG
start_in_libgen_msg = '''Что требуется поискать на Libgen? Напиши :-)

Если ты пишешь слово не полностью - не забывай использовать *, например запрос <b>'тестирова*'</b> будет находить и <b>'тестирование'</b> и <b>'тестированию'</b>

Если хочешь искать еще лучше - <b>кнопка помощи снизу :-)</b>
'''

# Текст после кнопки помощи в поиске по lg
help_in_fts3 = '''<b>Как делать сложные запросы</b>

1) <b>Используй символ подстановки "звездочка" (*)</b>
Например запрос <b>тестирова*</b> будет находить и <b>'тестирование'</b> и <b>'тестированию'</b>

2) <b>Используй поиск по определенным колонкам с помощью двоеточия (:)</b>
Например:
-  <code>НазваниеКолонки:Запрос</code>
-  <code>НазваниеКолонки:Запрос ОбщийЗапросПоВсемКолонкам</code>
-  <code>language:russian year:2017 Database*</code> - найдет все книги про базы данных на русском языке 2017 года 

Список колонок (кликабельно):
  <code>title</code>
  <code>tags</code>
  <code>language</code>
  <code>volumeinfo</code>
  <code>edition</code>
  <code>series</code>
  <code>author</code>
  <code>year</code>
  <code>identifier</code> - ISBN с тире
  <code>identifierwodash</code> - ISBN <b>без</b> тире
  <code>publisher</code>
  <code>pages</code>
  <code>issn</code>
  <code>asin</code>
  <code>filesize</code>
  <code>extension</code>
  <code>md5</code>

3) <b>Заключай запросы в двойные кавычки, это позволит найти несколько слов идущих строго подряд</b>
Например:
-  <code>"python разработка"</code>

4) <b>Используй оператор NEAR если нужно искать слова идущие не подряд, а где-то поблизости.</b>
Простой NEAR ищет на ближайшие 10 слов, указать дальность второго слова можно вот так NEAR/5 (в данном случае - искать в ближайших 5-ти словах)
Например:
-  <code>database NEAR/5 python</code>
'''

# Кнопка помощи, #TODO отрефакторить название, fts4 юзаем ведь
help_fts3_in_channel = '''<b>Как делать сложные запросы</b>
1) <b>Используй символ подстановки "звездочка" (*)</b>
Например запрос <b>тестирова*</b> будет находить и <b>'тестирование'</b> и <b>'тестированию'</b>

2) <b>Заключай запросы в двойные кавычки, это позволит найти несколько слов идущих строго подряд</b>
Например:
-  <code>"python разработка"</code>

4) <b>Используй оператор NEAR если нужно искать слова идущие не подряд, а где-то поблизости.</b>
Простой NEAR ищет на ближайшие 10 слов, указать дальность второго слова можно вот так NEAR/5 (в данном случае - искать в ближайших 5-ти словах)
Например:
-  <code>Тестир* NEAR/5 обесп*</code>
'''
# Текст главного меню
main_menu_msg = "Ты в главном меню. Что будем делать?"

# Шаблон по которому собирается статистика, смотри папку Statistics
statistics_template = "<code>Дата:     {date}\nДействие: {action}\nЗапросов: {action_count}\nЛюдей:    {user_count}</code>"

# Лимит отправки книг
send_books_limit = 3
# Лимит отправки книг в LG
send_libgen_limit = 3
# Пусть до базы канала
path_to_db = "data.sql"
# Путь до базы LG
path_to_lgdb = "lg_db_2.sql"
# Путь до базы статистики
path_to_statistics = "statistics.sql"



