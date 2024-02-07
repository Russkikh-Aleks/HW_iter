import types


class FlatIterator_1:

    def __init__(self, list_of_list):
        self.list_iter = sum([list(el) for el in list_of_list], [])

    def __iter__(self):
        return self

    def __next__(self):
        if self.list_iter:
            return self.list_iter.pop(0)
        else:
            raise StopIteration


class FlatIterator_2:

    def __init__(self, list_of_list):
        self.list_iter = FlatIterator_2.create_list(list_of_list)

    @staticmethod
    def create_list(elements):
        result = []
        for el in elements:
            if not isinstance(el, list):
                result.append(el)
            else:
                result.extend(FlatIterator_2.create_list(el))
        return result

    def __iter__(self):
        return self

    def __next__(self):
        if self.list_iter:
            return self.list_iter.pop(0)
        else:
            raise StopIteration


def flat_generator(list_of_lists):

    for el in sum(list_of_lists, []):
        yield el


def flat_generator_2(list_of_list):
    for el in list_of_list:
        if isinstance(el, list):
            yield from flat_generator_2(el)
        else:
            yield el


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator_1(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator_1(list_of_lists_1)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator_2(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator_2(list_of_lists_2)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator_2(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator_2(list_of_lists_2)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator_2(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':

    test_1()
    test_2()
    test_3()
    test_4()
