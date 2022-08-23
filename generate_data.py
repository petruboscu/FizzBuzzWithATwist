import threading

from fizzbuzz import FizzBuzz
from input import start, stop, step, cores

"""This class is used to generate the FizzBuzz files that we want to analyze to create the image"""


class GenerateData:

    def __init__(self):
        pass

    @staticmethod
    def fizzbuzz_count(upper_limit: int, print_state=False):
        count = FizzBuzz()
        count.fizzbuzz(upper_limit, print_state)
        count.calculate_output()
        if print_state:
            count.print_output()
        count.file_output()

    def generate_data(self):
        threads = []

        for limit in range(start, stop, step):
            # True should be added to the argument list if printing is needed
            threads.append(threading.Thread(target=self.fizzbuzz_count, args=(limit,)))
            if limit != 0 and limit % cores == 0:
                for thread in threads:
                    thread.start()
                    thread.join()
                threads = []


if __name__ == '__main__':
    generate_data = GenerateData()
    generate_data.generate_data()
