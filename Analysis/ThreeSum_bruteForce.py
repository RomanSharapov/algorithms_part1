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
    3-Sum brute-force algorithm O(N^3)
    It seems that speed is T(N) = 2.5E-8 * N^3
    Given N distinct integers, how many triples sum to exactly zero?
    :param a: list of integers
    :return count: how many triples sum to exactly zero
    """
    N = len(a)
    count = 0

    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if a[i] + a[j] + a[k] == 0:
                    count += 1
    return count
