import datetime
import pytz

starter = pytz.utc.localize(datetime.datetime(2015, 10, 21, 23, 29))

def to_timezone(name_string):
    new_timezone = pytz.timezone(name_string)
        
    event = starter.astimezone(new_timezone)
    
    return event

print(to_timezone('America/Sao_Paulo'))

