import json
import os
from error import ErrorCheck

class ReadWriteJSON:
    def get_config_path(self):
        config_path = os.path.join(
                os.path.join(
                    os.path.dirname(__file__),
                    "..", "config", "config.json"
                    )
                )

        ErrorCheck().error_check_for_loading_config(config_path)
        return config_path

    def read_config(self):
        config_path = self.get_config_path()

        with open(config_path, "r") as f:
            return json.load(f)

    def write_config(self, config):
        config_path = self.get_config_path()

        with open(config_path, "w") as f:
            json.dump(config, f, indent = 4)
