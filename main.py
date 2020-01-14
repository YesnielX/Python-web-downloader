import requests, time
from os import system, sys
from requests.exceptions import HTTPError

def __Home__():
  system('clear')
  system('cls')

  print('''
======================================
==============         ===============
=========                     ========
          Web Site Download
                 by @jojosamass

===========               ============
======================================
''')
  time.sleep(3)

  print('example: https://httpbin.org/ip')
  url = input('URL: ')
  print('')

  print('Waiting Connection . . .')
  print('')

  time.sleep(5)

  for url in [url]:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
        print('')

  downloaded = response.text

  nameFile = input('what name of the file to save: ')
  print('')#space

  print('file saved successfully ')
  print('')#space


  with open(nameFile, 'w') as nameFile:
    nameFile.write(downloaded)

  backhome = input('do you want to return to the start menu? [y/n]')
  print('')#space

  if backhome == 'y':
    __Home__()
  else:
    sys.exit()

__Home__()