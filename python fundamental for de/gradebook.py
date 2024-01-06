last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

print(gradebook)
print()

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
print(gradebook)

gradebook[5][1] +=5
print(gradebook)

gradebook[0].remove(98)
gradebook[1].remove(97)
gradebook[2].remove(85)
gradebook[3].remove(88)
gradebook[4].remove(100)
gradebook[5].remove(98)
print(gradebook)

gradebook[0].append("Pass")
gradebook[1].append("Pass")
gradebook[2].append("Pass")
gradebook[3].append("Pass")
gradebook[4].append("Pass")
gradebook[5].append("Pass")
print(gradebook)

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)