import yaml, os


def read_yaml_data():
    with open(os.path.join(os.path.dirname(__file__), "..", "test_data","json_data.yaml")) as json_data:
        return yaml.safe_load(json_data)
    
print(read_yaml_data()["posts_api"])