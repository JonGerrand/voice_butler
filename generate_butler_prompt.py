import argparse
import os
import datetime
import random
from typing import Dict
import yaml

def extract_butler_config(config_path='') -> Dict:
    """Parse butler config from file

    Args:
        config_path (str, optional): Path to `butler_config.yaml` file. 
            Defaults to ''.

    Returns:
        Dict: Config file contents
    """
    with open(os.path.join(config_path, 'butler_config.yaml'), 'r') as fstream:
        try:
            conf_dict = yaml.safe_load(fstream)
        except yaml.YAMLError as error:
            print (error)
            print ("Cannot load config. Exiting...")
            exit()
    
    return conf_dict



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
        return f"{salutation} {title}, {time_address} {time}" 

    else:
        try: 
            return f"The time is now {datetime.datetime.now().strftime(config['time']['date_time_format'])}"
        except:
            return f"The time is now {datetime.datetime.now().strftime('%H:%M')}"

def announce_prompt(prompt: str) -> None:
    print (prompt)

if __name__ == '__main__':
    config = extract_butler_config()
    prompt = tell_time(config=config)
    announce_prompt(prompt)