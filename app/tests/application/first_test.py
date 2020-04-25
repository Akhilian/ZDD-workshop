def func(x):
    return x + 1

class WhenGettingTheListOfPlanes:
    def should_return_4(self):
        assert func(3) == 4
