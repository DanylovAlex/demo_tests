import pytest
from pages.homepage import HomePage
from pages.product import ProductPage


@pytest.fixture()
def before_after():
    print('\n--> Before test')
    yield
    print('\n--> After test')


def test_demo(before_after):
    assert 1 == 1


def test_web(driver):
    homepage = HomePage(driver=driver)
    homepage.open()
    xpath = '//*[@id="ui-id-5"]'
    homepage.click_page(xpath)
    product = ProductPage(driver)
    product.check_page('Men')
