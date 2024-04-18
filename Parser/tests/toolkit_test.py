from src.utils.toolkit import get_response_bypassed, get_html_f, get_page_dict, remove_non_numeric_keys,\
get_last_page, count_ads_at_page, counter_ads_at_page_request


import pytest


### Unit tests
@pytest.mark.parametrize(
        "url, expected_code",
        [
            ("https://www.list.am/category/56/1?n=0&cmtype=1&price2=234567&crc=1&gl=2", 200),
            # ("https://www.list.am/category/56/1?n=0&cmtype=1&price2=234567&crc=1&gl=2", 404),
            # it won't work cause i havn't got a plug for 404, one way is provoke this error
            # 
        ]
)
def test_get_response_bypassed(url, expected_code):
    try:
        code_assertion = get_response_bypassed(url).status_code
        assert code_assertion == expected_code
    except:
        assert not expected_code


@pytest.mark.parametrize(
        "path_to_file, expected_result",
        [
            ("src/fixtures/index.html", True),
            ("src/fixtures/doesn't_exist.html_file", False),
            (1,False),
            (' ',False),
            ({1,'r',('2','2')}, False),
            ([],False),
        ])
def test_get_html_f(path_to_file, expected_result):
    try:
        result = get_html_f(path_to_file)
        if result != False:
            result = True # Therefore, the opened file status is 'True'.
        else: result = False
        assert result == expected_result
    except Exception:
        assert not expected_result

def test_get_page_dict():
    pass

def test_remove_non_numeric_keys():
    pass

def test_get_last_page():
    pass

def test_count_ads_at_page():
    pass

def test_counter_ads_at_page_request():
    pass
