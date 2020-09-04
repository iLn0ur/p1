# -*- coding: utf-8

# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Ни Е.А.

# ---------------------------------------------------------------------------------------------
# Понятие класса, объекта (стр. 1-22)

# 1. Создайте класс Glass с атрибутами capacity_volume и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)


class Glass:
    def __init__(self, capacity=0, occupied=0):
        if not isinstance(capacity, (int, float)):
            raise TypeError('не тот тип, чувак')
        if not isinstance(occupied, (int, float)):
            raise TypeError('Не тот тип, чувак!')
        if capacity < 0:
            raise ValueError('У тебя вместимость меньше 0!')
        if occupied < 0:
            raise ValueError('У тебя лбъем меньше 0!')
        if capacity < occupied:
            raise ValueError('объем больше вместимости')

        self.capacity_volume = capacity
        self.occupied_volume = occupied

    def __repr__(self):
        return f'Glass({self.capacity_volume}, {self.occupied_volume})'


# 2. Создайте два и более объектов типа Glass
#    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
#    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.



# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

class GlassDefaultArg:
    def __init__(self, occupied=0):
        if not isinstance(occupied, (int, float)):
            raise TypeError('Не тот тип, чувак!')
        if occupied < 0:
            raise ValueError('У тебя лбъем меньше 0!')

        self.occupied_volume = occupied
    def __repr__(self):
        return f'Glass({self.occupied_volume})'


# 4. Создайте класс GlassDefaultListArg (нужен только __init__) 
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?

class GlassDefaultListArg:
    def __init__(self, capacity=0, occupied=[]):
        if not isinstance(capacity, (int, float)):
            raise TypeError('не тот тип, чувак')
        if not isinstance(occupied, list):
            raise TypeError('Не тот тип, чувак!')
        if capacity < 0:
            raise ValueError('У тебя вместимость меньше 0!')
        # if occupied < 0:
        #     raise ValueError('У тебя лбъем меньше 0!')
        # if capacity < occupied:
        #     raise ValueError('объем больше вместимости')

        self.capacity_volume = capacity
        self.occupied_volume = occupied.copy()

        self.occupied_volume.append(100)

    def __repr__(self):
        return f'Glass({self.capacity_volume}, {self.occupied_volume})'


# 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
#    Вызовите методы add_water и remove.
#    Убедитесь, что методы правильно изменяют атрибут occupied_volume.

class GlassAddRemove:
    def __init__(self, capacity=0, occupied=0):
        if not isinstance(capacity, (int, float)):
            raise TypeError('не тот тип, чувак')
        if not isinstance(occupied, (int, float)):
            raise TypeError('Не тот тип, чувак!')
        if capacity < 0:
            raise ValueError('У тебя вместимость меньше 0!')
        if occupied < 0:
            raise ValueError('У тебя лбъем меньше 0!')
        if capacity < occupied:
            raise ValueError('объем больше вместимости')

        self.capacity_volume = capacity
        self.occupied_volume = occupied

    def add_water(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Жду число')
        if value < 0:
            raise ValueError('Жду положительное число')

        space = self.capacity_volume - self.occupied_volume
        if space < value:
            self.occupied_volume = self.capacity_volume
            return value - space
        else:
            self.occupied_volume += value
            return 0

    def remove_water(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Жду число')
        if value < 0:
            raise ValueError('Жду положительное число')

        if self.occupied_volume < value:
            rem = value - self.occupied_volume
            self.occupied_volume = 0
            return rem
        else:
            self.occupied_volume -= value
            return 0

    def __repr__(self):
        return f'Glass({self.capacity_volume}, {self.occupied_volume})'

# 6. Создайте три объекта типа GlassAddRemove, 
#    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
#    а. Получите типы объектов и класса
#    б. Проверьте тип созданного объекта.




# ---------------------------------------------------------------------------------------------
# Внутренние объекты класса (стр. 25-33)

# 7. Получите список атрибутов экземпляра класса в начале метода __init__, 
#    в середине __init__ и в конце __init__, (стр. 28-30)
#    а также после создания объекта.
#    Опишите результат.


# 8. Создайте три объекта Glass. (стр. 27)
#    Получите id для каждого объекта с соответсвующим id переменной self.



# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python;
#     - соглашения о стиле кодирования
#    Запустите код.

class d:
	def __init__(f, a=2):
		f.a = a
		
	def print_me(p):
		print(p.a)
		
d.print_me(d())

# 10. Исправьте
class A:
	def __init__(self, a):
		if 10 < a < 50:
			return
		self.a = a;	

# Объясните так реализовывать __init__ нельзя?
		
        
        
        
# 11. Циклическая зависимость (стр. 39-44)
# 

class Node:
    def __init__(self, prev=None, next_=None):
        self.__prev = prev
        self.__next = next_
    def set_next(self, next_):
        self.__next = next_

    def set_prev(self, prev):
        self.__prev = prev
        
    def __str__(self):
        ...
        
    def __repr__(self):
        ...

class LinkedList:



    def insert(self, node, index=0):
        '''
        Insert Node to any place of LinkedList
        node - Node
        index - position of node
        '''
        ...
        
       
    def append(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        ...

    def clear(self):
        '''
        Clear LinkedList
        '''
        ...

    def find(self, node):
        ...


    def remove(self, node):
        ...
        
    def delete(self, index):
        ...


if __name__ == '__main__':
    pass




















