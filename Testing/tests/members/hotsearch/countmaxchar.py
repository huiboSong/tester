# coding=utf-8
__author__ = 'co-mall'

class charcount():
    def charcount(self,str):
       list=list(str.size())
       for i in len(str):
           if str(i) not in list:
               list.append(str(i))

       count=int[len(list)]
       for i in len(list):
           mid=list(i)
           for j in str.size():
               if mid==str(j):
                   count[i]=count[i]+1

       index=0
       max=count[0]
       for i in len(count):
            if max<count[i]:
                max=count[i]
                index=i

       print '出现次数最多的字符位%s'+list(index)
       print 'chuxiancishu'+index


if __name__ == "__main__":
    charc=charcount()
    charc.charcount('aaabbccda')