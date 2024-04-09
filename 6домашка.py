result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("ValueError: a должно быть больше или равно b")
        if b == 0:
            raise ZeroDivisionError("ZeroDivisionError: деление на ноль")
        if b > 100:
            raise IndexError("IndexError: b должно быть меньше или равно 100")
        return a / b
    except ValueError as ve:
        print(ve)
    except IndexError as ie:
        print(ie)
    except ZeroDivisionError as zde:
        print(zde)
    except Exception as e:
        print("Произошла ошибка:", e)

data = {10: 2, 2: 5, "123": 4, 18: 0, 'some_key': 15, 8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)

print(result)