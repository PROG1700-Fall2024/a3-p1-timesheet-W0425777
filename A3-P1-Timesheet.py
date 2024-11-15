#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:W042577    
#Student Name: Katherine Tucker 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    WorkH = [] # change from strs
    LWork = []
    MWork = []
    WorkZ = 0
    
    def hours(day):
        WorkZ=float(input(f"Enter hours worked on Day #{day}: "))
        return WorkZ 

    for i in range(1,6):
        Dhours = hours(i)
        WorkH.append(Dhours)
        if Dhours < 7:
            LWork.append(i)
                   
    print("-"*100)
   
    MaxHours = max(WorkH)
    for i in range(len(WorkH)):
        if WorkH[i] == MaxHours:
            MWork.append(i+1)
 
    print("The most hours worked was on: ")
    for i in range(len(MWork)):
        print("Day #{0} when you worked {1:.0f} hours.".format(MWork[i], MaxHours))

    THours = sum(WorkH)
    AHours = sum(WorkH) / len(WorkH)

    print("-"*100)
    print("The total hours worked was: {0:.0f}".format(THours))
    print("The average number of hours worked each day was: {0}".format(AHours))

    # figure out how to call the return from the function
    print("-"*100)
   
    if len(LWork) > 0:
        print("Days you slacked off (i.e. worked less than 7 hours):")
        for i in range(len(LWork)):
            print("Day #{0}: {1:.0f} hours".format(LWork[i], WorkH[LWork[i]-1]))

#print("Day #{0}: {1} hours"
main()
# portential creat workH do the rest of the code 
# rerun list for last output so that it will print of the value is under 7 instead of appending the list, 
# can you print the index of a vlaue in a list?