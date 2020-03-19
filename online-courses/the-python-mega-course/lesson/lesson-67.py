
def mean_test(*args):
    return args

# print(mean(1, 3, 'a', 4)) -> returns tuple

def mean(*args):
    avg = sum(args) / len(args)
    return avg

print(mean(1, 2, 3, 4))