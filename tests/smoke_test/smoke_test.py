
from src.Utility.userHelperDB import UserHelperDB

import allure
import pytest
import logging as log

@allure.feature('Healthy check')
@pytest.mark.tcid01
def test_healthcheck():
    log.info("Hello World")


@pytest.mark.tcid02
def test_random_email_from_DB():
    exec = UserHelperDB()
    result = exec.get_random_email_from_DB()






