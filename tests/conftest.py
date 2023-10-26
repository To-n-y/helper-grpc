import httpx
import pytest


@pytest.fixture(scope="class", autouse=True)
def test_url() -> str:
    return "https://www.hangmanwords.com/words"


@pytest.fixture(scope="class", autouse=True)
def test_html() -> str:
    return "<html><ul class='Words_wordlist__i4vT0'><li>first</li><li>second</li></ul></html>"


@pytest.fixture(scope="class", autouse=True)
def test_arr() -> list[str]:
    return ["first", "second"]


@pytest.fixture()
def mock_req(respx_mock, test_html):
    rv = {
        "return_value:": httpx.Response(200, text=test_html),
    }
    respx_mock.get(test_html).mock(**rv)
