from devquote.core import get_quote

def test_get_quote():
    quote = get_quote("motivation")
    assert isinstance(quote, str)
