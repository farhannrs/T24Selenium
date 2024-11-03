import xml.etree.ElementTree as ET
import configparser

config = configparser.ConfigParser()
config.read("Resources/Appconfig.ini")


def project_name():
    for section in config.sections():
        if section == "config":
            for item in config.items(section):
                if "application" in item:
                    return item[1]


projectName = project_name()

# generic - will get application name from config
# tree = ET.parse(f'Resources/ElementFactory-{projectName}.xml')

tree = ET.parse(f'Resources/ElementFactory.xml')
root = tree.getroot()


def url():
    for section in config.sections():
        if section == "config":
            for item in config.items(section):
                if "url" in item:
                    return item[1]


def element_details(keyword):
    keyword_split = keyword.split('_')
    for module in root.findall('module'):
        if module.get('name') == keyword_split[0]:
            for element in module.findall('element'):
                if element.get('name') == keyword:
                    return element.get('attribute'), element.get('type')