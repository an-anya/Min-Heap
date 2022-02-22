class MagicList:
    def __init__(self):
        self.data = [0]

    def findMin(self):
        M = self.data
        if len(M)>1:
            return M[1]
        else:
            return None
        
    def insert(self, n):
        def maxpow(n):
            count=0
            for i in range(0,10000): 
                if n>=pow(2,i):
                    count+=1
                else:
                    return count
        l = self.data

        l.append(n)
        k=len(l)
        temp=0
        index=k-1
        for i in range(1,maxpow(k-1)+1):
            if l[(k-1)//pow(2,i)]>n:
                temp=l[(k-1)//pow(2,i)]
                l[index]=temp
                l[(k-1)//pow(2,i)]=n
                index//=2
            else:
                break
        

    def deleteMin(self):
        l = self.data
        if len(l)<1:
            return None
        l[1],l[-1]=l[-1],l[1]
        if len(l)==2:
            return l.pop()
        l.pop()
        k=len(l)
   
        i=1
        while(2*i+1<k):
            if l[i]>l[2*i] and l[i]>l[2*i+1]:
                if l[2*i]<l[2*i+1]:
                    l[i],l[2*i]=l[2*i],l[i]
                    i=2*i
                else:
                    l[i],l[2*i+1]=l[2*i+1],l[i]
                    i=2*i+1
            elif l[i]<=l[2*i] and l[i]>l[2*i+1]:
                l[i],l[2*i+1]=l[2*i+1],l[i]
                i=2*i+1
            elif l[i]>l[2*i] and l[i]<=l[2*i+1]:
                l[i],l[2*i]=l[2*i],l[i]
                i=2*i
            else :
                return None  
        if 2*i+1>=k and 2*i<k:
            if l[i]>l[2*i]:
                l[i],l[2*i]=l[2*i],l[i]
                i=2*i
        
        return None
    

def K_sum(L, K):
    A=MagicList()
    for item in L:
        A.insert(item)
    s=0
    for i in range(K):
        s+=A.findMin()
        A.deleteMin()
    return s


