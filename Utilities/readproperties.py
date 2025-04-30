import configparser
con = configparser.RawConfigParser()
con.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = con.get('common info','baseURL')
        return url
    @staticmethod
    def getUsername():
        uname = con.get('common info','username')
        return uname
    @staticmethod
    def getPassword():
        pwd = con.get('common info','password')
        return pwd
