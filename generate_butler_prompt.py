import argparse
import os


import butler.pocket_watch as watch
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


def announce_prompt(prompt: str) -> None:
    print (prompt)

if __name__ == '__main__':
    config = extract_butler_config()
    prompt = watch.tell_time(config=config)
    announce_prompt(prompt)