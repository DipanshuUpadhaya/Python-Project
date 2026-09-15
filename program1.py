from collections import Counter
def unique(lst):
    counts=Counter(lst)
    return [item for item,count in counts.items() if count==1]
numbers=[1,2,3,2,4,5,1,6,3,7]
print(unique(numbers))