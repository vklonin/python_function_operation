# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__

def open_browser(browser_name):
    pass
    print_function_description(open_browser, locals())


def go_to_companyname_homepage(page_url):
    pass
    print_function_description(go_to_companyname_homepage, locals())


def find_registration_button_on_login_page(page_url, button_text):
    pass
    print_function_description(find_registration_button_on_login_page, locals())

def print_function_description(func, locals):
    list_of_words = func.__name__.replace("_", " ").split(" ")
    list_of_words[0] = "Function: " + list_of_words[0].capitalize()
    list_of_words[len(list_of_words)-1] = list_of_words[len(list_of_words)-1] + ". with follwing args: " +', '.join(list(locals.values()))
    print(' '.join(list_of_words))



find_registration_button_on_login_page("www.google.com", "Submit")
go_to_companyname_homepage("www.cia.us")
open_browser("chromium")
