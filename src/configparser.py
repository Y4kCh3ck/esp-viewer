import os
import toml

class ConfigParser:

    config_file_path = os.environ.get('XDG_CONFIG_HOME') + "/ev_config.toml"

    def __init__(self):
        pass

    @classmethod
    def create_example(cls):
        # print(self.config_file_path)
        if not os.path.exists(cls.config_file_path):
            content = '''[ Board ]\nname = "esp-cam"\nmodel = "esp-cam"\n\ndigital_pins = [ ["pin1", "pin2", "pin3", "pin4", "pin5"], ["LED 1", "LED 2", "LED 3", "SPEAKER", "CAMERA"] ]'''

            with open(cls.config_file_path, 'w') as file:
                file.write(content)

    @classmethod
    def print_config(cls):
        with open(cls.config_file_path, 'r') as file:
            content = file.read()

        print(content)

    @classmethod
    def read_config_pins(cls):
        if os.path.exists(cls.config_file_path):
            with open(cls.config_file_path, 'r') as file:
                data = toml.load(file)
                board = data['Board']

                return dict(zip(board['digital_pins'][0],board['digital_pins'][1]))
        else:
            return []
