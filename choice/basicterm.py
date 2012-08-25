from __future__ import division, absolute_import, print_function, unicode_literals

import sys
if sys.version_info.major < 3:
    input = raw_input

from choice.util import idNameList

class BasicTermMenu(object):
    BACK_CHAR = 'b'
    PAGE_SIZE = 10

    """Basic menu using the console. No fancy terminal required. Supports paging of choices."""
    def __init__(self, choices, actions, global_actions, title):
        self.choices = idNameList(choices)
        self.actions = idNameList(actions)
        self.global_actions = idNameList(global_actions)
        self.title = title

    def pick_choice(self):
        curr_page = 0
        # Round up
        num_pages = (len(self.choices) + BasicTermMenu.PAGE_SIZE - 1) // BasicTermMenu.PAGE_SIZE

        print(self.title or "Make a choice:")
        while True:
            start = curr_page * BasicTermMenu.PAGE_SIZE
            end = start + BasicTermMenu.PAGE_SIZE
            for i, c in enumerate(self.choices[start:end]):
                print(" {}: {}".format(i, c[1]))
            if self.global_actions is not None:
                print()
                for ga in self.global_actions:
                    if ga[0] == ga[1]:
                        print("    {}".format(ga[0]))
                    else:
                        print(" {}: {}".format(ga[0], ga[1]))

            print("\nEnter number or name; return for next page")
            resp = input('? ').strip()
            print()
            if len(resp) == 0:
                curr_page += 1
                if curr_page >= num_pages:
                    curr_page = 0
            else:
                try:
                    resp_num = int(resp)
                    return resp_num + start
                except ValueError:
                    return str(resp)

    def pick_action(self):
        print("Select an action:")
        for i, ac in enumerate(self.actions):
            print(" {}: {}".format(i, ac[1]))
        print(" {}: back".format(BasicTermMenu.BACK_CHAR))
        resp = input('? ')
        print()
        return str(resp)

    def ask(self):
        """Returns (choice, action)"""
        choice = None
        while choice is None:
            resp = self.pick_choice()
            if isinstance(resp, int):
                if resp >= 0 and resp < len(self.choices):
                    choice = self.choices[resp]
                    break
            else:
                # Global action?
                for ga in self.global_actions:
                    if resp == ga[0]:
                        return None, ga[0]

                # Choice name?
                for c in self.choices:
                    if c[1] == resp:
                        choice = c
                        break

            if choice is None:
                print("{} is not a valid choice".format(resp))

        assert choice is not None
        if self.actions is None or len(self.actions) == 1:
            return choice[0]

        action = None
        while action is None:
            resp = self.pick_action()
            if resp == BasicTermMenu.BACK_CHAR:
                return self.ask()
            try:
                resp_num = int(resp)
                if resp_num >= 0 and resp_num < len(self.actions):
                    action = self.actions[resp_num]
                    break
            except ValueError:
                # Action name?
                if resp == 'back':
                    return self.ask()
                for ac in self.actions:
                    if ac[1] == resp:
                        action = ac
                        break
            if action is None:
                print("{} is not a valid choice".format(resp))

        assert action is not None
        return choice[0], action[0]


class BasicTermInput(object):
    def __init__(self, prompt, parser):
        self.prompt = prompt
        self.parser = parser

    def ask(self):
        resp = input('{}:\n? '.format(self.prompt))
        try:
            return self.parser(resp)
        except ValueError:
            print("Invalid value")
            return self.ask()


class BasicTermBinaryChoice(object):
    def __init__(self, prompt, default):
        self.prompt = prompt
        self.default = default

    def ask(self):
        if self.default is None:
            prompt = '{}\n(y/n)? '.format(self.prompt)
        elif self.default == True:
            prompt = '{}\n(Y/n)? '.format(self.prompt)
        elif self.default == False:
            prompt = '{}\n(y/N)? '.format(self.prompt)
        resp = input(prompt).lower().strip()

        if len(resp) == 0 and self.default is not None:
            return self.default
        if resp == 'y' or resp == 'yes' or resp == '1' or resp == 'true':
            return True
        elif resp == 'n' or resp == 'no' or resp == '0' or resp == 'false':
            return False
        else:
            print("Please answer 'y'es or 'n'o")
            return self.ask()

