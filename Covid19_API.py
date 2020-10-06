import requests
import datetime

report_date_yest = datetime.date.today() - datetime.timedelta(1)
day_today = datetime.date.today()


def give_report_date(user_date):
    global report_date
    if user_date == '':
        report_date = report_date_yest
        return print(f'Accessing to data for date: {report_date}')
    else:
        report_date = user_date
        return print(f'Accessing to data for date: {report_date}')


def data_seeker(key_word):
    text_number = ''
    global text_number
    data_seek = text_temp.index(key_word)
    for i in text_temp[data_seek:]:
        if i.isdigit() or i == '-':
            text_number = text_number + i
        elif i == ',':
            break
    return text_number


user_date = input(f"Enter a date to view Covid-19 statistic (YYYY-MM-DD) or press Enter to view yesterday`s data: ")

give_report_date(user_date)

url = "https://covid-19-statistics.p.rapidapi.com/reports/total"
print(f'\nCovid-19 cases Global & Poland - today`s date: {day_today}\n')

querystring = {"date": report_date}

headers = {
    'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com",
    'x-rapidapi-key': "e126757d79msh67924d6a173f6d1p1b04d6jsnf2729f7e3bcd"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.text)
text_temp = response.text

# key_word_global = ["confirmed", "confirmed_diff", "deaths", "deaths_diff", "active", "active_diff"]

print('--- Global ---')
data_seeker("date")
print(f'Data reporting date: {text_number}')

data_seeker("last_update")
print(f'Data last update date: {text_number[:10]}')

data_seeker("confirmed")
print(f'Cases total : {(int(text_number)):,}')

data_seeker("confirmed_diff")
print(f'Cases daily change : {(int(text_number)):,}')

data_seeker("deaths")
print(f'Deaths total : {(int(text_number)):,}')

data_seeker("deaths_diff")
print(f'Deaths daily change : {(int(text_number)):,}')

data_seeker("active")
print(f'Active cases total : {(int(text_number)):,}')

data_seeker("active_diff")
print(f'Active daily change : {(int(text_number)):,}')


url = "https://covid-19-statistics.p.rapidapi.com/reports"

querystring = {"date": report_date, "q": "poland"}

headers = {
    'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com",
    'x-rapidapi-key': "e126757d79msh67924d6a173f6d1p1b04d6jsnf2729f7e3bcd"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
text_temp = response.text
# print(response.text)

print('\n--- Poland ---')

data_seeker("date")
print(f'Data reporting date: {text_number}')

data_seeker("last_update")
print(f'Data last update date: {text_number[:10]}')

data_seeker("confirmed")
print(f'Cases total : {(int(text_number)):,}')

data_seeker("confirmed_diff")
print(f'Cases daily change : {(int(text_number)):,}')

data_seeker("deaths")
print(f'Deaths total : {(int(text_number)):,}')

data_seeker("deaths_diff")
print(f'Deaths daily change : {(int(text_number)):,}')

data_seeker("active")
print(f'Active cases total : {(int(text_number)):,}')

data_seeker("active_diff")
print(f'Active daily change : {(int(text_number)):,}')
