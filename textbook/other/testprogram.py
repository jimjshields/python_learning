game_input = raw_input('Let\'s play a game! Y/N/Maybe\n')

answers = {'Y': 'Great! Let\'s get started.', 'N': 'That\'s too bad - you are a sad, strange little person.', 'Maybe': 
'Pays to be decisive, good luck deciding what you want to be in life.'}

def play_game(g):
    if g == 'Y':
        nums = [n for n in range(1, 1001)]
        num_input = int(raw_input('Pick a number between 1 and 1000.\n'))
        if num_input in nums:
            print 'Cool beans! Ok, your number is ' + str(num_input) + '.'
        else:
            print 'Nice try. Pick again.'
            play_game(g)
            

if game_input in answers:
    print answers[game_input]

    play_game(game_input)
    
else:
    print 'Outside the box - I like it. You get to play the better game.'