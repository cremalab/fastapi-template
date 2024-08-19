import os


class Environment:
    """Helper class to get environment variables"""

    @classmethod
    def get_string(cls, config_name, default=""):
        return str(os.getenv(config_name, default))

    @classmethod
    def get_int(cls, config_name, default=0):
        return int(os.getenv(config_name, default))

    @classmethod
    def get_string_list(cls, config_name, default=[]):
        string = cls.get_string(config_name)
        if string == "":
            return default
        return list(map(lambda x: x.strip(), str(string).split(",")))
