import re


def int_to_anybase(dec_num: int, base: int) -> list:
    """
    将十进制的数字对象转为任意进制，输出一个列表

    :param dec_num: 输入的十进制数
    :param base: 要转换的进制
    :return rt_list: 输出一个数组，表示转换后的数
    """

    rt_list = []

    while True:
        remainder = dec_num % base       # 除数
        rt_list.append(remainder)
        dec_num = dec_num // base        # 余数

        if dec_num == 0:
            break

    rt_list.reverse()
    return rt_list


def anybase_to_int(anybase_list: list, base: int) -> int:
    """
    还原由int_to_anybase函数转换的十进制数

    :param anybase_list: 任意进制的列表
    :param base: 进制
    :return dec_num: 还原的十进制数
    """

    anybase_r = anybase_list.copy()
    anybase_r.reverse()

    dec_num = 0
    b = 1
    for i in anybase_r:
        dec_num = dec_num + i*b
        b = b * base

    return dec_num


class ALTranslater:
    def __init__(self, words: list = None, encode: str = 'utf-8'):
        """

        :param words: list, like ['b', 'aa']
        :param encode: https://docs.python.org/zh-cn/3.8/library/codecs.html#standard-encodings
        """
        if words is None:
            words = ['b', 'aa']

        self.encode_type = encode
        self.words = [str(i) for i in words]

        self.__pre_treat()
        self.base = len(self.words)

        # Mapping relation
        self.map = [i for i in range(len(self.words))]

    def __pre_treat(self):
        """
        对输入的单词列表进行预处理，去掉重复的单词
        """
        self.words = list({}.fromkeys(self.words).keys())   # 去重
        self.words.sort(key=lambda x: len(x))               # 按照长度排序

        # todo: 判断是否为前缀编码，因为涉及到多字符

        if len(self.words) < 2:
            raise Exception("Words smaller than 2!")

    def set_words(self, words: list = None):
        self.__init__(words=words)

    def set_encode(self, encode: str = 'utf-8'):
        self.__init__(encode=encode)

    def encode(self, str_in: str) -> str:
        """
        加密

        :param str_in:
        :return encoded_str:
        """
        # 先转成byte
        str_byte = str_in.encode(self.encode_type)

        # todo: 压缩源数据
        # str_compressed_str = zlib.compress(str_byte)

        # byte转成int
        str_int = int.from_bytes(str_byte, byteorder='big')
        # str_int = int.from_bytes(str_compressed_str, byteorder='big')

        # int转成指定进制
        str_base_list = int_to_anybase(str_int, self.base)

        # 替换对应的word
        encoded_str = ''.join(self.words[i] for i in str_base_list)

        return encoded_str

    def decode(self, str_in: str) -> str:
        """
        解密

        :param str_in:
        :return decoded_str:
        """
        map_rvs = self.map.copy()
        map_rvs.reverse()

        str_base = [str_in]
        for i in map_rvs:
            for j in range(len(str_base)):
                if isinstance(str_base[j], int):
                    str_base[j] = [str_base[j]]
                else:
                    str_base[j] = [item for item in re.split(r'(%s)' % self.words[i], str_base[j]) if item]     # 去掉空字符串
                    str_base[j] = [i if item == self.words[i] else item for item in str_base[j]]                # 替换为数字
            str_base = [element for sublist in str_base for element in sublist]

        # len(words)进制转为10进制
        str_i = anybase_to_int(str_base, self.base)

        # int解码为字节序
        str_ec = int.to_bytes(str_i, length=len(str_base), byteorder='big').lstrip(b'\x00')
        decoded_str = str_ec.decode(self.encode_type)

        return decoded_str
