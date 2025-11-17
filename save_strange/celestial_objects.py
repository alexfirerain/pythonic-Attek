from astrowidja.model.heavens import Chart
from astrowidja.utils.celestial import coor, ZodiacPoint
from enum import Enum, unique
from typing import Set, Optional, Any


class Astra(ZodiacPoint):
    def __init__(self, name: str, zodiac_position: float, heaven: Chart | None = None):
        self._name = name
        self._heaven = heaven
        self._zodiac_position = coor(zodiac_position)

    @property
    def heaven(self):
        return self._heaven

    @property
    def zodiac_position(self):
        return self._zodiac_position


def of_same_heaven(a: Astra, b: Astra) -> bool:
    if a.heaven is None or b.heaven is None:
        return False
    else:
        return a.heaven == b.heaven


@unique
class AstraEntity(Enum):
    """
    Астросущности, используемые в Астровидье.
    Каждая сущность имеет:
    - имя (name)
    - символ (symbol)
    - набор альтернативных имён (also)
    """

    SOL = ("Солнце", '☉', "Sun", "Sol")
    LUN = ("Луна", '☽', "Moon")
    MER = ("Меркурий", '☿', "Mercury")
    VEN = ("Венера", '♀', "Venus")
    MAR = ("Марс", '♂', "Mars")
    CER = ("Церера", '⚳', "Ceres")
    JUP = ("Юпитер", '♃', "Jupiter")
    SAT = ("Сатурн", '♄', "Saturn")
    CHI = ("Хирон", '⚷', "Chiron")
    URA = ("Уран", '♅', "Uranus")
    NEP = ("Нептун", '♆', "Neptune")
    PLU = ("Плутон", '⯓', "Pluto")
    RAH = ("Раху", '☊', "Rahu")
    LIL = ("Лилит", '⚸', "Lilith")

    def __init__(self, name: str, symbol: str, *also: str):
        self.name = name
        self.symbol = symbol
        self.also: Set[str] = set(also)

    @classmethod
    def get_entity_by_name(cls, name: str) -> Optional['AstraEntity']:
        """
        Идентифицирует астросущность по имени.
        В качестве имени может быть использовано основное
        или любое из альтернативных имён, а также символ астры.
        @param name обозначение астры, по которому идентифицируется сущность.
        @return идентифицированная астросущность или None,
        если астросущность не идентифицирована
        """
        name = name.strip().lower()
        for entity in cls:
            if entity.name.lower() == name:
                return entity
            if any(alt.lower() == name for alt in entity.also):
                return entity
            if entity.symbol == name:
                return entity
        return None

    @classmethod
    def find_symbol_for(cls, name: str) -> str:
        """
        Находит и отдаёт символ, связанный с астросущностью,
        какое-то имя которой передано в аргументе и распознано.
        @param name имя, псевдоним или символ астры.
        @return символ астросущности, распознанной в астре, или '*', если не распознано.
        """
        entity = cls.get_entity_by_name(name)
        return entity.symbol if entity else '*'

    @classmethod
    def find_symbol_for_astra(cls, astra: Any) -> str:
        """
        Находит и отдаёт символ, связанный с астросущностью,
        найденной через имя астры, переданной в аргументе.
        @param astra астра, символ для которой определяется.
        @return char, соответствующий распознанной астре, или '*', если не распознано.
        """
        return cls.find_symbol_for(astra.getName())

    @classmethod
    def get_astra_entity_number(cls, astra: Any) -> int:
        """
        Находит для данной астры, под каким номером значится
        соответствующая астросущность, т.е. какой ордена имеет в перечислении.
        Это зависит от конкретной реализации класса AstraEntity.
        Сущность ищется по совпадению имени астры.
        Если имя не опознано, выдаётся следующий номер за наибольшим,
        т.е. равный размеру известных астросущностей.

        @param astra астра, чей номер в реестре смотрится.
        @return ординальный номер соответствующей астре сущности,
        если же такой не найдено, то количество сущностей в реестре.
        """
        entity = cls.get_entity_by_name(astra.getName())
        return entity.value[0] if entity else len(cls)