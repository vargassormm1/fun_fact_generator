import requests
from pywebio.output import *
from pywebio.session import *


url = "https://uselessfacts.jsph.pl/random.json?language=en"

def get_fun_fact():
    response = requests.get(url).json()
    print(response)
    return response['text']

def fun_fact():
    clear()
    fact = get_fun_fact()
    put_text(fact)
    put_button("click me", onclick=fun_fact, color='success', outline=True)


if __name__ == '__main__':
    fun_fact()

