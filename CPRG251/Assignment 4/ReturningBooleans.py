"""
Due to python weak typing, i was thinking how best to make sure that when a variable needs to be set by users input, what the safest way to do it?

The best way to do it is with bool()

bool because it accepts almost anything

String, int, floats, lists.

When bool is passed in true or false, it returns what was passed in.

When passed in a blank string,list or 0, it will return false

But if it has contents then it will return True

The goal isn't to babysit the user.

Its to make sure that our module doesn't explode.
"""

def boolReturn(argument):
    return bool(argument)