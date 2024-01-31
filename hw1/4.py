stud_list = input()
vacant = int(input())

def Artek(s, n):
    studs = s.split(', ')
    nice = []
    for stud in studs:
        if '5' in stud:
            nice.append(stud[:-2])
    nice.sort()
    print(nice[:n])

Artek(stud_list, vacant)

