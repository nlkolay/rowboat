# Rowboat Simulation System 🚣

## О проекте

Это симулятор управления вёсельной лодкой с учетом факторов окружающей среды. Проект реализует:
- Моделирование физики движения лодки
- Учет влияния ветра и течения
- Управление веслами и направлением
- Автоматизированное тестирование

## Основные возможности

- 🚣 Реалистичное моделирование движения лодки
- 🌬️ Учет влияния ветра и течения
- ⚙️ Контроль угла погружения весел
- 📊 Получение текущего статуса лодки
- 🧪 Полный набор автоматизированных тестов

## Установка

Клонируйте репозиторий:
```bash
git clone https://github.com/nlkolay/rowboat.git
cd rowboat
```

## Использование 

Пример базового использования: 
```python
from boat import Rowboat, Oar, Environment

# Создание лодки с 4 веслами
oars = [Oar(2.5, "carbon") for _ in range(4)]
boat = Rowboat(oars, max_riders=4)

# Настройка окружения
env = Environment(
    wind_speed=3.0, 
    wind_direction=45,
    current_speed=1.0, 
    current_direction=180
)
boat.set_environment(env)

# Управление лодкой
boat.row(power=0.8, riders=2)
boat.steer(30)

# Получение статуса
status = boat.get_status()
print(status)
```