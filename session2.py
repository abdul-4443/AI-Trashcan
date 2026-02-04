"""
Q1: Create a list: fruits = [&#39;apple&#39;, &#39;banana&#39;, &#39;cherry&#39;, &#39;date&#39;, &#39;fig&#39;]
Print:
First element
Last element
First three elements
Last two elements
"""

fruits = ['apple', 'banana', 'cherry', 'date', 'fig']

print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("First three elements:", fruits[:3])
print("Last two elements:", fruits[-2:])

"""
Q2: Using the same fruits list:
Replace the second element with &#39;blueberry&#39;
Delete the last element
Add a new element &#39;grape&#39;
"""
fruits[1] = 'blueberry'    
del fruits[-1]
fruits.append('grape')     

print(fruits)

"""
Q3: Create a numeric list: [10, 5, 7, 3, 9]
Find:
Sum of the list
Maximum number
Minimum number
Sort the list in ascending order
"""
numbers = [10, 5, 7, 3, 9]

print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

numbers.sort()
print("Sorted list:", numbers)


"""
Q4: Create a list of squares of even numbers from 1 to 10 using a one-liner list
comprehension
Create a list containing only the fruits whose names have less than 6 characters
"""
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print("Even squares:", even_squares)

short_fruits = [f for f in fruits if len(f) < 6]
print("Fruits with <6 characters:", short_fruits)

"""
Q5: Create a tuple: colors = (&#39;red&#39;, &#39;green&#39;, &#39;blue&#39;, &#39;yellow&#39;)
Access:
First element
Last element
Slice from the second to the third element
Try modifying: colors[1] = &#39;black&#39; → Observe the error
"""
colors = ('red', 'green', 'blue', 'yellow')

print("First element:", colors[0])
print("Last element:", colors[-1])
print("Slice (2nd to 3rd):", colors[1:3])

"""
Q6: Create a tuple: (1, 2, 2, 3, 4, 2, 5)
Find:
How many times 2 appears
The index of the first 3
"""

nums = (1, 2, 2, 3, 4, 2, 5)

print("Count of 2:", nums.count(2))
print("Index of first 3:", nums.index(3))


"""
Q7: Create a dictionary: student = {&#39;name&#39;:&#39;Ali&#39;, &#39;age&#39;:20, &#39;grade&#39;:&#39;A&#39;}
Print:
Student&#39;s name
Add a new key &#39;city&#39; = &#39;Lahore&#39;
Update &#39;grade&#39; = &#39;A+&#39;
Delete the &#39;age&#39; key
"""
student = {'name': 'Ali', 'age': 20, 'grade': 'A'}

print("Student name:", student['name'])

student['city'] = 'Lahore'    
student['grade'] = 'A+'       
del student['age']             

print(student)

"""
Q8: Create a dictionary: scores = {&#39;Math&#39;:90, &#39;Physics&#39;:85, &#39;Chemistry&#39;:92}
Print:
List of all keys
List of all values
Total score (sum of all values)
Format a string using the dictionary: &quot;Ali scored 90 in Math&quot; dynamically using
scores
"""
scores = {'Math': 90, 'Physics': 85, 'Chemistry': 92}

print("Keys:", list(scores.keys()))
print("Values:", list(scores.values()))
print("Total score:", sum(scores.values()))

print(f"Ali scored {scores['Math']} in Math")

"""
Q9: Create a set: tools = {&#39;Photoshop&#39;, &#39;Illustrator&#39;, &#39;Acrobat&#39;}
Add &#39;Premiere&#39;
Remove &#39;Acrobat&#39;
Try adding a list [&#39;InDesign&#39;,&#39;Bridge&#39;] → Observe the error
Clear the set completely
"""
tools = {'Photoshop', 'Illustrator', 'Acrobat'}

tools.add('Premiere')
tools.remove('Acrobat')

tools.clear()
print(tools)

"""
Q10: Create two sets:
DS_skills = {&#39;Python&#39;, &#39;R&#39;, &#39;SQL&#39;, &#39;Git&#39;}
DE_skills = {&#39;Python&#39;, &#39;Java&#39;, &#39;SQL&#39;, &#39;Hadoop&#39;}
Find:
Union of both sets
Intersection of both sets
Difference: DS_skills - DE_skills
Symmetric difference of both sets
"""
DS_skills = {'Python', 'R', 'SQL', 'Git'}
DE_skills = {'Python', 'Java', 'SQL', 'Hadoop'}

print("Union:", DS_skills | DE_skills)
print("Intersection:", DS_skills & DE_skills)
print("Difference (DS - DE):", DS_skills - DE_skills)
print("Symmetric Difference:", DS_skills ^ DE_skills)