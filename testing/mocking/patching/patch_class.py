from mock import patch

import mymodule

cls = mymodule.Class("arg")
@patch('mymodule.Class')
def fun(MockClass):
    instance = mymodule.Class("mock")
    instance.method("mock")
    MockClass.assert_called_with("mock")
    print("Successfully tested mock")
fun()
