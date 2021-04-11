# # # from benchtest.benchmark import BenchMark
# #
# # benchmark = BenchMark()
# #
# #
# # def data_generator():
# #     return [None] * 10 ** 6
# #
# #
# # lst = data_generator()
# #
# #
# # @benchmark.bench_test('test')
# # def bench_test_list():
# #     k = 'a' in lst
# #
# #
# # benchmark.generate_report()
#
# import cProfile
# import pstats
# import profile
#
# # pr = profile.Profile(your_time_func)
lst = [None] * 10 ** 6
#
#
# def search_list():
#     k = 'a' in lst
#
#
# def bench_test_list():
#     for i in range(100):
#         search_list()
#
#
# pr = cProfile.Profile()
# pr.enable()
#
#
# bench_test_list()
#
# pr.disable()
#
# ps = pstats.Stats(pr).sort_stats('tottime')
# ps.print_stats()
#
#
# # import profile
# # pr = profile.Profile()
# # for i in range(5):
# #     print(pr.calibrate(10000))

from benchtest import BenchMark

lst = [None] * 10 ** 6


def search_list():
    k = 'a' in lst


class BenchTestListSearch(BenchMark):
    def test_list_search(self):
        for i in range(100):
            search_list()


BenchTestListSearch()
