import re

def pass_startwith_alpha(i):
    return i[0].isalpha()


def pass_within_length(i,bottom,top):
    return len(i)<top and len(i)>bottom

def pass_without_upper(i):
    return i.islower()

def pass_startwith_digit(i):
    return i[0].isdigit()
