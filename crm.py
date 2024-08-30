import pandas as pd
import numpy as np
df = pd.read_csv("C:/python/Project1/data.csv")
print("data loaded succesfully")
print()
remainingDF = df[df["status"] == 0]
completedDF = df[df["status"] == 1]
print()
print("remaining leads :", remainingDF.shape[0])
print("completed leads :", completedDF.shape[0])
print()
while True:
    print(" --------------------------")
    print("| Crm system               |")
    print("| 1. get next lead         |")
    print("| 2. show remaining leads  |")
    print("| 3. show completed leads  |")
    print("| 4. Show all data         |")
    print("| 5. exit                  |")
    print(" --------------------------")
    print()
    choice = int(input("Enter your choice :"))

    if choice == 1:
        next = remainingDF.iloc[0]
        print("Lead :")
        print("Name:{} , Number:{}".format(next["Names"] , next["Phone Numbers"]))
        print("enter result after reading the cell")
        print()
        print(" ---------------------------")
        print("| Possible Results          |")
        print("| 1. Intrested              |")
        print("| 2. Not Intrested          |")
        print("| 3. Call Back Later        |")
        print("| 4. DNP (Did Not Pick)     |")
        print("| 5. Junk Lead/Wrong Number |")
        print(" ---------------------------")
        res= int(input("Enter Choice \n"))
        match(res):
            case 1:
                print("Lead is Intrested")
                answer = "Intrested"
            case 2:
                print("Lead is Not Intrested")
                answer = "Not Intrested"
            case 3:
                print("Lead asked to Call Back Later")
                answer = "Call Back Later"
            case 4:
                print("Lead Did Not Pick The Call")
                answer = "DNP (Did Not Pick)"
            case 5:
                print("Lead is Junk Lead/Wrong Number")
                answer = "Junk Lead/Wrong Number"
            case _:
                print("INVALID OPTION")
                answer = "N\A"

        df.loc[df['Phone Numbers'] == next['Phone Numbers'], 'status']=1
        df.loc[df['Phone Numbers'] == next['Phone Numbers'], 'result']=str(answer)

        df.to_csv('C:/python/Project1/data.csv', index = False)
        remainingDF = df[df["status"] == 0]
        completedDF = df[df["status"] == 1]
        print("Data loaded succesfully")
        print()

    if choice == 2:
        print("____________________________________________________________")
        print(remainingDF)
        print("____________________________________________________________")
        print()
        
    if choice == 3:
        print("____________________________________________________________")
        print(completedDF)
        print("____________________________________________________________")
        print()
    if choice == 5:
        print("python file exited succesfully")
        break
    if choice == 4:
        print("____________________________________________________________")
        print(df)
        print("____________________________________________________________")
        print()
