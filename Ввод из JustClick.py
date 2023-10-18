from datetime import datetime, date, time
import secrets

to_Excel = ['имя','отчество','фамилия','city','telefon','.','email','date']

# функция для формирования правильного номера телефона +71234567890 из строки
def right_tlfn(telefon) :
    if telefon[0] == '8' : telefon = '+7'+telefon[1:]
    telefon = telefon.replace(' ','')
    telefon = telefon.replace('-','')
    telefon = telefon.replace('(','')
    telefon = telefon.replace(')','')
    telefon = telefon.replace('\t','')
    return telefon
#   print('Длина телефонного номера = :',telefon[0],telefon[1],telefon[-1],len(telefon))

def new_client(to_Excel) :
    from_justClick = input('Введи запись из JustClick: ')
    from_justClick2 = input('Введи запись из JustClick: ')
    splitted_text = from_justClick.split()
    to_Excel[0] = splitted_text[1].capitalize() #имя
    to_Excel[1] = splitted_text[2].capitalize() #отчество
    to_Excel[2] = splitted_text[0].capitalize() #фамилия
    print(to_Excel)
    

# предполагаю, что почта всегда начинается с буквы, поэтому надо найти первую букву
    i = 0
    while from_justClick2[i].isalpha() != True : i += 1

    telefon = from_justClick2[:i-1]

    to_Excel[4] = right_tlfn(telefon)
    from_justClick2 = from_justClick2[i:]               #  отделяем телефон от строки. 

    splitted_text = from_justClick2.split()
    to_Excel[6] = splitted_text[0] #почта
# После этого надо найти индекс, с которого начинается дата. Предыдущее поле заканчивается на ещё.
    i = 1                                               # потому что в 0 поле точно почта.
    while splitted_text[i] != 'еще' :    i +=1

    to_Excel[7] = splitted_text[i+1]                    #когда
# if splitted_text[6] == 'Вчера' : to_Excel[i+1] = datetime.date(datetime.now(tz=None))      
# elif splitted_text[6] == 'Сегодня' : to_Excel[i+1] = datetime.date(datetime.now(tz=None))

    to_Excel[3] = splitted_text[i+4]                    #город
    return to_Excel
                                                    # Строка для ввода в ОТкрытие

while True :
    to_Excel = new_client(to_Excel = ['имя','отчество','фамилия','city','telefon','.','email','date'])
    to_OpenBroker = ''
    to_OpenBroker = to_OpenBroker.join([to_Excel[2],' ',to_Excel[0],' ',to_Excel [1],' ',to_Excel[4],' ',to_Excel[3]])
    to_Excel_joined = ''
    to_Excel_joined = to_Excel_joined.join([to_Excel[0],' ',to_Excel[1],' ',to_Excel[2],' ',to_Excel[3],' ',to_Excel[4],' ',to_Excel[5],' ',to_Excel[6],' ',str(to_Excel[7]),' '])
    print(f'Строка для Excel \n{to_Excel_joined}')
    print(f'Строка для Открытия: \n{to_OpenBroker}')