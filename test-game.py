def  play_game():
    print('Эта игра где тебе нужно найти банан')
    name = input("Напиши как тебя звать: \n")
    if len(name)>10:
        print('Ну и имечко!')
    money = 0
    clock = 3
    exit = False
    while not exit:
        print(name, "в спальне")
        standup = input('1-встать.\n2-лежать.\n3-медитировать.\n4-упасть\n')
        if standup == '1':
            print('Ты наступаешь на кота и он царапает твою ногу')
            return False
        elif standup == '2':
            print('Ты спишь дальше')
            return False
        elif standup == '4':
            print('Ты упал')
            return False
        elif standup == '3':
            print('медитируешь')
            while not exit:
                print(
                    name, "куда пойдешь дальше?",
                    'налево пойдешь-умрешь.направо пойдешь-в ловушку попадешь. в лес пойдещь-выйграешь. накухню пойдешь-в магазин попадешь.'
                )

                walk = input(
                    '1 - на кухню.\n2 - в подвал.\n3 - на балкон.\n4 - в ванну. \n5 - в канаву.\n')
                if walk == '1':
                    print('Ты пришел на кухню и на кухне тебя встретила мама с пирожками')
                    while True:
                        pies = input(
                            '1 - ты просишь у мамы пирожков.\n2 - ты просто садишься за стол и требуешь пирожков.\n3 - ты спрашиваешь с чем пирожки\n'
                        )
                        if pies == '1':
                            print(
                                'Мама отправляет тебя мыть руки и после этого накладывает пирожков тебе в тарелку.'
                            )
                            print('Ты все еще на кухне')
                        elif pies == '2':
                            print(
                                'Маму овладевает ужас, она злится и спрашивает тебя:\nА ты не офигел сына?'
                            )
                            return False
                        elif pies == '3':
                            print(
                                'Мама говорит, что они с капустой и ты корчишь не самую приятную рожу и выбегаешь на улицу')
                            exit = True
                            break
                        else:
                            print('Выбери правильный вариант!')
                elif walk == '2':
                    while not exit:
                        print('Ты в подвале. Перед тобой три двери.')
                        choose = input(
                            '1 - львы,которые не ели год.\n2 - киллер.\n3 - игра_младеньчик в желтом.\n')
                        if choose == '1':
                            print('game over')
                            return False
                        elif choose == '2':
                            print('lol')
                            return False
                        elif choose == '3':
                            print(
                                'haahahahha. YOU are winner. ты играешь в эту игру. вдруг все исчезает и ты оказываешься в магазине')
                            exit = True
                            break
                        else:
                            print('Выбери правильный вариант!')

                elif walk == '3':
                    while not exit:
                        print('перед тобой балкон очень в плачевном состоянии')
                        balcony = input('1 - пойти по безопасному пути.\n2 - встать на шаткую доску.\n')
                        if balcony == '1':
                            print('ты нашел старую заначку с бананом!')
                            return True
                        elif balcony == '2':
                            print('Ты упал')
                            return False
                        else:
                            print('Выбери правильный вариант!')

                elif walk == '4':
                    while not exit:
                        print("ты должен сделать пару вещей выбери их")
                        bathroom = input("1 - чистить зубы. \n2 - умыться\n")
                        if bathroom == "1":
                            print("после того как позавтрокаешь лучше ещё почистить зубы")
                        elif bathroom == "2":
                            print('время завтрака')
                            print('ты позавтракали и захотел банан, но дома его нет и ты пошёл в магазин')
                            exit = True
                            break
                elif walk == '5':
                    print('ты нашел камень и ты сломал голову и потерял много крови и умер...')
                    return False
                else:
                    print('Выбери праавильный вариант!')
        else:
            print('Выбери правильный вариант!')

    print("ты пришёл в магазин к тете Гале")
    print("ты видишь банан, но его хотят взять ты бежишь и берёшь его первым")
    return True

exit = False
while not exit:
    print('\n\nСыграем в игру?')
    choice = input('1 - да\n2 - нет\n')
    if choice == '1':
        result = play_game();
        if result:
            print("\nТы победил!!!!!!!!!!!!\n")
        else:
            print("\nТы проиграл! Looooser!!!!\n")
    elif choice == '2':
        exit = True
        print('Слабак!')
    else:
        print('Не понятно! Научись тыкать в клавиатуру!')

