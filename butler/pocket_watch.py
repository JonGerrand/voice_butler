import random
import datetime
from unittest import case

from soupsieve import match

def pronounce_time(hrs: str, min: str) -> str:
    """Convert time format %H:%M to a time utterance

    Args:
        hrs (str): The current hour (24-hr format)
        min (str): The current min. 

    Returns:
        str: The time translated to an utterance. 
             E.g. "07:15" -> "Quater-past 7" 
                  "18:37" -> "Six thirty-seven" 
    """

    first_special_intervals = {
        "15": "Quater-past",
        "30": "Half-past",
    }

    hours = {
        "00": "Twelve",
        "11": "Eleven",
        "10": "Ten",
        "09": "Nine",
        "08": "Eight",
        "07": "Seven",
        "06": "Six",
        "05": "Five",
        "04": "Four",
        "03": "Three",
        "02": "Two",
        "01": "One",
        "12": "Twelve",
        "13": "One",
        "14": "Two",
        "15": "Three",
        "16": "Four",
        "17": "Five",
        "18": "Six",
        "19": "Seven",
        "20": "Eight",
        "21": "Nine",
        "22": "Ten",
        "23": "Eleven",
    }

    second_special_intervals = {
        "00" : "O'clock",
        "11" : "eleven",
        "12" : "twelve",
        "13" : "thirteen",
        "14" : "fourteen",
        "16" : "sixteen",
        "17" : "seventeen",
        "18" : "eighteen",
        "19" : "nineteen",
    }

    minutes = {
        "0" : "",
        "1" : "one",
        "2" : "two",
        "3" : "three",
        "4" : "four",
        "5" : "five",
        "6" : "six",
        "7" : "seven",
        "8" : "eight",
        "9" : "nine",
    }

    deci_minutes = {
        "0" : "Oh",
        "2" : "twenty",
        "3" : "thirty",
        "4" : "forty",
        "5" : "fifty",
    }

    # First phrase
    first_phrase = ""
    if min in first_special_intervals.keys():
        first_phrase = first_special_intervals[min]
        second_phrase = hours[hrs]
        return f"{first_phrase} {second_phrase}" 
    else: 
        first_phrase = hours[hrs]
                
    # Second phrase
    second_phrase = ""
    if min in second_special_intervals.keys():
        second_phrase = second_special_intervals[min]
    else: 
        second_phrase = f"{deci_minutes[min[0]]} {minutes[min[1]]}"

    return f"{first_phrase} {second_phrase}" 
                

def tell_time(config, tone="informal") -> str:
    """Get the butler to tell the time. 

    Args:
        tone (str, optional): Mode of speech. Defaults to 'informal'

    Returns:
        str: The formed text.
    """
    if tone == 'informal':
        title = random.sample(config['host']['titles'], 1)[0]
        salutation = random.sample(config['salutations'],1)[0]
        time_address = random.sample(config['time']['time_introductions'],1)[0]
        try: 
            time = datetime.datetime.now().strftime(
                    config['time']['date_time_format'])
        except: 
            time = datetime.datetime.now().strftime('%H:%M')
        return f"{salutation} {title}, {time_address} {time}." 

    else:
        try: 
            return f"The time is now {datetime.datetime.now().strftime(config['time']['date_time_format'])}."
        except:
            return f"The time is now {datetime.datetime.now().strftime('%H:%M')}."
