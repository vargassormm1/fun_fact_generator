import requests
from pywebio.output import *
from pywebio.session import *

url = "https://catfact.ninja/fact"

def fun_fact():
    clear()
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        fact = data['fact']
    except requests.exceptions.RequestException as e:
        fact = "An error occurred while fetching the cat fact."
        print(f"RequestException: {e}")
    except ValueError as e:
        fact = "Error parsing the response."
        print(f"ValueError: {e}")
    except KeyError as e:
        fact = "Unexpected response format received."
        print(f"KeyError: {e}")

    put_text(fact)
    put_button("click me", onclick=fun_fact, color='success', outline=True)

if __name__ == '__main__':
    fun_fact()

