import S_AES

k = "00011000010111011001011010100101"
p = ['1100110011110000', '1111111111111111', '0000000000000000']
c = ['0001111011000001', '1110011110110000', '1110011010001010']

search_k1 = []
m_c_text = []
m_p_text = []
for id_1 in range(pow(2, 16)):
    k_1 = '{0:0{1}b}'.format(id_1, 16)
    aes_1 = S_AES.S_AES(k_1)
    m_c = aes_1.jiami(p[0])
    m_c_text.append(m_c)

    k_2 = '{0:0{1}b}'.format(id_1, 16)
    aes_2 = S_AES.S_AES(k_2)
    m_p = aes_2.jiemi(c[0])
    m_p_text.append(m_p)

for i in range(pow(2, 16)):
    for j in range(pow(2, 16)):
        if m_c_text[i] == m_p_text[j]:
            k_1 = '{0:0{1}b}'.format(i, 16)
            k_2 = '{0:0{1}b}'.format(j, 16)
            search_k1.append(str(k_1) + str(k_2))

search_k2 = []
for i in range(len(search_k1)):
    key = search_k1[i]
    k_1 = key[0:16]
    aes_1 = S_AES.S_AES(k_1)
    m_c = aes_1.jiami(p[1])

    k_2 = key[16:32]
    aes_2 = S_AES.S_AES(k_2)
    m_p = aes_2.jiemi(c[1])

    if m_c == m_p:
        search_k2.append(key)

search_k3 = []
for i in range(len(search_k2)):
    key = search_k2[i]
    k_1 = key[0:16]
    aes_1 = S_AES.S_AES(k_1)
    m_c = aes_1.jiami(p[1])

    k_2 = key[16:32]
    aes_2 = S_AES.S_AES(k_2)
    m_p = aes_2.jiemi(c[1])

    if m_c == m_p:
        search_k3.append(key)

print(search_k3)
print('找到' + str(len(search_k3)) + '个可能的密钥')
tr_k = []
print('经验证')
for i in range(len(search_k3)):
    num = 0
    for j in range(len(p)):
        enc, det = S_AES.dou_use(p[j], search_k3[i])
        if (enc == c[j]) & (det == p[j]):
            num += 1
    if num == len(p):
        print('找到正确的密钥' + '\n' + 'Key=' + str(search_k3[i]))
        tr_k.append(search_k3[i])
print(tr_k)
print('共找到' + str(len(tr_k)) + '个正确的密钥')
