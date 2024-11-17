from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys

is_headless = False
is_linux = False
options = webdriver.ChromeOptions()
proxy = "web-test.apps.pkhbluataro.eastasia.aroapp.io"
options.add_argument(f"--proxy-server={proxy}")
options.add_argument("start-maximized")

if sys.platform == "linux":
    is_linux = True

if is_headless:
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')


def init_driver(context, tags):
    if is_linux:
        try:
            for i in tags:
                if "container" in i:
                    tag = i.split('=')[1]
                    module_name = tag[:-1]
                    container_number = tag[-1]
                    options.set_capability("nodename:applicationName", f"{module_name}{container_number}")
        except:
            pass
        context.driver = webdriver.Remote(command_executor="http://172.18.41.15:8083", options=options)
    else:
        options.binary_location = 'D:/Software-Setup/chrome-win64/chrome.exe'
        service = Service(executable_path='D:/Software-Setup/chromedriver.exe')
        context.driver = webdriver.Chrome(service=service, options=options)