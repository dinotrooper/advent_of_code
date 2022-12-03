from unittest import TestCase
import main

class TestMain(TestCase):
    def setUp(self):
        self.text = "test_input.txt"
        self.puzzle_input = main.get_puzzle_input(self.text)
        return super().setUp()

    def test_sum_prio(self):
        assert main.sum_prio(self.text) == 70

    def test_sacks(self):
        sacks = main.get_sacks(self.puzzle_input)
        assert len(sacks) == 6
        first, second = main.get_compartments_of_sack(sacks[0])
        assert first == "vJrwpWtwJgWr"
        assert second == "hcsFMMfFFhFp"

    def test_get_common_item_in_sack(self):
        sack = ("vJrwpWtwJgWr", "hcsFMMfFFhFp")
        assert main.get_common_item_in_compartments(sack) == 'p'

    def test_get_prio_of_item(self):
        assert main.get_prio_of_item('p') == 16
        assert main.get_prio_of_item('L') == 38
        assert main.get_prio_of_item('P') == 42
        assert main.get_prio_of_item('v') == 22
        assert main.get_prio_of_item('t') == 20
        assert main.get_prio_of_item('s') == 19

    def test_get_common_item_in_three_sacks(self):
        sacks = main.get_sacks(self.puzzle_input)
        first = sacks[0:3]
        second = sacks[3:]
        assert main.get_common_item_in_three_sacks(first) == "r"
        assert main.get_common_item_in_three_sacks(second) == "Z"

    def test_group_up_sacks(self):
        sacks = main.get_sacks(self.puzzle_input)
        first, second = main.group_up_sacks(sacks)
        assert len(first) == 3
        assert first == [x.strip() for x in self.puzzle_input[:3]]
        assert second == [x.strip() for x in self.puzzle_input[3:]]
