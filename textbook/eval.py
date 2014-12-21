import math

def eval_loop():
    while True:
        user_input = raw_input('Enter an equation to evaluate:')
        if user_input == 'Done':
            break
        print eval(user_input)

    print eval(user_input)

eval_loop()