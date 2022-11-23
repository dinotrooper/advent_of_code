from math import ceil

class DiagnosticReport:
    def __init__(self, puzzle_input="puzzle_input.txt"):
        self.values = []
        self._get_values(puzzle_input)

    def _get_values(self, file):
        with open(file, "r") as input:
            for line in input.readlines():
                line = line.strip()
                self.values.append(line)

    def get_life_support_rating(self):
        oxygen_rating = int(self._get_oxygen_rating(), 2)
        co2_rating = int(self._get_co2_rating(), 2)
        return oxygen_rating * co2_rating

    def _get_oxygen_rating(self):
        return self._get_oxygen_list(0, self.values)

    def _get_oxygen_list(self, index, old_list):
        if len(old_list) == 1:
            return old_list[0]
        new_list = []
        for value in old_list:
            if value[index] == self._get_oxygen_num(old_list, index):
                new_list.append(value)
        return self._get_oxygen_list(index + 1, new_list)

    def _get_oxygen_num(self, value_list, index):
        most_common = self._get_most_common_limit(value_list)
        num_ones = self._get_count_of_ones(value_list)[index]
        if int(num_ones) == int(most_common):
            return "1"
        return "1" if num_ones > most_common else "0"

    def _get_most_common_limit(self, value_list):
        return ceil(len(value_list) / 2)

    def _get_count_of_ones(self, value_list):
        val_len = len(value_list[0])
        count = [0] * val_len
        for line in value_list:
           for i, digit in enumerate(line):
               if  int(digit) == 1:
                   count[i] = count[i] + 1
        return count

    def _get_co2_rating(self):
        return self._get_co2_list(0, self.values)

    def _get_co2_list(self, index, old_list):
        if len(old_list) == 1:
            return old_list[0]
        new_list = []
        for value in old_list:
            if value[index] == self._get_co2_num(old_list, index):
                new_list.append(value)
        return self._get_co2_list(index + 1, new_list)

    def _get_co2_num(self, value_list, index):
        most_common = self._get_most_common_limit(value_list)
        num_ones = self._get_count_of_ones(value_list)[index]
        if num_ones == most_common:
            return "0"
        return "1" if num_ones < most_common else "0"

def main():
    dr = DiagnosticReport("test_input.txt")
    # Test get ones 
    test_oxygen_list = ["11110", "10110", "10111", "10101", "11100", "10000", "11001"]
    one_list = dr._get_count_of_ones(test_oxygen_list)
    assert one_list == [7, 3, 5, 3, 3]
    # Test get_oxygen_num
    test_oxygen_list = ["11110", "10110", "10111", "10101", "11100", "10000", "11001"]
    oxy_num = dr._get_oxygen_num(test_oxygen_list,  1)
    assert oxy_num == "0"
    dr_2 = DiagnosticReport()
    print(dr_2.get_life_support_rating())


if __name__ == "__main__":
    main()
