import os
from paths import directory, parent_directory, output_path


class FizzBuzz:
    first_value = 3
    second_value = 5

    def __init__(self):
        self.values = None
        self.number = 0
        self.fizz_count = 0
        self.buzz_count = 0
        self.fizzbuzz_count = 0
        self.number_count = 0
        self.string_list_of_numbers = None
        self.int_list_of_numbers = None
        self.sum_of_numbers = 0

    def fizzbuzz(self, upper_limit: int, print_state: bool):

        self.number = upper_limit

        values = []
        for i in range(1, upper_limit + 1):
            current_value = ''
            if i % FizzBuzz.first_value == 0 or i % FizzBuzz.second_value == 0:
                if i % FizzBuzz.first_value == 0:
                    current_value += 'Fizz'
                if i % FizzBuzz.second_value == 0:
                    current_value += 'Buzz'
            else:
                current_value = str(i)
            values.append(current_value)

        self.values = values

    def calculate_output(self):
        self.fizz_count = self.values.count('Fizz')
        self.buzz_count = self.values.count('Buzz')
        self.fizzbuzz_count = self.values.count('FizzBuzz')
        self.number_count = self.number - self.fizz_count - self.buzz_count - self.fizzbuzz_count
        self.string_list_of_numbers = [value for value in self.values if value.isnumeric()]
        self.int_list_of_numbers = [int(value) for value in self.values if value.isnumeric()]
        self.sum_of_numbers = sum(self.int_list_of_numbers)

    def print_output(self):
        print(f'Values: {",".join(self.values)} \n'
              f'Fizz Count: {self.fizz_count} \n'
              f'Buzz Count: {self.buzz_count} \n'
              f'FizzBuzz Count: {self.fizzbuzz_count} \n'
              f'Number Count: {self.number_count} \n'
              f'List of numbers: {",".join(self.string_list_of_numbers)} \n'
              f'Sum of numbers: {self.sum_of_numbers} \n')

    def file_output(self):

        if os.path.isdir(output_path) is False:
            path = os.path.join(parent_directory, directory)
            os.mkdir(path)

        with open(f"{output_path}\\FizzBuzz({self.number})_Output.txt", "w") as file:
            file.write(f'Fizz Count: {self.fizz_count} \n'
                       f'Buzz Count: {self.buzz_count} \n'
                       f'FizzBuzz Count: {self.fizzbuzz_count} \n'
                       f'Number Count: {self.number_count} \n'
                       f'List of numbers: {",".join(self.string_list_of_numbers)} \n'
                       f'Sum of numbers: {self.sum_of_numbers} \n')
