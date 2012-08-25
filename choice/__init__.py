from __future__ import division, absolute_import, print_function, unicode_literals

from choice.basicterm import *


# TODO: progressive enhancement
_MenuType = BasicTermMenu
_InputType = BasicTermInput
_BinaryChoiceType = BasicTermBinaryChoice

def Menu(choices, actions, global_actions=None, title=None):
    return _MenuType(choices, actions, global_actions, title)
def Input(prompt, parser=str):
    return _InputType(prompt, parser)
def Binary(prompt, default=None):
    return _BinaryChoiceType(prompt, default)
