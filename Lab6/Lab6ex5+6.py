def main():
    i = 0
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    for i in days:
        print(i, end = " ")
    tupleProof(days)

def tupleProof(x):
    i = 0
    x.append("St. Paddies Day")
    for i in x:
        print(i, end = " ")
main()
