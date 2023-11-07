#异或
def yihuo(str, key):
    result = ''.join(['0' if s == k else '1' for s, k in zip(str, key)])
    return result



class S_AES:
    def __init__(self, key):
        self.key = key
        self.w0 = []
        self.w1 = []
        self.w2 = []
        self.w3 = []
        self.w4 = []
        self.w5 = []
        # S盒
        self.s_he = [["1001", "0100", "1010", "1011"],
                     ["1101", "0001", "1000", "0101"],
                     ["0110", "0010", "0000", "0011"],
                     ["1100", "1110", "1111", "0111"]]
        # 逆S盒
        self.ni_s_he = [["1010", "0101", "1001", "1011"],
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
        self.w3 = yihuo(self.w1, self.w2)
        self.w4 = yihuo(self.w2, self.g(self.w3, 2))
        self.w5 = yihuo(self.w4, self.w3)

    #乘法
    def chenfa(self, str, n):
        self.chenfa_he = {
            2: [0, 2, 4, 6, 8, 10, 12, 14, 3, 1, 7, 5, 11, 9, 15, 13],
            4: [0, 4, 8, 12, 3, 7, 11, 15, 6, 2, 14, 10, 5, 1, 13, 9],
            9: [0, 9, 1, 8, 2, 11, 3, 10, 4, 13, 5, 12, 6, 15, 7, 14]
        }
        int_str = int(str, 2)
        result = '{0:0{1}b}'.format(self.chenfa_he.get(n, [0] * 16)[int_str], 4)
        return result


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
            return self.s_he[int(n0, 2)][int(n1, 2)]
        else:
            return self.ni_s_he[int(n0, 2)][int(n1, 2)]

    # 半字节替换
    def tihuan(self, str, n):
        str_sub = ''
        for i in range(4):
            str_s = self.S_he_tihuan(str[i * 4:4 * i + 4], n)
            str_sub += str_s
        return str_sub



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


    # 行移位
    def hang_yiwei(self, str):
        return str[0:4] + str[12:16] + str[8:12] + str[4:8]


    # 加密
    def jiami(self, p):
        self.p = p
        mingwen = yihuo(self.p, self.w0 + self.w1)  # 轮秘钥加
        # 第一轮
        mingwen = self.tihuan(mingwen, 1)  # 半字节替代
        mingwen = self.hang_yiwei(mingwen)  # 行移位
        mingwen = self.lie_hunxiao(mingwen, 1)  # 列混淆
        mingwen = yihuo(mingwen, self.w2 + self.w3)  # 轮秘钥加
        # 第二轮
        mingwen = self.tihuan(mingwen, 1)  # 半字节替代
        mingwen = self.hang_yiwei(mingwen)  # 行移位
        miwen = yihuo(mingwen, self.w4 + self.w5)  # 轮秘钥加
        # print("密文为: " + str(ciphertext))
        return miwen

    # 解密
    def jiemi(self, text):
        miwen = text
        # 轮秘钥加
        miwen = yihuo(miwen, self.w4 + self.w5)
        # 行移位
        miwen = self.hang_yiwei(miwen)
        # 半字节替代
        miwen = self.tihuan(miwen, 2)
        # 轮秘钥加
        miwen = yihuo(miwen, self.w2 + self.w3)
        # 列混淆
        miwen = self.lie_hunxiao(miwen, 2)
        # 行移位
        miwen = self.hang_yiwei(miwen)
        # 半字节替代
        miwen = self.tihuan(miwen, 2)
        # 轮秘钥加
        mingwen = yihuo(miwen, self.w0 + self.w1)

        # print("明文为: " + Plainttext)
        return mingwen

#单重加密
def single_use_jiami(text, key):
    s_aes = S_AES(key)
    enc = s_aes.jiami(text)
    return enc

def single_use_jiemi(text, key):
    s_aes = S_AES(key)
    det = s_aes.jiemi(text)
    return det

# 双重加密
def dou_use_jiami(text, key):
    s_aes1 = S_AES(key[0:16])
    s_aes2 = S_AES(key[16:32])
    midc = s_aes1.jiami(text)
    enc = s_aes2.jiami(midc)
    return enc

def dou_use_jiemi(text, key):
    s_aes1 = S_AES(key[0:16])
    s_aes2 = S_AES(key[16:32])
    midt = s_aes2.jiemi(text)
    det = s_aes1.jiemi(midt)
    return det

#三重加密
def tri_use_jiami(text, key):
    k1 = key[:16]
    k2 = key[16:32]
    k3 = key[32:48]
    aes1 = S_AES(k1)
    aes2 = S_AES(k2)
    aes3 = S_AES(k3)
    r1 = aes1.jiami(text)
    r2 = aes2.jiemi(r1)
    r3 = aes3.jiami(r2)
    return r3

def tri_use_jiemi(text, key):
    k1 = key[:16]
    k2 = key[16:32]
    k3 = key[32:48]
    aes1 = S_AES(k1)
    aes2 = S_AES(k2)
    aes3 = S_AES(k3)
    d1 = aes3.jiemi(text)
    d2 = aes2.jiami(d1)
    d3 = aes1.jiemi(d2)
    return d3

#CBC模式
def CBC_en(text, key):
    k0 = '0110010111011011'  # 初始向量
    k1 = '0'
    R = '0'
    for i in range(int(len(text) / 16)):
        p0 = text[i * 16:(i + 1) * 16]  # 更新当前分组的明文p0
        p1 = yihuo(p0, k0)  # 与k0进行异或操作，使用函数xor，获得p1
        k1 = key[i * 16:(i + 1) * 16]  # 更新当前分组的密钥k1
        key1 = S_AES(k1)
        r = S_AES.jiami(key1, p1)  # k1为密钥，p1为明文进行S-AES加密
        k0 = r
        R = R + r  # 连接密文
    Result = R[1:len(text) + 1]
    print("CBC模式下的S-AES加密结果：", Result)
    return Result


def CBC_de(text, key):
    k0 = '0110010111011011'  # 初始向量
    k1 = '0'
    R = '0'
    for i in range(int(len(text) / 16)):
        p0 = text[i * 16:(i + 1) * 16]  # 更新当前分组的密文p0
        k1 = key[i * 16:(i + 1) * 16]  # 更新当前分组的密钥k1
        key1 = S_AES(k1)
        r = S_AES.jiemi(key1, p0)  # k1为密钥，p1为密文进行S-AES解密
        p1 = yihuo(r, k0)  # 与k0进行异或操作，使用函数xor，获得p1
        k0 = p0
        R = R + p1  # 连接密文
    Result = R[1:len(text) + 1]
    print("CBC模式下的S-AES解密结果：", Result)
    return Result


def CBC(text, k):
    # CBC对比篡改密文前后的解密结果

    return CBC_en(text, k), CBC_de(CBC_en(text,k), k)

# CBC对比篡改密文前后的解密结果
'''k='001100110011001100110011001100110011001100110011'
p_CBC='110011001100110011001100110011001100110011001100'
print("明文为：",p_CBC,"\n密钥为：",k)
m=CBC_en(p_CBC,k)
print("对密文进行解密")
m0=CBC_de(m,k)
m1='111100010110010000011111011110111111000101100100'
print("\n更改/替换密文中的片段，将第一个密文分组替换为与第三个密文分组相同，得到错误的密文：",m1)
print("对错误密文进行解密")
m2=CBC_de(m1,k)
print("\n对两次解密结果进行异或操作，得出错误密文解密出的明文共有14位错误，错误位置见下方，1代表错误：")
print(xor(m0,m2))'''
