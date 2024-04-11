
from src.Helper.userHelperDB import UserHelperDB

import allure
import pytest


@allure.feature("Checking DB connection")
@pytest.mark.tcid02
def test_random_email_from_DB():
    exec = UserHelperDB()
    result = exec.get_random_email_from_DB
    group_ID = "APG777"
    # import pdb; pdb.set_trace()
    assert result[0]['group'] == group_ID, f"The expected group: {group_ID} but returned group: {result[0]['group']}"






