
from hello import say_hello

def test_say_hello():
    assert say_hello("World") == "Hello, World!"
    assert say_hello("Jenkins") == "Hello, Jenkins!"
