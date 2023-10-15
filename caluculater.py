#電卓
def caluculater(integerOne,integerSecond,caluculateMethod):
    ans=0
    mehtodName=""

    if caluculateMethod=="*": 
        mehtodName="掛け算"
        ans=integerOne*integerSecond    

    if caluculateMethod=="/":
        mehtodName="割り算"
        ans=integerOne/integerSecond    
    
    if caluculateMethod=="+":
        mehtodName="足し算"
        ans=integerOne+integerSecond    

    if caluculateMethod=="-":
        mehtodName="引き算"
        ans=integerOne-integerSecond    
        
    print("指定された計算方法は",mehtodName,"です。")
    print("計算内容: ",integerOne," ",caluculateMethod," ",integerSecond)
    print("電卓の計算結果は、",ans,"です。")
