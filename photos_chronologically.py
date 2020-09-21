
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
