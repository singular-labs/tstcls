# pytest-tstcls
Test Class Base

## How to use
### Simple Tests
```python
from tstcls import TestClassBase

class TestMyClass(TestClassBase):
    def setup_test(self):
        self.tester = MyClass()

    def test_my_method(self):
        ###
        self.tester.my_method()
        ###
```
### Use Mocks
```python
from tstcls import TestClassBase

class TestMyClass(TestClassBase):
    def setup_test(self):
        self.my_mocked_dependency = Mock()
        self.tester = MyClass(self.my_mocked_dependency)

    def test_my_method(self):
        self.my_mocked_dependency.return_value = 123

        ###
        self.tester.my_method()
        ###
```
### Use fixtures as usual
```python
from tstcls import TestClassBase

class TestMyClass(TestClassBase):
    @pytest.fixture
    def my_fixture(self):
        return 321

    def setup_test(self, my_fixture):
        self.tester = MyClass(my_fixture)

    def test_my_method(self, my_fixture):
        ###
        self.tester.my_method()
        ###
```
