import pytest
from population_sort import read_data, sort_data

# Фікстура для тестування
@pytest.fixture
def sample_data():
    return [
        ("Ukraine", 603500, 41000000),
        ("Poland", 312696, 38300000),
        ("Germany", 357022, 83783942),
        ("France", 551695, 65273511),
    ]

# Тест для read_data
def test_read_data(tmp_path):
    # Створюємо тестовий файл
    test_file = tmp_path / "test_countries.txt"
    content = "Ukraine, 603500, 41000000\nPoland, 312696, 38300000\nGermany, 357022, 83783942\nFrance, 551695, 65273511\n"
    test_file.write_text(content)

    # Викликаємо функцію
    data = read_data(test_file)

    # Перевіряємо результат
    assert len(data) == 4
    assert data[0] == ("Ukraine", 603500.0, 41000000)
    assert data[1] == ("Poland", 312696.0, 38300000)

# Тест для sort_data
@pytest.mark.parametrize("index, expected", [
    (1, [("Ukraine", 603500, 41000000), ("France", 551695, 65273511), ("Germany", 357022, 83783942),("Poland", 312696, 38300000)]),  # Сортування за площею
    (2, [("Germany", 357022, 83783942), ("France", 551695, 65273511), ("Ukraine", 603500, 41000000),("Poland", 312696, 38300000), ]),  # Сортування за населенням
])
def test_sort_data(sample_data, index, expected):
    sorted_data = sort_data(sample_data, index)
    assert sorted_data == expected
