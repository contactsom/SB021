scores=[56,75,45,89,75,34,89,75,34]
print("Actual List ",scores)
# 1. Remove the duplicate from list
print("******** START- 1. Remove the duplicate from list ******** ")
uniqueScore=list(set(scores))
print("Unique List ",uniqueScore)
print("******** END- 1. Remove the duplicate from list ******** ")


# 2. Sort in descending orders
print("******** START- 2. Sort in descending orders ******** ")
uniqueScore.sort(reverse=True)
print("Sorted List ",uniqueScore)
print("******** END- 2. Sort in descending orders ******** ")



# 3. Average of all the scores
print("******** START- 3. Average of all the scores ******** ")
average=sum(uniqueScore)/len(uniqueScore)
print("Average ::",average)
print("******** END- 3. Average of all the scores ******** ")


# 4. Count the student scoring > 70
print("******** START- 4. Count the student scoring > 70 ******** ")

count=0
for score in uniqueScore:
    if(score>70):
        count=count+1

print("Count the student scoring > 70 :: ",count)
print("******** END- 4. Count the student scoring > 70 ******** ")
