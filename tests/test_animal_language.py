from animal_language import __version__
from animal_language import ALTranslater


def test_version():
    assert __version__ == '0.1.0'


def test_encode_and_decode_1():
    test_str = 'hello, i am very excited to use it for fun.'
    test_list = ['m', 'e', 'a', 'oo']
    translater = ALTranslater(test_list)
    encoded = translater.encode(test_str)
    decoded = translater.decode(encoded)
    assert decoded == test_str


def test_encode_and_decode_2():
    test_str = '自定义一个词语集合，然后用这个集合中的词语表示任意一句话。'
    test_list = ['喵', '汪', '哞', '咩', '呱', '嗷呜', '叽', '嘎', '👽']
    translater = ALTranslater(test_list, 'gbk')
    encoded = translater.encode(test_str)
    decoded = translater.decode(encoded)
    assert decoded == test_str
