





if __name__ == "__main__":
    import timeit
    import numpy
    from matrix_operations import get_diagonal as gd

    print(gd)
    timings = timeit.repeat('gd([[3,2,1],[2,3,1]])', number=50000, repeat=5)
    print(timings)
