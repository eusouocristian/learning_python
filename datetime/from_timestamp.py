import datetime
def timestamp_oldest(*args):
    lista = []
    for item in args:
        lista.append(item)

    lista.sort()
    last = lista[0]
    datetime_last = datetime.datetime.fromtimestamp(last)
    
    return datetime_last

a = timestamp_oldest(1582308796.690014, 1582368796.690014, 1582338796.690014, 1582348796.690014)
print(a) # 2020-02-22 07:53:16.690014