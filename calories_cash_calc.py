"""
Модуль содержит классы: калькулятор калорий и калькулятор денежных средств.
"""
import datetime as dt


class Record():
    """Класс для создания записей калькуляторов."""

    today = dt.datetime.today().date()

    def __init__(self, amount: int, comment: str, date: 'date' = today):
        """Конструктор инициализирует количеcтво 'amount' (денежная сумма или
        количество килокалорий), дату создания записи 'date' (передается в
        явном виде в конструктор или присваивается значение по умолчанию -
        теущая дата), комментарий 'comment' (поясняет на что потрачены деньги
        или откуда взялись калории).
        """
        self.amount = amount
        self.comment = comment
        date_format = '%d.%m.%Y'
        if not isinstance(date, dt.date):
            self.date = dt.datetime.strptime(date, date_format).date()
        else:
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
        self.today = dt.datetime.today().date()

    def add_record(self, record: object):
        """Добавляет новую запись в список."""
        self.records.append(record)
        return f'Запись добавлена в список.'

    def get_today_stats(self):
        """Считает статистику за сегодня."""
        count = 0
        for record in self.records:
            if record.date != self.today:
                continue
            count += record.amount
        return count

    def get_week_stats(self):
        """Считает статистику за последние 7 дней."""
        count = 0
        for record in self.records:
            if self.today - dt.timedelta(days=6) <= record.date <= self.today:
                count += record.amount
        return count


class CaloriesCalculator(Calculator):
    """Класс реализует функционал калькулятора каллорий."""

    def __init__(self, limit: int):
        """Инициализация калькулятора калорий."""
        super().__init__(limit)

    def get_today_stats(self):
        """Считает сколько каллорий уже съедено сегодня."""
        count = super().get_today_stats()
        return f'За сегодня получено {count} калорий.'

    def get_calories_remained(self):
        """Определяет сколько еще калорий можно/нужно получить сегодня."""
        count = super().get_today_stats()
        if count < self.limit:
            balance = self.limit - count
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {balance} кКал')
        return f'Хватит есть!'

    def get_week_stats(self):
        """Считает сколько калорий получено за последние 7 дней."""
        count = super().get_week_stats()
        return f'За последние 7 дней получено {count} калорий.'


class CashCalculator(Calculator):
    """Класс реализует функционал калькулятора денежных средств."""

    def __init__(self, limit: int):
        """Инициализация калькулятора денежных средств."""
        super().__init__(limit)

    def get_today_stats(self):
        """Считает сколько сегодня потрачено денег."""
        count = super().get_today_stats()
        return f'За сегодня потрачено {count} денег.'

    def get_today_cash_remained(self, currency: str):
        """Определяет сколько еще денег сегодня можно потратить в рублях,
        долларах, евро.
         """
        pass

    def get_week_stats(self):
        """Считает сколько денег потрачено за последние 7 дней."""
        count = super().get_week_stats()
        return f'За последние 7 дней потрачено {count} денег.'
