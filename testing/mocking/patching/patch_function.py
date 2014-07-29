from mock import patch

import mymodule

@patch('mymodule.foo')
def fun(mock_foo):
    mock_foo("mock_foo")
    mymodule.foo.assert_called_with("mock_foo")
    print("Successfully tested mock")
fun()
