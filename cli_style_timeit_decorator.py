import gc
import timeit
import heapq
import functools
import statistics


def cli_timeit(original_f=None, *, number=1000):  # in Python 3, all arguments after * must be named

    if number < 3:
        raise TypeError('Argument number must be larger than 3.')

    def actual_decorator(f):

        @functools.wraps(f)  # preserve the function signature and docstring of the wrapped function
        def wrapper(*args, **kwargs):

            is_gc_enabled = gc.isenabled()
            gc.disable()

            try:
                best_of_3 = [float('-inf') for _ in range(3)]
                heapq.heapify(best_of_3)

                for _ in range(number):
                    start = timeit.default_timer()
                    result = f(*args, **kwargs)
                    end = timeit.default_timer()
                    execution_time = (end - start)
                    
                    heapq.heappushpop(best_of_3, (-1)*execution_time)  # max-heap, to keep the shortest three execution_time

                mean_best_of_3 = (-1)*statistics.mean(best_of_3)

                common_info = "{} loops, best of 3: ".format(number)
                if mean_best_of_3 >= 1:
                    print(common_info + "{:.3f} sec per loop".format(mean_best_of_3))
                elif mean_best_of_3 * 1000 >= 1:
                    print(common_info + "{:.3f} msec per loop".format(mean_best_of_3*1000))
                else:
                    print(common_info + "{:.3f} usec per loop".format(mean_best_of_3*1000000))

            finally:
                if is_gc_enabled:
                    gc.enable()

            return result

        return wrapper

    if original_f:  # scenario when the decorator used without args
        return actual_decorator(original_f)

    return actual_decorator  # scenario when the decorator used with args


if __name__ == "__main__":

    @cli_timeit
    def foo():
        return "-".join(map(str, range(100)))

    @cli_timeit(number=10000)
    def bar():
        return "-".join(map(str, range(100)))

    foo()
    bar()
