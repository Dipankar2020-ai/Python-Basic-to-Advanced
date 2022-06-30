
#
# Complete the 'strmethod' function below.
#
# The function accepts following parameters:
#  1. STRING para
#  2. STRING spch1
#  3. STRING spch2
#  4. LIST li1
#  5. STRING strf
#

def stringmethod(para, special1, special2, list1, strfind):
    # Write your code here
    l1=list(special1)
    for i in l1:
        para=para.replace(i,'')
    word1=para
    l2=word1[0:70]
    word2=l2[::-1]
    print(word2)
    
    l3=list(special2)
    for i in word2:
        l4=word2.replace(' ','')
    print(special2.join(l4[i] for i in range(0,len(l4),1)))
    res=[ele for ele in list1 if(ele in para)]
    if(len(res)==len(list1)):
        print("Every string in {} were present".format(list1))
    else:
        print("Every string in {} were not present".format(list1))
    wordList=word1.split()
    print(wordList[:20])
    word=word1.split()
    str2=[]
    str3=[]
    for i in word:
        if i not in str2:
            str2.append(i)
    for i in range(0,len(str2)):
        if word.count(str2[i])<3:
            str3.append(str2[i])
    print(str3[-20: ])
    print(word1.rindex(strfind))

if __name__ == '__main__':
    para = input()

    spch1 = input()

    spch2 = input()
    
    qw1_count = int(input().strip())

    qw1 = []

    for _ in range(qw1_count):
        qw1_item = input()
        qw1.append(qw1_item)

    strf = input()

    stringmethod(para, spch1, spch2, qw1, strf)
