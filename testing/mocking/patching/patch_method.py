from mock import patch

import mymodule

@patch('mymodule.Class.method')
def fun(mock_method):
    instance = mymodule.Class()
    instance.method("mock")
    mock_method.assert_called_with("mock")
    print("Successfully tested mock")
fun()
