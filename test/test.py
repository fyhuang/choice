import choices

posts = ['post {}'.format(num) for num in range(15)]

resp = choices.Menu(posts, ['edit', 'delete', 'publish'], ['newpost', 'exit']).ask()
print(resp)

resp = choices.Input('Enter an integer', int).ask()
