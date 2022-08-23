from math import sqrt

import numpy as np
from PIL import Image

from input import start, stop, step
from paths import parent_directory, output_path

"""This class is used to generate the FizzBuzz Image from the data we collect"""


class GenerateImage:

    def __init__(self):
        self.data = []
        self.data_subset = []

    def read_data(self, index):
        with open(f"{output_path}\\FizzBuzz({index})_Output.txt", "r") as file:
            fizz_count = buzz_count = fizzbuzz_count = 0
            for line in file:
                if "Fizz Count" in line:
                    fizz_count = int(line.strip().split()[2])
                elif "Buzz Count" in line:
                    buzz_count = int(line.strip().split()[2])
                if "FizzBuzz Count" in line:
                    fizzbuzz_count = int(line.strip().split()[2])

        self.data.append(np.uint8((fizz_count + buzz_count + fizzbuzz_count) % 256 + (fizz_count + buzz_count)
                                  % (fizzbuzz_count + (fizz_count + buzz_count) % 256 + 1)) - fizzbuzz_count % 256)

    def generate_image(self):
        for index in range(start, stop, step):
            self.read_data(index)
        image = Image.new(mode="L", size=(int(sqrt(stop - 1)), int(sqrt(stop - 1))))
        image.putdata(self.data)
        image.show()
        image.save(f"{parent_directory}\\FizzBuzz.jpeg")


if __name__ == '__main__':
    generate_image = GenerateImage()
    generate_image.generate_image()
