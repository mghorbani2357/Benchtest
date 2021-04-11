import cProfile
import pstats

from ._version import get_versions

__version__ = get_versions()['version']
del get_versions


class BenchMark:
    report = dict()
    functions = list()

    def __init__(self):
        self.__test()

    def __test(self):
        method_list = list()

        for function in dir(self):
            if callable(getattr(self, function)) and function.startswith('test'):
                method_list.append(getattr(self, function))

        for function in method_list:
            pr = cProfile.Profile()
            pr.enable()

            function()

            pr.disable()

            print(function.__name__ + ':')

            ps = pstats.Stats(pr).sort_stats('tottime')
            ps.print_stats()
