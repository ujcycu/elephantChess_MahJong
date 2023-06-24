import random

# 中文對應
#0,1-10,11-15 #16,17-26,27-31
elephant = [ 
    "將","士","士","象","象","車","車","馬", #0-7 
    "馬","包","包","卒","卒","卒","卒","卒", #8-15
    "帥","仕","仕","相","相","俥","俥","傌", #16-23 
    "傌","炮","炮","兵","兵","兵","兵","兵"  #24-31
]


# 序號轉中文
def transChi(array):
    arr = []
    for i in array:
        arr.append(elephant[i])
        #print(elephant[i])
    return arr

# 判定湖了
def classify(array):
    chi = transChi(array)
    countB = chi.count('卒')
    countR = chi.count('兵')
    if countB == 5 or countR == 5:
        return "5win!!!"
    elif countB == 3 or countR == 3:
        if countB == 2 or countR == 2:
            return "3卒/兵+2卒/兵!!!"
        else:
            two = matchTwo(array) #找對子
            if two == True:
                return "3卒/兵+對子!!!"
            else:
                return "KOG1"
    elif countB == 2 or countR == 2:
        three = matchThree(array) #找順子
        if three == True:
            return "2卒/兵+順子!!!"
        else:
            return "KOG2"
    else:
        two = matchTwo(array)
        three = matchThree(array)
        if two == True and three == True:
            return "對子+順子"
        else:
            return "KOG3"
        
# 對子
def matchTwo(array): #0, 1-10; 16, 17-26
    for i in array:
        if i == 0: #將
            for j in array:
                if j == 16:
                    return True #"將帥"
        elif i > 0 and i <= 10: #士象車馬包 1-10
            if i%2 == 0:
                for j in array:
                    if j == i-1:
                        return True #"兩支一樣的(黑)"
        elif i > 16 and i <= 26:
            if i%2 == 0:
                for j in array:
                    if j == i-1:
                        return True #"兩支一樣的(紅)"
                    
# 順子 #將士象/車馬包/帥仕相/俥傌炮
def matchThree(array): #0, 1-10; 16, 17-26
    for i in array:
        if i == 0:
            for j in array:
                if j == 1 or j == 2:
                    for k in array:
                        if k == 3 or k == 4:
                            return True #將士象
        elif i == 5 or i == 6:
            for j in array:
                if j == 7 or j == 8:
                    for k in array:
                        if k == 9 or k == 10:
                            return True #車馬包
        elif i == 16:
            for j in array:
                if j == 17 or j == 18:
                    for k in array:
                        if k == 19 or k == 20:
                            return True #帥仕相
        elif i == 21 or i == 22:
            for j in array:
                if j == 23 or j == 24:
                    for k in array:
                        if k == 25 or k == 26:
                            return True #俥傌炮

elephant_num = []
for i in range(32):
    elephant_num.append(i)
#print(elephant_num)
#transChi(elephant_num)

#chess = [11, 12, 13, 14, 15] #5卒
#chess = [31, 27, 29, 28, 30] #5兵
#chess = [0, 9, 13, 11, 16] #['將', '包', '卒', '卒', '帥']
#chess = [25, 2, 23, 22, 1] 

#print(transChi(chess).count('卒'),"卒",transChi(chess).count('兵'),"兵")
chess = random.sample(elephant_num, 5)
print(chess)
print(transChi(chess))
print(classify(chess))
