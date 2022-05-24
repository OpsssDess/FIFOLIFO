# LIFO and FIFO


stack = {"LIFO": [], "FIFO": []}

while True:
    print('Вы хотите взять или положить?(put or take)')
    answer = input('')

    if answer == 'put':
        print('Куда хотите положить свою вещь (LIFO или FIFO)?')
        answer = input('')
        thing = input('Что отдаёте? ')
        if answer == 'LIFO':
            stack["LIFO"].append(thing)
            print(stack)
        else:
            stack["FIFO"].insert(0, thing)
            print(stack)

    else:
        if bool(stack["FIFO"]) is False and bool(stack["LIFO"]) is False:
            print('сейчас можно только положить!')
            continue
        print('Откуда Вам выдать вещь (LIFO или FIFO)?')
        answer = input('')
        if answer == 'LIFO':
            if bool(stack["LIFO"]) is False:
                print('LIFO пуст')
                continue
            else:
                print(f'возьмите {stack["LIFO"].pop()}')
                print(stack)
        else:
            if bool(stack["FIFO"]) is False:
                print('FIFO пуст')
                continue
            else:
                print(f'возьмите {stack["FIFO"].pop()}')
                print(stack)
