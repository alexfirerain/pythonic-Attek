from abc import ABC, abstractmethod
from enum import Enum, unique
from typing import Union, NamedTuple, Set, Optional, Any


CIRCLE = 360.0
HALF_CIRCLE = 180.0


class ZodiacPoint(ABC):
    @property
    @abstractmethod
    def zodiac_position(self) -> float:
        pass

    def __float__(self) -> float:
        """
        Возвращает зодиакальную позицию объекта в виде float.
        Позволяет использовать объект напрямую в математических выражениях.
        """
        return self.zodiac_position

    def __add__(self, other) -> float:
        """
        Сложение координат: self + other.
        Результат нормализуется как зодиакальная координата.
        """
        return coor(float(self) + float(other))

    def __radd__(self, other) -> float:
        """
        Обратное сложение: other + self.
        :param other: Другая точка в зодиакальном круге
         (float, ZodiacPoint или что-то преобразуемое в float).
        :return: Координата в зодиакальном круге, соответствующая сумме
        обратного сложения координат self + other
        """
        return self.__add__(other)

    def __sub__(self, other) -> float:
        """
        Вычитание координат: self - other.
        :param other:
        :return:
        """
        return coor(float(self) - float(other))

    def __rsub__(self, other) -> float:
        """
        Обратное вычитание: other - self.
        """
        return self.__sub__(other)


def coor(value: Union[float, int, str, ZodiacPoint]) -> float:
    """
    Преобразует значение в корректную зодиакальную координату от 0 до 360.

    :param value: Значение для преобразования: `float` или `int` берутся напрямую,
        строка пытается преобразоваться в число, а объект `ZodiacPoint` извлекает координату.
    :return: Зодиакальную координату в диапазоне [0, 360).
    :raises: ValueError если значение не может быть преобразовано в координату.
    """
    try:
        return float(value) % CIRCLE
    except ValueError | TypeError as e:
        raise TypeError(f"Невозможно использовать '{value}' ({type(value).__name__}) как координату") from e


class ZodiacPosition(NamedTuple):
    degrees: int
    minutes: int
    seconds: int

    @staticmethod
    def from_signed_coordinate(signed_position: 'SignedZodiacPosition') -> 'ZodiacPosition':
        return ZodiacPosition(
            (signed_position.sign - 1) * 30 + signed_position.degrees,
            signed_position.minutes,
            signed_position.seconds
        )

    def to_coordinate(self) -> float:
        return self.degrees + self.minutes / 60 + (self.seconds - 0.5) / 3600


class SignedZodiacPosition(NamedTuple):
    sign: int  # от 1 до 12
    degrees: int
    minutes: int
    seconds: int

    @staticmethod
    def from_unsigned_position(unsigned_position: 'ZodiacPosition') -> 'SignedZodiacPosition':
        return SignedZodiacPosition(
            (unsigned_position.degrees // 30) + 1,
            unsigned_position.degrees % 30,
            unsigned_position.minutes,
            unsigned_position.seconds
        )

    def to_coordinate(self) -> float:
        return self.sign * 30 + self.degrees + self.minutes / 60 + (self.seconds - 0.5) / 3600


class ZodiacSign(Enum):
    ARIES = '♈'
    TAURUS = '♉'
    GEMINI = '♊'
    CANCER = '♋'
    LEO = '♌'
    VIRGO = '♍'
    LIBRA = '♎'
    SCORPIO = '♏'
    SAGITTARIUS = '♐'
    CAPRICORN = '♑'
    AQUARIUS = '♒'
    PISCES = '♓'

    def __init__(self, symbol: str):
        self._symbol = symbol

    @property
    def symbol(self) -> str:
        return self._symbol

    @classmethod
    def get_zodium_of(cls, position: float | int | str | ZodiacPoint) -> "ZodiacSign":
        """
        Возвращает объект ZodiacSign, соответствующий знаку зодиака по заданной координате.

        :rtype: "ZodiacSign"
        :param position: Зодиакальная позиция (от 0 до 360 градусов)
        :return: Знак зодиака, соответствующий данной координате.
        """
        index = int(coor(position) // 30)
        return list(cls)[index]

    @classmethod
    def zodium_icon(cls, position: float | int | str | ZodiacPoint | ZodiacPosition | SignedZodiacPosition) -> str:
        """
        Возвращает символ знака зодиака по заданной координате.
        :param position: Зодиакальная позиция (от 0 до 360 градусов)
        :return: Символ знака зодиака.
        """
        if isinstance(position, ZodiacPosition):
            return list(cls)[position.degrees // 30].symbol
        elif isinstance(position, SignedZodiacPosition):
            return list(cls)[position.sign - 1].symbol
        return cls.get_zodium_of(position).symbol

    @classmethod
    def icon_for_zodium(cls, number: int) -> str:
        """
        Возвращает символ знака зодиака по его порядковому номеру.
        :rtype: str
        :param number: Номер знака зодиака (от 1 до 12, где 1 = Овен, 12 = Рыбы).
        :returns: Символ знака зодиака (например, '♍' для 6-го знака, Девы).
        :raises: ValueError: Если number не находится в диапазоне [1, 12].
                TypeError: Если number не является целым числом.

        >>> ZodiacSign.icon_for_zodium(1)
        '♈'
        >>> ZodiacSign.icon_for_zodium(12)
        '♓'
        """
        if 0 < number <= 12:
            return list(cls)[number - 1].symbol
        else:
            raise ValueError(f"Неверный номер знака зодиака: {number}")

