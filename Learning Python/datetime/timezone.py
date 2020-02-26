import datetime
import pytz # python -m pip install pytz

# cria fusos horarios UTC=0, UTC+11 e UTC-3
UTC_timezone = datetime.timezone(datetime.timedelta(hours=0))
sydney_timezone = datetime.timezone(datetime.timedelta(hours=11))
saopaulo_timezone = datetime.timezone(datetime.timedelta(hours=-3))

# cria um datetime objeto com timezone = UTC timezone
current_UTC_time = datetime.datetime(2020, 2, 22, 22, 25, 0, tzinfo=UTC_timezone)

# Imprime o que seria o horário em Sao Paulo quando o horario UTC = current_UTC_time
print('Hora UTC: ', current_UTC_time)
print('Hora em Sao Paulo: ', current_UTC_time.astimezone(saopaulo_timezone))
print('Hora em Sydney: ', current_UTC_time.astimezone(sydney_timezone))

#-----------------------------------------
# trabalhando com a biblioteca pytz

UTC = pytz.timezone('UTC')
Sao_Paulo = pytz.timezone('America/Sao_Paulo')
Sydney = pytz.timezone('Australia/Sydney')
# all timezones here:  
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# pytz.all_timezones
# pytz.country_timezones['us']

# seta o formato desejado
fmt = '%d/%m/%Y  %H:%M:%S  %Z%z'

# localiza o fuso horario correspondente a UTC
event_UTC = UTC.localize(datetime.datetime(2020, 2, 21, 22, 50, 0))
# set start_SP as Sao Paulo timezone
event_SP = event_UTC.astimezone(Sao_Paulo)
print('Hora em SAO PAULO: ', event_SP.strftime(fmt))








