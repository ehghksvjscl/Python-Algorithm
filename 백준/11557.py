num1 = int(input())

for n1 in range(num1):
    school_count = int(input())
    good_school = "" 
    good_school_number = 0 

    for school in range(school_count):
        a,b = input().split()
        b = int(b)
        if b > good_school_number:
            good_school_number = b
            good_school = a

    print(good_school)