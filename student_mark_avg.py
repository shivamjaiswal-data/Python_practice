def avg_marks(student):
    for name,marks in student.items():
        avg = sum(marks)/len(marks)
      
        if avg > 40 :
            result = "passed"
        else:
            result = "Fail"
        print(name,round(avg),result)

print(avg_marks({"ram" : [20,30,59],"shyam": [50,60,70],"shivam": [80,50,70]}))

    
