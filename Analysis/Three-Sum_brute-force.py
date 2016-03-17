import time
# import cProfile
#
#
# def do_cprofile(func):
#     def profiled_func(*args, **kwargs):
#         profile = cProfile.Profile()
#         try:
#             profile.enable()
#             result = func(*args, **kwargs)
#             profile.disable()
#             return result
#         finally:
#             profile.print_stats()
#     return profiled_func


def three_sum(a):
    """
    3-Sum brute-force algorithm
    Given N distinct integers, how many triples sum to exactly zero?
    :param a: list of integers
    :return count: how many triples sum to exactly zero
    """
    N = len(a)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if a[i] + a[j] + a[k] == 0:
                    count += 1
    return count


def main(source):
    a = [int(i.strip()) for i in source if i]

    start = time.time()
    print(three_sum(a))
    print('Elapsed {} seconds'.format(time.time() - start))


if __name__ == "__main__":
    while True:
        choice = input('What do you want?\n'
                       '[1] Test\n'
                       '[2] Execute from cli\n'
                       '[3] Execute from file\n'
                       '[4] Quit\n'
                       'Choose: ')
        if choice == '1':
            main('30 -40 -20 -10 40 0 10 5'.split())
        elif choice == '2':
            main(input('Enter values delimited by spaces: ').split())
        elif choice == '3':
            main(open(input('Enter file name: ')).readlines())
        elif choice == '4':
            print('Bye')
            break
