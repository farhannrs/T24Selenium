import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from Helper import configReader
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Helper import randomData
from ENZO.Resources import DriverFactory
import json

ID = "none"


def navigate_to_url(context):
    try:
        if DriverFactory.is_linux:
            url = "http://web-test.apps.pkhbluataro.eastasia.aroapp.io/Browser/"
        else:
            url = configReader.url()
        context.driver.get(url)
        for i in range(3):
            if context.driver.title != 'Transact Login':
                try:
                    WebDriverWait(context.driver, 10).until(EC.title_is('Transact Login'))
                except:
                    context.driver.execute_script('window.location.reload()')
            else:
                break
    except Exception:
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot', attachment_type=AttachmentType.PNG)
        raise


def enter_text(context, value, keyword):
    try:
        # handling alert regarding session handling
        click_alert(context, 'accept')
        if '_' in keyword:
            # web element from factory
            web_element = find_element(context, keyword)
        else:
            # dynamic element
            web_element = WebDriverWait(context.driver, 60, poll_frequency=2, ignored_exceptions=(
                ElementNotVisibleException, ElementNotSelectableException)).until(
                EC.element_to_be_clickable(
                        (By.XPATH,
                         f'//label[text()="{keyword}"]//parent::div//parent::div//following-sibling::div//input')))
        value = get_context_value(context, value)
        web_element.clear()
        web_element.send_keys(value)
        web_element.send_keys(Keys.TAB)
        try:
            WebDriverWait(context.driver, 1).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='WRAPPER_TXT_EB64B2C073BD2C0F209366']")))
            WebDriverWait(context.driver, 20).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@id='WRAPPER_TXT_EB64B2C073BD2C0F209366']")))
        except:
            pass
    except Exception:
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot', attachment_type=AttachmentType.PNG)
        raise


def clear_text(context, keyword):
    try:
        web_element = find_element(context, keyword)
        web_element.clear()
    except Exception:
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot', attachment_type=AttachmentType.PNG)
        raise


def select_dropdown(context, value, keyword):
    try:
        # handling alert regarding session handling
        click_alert(context, 'accept')
        if '_' in keyword:
            # web element from factory
            web_element = find_element(context, keyword)
        else:
            # dynamic element
            web_element = WebDriverWait(context.driver, 60, poll_frequency=2, ignored_exceptions=(
                    ElementNotVisibleException, ElementNotSelectableException)).until(
                    EC.element_to_be_clickable(
                        (By.XPATH,
                         f'//label[text()="{keyword}"]//parent::div//parent::div//following-sibling::div//select')))
        select = Select(web_element)
        try:
            select.select_by_visible_text(value)
            web_element.send_keys(Keys.TAB)
        except:
            select.select_by_value(value)
            web_element.send_keys(Keys.TAB)
        # wait for the loader to disappear
        try:
            WebDriverWait(context.driver, 1).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='WRAPPER_TXT_EB64B2C073BD2C0F209366']")))
            WebDriverWait(context.driver, 20).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@id='WRAPPER_TXT_EB64B2C073BD2C0F209366']")))
        except:
            pass
    except Exception:
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot', attachment_type=AttachmentType.PNG)
        raise


def click(context, keyword):
    try:
        # handling alert regarding session handling
        click_alert(context, 'accept')
        if '_' not in keyword:
            web_element = WebDriverWait(context.driver, 60, poll_frequency=2, ignored_exceptions=(
                ElementNotVisibleException, ElementNotSelectableException)).until(
                EC.element_to_be_clickable(
                    (By.XPATH, f'//span[text()="{keyword}"]//parent::a |'
                               f'//span[text()="{keyword}"]//parent::div//parent::div//following-sibling::div//span[@class="ddSpan"] |'
                               f'//label[text()="{keyword}"]//parent::div//parent::div//following-sibling::div//span[@class="ddSpan"]')))
        else:
            web_element = find_element(context, keyword)
        try:
            ActionChains(context.driver).scroll_to_element(web_element).perform()
            for i in range(3):
                web_element.click()
                break
        except (StaleElementReferenceException, ElementClickInterceptedException):
            print('---log: handling stale element')
            context.driver.implicitly_wait(5)
            context.driver.execute_script("arguments[0].scrollIntoView();", web_element)
            context.driver.execute_script("arguments[0].click();", web_element)
    except Exception:
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot', attachment_type=AttachmentType.PNG)
        raise


def click_tab(context, keyword):
    try:
        # handling alert regarding session handling
        click_alert(context, 'accept')
        web_element = WebDriverWait(context.driver, 60, poll_frequency=2, ignored_exceptions=(
            ElementNotVisibleException, ElementNotSelectableException)).until(
            EC.element_to_be_clickable(
                (By.XPATH, f'//a[text()="{keyword}"')))
        ActionChains(context.driver).scroll_to_element(web_element).perform()
        web_element.click()
    except Exception:
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot', attachment_type=AttachmentType.PNG)
        raise

def field_notEditable(context, keyword):
    try:
        # handling alert regarding session handling
        click_alert(context, 'accept')
        if '_' in keyword:
            # web element from factory
            web_element = find_element(context, keyword)
            field_type = web_element.get_attribute('type')
            assert not field_type == 'text', f"{keyword} field is editable input type='{field_type}'"
        else:
            # dynamic element
            web_element = WebDriverWait(context.driver, 60, ignored_exceptions=(
                StaleElementReferenceException, ElementClickInterceptedException)).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     f'//label[text()="{keyword}"]//parent::div//parent::div//following-sibling::div//input')))
        field_type = web_element.get_attribute('type')
        assert not field_type == 'text', f"{keyword} field is editable input type='{field_type}'"
        try:
            WebDriverWait(context.driver, 1).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='WRAPPER_TXT_EB64B2C073BD2C0F209366']")))
            WebDriverWait(context.driver, 20).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@id='WRAPPER_TXT_EB64B2C073BD2C0F209366']")))
        except:
            pass
    except Exception:
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot',
                      attachment_type=AttachmentType.PNG)
        raise


def field_editable(context, keyword):
    try:
        # handling alert regarding session handling
        click_alert(context, 'accept')
        if '_' in keyword:
            # web element from factory
            web_element = find_element(context, keyword)
            field_type = web_element.get_attribute('type')
            assert field_type == 'text', f"{keyword} field is not editable input type='{field_type}'"
        else:
            # dynamic element
            web_element = WebDriverWait(context.driver, 60, ignored_exceptions=(
                StaleElementReferenceException, ElementClickInterceptedException)).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     f'//label[text()="{keyword}"]//parent::div//parent::div//following-sibling::div//input')))
        field_type = web_element.get_attribute('type')
        assert field_type == 'text', f"{keyword} field is not editable input type='{field_type}'"
        try:
            WebDriverWait(context.driver, 1).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='WRAPPER_TXT_EB64B2C073BD2C0F209366']")))
            WebDriverWait(context.driver, 20).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@id='WRAPPER_TXT_EB64B2C073BD2C0F209366']")))
        except:
            pass
    except Exception:
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot',
                      attachment_type=AttachmentType.PNG)
        raise

def click_radio_button_dynamic(context, value, button):
    try:
        click_alert(context, 'accept')
        if "_" in button:
            element_attribute, element_type, = configReader.element_details(button)
            element_attribute_checked = element_attribute.replace("]", f" and text() = {value}]//preceding-sibling::input[@checked='checked']")
            try:
                if context.driver.find_element(By.XPATH, element_attribute_checked).is_displayed():
                    pass
            except NoSuchElementException:
                element_attribute = element_attribute.replace("]", f" and text() = {value}]")
                web_element = context.driver.find_element(By.XPATH, element_attribute)
                ActionChains(context.driver).scroll_to_element(web_element).perform()
                web_element.click()
        else:
            element_attribute_checked = f"//span[text()='{button}']//parent::div//parent::div//following-sibling::div//input[@value={value} and @checked='checked']"
            try:
                if context.driver.find_element(By.XPATH, element_attribute_checked).is_displayed():
                    pass
            except NoSuchElementException:
                element_attribute = f"//span[text()='{button}']//parent::div//parent::div//following-sibling::div//input[@value ={value}]//parent::div"
                web_element = context.driver.find_element(By.XPATH, element_attribute)
                ActionChains(context.driver).scroll_to_element(web_element).perform()
                web_element.click()
    except Exception:
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot', attachment_type=AttachmentType.PNG)
        raise


def select_dropdown_by_value(context, value, keyword):
    try:
        click_alert(context, 'accept')
        web_element = find_element(context, keyword)
        select = Select(web_element)
        select.select_by_value(value)
        # web_element.send_keys(Keys.TAB)
        # wait for the loader to disappear
        try:
            WebDriverWait(context.driver, 1).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='WRAPPER_TXT_EB64B2C073BD2C0F209366']")))
            WebDriverWait(context.driver, 20).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@id='WRAPPER_TXT_EB64B2C073BD2C0F209366']")))
        except:
            pass
    except Exception:
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot', attachment_type=AttachmentType.PNG)
        raise


def click_dropdown_value_dynamic(context, value):
    try:
        click_alert(context, 'accept')
        xpath = f"//span[text()='{value}']"
        web_element = WebDriverWait(context.driver, 60, poll_frequency=2, ignored_exceptions=(
            ElementNotVisibleException, ElementNotSelectableException)).until(
            EC.element_to_be_clickable(
                (By.XPATH, xpath)))
        ActionChains(context.driver).scroll_to_element(web_element).perform()
        web_element.click()
    except Exception:
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot', attachment_type=AttachmentType.PNG)
        raise


# old-not used
def click_radio_button(context, keyword):
    try:
        click_alert(context, 'accept')
        element_attribute, element_type, = configReader.element_details(keyword)
        element_attribute_checked = element_attribute.replace("]", "and @checked = 'checked']/parent::*")
        try:
            if context.driver.find_element(By.XPATH, element_attribute_checked).is_displayed():
                pass
        except NoSuchElementException:
            web_element = context.driver.find_element(By.XPATH, f'{element_attribute}/parent::*')
            # scroll to the button
            # context.driver.execute_script("arguments[0].scrollIntoView();", web_element)
            ActionChains(context.driver).scroll_to_element(web_element).perform()
            web_element.click()
    except Exception:
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot', attachment_type=AttachmentType.PNG)
        raise


def click_alert(context, value):
    try:
        if value == 'accept':
            context.driver.switch_to.alert.accept()
            print("alert handled")
        else:
            context.driver.switch_to.alert.dismiss()
    except:
        pass


def dynamic_limit(context, field):
    # wait for the dropdown to load completely
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[text() = 'Limit Id']")))
    # finding all dropdown limit IDs and storing them in list
    limit_ids = context.driver.find_elements(By.XPATH, "//span[@title='@ID']")
    dynamic_limit_id = f'101647.0006200.{randomData.create_limit_id(limit_ids)}'
    enter_text(context, dynamic_limit_id, field)


def verify_message(context, keyword):
    try:
        web_element = find_element(context, keyword)
        if web_element.is_displayed():
            text = web_element.text
            text_list = text.split(" ")
            try:
                context.code.append(text_list[2])
                context.dict[f'{text_list[7]}'] = text_list[2]
                print(context.code)
                context.dict['isCreated'] = 'Passed'
                # save_value_in_data(context, "isCreated", "Passed")
            except:
                pass
    except (TimeoutException, ElementNotVisibleException, NoSuchElementException):
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot', attachment_type=AttachmentType.PNG)
        raise


def save_value_in_context(context, key, field):
    try:
        web_element = find_element(context, field)
        if web_element.is_displayed():
            text = web_element.text
            context.dict[f'{key}'] = text
    except (TimeoutException, ElementNotVisibleException, NoSuchElementException):
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot', attachment_type=AttachmentType.PNG)
        raise


def save_value_in_data(context, key, field):
    try:
        web_element = find_element(context, field)
        if web_element.is_displayed():
            text = web_element.text
            with open('Features/Temenos/PreReq/data.json', 'r+') as f:
                data_vars = f.read()
                if "{" not in data_vars:
                    data_vars = "{" + data_vars + "\n}"
                try:
                    data_json = json.loads(data_vars)
                    if key not in data_json.keys():
                        data_vars = data_vars.replace('}', f',"{key}":"{text}"\n}}')
                        data_json = json.loads(data_vars)
                    else:
                        data_json[f'{key}'] = text
                    f.seek(0)
                    f.truncate(0)
                    json.dump(data_json, f, sort_keys=True, indent=4)

                except:
                    pass
    except (TimeoutException, ElementNotVisibleException, NoSuchElementException):
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot',
                      attachment_type=AttachmentType.PNG)
        raise



def verify_homepage(context, keyword):
    try:
        try:
            # handling maintenance fee alert, to be removed when fixed
            WebDriverWait(context.driver, 5, ignored_exceptions= (TimeoutException,)).until(EC.alert_is_present())
            alert = context.driver.switch_to.alert
            alert.accept()

        except TimeoutException:
            web_element = find_element(context, keyword)
            web_element.is_displayed()
            if context.is_auth is False:
                context.dict['isCreated'] = 'Failed'
            # save_value_in_data(context, "isCreated", "Failed")
    except (TimeoutException, ElementNotVisibleException, NoSuchElementException):
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot', attachment_type=AttachmentType.PNG)
        raise


def verify_enquiry(context, keyword):
    try:
        if '_' in keyword:
            # web element from factory
            if keyword == '':
                keyword = 'Enquiry_ToggleButton'
            web_element = find_element(context, keyword)
        else:
            # dynamic element
            web_element = WebDriverWait(context.driver, 60, ignored_exceptions=(
                    StaleElementReferenceException, ElementClickInterceptedException)).until(
                    EC.element_to_be_clickable(
                        (By.XPATH,
                         f'//span[text()="{keyword}"] |'
                         f'//span[text()="{keyword}"]//parent::div//parent::div//parent::div |'
                         f'//label[text()="{keyword}"]//parent::div//parent::div//parent::div')))
        web_element.is_displayed()
    except (TimeoutException, ElementNotVisibleException, NoSuchElementException):
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot', attachment_type=AttachmentType.PNG)
        raise


def check_mandatory_validation(context, error, field_name):
    try:
        web_element = WebDriverWait(context.driver, 60, ignored_exceptions=(
            StaleElementReferenceException, ElementClickInterceptedException)).until(
            EC.element_to_be_clickable(
                (By.XPATH, f'//a[text()="{field_name}: {error}"]')))
        ActionChains(context.driver).scroll_to_element(web_element).perform()
        web_element.is_displayed()
    except (TimeoutException, ElementNotVisibleException, NoSuchElementException):
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot', attachment_type=AttachmentType.PNG)
        raise


def verify_field_not_empty(context, field):
    try:
        web_element = WebDriverWait(context.driver, 5, ignored_exceptions=(
            StaleElementReferenceException, ElementClickInterceptedException)).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f'//span[text()="{field}"]//parent::div//parent::div//following-sibling::div//input |'
                 f'//label[text()="{field}"]//parent::div//parent::div//following-sibling::div//input')))
        if web_element.is_displayed():
            value = web_element.get_attribute("value")
            assert value != '' or value == 'None'
    except (TimeoutException, ElementNotVisibleException, NoSuchElementException):
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot',
                      attachment_type=AttachmentType.PNG)
        raise


def verify_account_statement(context, value, position, keyword):
    try:
        element_attribute, element_type, = configReader.element_details(keyword)
        element_attribute = element_attribute.replace("X", position)
        web_element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, element_attribute)))
        if value == 'null':
            value = ''
        amount_present = web_element.text
        assert amount_present == value
    except (TimeoutException, ElementNotVisibleException, NoSuchElementException):
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot', attachment_type=AttachmentType.PNG)
        raise


def verify_field_value(context, value, field):
    try:
        value = get_context_value(context, value)
        web_element = WebDriverWait(context.driver, 60, poll_frequency=2, ignored_exceptions=(
            ElementNotVisibleException, ElementNotSelectableException)).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f'//span[text()="{field}"]//parent::div//parent::div//following-sibling::div//span |'
                 f'//label[text()="{field}"]//parent::div//parent::div//following-sibling::div//span')))
        if web_element.is_displayed():
            text = web_element.text
            assert text == value
    except:
        web_element = WebDriverWait(context.driver, 5, ignored_exceptions=(
            StaleElementReferenceException, ElementClickInterceptedException)).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f'//span[text()="{field}"]//parent::div//parent::div//following-sibling::div//input[@value="{value}"] |'
                 f'//label[text()="{field}"]//parent::div//parent::div//following-sibling::div//input[@value="{value}"]')))
        web_element.is_displayed()
    finally:
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot', attachment_type=AttachmentType.PNG)


def find_element(context, keyword):
    element_attribute, element_type, = configReader.element_details(keyword)
    if element_type == "XPATH":
        web_element = WebDriverWait(context.driver, 60, poll_frequency=2, ignored_exceptions=(
            ElementNotVisibleException, ElementNotSelectableException)).until(
            EC.element_to_be_clickable(
                (By.XPATH, element_attribute)))
        return web_element
    elif element_type == "ID":
        web_element = WebDriverWait(context.driver, 60, ignored_exceptions=(
            StaleElementReferenceException,)).until(
            EC.visibility_of_element_located(
                (By.ID, element_attribute)))
        return web_element
    elif element_type == "NAME":
        web_element = WebDriverWait(context.driver, 60, ignored_exceptions=(
            StaleElementReferenceException,)).until(
            EC.element_to_be_clickable(
                (By.NAME, element_attribute)))
        return web_element
    elif element_type == "TAG_NAME":
        web_element = WebDriverWait(context.driver, 60, ignored_exceptions=(
            StaleElementReferenceException,)).until(
            EC.element_to_be_clickable(
                (By.TAG_NAME, element_attribute)))
        return web_element
    elif element_type == "CSS_SELECTOR":
        web_element = WebDriverWait(context.driver, 60, ignored_exceptions=(
            StaleElementReferenceException,)).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, element_attribute)))
        return web_element
    elif element_type == "CLASS_NAME":
        web_element = WebDriverWait(context.driver, 60, ignored_exceptions=(
            StaleElementReferenceException,)).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, element_attribute)))
        return web_element
    elif element_type == "LINK_TEXT":
        web_element = WebDriverWait(context.driver, 60, ignored_exceptions=(
            StaleElementReferenceException,)).until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, element_attribute)))
        return web_element
    elif element_type == "PARTIAL_LINK_TEXT":
        web_element = WebDriverWait(context.driver, 60, ignored_exceptions=(
            StaleElementReferenceException,)).until(
            EC.element_to_be_clickable(
                (By.PARTIAL_LINK_TEXT, element_attribute)))
        return web_element


def update_field_value(context, field):
    try:
        web_element = WebDriverWait(context.driver, 60, poll_frequency=2, ignored_exceptions=(
            ElementNotVisibleException, ElementNotSelectableException)).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f'//span[text()="{field}"]//parent::div//parent::div//following-sibling::div//input |'
                 f'//label[text()="{field}"]//parent::div//parent::div//following-sibling::div//input')))
        if web_element.is_displayed():
            previous_value = web_element.get_attribute("value")
            print(previous_value, type(previous_value))
            updated_value = float(previous_value) + 1

            web_element.clear()
            web_element.send_keys(updated_value)
            web_element.send_keys(Keys.TAB)
    except (TimeoutException, ElementNotVisibleException, NoSuchElementException):
        allure.attach(context.driver.get_screenshot_as_png(), name='error_screenshot',
                      attachment_type=AttachmentType.PNG)
        raise


def switch_window(context):
    try:
        WebDriverWait(context.driver, 5).until(
            EC.new_window_is_opened(context.driver.window_handles))
        context.driver.switch_to.window(context.driver.window_handles[-1])
        context.driver.maximize_window()
    except:
        context.driver.switch_to.window(context.driver.window_handles[-1])
        context.driver.maximize_window()


def switch_window_back(context):
    try:
        context.driver.switch_to.window(context.driver.window_handles[-2])
        context.driver.maximize_window()
    except:
        context.driver.switch_to.window(context.driver.window_handles[-2])
        context.driver.maximize_window()


def get_context_value(context, value):
    try:
        if "MobileNumber" in value:
            context.dict['MobileNumber'] = randomData.create_mobile_number()
            return context.dict['MobileNumber']
        elif "Code" in value:
            return context.code[-1]
        elif "ReversalLimit" in value:
            return context.code[0]
        elif value == 'CNIC':
            context.dict['CNIC'] = randomData.create_cnic()
            return context.dict['CNIC']
        elif "Date" in value:
            return randomData.generate_random_date_in_format()
        elif "SameCNIC" in value:
            try:
                if context.dict_scenario["SameCNIC"] != '':
                    value = context.dict_scenario["SameCNIC"]
                    return value
                else:
                    context.dict_scenario["SameCNIC"] = randomData.create_cnic()
                    return context.dict_scenario["SameCNIC"]
            except:
                pass
        elif "SameHajjID" in value:
            try:
                if context.dict_scenario["SameHajjID"] != '':
                    return context.dict_scenario["SameHajjID"]
            except:
                x = randomData.create_hajjID()
                context.dict_scenario["SameHajjID"] = x
                return x
        elif "hajjID" in value:
            try:
                if context.dict["hajjID"] != '':
                    value = context.dict["hajjID"]
                    return value
            except:
                context.dict["hajjID"] = randomData.create_hajjID()
                return context.dict["hajjID"]
        elif "NTN" in value:
            return randomData.create_ntn()
        else:
            try:
                with open('Features/Temenos/PreReq/data.json', 'r') as f:
                    data_vars = f.read()
                    data_json = json.loads(data_vars)
                    return data_json[value]
            except:
                return value
    except:
        pass


def step_user_scrolls_down(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    context.driver.execute_script("window.scrollBy(0,2000)", "")


def hover(context, element):
    web_element = find_element(context, element)
    ActionChains(context.driver).scroll_to_element(web_element).perform()
    hover_element = ActionChains(context.driver).move_to_element(web_element)
    hover_element.perform()


def write_to_data_gen_file(context, account_status):
    try:
        ac_num = get_context_value(context, 'NewAccountNumber')
        with open('Features/Temenos/AccountCreation/data.txt', 'a') as f:
            try:
                f.write(f'{context.dict["CustomerNumber"]},{ac_num},{context.dict["MobileNumber"]},{context.dict["CNIC"]},{account_status} \n')
            except:
                print('---log: there was an error in writing value. Check if the test case has passed')
    except:
        print('---log: file or folder not found where values are to be saved!')
        raise


def quit_browser(context):
    context.driver.close()
    context.driver.quit()