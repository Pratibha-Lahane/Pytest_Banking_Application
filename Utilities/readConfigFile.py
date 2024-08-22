import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\Config.ini")


class ReadConfig_class:

    @staticmethod
    def getUsername():
        Username = config.get('Login Data', 'Username')
        return Username

    @staticmethod
    def getPassword():
        Password = config.get('Login Data', 'Password')
        return Password
