name = "Ben Stobie"
courseId = "Dt080A/2"
mark = int(input("Please input the student's mark: "))

print("Student name: ", name)
print("Course ID: ",courseId)

if mark < 40:
    print("Fail")
elif mark < 50:
    print("Pass")
elif mark < 60:
    print("Lower Merit")
elif mark < 70:
    print("Higher Merit")
else:
    print("Distinction")
