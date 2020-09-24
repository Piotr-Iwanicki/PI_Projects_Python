##Welcome to GitHub PI_Projects_Python Page

###My projects in Python 3

**Currently there are 3 files in Python available:**

1. ***photos_chronologically.py*** : The script allows you to sort photos according to the time and date the file was created and rename them to a unified one. This can be helpful when you want to display photos collected from various devices on a smartTV using a USB flash drive.

```python
import os
import datetime
import collections
from shutil import copy2
from shutil import rmtree
import time

f_name = "wakacje_2020_"                # tak będą nazywać się pliki ze zdjęciami po sortowaniu
directory = r"D:\Foto_wakacje_2020"
dest_dir = r"D:\Foto_wakacje_2020\Sorted"

print("\nInformacje wstępne:\n")
print(f"* Obecnie ustawiona nazwa dla plików posortowanych to '{f_name}+kolejny nr'.")
print(f"* Obecnie wybrany katalog ze zdjęciami to: '{directory}'.")
print(f"* Obecnie wskazany katalog ze zdjęciami posortowanymi chronologicznie to: '{dest_dir}'.")
print("\n")
print(f"* UWAGA ! Program zmieni nazwy zdjęć na nowe oraz skopiuje pliki z katalogu '{directory}' do '{dest_dir}'"
      f"/ jednocześnie układając je chronologicznie.")


user_choice = input("Wciśnij [Enter] by rozpocząć lub [q] by przerwać działanie skryptu: ")
if user_choice == 'q':
    exit()

if os.path.isdir(dest_dir):
    print("\nKatalog docelowy - 'Sorted' już istnieje i będzie nadpisany!")
    rmtree(dest_dir)

files = os.listdir(directory)
files_dict = {}

y = 0
list_f_names = []
list_dt_marker = []

for i in files:
    file_path = directory + "\\" + i
    list_f_names.append(i)
    time_extracted = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    list_dt_marker.append(time_extracted)
    y += 1

dict_files = {}

for i in range(len(list_f_names)):
    dict_files.setdefault(list_f_names[i], list_dt_marker[i])

print(f"\nilość plików - {y}\n")
time.sleep(4)

list_files_sort = sorted(dict_files.items(), key=lambda x: x[1])
dict_files_sort = collections.OrderedDict(list_files_sort)

'''
for i in dict_files_sort:           #wypisuje posortowane chronologicznie nazwy plików
    print(i, dict_files_sort[i])
'''
licznik = 1000

os.mkdir(dest_dir)

for i in dict_files_sort:
    file_path_src = directory + "\\" + i
    copy2(file_path_src, dest_dir + "\\" + f_name + str(licznik) + i[(len(i) - 4):])
    print(copy2(file_path_src, dest_dir + "\\" + f_name + str(licznik) + i[(len(i) - 4):]))
    licznik += 1
else:
    print("\nZakończono sortowanie i zmianę nazw wg kolejności.")
    print(f"Posortowane zdjęcia znajdują się w katalogu '{dest_dir}'.\n")

```

2. ***header_reader.py*** : The script uses Selenium Webdriver and reads headers from selected websites, it can also search for them by keywords. The script is still being expanded with new functionalities.

```python
# Under constriction !!!

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')

www_list = ['https://www.techmaniak.pl/', 'https://spidersweb.pl/', 'https://www.geekweek.pl/']
key_words = ['iphone', 'Iphone', 'iPhone', 'Apple', 'Microsoft', 'Xbox', 'PS5']

driver.get(www_list[0])

header_list = driver.find_elements_by_class_name("anal-list-title")

print(f"\nAnalysing: {www_list[0]}\n")
for i in header_list:
  for x in key_words:
    if x in i.text:
      print(" * ", i.text, "->", www_list[0])

driver.get(www_list[1])

header_list = driver.find_elements_by_class_name("post-title")

print(f"\nAnalysing: {www_list[1]}\n")

for i in header_list:
  for x in key_words:
    if x in i.text:
      print(" * ", i.text, "->", www_list[1])

driver.get(www_list[2])

driver.find_element_by_class_name("rodo__button").click()
header_list = driver.find_elements_by_class_name("news__title")

print(f"\nAnalysing: {www_list[2]}\n")

for i in header_list:
  for x in key_words:
    if x in i.text:
      print(" * ", i.text, "->", www_list[2])

driver.close()
```

3. ***factorial_3_ways.py*** : The script computes the factorial value for a given number in 3 ways: using the 'math' module, computing iteratively and computing recursively.
```python
import math

number = (input("Enter a number to calculate the factorial: "))

if not number.isdigit():
    print("Sorry, number must be an integer !")
    print(f"Input is digit? - {number.isdigit()}")
    exit()

number = int(number)
print("")

control_result = math.factorial(number)
print(f'*Control result, factorial of {number} = {control_result}')
print("")
print("*By iteration")

def GiveFactorial(number):
    if number == 1 or number == 0:
        return print(f'Factorial of {number} = {1}')
    else:
        fact = number
        for i in range(fact - 1):
            fact = fact * (i + 1)
        return print(f'Factorial of {number} = {fact}')

GiveFactorial(number)
print("")
print("*By recursion")

def giverecursfactorial(x):
    if x == 1 or x ==0 :
        return 1
    else:
        return x * giverecursfactorial(x - 1)

print(f'Factorial of {number} = ', giverecursfactorial(number))
```

