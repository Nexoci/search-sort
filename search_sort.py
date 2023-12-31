#Made By: Konnor
#Date: Sep 21st, 2023
#Search and Sort a Student List
import time
options=[1,2]
students = ["Beatrice","Bart","Zeek","Jackey Chan","Dwayne","Jack","Mark","Jyden Guy","Asheu","Apu","Ventrax The Conquerer Of The Galaxy","John","Porky","Idinia","Arker"]
def begin():
    done = False
    while not done:
        try:
            print("Welcome To A Student List\n\n1: Add Student\n2: Search For Student\n3: Exit\n")
            choice = input("What Is Your Choice: ")
            key = {1: add, 2: search,}
            choice = int(choice)
            if choice == 3:
                print("Goodbye")
                done = True
            elif choice > 3:
                print("Invalid choice. Please try again.")
                time.sleep(1)
            elif choice in key:
                key[choice]()
        except:
            print("Invalid choice. Please try again.")
            time.sleep(1)
def add():
    name = input("Enter student name to add: ")
    students.append(name)
    bubbleSort(students)
    print("Student data added successfully.")
    time.sleep(1)
    
def search():
    bubbleSort(students)
    search=input("What Student are you looking for: ")
    index =binary_search(students, 0, len(students),search)
    if index != -1:
        print(f"{search} is at Index {index}.\n")
        time.sleep(2)
    else:
        print(f"{search} not found in the student list.\n")
        time.sleep(2)
def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return
def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
begin()
