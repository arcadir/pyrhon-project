#文字列検索

def strSearch(compareStr,targetStr):
    print(compareStr,"に",targetStr,"があるか検索します。")
    if compareStr.find(targetStr) == -1:
        print("該当の文字列はありませんでした。")
    else:
        print("該当あり")
        print("該当の文字列開始位置は、",compareStr.find(targetStr),"です。")
        print("該当の文字列終了位置は、",compareStr.find(targetStr)+len(targetStr),"です。")
