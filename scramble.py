
# Scramble-function
def scrambled(orig):
    import random
    dest = orig[:]
    random.shuffle(dest)
    return dest