import yaml
import os

def get_configs():
    file_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")
    with open(file_path) as config:
        #yamldata = yaml.safe_load(config)
        return yaml.safe_load(config)