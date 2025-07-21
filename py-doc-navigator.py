target = 0

while target != -1:
    print("Enter [a] for available modules, [l] for loaded modules, or [-1] to quit")
    raw_target = input('> ')
    if raw_target in ['a', 'A']:
        print('Available modules:')
        print(help('modules'))
    elif raw_target in ['l', 'L']:
        loaded_modules = dir()
        loaded_modules_index = list(range(len(loaded_modules)))
        print('Loaded modules:')
        print(dict(zip(loaded_modules_index, loaded_modules)))
    elif raw_target == '-1':
        target = int(raw_target)
        print('Exiting...')
    else:
        print(f'The input >{raw_target}< was not recognised.')