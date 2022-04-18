# CTI-110
# P2HW2 - Score Avg
# Trent Boyer
# 15APR22
#

#Get 7 scores

item1 = float(input('\nEnter score #1: '))
item2 = float(input('Enter score #2: '))
item3 = float(input('Enter score #3: '))
item4 = float(input('Enter score #4: '))
item5 = float(input('Enter score #5: '))
item6 = float(input('Enter score #6: '))
item7 = float(input('Enter score #7: '))
#store in list
scores_list = [item1, item2, item3, item4, item5, item6, item7]

# determine low score                  
lowest_score = str(min(scores_list))

#drop low score
scores_list.remove(min(scores_list))

# find average
scores_average = sum(scores_list) / len(scores_list)


modified_list = scores_list


print("\n\n-------Results_______")
print('Lowest Score:', lowest_score)
print('Modified List:', modified_list)
print('Scores Average:', scores_average)

