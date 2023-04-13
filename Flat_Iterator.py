class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list


    def __iter__(self):
        self.cursor = 0
        self.list_iter = iter(self.list_of_list[self.cursor])
        return self

    def __next__(self):
        try:
            item = next(self.list_iter)
        except StopIteration:
            self.cursor += 1
            if self.cursor >= len(self.list_of_list):
                raise StopIteration
            self.list_iter = iter(self.list_of_list[self.cursor])
            item = next(self.list_iter)
        return item

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':

    list_of_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    Iterator = FlatIterator(list_of_list)
    for i in Iterator:
        print(i)

    test_1()