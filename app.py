student = [] ;
n = int(input("사람 수 입력 : ")) ;
for i in range(n) : 
    name = input("이름 입력 : ") ;
    math = int(input("수학 점수 : ")) ;
    eng = int(input("영어 점수 : ")) ;
    total = math + eng ;
    avg = (total / 2) ;
    app = {
                "name": name,
                "math": math,
                "eng": eng,
                "total": total,
                "avg": avg,
                
            }
    student.append(app) ; 
print(len(student)) ;
print(student) ;