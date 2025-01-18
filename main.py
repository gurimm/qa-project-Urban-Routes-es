from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import data


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_round = (By.CLASS_NAME, "button round")
    button_comfort_xpath = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    set_phone_number = (By.CLASS_NAME, 'np-text')
    input_phone_number = (By.ID, 'phone')
    number = (By.XPATH, '//*[@id="phone"]')
    button_next_xpath = (By.XPATH, '//*[text()="Siguiente"]')
    input_code = (By.ID, 'code')
    button_confirm_xpath = (By.XPATH, '//*[text()="Confirmar"]')
    select_taxi_xpath = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    button_payment_method = (By.CLASS_NAME, "pp-button")
    button_add_card = (By.CLASS_NAME, "pp-plus")
    set_credit_card = (By.CLASS_NAME, 'card-number-input')
    input_credit_card_xpath = (By.XPATH, '//*[@id="number"]')
    input_card_cvv_xpath = (By.XPATH, '//div[@class="card-code-input"]/input[@id="code"]')
    submit_card_xpath = (By.XPATH, '//*[text()="Agregar"]')
    button_close_xpath = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    input_comment_xpath = (By.XPATH, '//*[@id="comment"]')
    checkbox_bket_scrvs_xpath = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    counter_ice_cream = (By.CLASS_NAME, "counter-plus")
    button_smart_order = (By.CLASS_NAME, "smart-button-main")
    modal_order = (By.CLASS_NAME, "order-details")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def select_taxi(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.select_taxi_xpath).click()

    def select_comfort_rate(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.button_comfort_xpath).click()

    def select_number_button(self):
         self.driver.implicitly_wait(20)
         self.driver.find_element(*self.set_phone_number).click()

    def add_phone_number(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.number).send_keys(data.phone_number)

    def set_phone(self):
         self.driver.implicitly_wait(20)
         self.select_number_button()
         self.driver.implicitly_wait(20)
         self.add_phone_number()

    def click_on_next_button(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element(*self.button_next_xpath).click()

    def send_cell_info(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.button_confirm_xpath).click()

    def get_phone(self):
        return self.driver.find_element(*self.input_phone_number).get_property('value')


    def code_number(self):
        self.driver.implicitly_wait(15)
        phone_code = retrieve_phone_code(driver=self.driver)
        self.driver.implicitly_wait(15)
        self.driver.find_element(*self.input_code).send_keys(phone_code)


    def payment_method(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.button_payment_method).click()

    def add_card_option(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.button_add_card).click()

    def card_register(self):
        self.driver.implicitly_wait(20)
        self.payment_method()
        self.driver.implicitly_wait(20)
        self.add_card_option()

    def select_number(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element(*self.set_credit_card).click()

    def input_number(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element(*self.input_credit_card_xpath).send_keys(data.card_number)

    def card_input(self):
        self.driver.implicitly_wait(15)
        self.select_number()
        self.driver.implicitly_wait(15)
        self.input_number()

    def get_card_input(self):
        return self.driver.find_element(*self.input_credit_card_xpath).get_property('value')


    def code_card_input(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.input_card_cvv_xpath).send_keys(data.card_code)

    def cvv_code(self):
        self.driver.implicitly_wait(15)
        self.code_card_input()

    def get_cvv_card(self):
        return self.driver.find_element(*self.input_card_cvv_xpath).get_property('value')

    def registered_card(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.submit_card_xpath).click()

    def add_card(self):
        self.driver.implicitly_wait(20)
        self.card_input()
        self.driver.implicitly_wait(20)
        self.cvv_code()
        self.driver.implicitly_wait(20)
        self.registered_card()

    def close_modal(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.button_close_xpath).click()

    def set_message(self, message):
        self.driver.implicitly_wait(15)
        message_field = self.driver.find_element(*self.input_comment_xpath)
        message_field.send_keys(message)

    def get_message(self):
        return self.driver.find_element(*self.input_comment_xpath).get_property('value')

    def select_blanket_and_tissues(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element(*self.checkbox_bket_scrvs_xpath).click()

    def get_blanket_and_scarves(self):
        return self.driver.find_element(*self.checkbox_bket_scrvs_xpath).get_property('value')

    def select_ice_cream(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element(*self.counter_ice_cream).click()
        self.driver.find_element(*self.counter_ice_cream).click()

    def get_ice_cream(self):
        return self.driver.find_element(*self.counter_ice_cream).get_property('value')

    def select_order(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element(*self.button_smart_order).click()


    def driver_modal(self):
        self.driver.implicitly_wait(100)
        self.driver.find_element(*self.modal_order)
        self.driver.implicitly_wait(100)


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # 1.Configurar la dirección
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(10)
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

        # 2.Seleccionar taxi y tarifa
        routes_page.select_taxi()
        routes_page.select_comfort_rate()

        # 3.Rellenar el número de teléfono y obtener código
        phone_number = data.phone_number
        routes_page.set_phone()
        assert routes_page.get_phone() == phone_number

        routes_page.click_on_next_button()
        routes_page.code_number()
        routes_page.send_cell_info()

        # 4.Agregar una tarjeta de crédito
        routes_page.card_register()
        routes_page.add_card()
        routes_page.close_modal()
        assert routes_page.get_card_input() == data.card_number
        assert routes_page.get_cvv_card() == data.card_code

        # 5.Escribir un mensaje para el controlador
        message = data.message_for_driver
        routes_page.set_message(message)
        assert routes_page.get_message() == data.message_for_driver

        # 6.Pedir una manta y pañuelos
        routes_page.select_blanket_and_tissues()
        assert routes_page.get_blanket_and_scarves() == routes_page.select_blanket_and_tissues()

        # 7.Pedir 2 helados
        routes_page.select_ice_cream()
        assert routes_page.get_ice_cream() == routes_page.select_ice_cream()

        # 8.Aparece el modal para buscar un taxi
        routes_page.select_order()

        # 9.Esperar a que aparezca la información del conductor en el modal
        routes_page.driver_modal()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()