import S_AES

k = "11100001101010011100001110100101"
p = '1011001110100100'
c = '0011100000101010'

search_k = []
m_c_text = []
m_p_text = []
for id in range(pow(2, 16)):
    k_1 = '{0:0{1}b}'.format(id, 16)
    aes_1 = S_AES.S_AES(k_1)
    m_c = aes_1.jiami(p)
    m_c_text.append(m_c)

    k_2 = '{0:0{1}b}'.format(id, 16)
    aes_2 = S_AES.S_AES(k_2)
    m_p = aes_2.jiemi(c)
    m_p_text.append(m_p)

for i in range(pow(2, 16)):
    for j in range(pow(2, 16)):
        if m_c_text[i] == m_p_text[j]:
            k_1 = '{0:0{1}b}'.format(i, 16)
            k_2 = '{0:0{1}b}'.format(j, 16)
            search_k.append(str(k_1) + str(k_2))

print(search_k)
print('找到' + str(len(search_k)) + '个可能的密钥')
tr_k = []
print('经验证')
for i in range(len(search_k)):
    enc, det = S_AES.dou_use(p, search_k[i])
    if enc == c and det==p:
        print('找到正确的密钥' + '\n' + 'Key=' + str(search_k[i]))
        tr_k.append(search_k[i])
# 单个明密文对可能有很多种可能的密钥
print(tr_k)
print('共找到' + str(len(tr_k)) + '个正确的密钥')
