class Super:
    def __init__(self, x):
        ...Специальный код...

class Sub(Super):
    def __init__(self, x, y):
        Super.__init__(self, x) # Выполнить метод init суперкласса
        ...Специальный код...

I = Sub(1, 2)