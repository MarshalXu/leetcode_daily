#-*- coding:utf-8 -*-
import numpy as np
def viterbi(trainsition_probability,emission_probability,pi,obs_seq):

    #转换为矩阵进行计算
    trainsition_probability=np.array(trainsition_probability)
    emission_probability=np.array(emission_probability)
    pi=np.array(pi)

    #定义要返回的矩阵
    F = np.zeros((Row, Col))

    #初始状态
    F[:,0]=pi*np.transpose(emission_probability[:,obs_seq[0]])


    for t in range(1,Col):
        list_max=[]
        for n in range(Row):
            list_x=list(np.array(F[:,t-1])*np.transpose(trainsition_probability[:,n]))

            #获取最大概率
            list_p=[]
            for i in list_x:
                list_p.append(i*10000)
            list_max.append(max(list_p)/10000)

        F[:, t] = np.array(list_max) * np.transpose(emission_probability[:,obs_seq[t]])

    return F


if __name__ == '__main__':
    #隐藏状态
    invisible=['Sunny','Cloud','Rainy']
    #初始状态
    pi=[0.63,0.17,0.20]
    #转移矩阵 
    trainsition_probability=[[0.5,0.375,0.125],
                             [0.25,0.125,0.625],
                             [0.25,0.375,0.375]]
    #发射矩阵
    emission_probability=[[0.6,0.2,0.15,0.05],
                          [0.25,0.25,0.25,0.25],
                          [0.05,0.10,0.35,0.5]]
    #最后显示状态
    obs_seq=[0,2,3]

    #最后返回一个Row*Col的矩阵结果
    Row = np.array(trainsition_probability).shape[0]
    Col = len(obs_seq)

    F=viterbi(trainsition_probability, emission_probability, pi, obs_seq)

    print(F)

def viterbi(nodes):
    paths = {'b':nodes[0]['b'], 's':nodes[0]['s']}
    for l in range(1,len(nodes)):
        paths_ = paths.copy()
        paths = {}
        for i in nodes[l].keys():
            nows = {}
            for j in paths_.keys():
                if j[-1]+i in zy.keys():
                    nows[j+i]= paths_[j]+nodes[l][i]+zy[j[-1]+i]
            k = np.argmax(nows.values())
            paths[nows.keys()[k]] = nows.values()[k]
    return paths.keys()[np.argmax(paths.values())]

def simple_cut(s):
    if s:
        r = model.predict(np.array([list(chars[list(s)].fillna(0).astype(int))+[0]*(maxlen-len(s))]), verbose=False)[0][:len(s)]
        r = np.log(r)
        nodes = [dict(zip(['s','b','m','e'], i[:4])) for i in r]
        t = viterbi(nodes)
        words = []
        for i in range(len(s)):
            if t[i] in ['s', 'b']:
                words.append(s[i])
            else:
                words[-1] += s[i]
        return words
    else:
        return []


["MinStack","push","push","push","min","pop","top","min"]
[[],[-2],[0],[-3],[],[],[],[]]