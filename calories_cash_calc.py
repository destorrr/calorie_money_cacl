"""
Модуль содержит классы: калькулятор калорий и калькулятор денежных средств.
"""


class Record():
    """Класс для создания записей калькуляторов."""

    def __init__(self, amount: int, comment: str, date: 'date'):
        """Конструктор инициализирует количеcтво 'amount' (денежная сумма или
        количество килокалорий), дату создания записи 'date' (передается в
        явном виде в конструктор или присваивается значение по умолчанию -
        теущая дата), комментарий 'comment' (поясняет на что потрачены деньги
        или откуда взялись калории).
        """
        self.amount = amount
        self.comment = comment
        self.date = date


class Calculator():
    """Содержит общую функциональность калькуляторов: хранение записей,
    фиксирование дненого лимита, суммирование записей за конкретные даты.
    """

    def __init__(self, limit: int):
        """Инициализация общего калькулятора.
        """
        self.limit = limit
        self.records = []

    def add_record(self, record: object):
        """Добавляет новую запись в список."""
        self.records.append(record)
        return f'Запись добавлена в список.'

    def get_today_stats(self):
        """Считает статистику за сегодня."""
        pass

    def get_week_stats(self):
        """Считает статистику за последние 7 дней."""
        pass


class CaloriesCalculator(Calculator):
    """Класс реализует функционал калькулятора каллорий."""

    def __init__(self, limit: int):
        """Инициализация калькулятора калорий."""
        super().__init__(limit)

    def get_today_stats(self):
        """Считает сколько каллорий уже съедено сегодня."""
        pass

    def get_calories_remained(self):
        """Определяет сколько еще калорий можно/нужно получить сегодня."""
        pass

    def get_week_stats(self):
        """Считает сколько калорий получено за последние 7 дней."""
        pass


class CashCalculator(Calculator):
    """Класс реализует функционал калькулятора денежных средств."""

    def __init__(self, limit: int):
        """Инициализация калькулятора денежных средств."""
        super().__init__(limit)

    def get_today_stats(self):
        """Считает сколько сегодня потрачено денег."""
        pass

    def get_today_cash_remained(self, currency: str):
        """Определяет сколько еще денег сегодня можно потратить в рублях,
        долларах, евро.
         """
        pass

    def get_week_stats(self):
        """Считает сколько денег потрачено за последние 7 дней."""
        pass
