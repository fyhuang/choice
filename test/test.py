import choices

posts = ['post {}'.format(num) for num in range(15)]

resp = choices.Menu(posts, ['edit', 'delete', 'publish'], ['newpost', 'exit']).ask()
print(resp)

resp = choices.Input('Enter an integer', int).ask()

resp = choices.Binary('Yes or no?', True).ask()
resp = choices.Binary('yes or No?', False).ask()
resp = choices.Binary('yes or no?').ask()
