import choice

posts = ['post {}'.format(num) for num in range(15)]

resp = choice.Menu(posts, ['edit', 'delete', 'publish'], ['newpost', 'exit']).ask()
print(resp)

resp = choice.Input('Enter an integer', int).ask()
resp = choice.Input('Enter a string with "a" in it', choice.validate(lambda s: "a" in s)).ask()

resp = choice.Binary('Yes or no?', True).ask()
resp = choice.Binary('yes or No?', False).ask()
resp = choice.Binary('yes or no?').ask()
