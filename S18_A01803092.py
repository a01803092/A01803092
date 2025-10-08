print( "a. analisis de temperatura por semana")

Temp= [22,28,21,30,23,31,33]

avgtemperature= sum(Temp) / len(Temp)

print("the average temperature is", avgtemperature)

for Temperature in Temp:
    if Temperature >= avgtemperature:
        print(Temperature, "is above average")
    else:
        print(Temperature, "is below average")





print( "b. Grades of students")

students = ["Andre", "Manuel", "Valeria", "Isabela", "Pato"]
averages = [85, 70, 55, 92, 48]

class_average = sum(averages) / 5
print ("the class average is:", class_average)

passed = [grade for grade in averages if grade >=70]
percentage_passed = (len(passed)/ len(averages))*100
print("Percentage of students who passed:", percentage_passed)
failed = [grade for grade in averages if grade <=69]
percentage_failed = (len(failed)/ len(averages))*100
print ("percentage of students that failed:", percentage_failed)



print ("c. shopping list")
shopping_list = ["Milk", "Eggs", "Bread", "Apples", "Cheese"]
purchased = [False, True, False, False, True]
for i in range(len(shopping_list)):
    if not purchased[i]:
        print(f"You still need to buy: {shopping_list[i]}")

# b) Ask the user if they have purchased them
for i in range(len(shopping_list)):
    if not purchased[i]:
        answer = input(f"Have you bought {shopping_list[i]}? (yes/no): ").lower()
        if answer == "yes":
            purchased[i] = True

print("\nUpdated purchased list:", purchased)



print ("d. numbers list")
numbers = [10, 3, 25, 7, 15, 2, 18]

max_value = max(numbers)
min_value = min(numbers)
ordered_list = sorted(numbers)

print("Maximum:", max_value)
print("Minimum:", min_value)
print("Ordered list:", ordered_list)



print (" even and odd numbers")
numbers = [10, 3, 25, 7, 15, 2, 18]

even_numbers = [n for n in numbers if n % 2 == 0]
odd_numbers = [n for n in numbers if n % 2 != 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)




usernames = ["andre", "luis", "maria"]

while True:
    new_user = input("Enter a new username: ").lower()
    if new_user in usernames:
        print("That username already exists. Try with onother one.")
    else:
        usernames.append(new_user)
        print("Username added!")
        break

print("List of usernames:", usernames)