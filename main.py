# LIFO and FIFO

with open('goods', mode="r") as file:
    stack = [line.strip() for line in file]

while True:
    print('Вы хотите взять или положить?(put or take)')
    answer = input('')

    if answer == 'put':
        print('Куда хотите положить свою вещь (LIFO или FIFO)?')
        answer = input('')
        thing = input('Что отдаёте? ')
        if answer == 'LIFO':
            stack.append(thing)
            print(stack)
        else:
            stack.insert(0, thing)
            print(stack)

    else:
        if not stack:
            print('сейчас можно только положить!')
            continue
        print('Откуда Вам выдать вещь (LIFO или FIFO)?')
        answer = input('')
        if answer == 'LIFO':
            print(f'возьмите {stack.pop()}')
            print(stack)
        else:
            print(f'возьмите {stack.pop()}')
            print(stack)
