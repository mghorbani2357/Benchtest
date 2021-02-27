from functools import wraps
import time
import json


class BenchMark:
    report = dict()

    def __init__(self):
        pass

    def generate_report(self):
        print(json.dumps(self.report))

    def bench_test(self, name, iterations=100, input_generator=None):
        def decorator(function):
            beginning_time = time.time()
            for i in range(iterations):
                function()
            # if name == '':
            name = function.__name__
            self.report[name] = (time.time() - beginning_time) / iterations

        return decorator
