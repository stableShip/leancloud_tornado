import ConfigParser
import os



configParser = ConfigParser.ConfigParser()
filePath = os.path.split(os.path.realpath(__file__))[0]
configFile = filePath + "/development.conf"
configParser.read(configFile)

