import yaml
from LoginTests.statics import LOGGER


def get_data():
    """
    :return: list of dic from yaml file.
    """
    LOGGER.debug('Trying to read inputs.')
    with open('LoginTests\\csv.yml', 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)


def login_assertion(data, index, driver):
    elements = driver.find_elements('xpath', '//div[@class="nav_username__k_aWG pointer "]')
    LOGGER.debug('Assertion is Checking...')
    words = elements[0].text.split('\n')
    actual_result = words[1].encode('utf-8').decode('utf-8')
    LOGGER.debug(f'Assertion: {actual_result} Compare with {data.get(index).get("username")}')
    assert actual_result == data.get(index).get("username")
    LOGGER.debug('--------------------- ')
