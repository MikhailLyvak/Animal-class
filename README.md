# Урок №8 Класи в деталях

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.

Не забудьте цього разу зробити `pip install -r requirements.txt` - цього разу є тести!

Ваша задача на сьогодні створити класс для тваринки яка вміє їсти, рухитись і для цього вона використовує калорії.
Отож, задача наступна:
Створити класс `Animal` який має приймати такі атрибути:
* `name` - Де ми будемо зберігати ім'я тваринки
* `current_fead` - Поточна ситість тваринки в форматі `int` 
* `max_fead` - Максимальна ситість тваринки в форматі `int` яка не може бути перевищена
* `speed` - Швидкість тварники у кілометрах у форматі `int`
* `loss_fead_per_km` - Кількість клорій(ситості), яку тварина втрачає за 1 кілометер у форматі `int`
* `position` - Поточна позиція тваринки у форматі `int`

    Наступна задача створити строкову репрезентація класса яка буде повертари
    `Cat Feed: 70/200 Speed: 20 Loss: 2 | Position: 0`
    Скопіюйте і вставте цей код для первірки вашого классу
```python
cat = Animal("Cat", 70, 200, 20, 2)
print(cat)

# Має повернути:  Cat Feed: 70/200 Speed: 20 Loss: 2 | Position: 0
```

Далі створимо метод `can_move_to` який буде приймати `distance` i `animal` і повертати `True` якщо тваринці вистачить калорій подолати цю дистанцію
і `False` якщо калорій не достатньо

Скопіюйте і вставте цей код для первірки вашого классу

```python
cat = Animal("Cat", 70, 200, 20, 2)
print(cat.can_move_to(10, cat)) # Має повернути: True
print(cat.can_move_to(100, cat)) # Має повернути: False
```
Наступний метод це `move_to` який буде приймати `distance` і викликати метод `can_move_to` який ми написали вище і якщо результатом `can_move_to` буде `True` 
то ми віднімаємо відповідну к-ть калорій і змінюємо положення тваринки, а якшо `False` то виводить в консоль `Not enough feed`.

Код який можете скопіювати і вставити для первірки

```python
cat = Animal("Cat", 70, 200, 20, 2)
print(cat)
cat.move_to(50)
print(cat)

print("====================================")

cat = Animal("Cat", 70, 200, 20, 2)
print(cat)
cat.move_to(10)
print(cat)

# Рузальтат має бути таким

# Cat Feed: 70/200 Speed: 20 Loss: 2 | Position: 0 
# Not enough feed  <- Повідомлення в консоль бо кіт немає достатньо калорій для такої подорожі
# Cat Feed: 70/200 Speed: 20 Loss: 2 | Position: 0  <- позиція і ситість не помінялись бо кіт немає достатньо калорій для такої подорожі
# ====================================
# Cat Feed: 70/200 Speed: 20 Loss: 2 | Position: 0 
# Cat Feed: 50/200 Speed: 20 Loss: 2 | Position: 10
```

Ну і останній метод `feed` який буде приймати `calories` і додавати їх до насичення тварини якщо к-ть калорій не перевищує ліміт `max_fead`, якщо ж ліміт буде перевищено ми нічього не робимо а виводимо в консоль 
`Too much feed`

Код який можете скопіювати і вставити для первірки

```python
cat = Animal("Cat", 70, 200, 20, 2)
print(cat)
cat.feed(50)
print(cat)

print("====================================")

cat = Animal("Cat", 70, 200, 20, 2)
print(cat)
cat.feed(200)
print(cat)

# Рузальтат має бути таким

# Cat Feed: 70/200 Speed: 20 Loss: 2 | Position: 0 
# Cat Feed: 120/200 Speed: 20 Loss: 2 | Position: 0 <- тут ми успішно накормили кота
# ====================================
# Cat Feed: 70/200 Speed: 20 Loss: 2 | Position: 0 
# Too much feed <- тут кіт не може стільки з'їсти тому виводимо таке повідомлення 
# Cat Feed: 70/200 Speed: 20 Loss: 2 | Position: 0  <- Насичення в такому випадку не помінялось

```

# Тепер твій код готовий!) Саме час його первірити, введи це в консоль щоб запустити тести і побачити чи все працює і чи треба щось пофіксити!

`pytest tests.py`
