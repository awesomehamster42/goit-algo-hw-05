import sys
from pathlib import Path

def parse_log_line(line: str) -> dict:    # Приймаємо рядок і повертаємо словник з розібраними частинами
    parts = line.strip().split(' ', 3)
    return (
        {
            'date': parts[0],
            'time': parts[1],
            'level': parts[2],
            'message': parts[3]
        } if len(parts) == 4 else
        {
            'date': '',
            'time': '',
            'level': 'UNKNOWN',
            'message': line.strip()
        }
    )

def load_logs(file_path: str) -> list:    # Завантаження лог-файлу і повернення списку словників
    path = Path(file_path)
    if not path.exists():
        print(f"Файл не знайдено: {file_path}")
        sys.exit(1)

    try:
        with path.open('r') as file:
            return [parse_log_line(line) for line in file if line.strip()]
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)

def filter_logs_by_level(logs: list, level: str) -> list:    # Фільтруємо за рівнем логування
    return list(filter(lambda log: log['level'].upper() == level.upper(), logs))

def count_logs_by_level(logs: list) -> dict:    # Підрахунок записів за рівнем логування
    levels = set(log['level'].upper() for log in logs)
    return {lvl: len(list(filter(lambda log: log['level'].upper() == lvl, logs))) for lvl in levels}

def display_log_counts(counts: dict):    # Форматування і вивід в читабельній формі
    print("-" * 35)
    print(f"{'Рівень логування':<10} | {'Кількість':>10}")
    print("-" * 35)
    for level in sorted(counts):
        print(f"{level:<10}       | {counts[level]:>2}")
    print("-" * 35)

def display_filtered_logs(logs: list, level: str):    # Вивід логів певного рівня
    filtered = filter_logs_by_level(logs, level)
    if not filtered:
        print(f"Немає записів рівня '{level}'.")
        return
    print(f"\n Деталі логів для рівня {level.upper()}:")
    [print(f"{log['date']} {log['time']} {log['level']} {log['message']}") for log in filtered]

def main():
    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)

    if level:
        display_filtered_logs(logs, level)
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

if __name__ == "__main__":
    main()