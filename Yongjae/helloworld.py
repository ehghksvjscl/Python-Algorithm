point_1 = int(input()) #각 점수 입력받기
point_2 = int(input())
point_3 = int(input())
point_4 = int(input())
point_5 = int(input())
point_list = [point_1, point_2, point_3, point_4, point_5] # 리스트 선언

def Aver(point_list): #리스트의 평균값을 구하는 함수
    point_list.sort() 
    point_list[0] = 40
    point_list[1] = 40
    Aver = sum(point_list)/len(point_list) #리스트 평균 값
    return int(Aver) #반환

print(Aver(point_list)) #함수 호출