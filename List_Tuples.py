# 🧠 Python Practice: Lists and Tuples

# Checking if a list is a palindrome
my_list = [1, 2, 3, 2, 1]

# Uncomment this to add user input in the future
# my_list.append(int(input("Enter a number to add to the list: ")))

reversed_list = my_list.copy()
reversed_list.reverse()

if my_list == reversed_list:
    print("✅ It's a palindrome list!")
else:
    print("❌ It's not a palindrome list.")

# Tuple operations
marks = (3, 4, 5, 6, 6)
print("Number of times 6 appears:", marks.count(6))

grades_tuple = ("C", "D", "A", "A", "B", "B", "A")
print("Grade A appears:", grades_tuple.count("A"), "times")

# Sorting a list of grades
grades_list = ["C", "D", "A", "A", "B", "B", "A"]
grades_list.sort()
print("Sorted grades:", grades_list)
