
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')

www_list = ['https://www.techmaniak.pl/', 'https://spidersweb.pl/', 'https://www.geekweek.pl/']
key_words = ['iphone', 'Iphone','iPhone', 'Apple', 'Microsoft', 'Xbox', 'PS5']

driver.get(www_list[0])

header_list = driver.find_elements_by_class_name("anal-list-title")

print(f"\nAnalysing: {www_list[0]}\n")
for i in header_list:
  for x in key_words:
    if x in i.text:
      print(" * ",i.text,"->",www_list[0] )

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