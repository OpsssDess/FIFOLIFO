# LIFO and FIFO
import json
with open('goods', mode="r") as file:
    stock = json.load(file)

print(stock)

while True:
    print('Вы хотите взять или положить?(put or take, quit)')
    answer = input('')
    if answer == 'put':
        print('Куда хотите положить свою вещь (LIFO или FIFO)?')
        answer = input('')
        thing = input('Что отдаёте? ')
        count = int(input("Сколько штук?"))
        if answer == 'LIFO':
            stock.append({"name": thing,  "amount": count})
            print(stock)
        else:
            stock.insert(0, {"name": thing,  "amount": count})
            print(stock)
    elif answer == 'quit':
        with open('goods', 'w', encoding='utf-8') as f:
            json.dump(stock, f)
        break
    else:
        if not stock:
            print('сейчас можно только положить!')
            continue
        else:
            b = stock[len(stock)-1]
            if b['amount'] == 1:
                stock.pop()
            else:
                b['amount'] -= 1
            print(f'Вы можете взять 1 штуку {b["name"]}')
            print(stock)
