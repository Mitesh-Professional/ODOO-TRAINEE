# List Methods

list_items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("This List is Default List:- ", list_items)
list_items.append(10)
print("Append Method in list:- ", list_items)
list_items.clear()
print("Clear Method is List:-", list_items)
list_items = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
value = list_items.count(1)
# Two Time 1 occurr in list
print("Count Method in List:- ", value)
list_item2=[10,11,12]
list_items.extend(list_item2)

print("Extend Method in List:- ", list_items)

value = list_items.index(10)
print("Index Method in List:- ", value)

list_items.insert(0,0)
print("Insert Method in List:- ",list_items)

list_items.pop(1)
print("Pop Method in List:- ",list_items)

list_items.remove(12)
print("Remove Method in List:- ", list_items)

list_items.reverse()
print("Revers Method in List:- ", list_items)

list_items = [3,1,2,10,4,7,5,6,9,7]
list_items.sort()
print("Sort Method in List:- ", list_items)

