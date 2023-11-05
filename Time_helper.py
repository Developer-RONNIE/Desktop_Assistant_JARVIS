import datetime

def get_formatted_time():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%I:%M %p")
    return formatted_time
