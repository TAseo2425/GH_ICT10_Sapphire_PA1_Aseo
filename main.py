
from pyscript import display, document


def temp_update(t):
    document.getElementById('output').innerHTML = ' '
    fahrenheit = float(document.getElementById('temperature').value)

    celsius = round((fahrenheit - 32) * (5/9), 2)

    if celsius >= 37.8:
        display(f'Your temperature is {celsius}°C; you have a fever.', target='output')
    else:
        display(f'Your temperature is {celsius}°C; you do not have a fever.', target='output')