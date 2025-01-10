#LIST DS ASSIGNMENTS:
list1=["Ethan", "Sophia", "Liam", "Aria", "Noah"]
list2=["Olivia","Olivia","Isabella"]
list3=["car","bike","van","bus"]
#1. w.p.p to concatenate two lists
print(list1+list2)
print(list1*3)
#2. W.P.P to find length of the list
print(len(list1))
#3. W.P.P to find position of a perticular sub string
print(list1[1:4])
#4. W.P.P to append a perticular element in the existing list
list2.append("varun")
print(list2)
#5. w.p.p. to insert a perticular element at desired index
list2.insert(0,"prabhas")
print(list2)
#6. w.p.p to merge two list and store a final list in list1
list1.extend(list2)
print(list1)
#7. w.p.p to remove a desired element from the list
'''list2.remove("varun")
print(list2)'''
#8. w.p.p to pop top element from the list
'''list3.pop(2)
print(list3)
print(list3.pop(2))
#9. w.p.p to delete entire list
del list3
print(list3)'''
#10. w.p.p to convert a string into a list using builtin function
string="varun"
list4=list(string)
print(list4)
