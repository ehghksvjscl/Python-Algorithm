datas = [['eve', "010-9999-9999"], ['kim', "010-1111-1111"],['kim',"010-2222-2222"]]
datas = [
 ["aaaa" , "010-7470-9619"],
 ["aaa" , "010-5711-7180"],
 ["aa" , "010-3009-2551"],
 ["a" , "010-4362-3829"],
 ["abc" , "010-4166-8204"],
]

datas = [
    ["asdf" ,"010-9999-9999"],
    ["dddd" ,"010-0000-0000"],
    ["a" ,"010-4817-2344"],
    ["b" ,"010-0000-0001"],
    ["aaaa" ,"010-0000-0000"],
    ["aaa" ,"010-0000-0001"],
    ["aaa" ,"010-0000-0002"], 
]


def solution(datas):
    # datas.sort(key=lambda x: (x[0], x[1]))

    a = sorted(datas, key=lambda x: (x[0], x[1]))
    return a

for i in solution(datas):
    print(i[0], i[1])
