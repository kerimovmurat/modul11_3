import inspect


def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__
    # Получаем модуль, к которому принадлежит объект
    obj_module = getattr(obj, '__module__', 'Built-in')
    # Получаем список всех атрибутов и методов объекта
    obj_attrs = dir(obj)

    # Получаем методы, которые являются вызываемыми и не служебные
    attributes = [attr for attr in obj_attrs if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [meth for meth in obj_attrs if callable(getattr(obj, meth)) and not meth.startswith("__")]
    # словарь с информацией об объекте
    info = {
        "type": obj_type,
        "modul": obj_module,
        'attributes': attributes,
        'methods': methods
    }
    return info

class Car():
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def stop(self):
        return f'{self.make} {self.model} stop'
    def start(self):
        return f'{self.make} {self.model} start'

car = Car('Toyota', 'Corolla')

info = introspection_info(car)
print(info)
print(car.stop())
