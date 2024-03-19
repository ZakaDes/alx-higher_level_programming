#!/usr/bin/python3
def multiple_returns(sentence):
    mtpl = ()
    if len(sentence) == 0:
        mtpl, None
    else:
        mtpl = len(sentence), sentence[0]
    return (mtpl)
