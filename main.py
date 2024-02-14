calculator = (input("Ведите 2 числа(от 1 до 10) и знак арифметической операции между ними : П: 1+2 ").split())
calc = "".join(calculator)

def main(calk):
    if calc[1] == "+":
        return str(int(calc[0]) + int(calc[2]))
    elif calc[1] == "-":
        return str(int(calc[0]) - int(calc[2]))
    elif calc[1] == "*":
        return str(int(calc[0]) * int(calc[2]))
    elif calc[1] == "/":
        return str((int(calc[0]) // int(calc[2])))


try:
    calc[3]
    calc[0].isdigit() and int(calc[2:]) and calc[1] in "+-/*"
    0 < int(calc[0]) <= 10 and 0 < int(calc[2:]) <= 10

except IndexError:
    print("throws Exception //т.к. строка не является математической операцией")
except ValueError:
    print(
        "throws Exception //т.к. формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")
except Exception:
    print("throws Exception ")
else:
    print(main(calc))