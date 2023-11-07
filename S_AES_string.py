def yihuo(str, key):
    result = ''.join(['0' if s == k else '1' for s, k in zip(str, key)])
    return result


class S_AES_string:
    def __init__(self, key):
        self.key = key
        self.w0 = []
        self.w1 = []
        self.w2 = []
        self.w3 = []
        self.w4 = []
        self.w5 = []
        # S盒
        self.sbox = [["1001", "0100", "1010", "1011"],
                     ["1101", "0001", "1000", "0101"],
                     ["0110", "0010", "0000", "0011"],
                     ["1100", "1110", "1111", "0111"]]
        # 逆S盒
        self.I_sbox = [["1010", "0101", "1001", "1011"],
                       ["0001", "0111", "1000", "1111"],
                       ["0110", "0000", "0010", "0011"],
                       ["1100", "0100", "1101", "1110"]]
        # 轮常量
        self.Rcon = ['10000000', '00110000']
        self.key_tuozhan()

    # 密钥扩展
    def key_tuozhan(self):
        self.w0 = self.key[0:8]
        self.w1 = self.key[8:16]
        self.w2 = yihuo(self.w0, self.g(self.w1, 1))
        # print(self.w2)
        self.w3 = yihuo(self.w1, self.w2)
        # print(self.w1, self.w2, self.w3, self.w4, self.w5)
        self.w4 = yihuo(self.w2, self.g(self.w3, 2))
        self.w5 = yihuo(self.w4, self.w3)

    # 轮密钥加
    def g(self, w, n):
        # 先替换再异或
        N_ = self.S_he_tihuan(w[4:8], 1) + self.S_he_tihuan(w[0:4], 1)
        W_ = yihuo(N_, self.Rcon[n - 1])
        return W_

    # S_box替换
    def S_he_tihuan(self, N, n):
        n0 = N[0:2]
        n1 = N[2:4]
        if n == 1:
            return self.sbox[int(n0, 2)][int(n1, 2)]
        else:
            return self.I_sbox[int(n0, 2)][int(n1, 2)]

    # 半字节替换
    def tihuan(self, str, n):
        str_sub = ''
        for i in range(4):
            str_s = self.S_he_tihuan(str[i * 4:4 * i + 4], n)
            str_sub += str_s
        return str_sub

    # 行移位
    def hang_yiwei(self, str):
        return str[0:4] + str[12:16] + str[8:12] + str[4:8]

    # 列混淆
    def lie_hunxiao(self, str, n):
        s_ = ""
        if n == 1:
            for i in range(4):
                if i % 2:  # 单数1，3
                    s0_i = yihuo(str[i * 4:4 * (i + 1)], self.chenfa(str[(i - 1) * 4:4 * i], 4))
                else:
                    s0_i = yihuo(str[i * 4:4 * (i + 1)], self.chenfa(str[(i + 1) * 4:4 * (i + 2)], 4))
                s_ += s0_i
        elif n == 2:
            for i in range(4):
                if i % 2:  # 单数1，3
                    s0_i = yihuo(self.chenfa(str[(i - 1) * 4:4 * i], 2), self.chenfa(str[i * 4:4 * (i + 1)], 9))
                else:
                    s0_i = yihuo(self.chenfa(str[i * 4:4 * (i + 1)], 9), self.chenfa(str[(i + 1) * 4:4 * (i + 2)], 2))
                s_ += s0_i
        return s_

    # 乘法
    def chenfa(self, str, n):
        self.chenfa_he = {
            2: [0, 2, 4, 6, 8, 10, 12, 14, 3, 1, 7, 5, 11, 9, 15, 13],
            4: [0, 4, 8, 12, 3, 7, 11, 15, 6, 2, 14, 10, 5, 1, 13, 9],
            9: [0, 9, 1, 8, 2, 11, 3, 10, 4, 13, 5, 12, 6, 15, 7, 14]
        }
        int_str = int(str, 2)
        result = '{0:0{1}b}'.format(self.chenfa_he.get(n, [0] * 16)[int_str], 4)
        return result

    # 加密
    def jiami(self, p):
        miwen = ''
        for i in range(len(p) // 2):
            p_text = p[i * 2: (i + 1) * 2]
            p_text = self.ascii_to_binary(p_text[0]) + self.ascii_to_binary(p_text[1])
            p_text = yihuo(p_text, self.w0 + self.w1)  # 轮秘钥加
            # 第一轮
            p_text = self.tihuan(p_text, 1)  # 半字节替代
            p_text = self.hang_yiwei(p_text)  # 行移位
            p_text = self.lie_hunxiao(p_text, 1)  # 列混淆
            p_text = yihuo(p_text, self.w2 + self.w3)  # 轮秘钥加
            # 第二轮
            p_text = self.tihuan(p_text, 1)  # 半字节替代
            p_text = self.hang_yiwei(p_text)  # 行移位
            ciphertext0 = yihuo(p_text, self.w4 + self.w5)  # 轮秘钥加
            miwen += self.binary_to_ascii(ciphertext0[0:8]) + self.binary_to_ascii(ciphertext0[8:16])
        print("密文为: " + str(miwen))
        return miwen

    # 解密
    def jiemi(self, text):
        mingwen = ''
        for i in range(len(text) // 2):
            ciphertext = text[i * 2: (i + 1) * 2]
            ciphertext = self.ascii_to_binary(ciphertext[0]) + self.ascii_to_binary(ciphertext[1])
            # 轮秘钥加
            ciphertext = yihuo(ciphertext, self.w4 + self.w5)
            # 行移位
            ciphertext = self.hang_yiwei(ciphertext)
            # 半字节替代
            ciphertext = self.tihuan(ciphertext, 2)
            # 轮秘钥加
            ciphertext = yihuo(ciphertext, self.w2 + self.w3)
            # 列混淆
            ciphertext = self.lie_hunxiao(ciphertext, 2)
            # 行移位
            ciphertext = self.hang_yiwei(ciphertext)
            # 半字节替代
            ciphertext = self.tihuan(ciphertext, 2)
            # 轮秘钥加
            Plainttext0 = yihuo(ciphertext, self.w0 + self.w1)
            mingwen += self.binary_to_ascii(Plainttext0[0:8]) + self.binary_to_ascii(Plainttext0[8:16])
        print("明文为: " + mingwen)
        return mingwen

    def binary_to_ascii(self, binary_str):
        num = int(binary_str, 2)
        ch = chr(num)
        return ch

    def ascii_to_binary(self, ascii_str):
        num = ord(ascii_str)
        binary = bin(num)[2:].zfill(8)
        return binary


def use(text, key):
    s_aes = S_AES_string(key)
    # 输入明文分组为2 Bytes
    enc = s_aes.jiami(text)
    det = s_aes.jiemi(enc)
    return enc, det