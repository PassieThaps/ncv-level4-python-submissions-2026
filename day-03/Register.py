learners = {
    "2024001": {"name": "Thandi", "marks": [65, 72, 58]},
    "2024002": {"name": "Sipho", "marks": [48, 90, 55]},
    "2024003": {"name": "Lerato", "marks": [81, 39, 77]},
    "2024004": {"name": "Dumisani", "marks": [72, 72, 48]},
    "2024005": {"name": "Naledi", "marks": [90, 55, 72]}
}


def demonstrate_collections():
    # 1.1 List of marks, first mark, last mark and first two marks
    marks = learners["2024001"]["marks"][:]
    print("All marks:", marks)
    print("First mark:", marks[0])
    print("Last mark:", marks[-1])
    print("First two marks:", marks[:2])
    
    # 1.2 Classroom coordinate tuple and unpacking
    classroom_position = (3, 5)
    row, seat = classroom_position
    print("Row:", row, "Seat:", seat)
    
    # 1.3 Set of unique module codes and membership test
    codes = {"IISL2", "CHARD", "SYSAD", "DCN"}
    print("Unique module codes:", len(codes))
    print("DCN is included:", "DCN" in codes)


# 2.1 Calculate total using a loop (without sum)
def total_of(values):
    total = 0
    for value in values:
        total = total + value
    return total

# 2.2 Calculate mean using total_of; handle empty list
def mean_of(values):
    if len(values) == 0:
        return None
    return total_of(values) / len(values)

# 2.3 Find highest and lowest using comparisons; handle empty list
def max_of(values):
    if len(values) == 0:
        return None
    highest = values[0]
    for value in values:
        if value > highest:
            highest = value
    return highest

def min_of(values):
    if len(values) == 0:
        return None
    lowest = values[0]
    for value in values:
        if value < lowest:
            lowest = value
    return lowest

# 2.4 Calculate range and values above the mean
def range_of(values):
    if len(values) == 0:
        return None
    return max_of(values) - min_of(values)

def above_mean(values):
    average = mean_of(values)
    result = []
    if average is None:
        return result
    for value in values:
        if value > average:
            result.append(value)
    return result

# 3.1 Find the first matching index, or -1
def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

# 3.2 Find all matching indices, including duplicates
def find_all(values, target):
    positions = []
    for i in range(len(values)):
        if values[i] == target:
            positions.append(i)
    return positions

# 3.3 Count matches without count()
def count_of(values, target):
    count = 0
    for value in values:
        if value == target:
            count = count + 1
    return count

# 3.4 Find all modes using a frequency dictionary (including ties)
def mode_of(values):
    if len(values) == 0:
        return []
    frequencies = {}
    for value in values:
        if value in frequencies:
            frequencies[value] = frequencies[value] + 1
        else:
            frequencies[value] = 1
    largest_count = 0
    for value in frequencies:
        if frequencies[value] > largest_count:
            largest_count = frequencies[value]
    modes = []
    for value in frequencies:
        if frequencies[value] == largest_count:
            modes.append(value)
    return modes

# 4.1 Bubble sort ascending on a copy using adjacent swaps
def bubble_sort(values):
    items = values[:]
    n = len(items)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

# 4.2 Selection sort ascending on a copy
def selection_sort(values):
    items = values[:]
    n = len(items)
    for i in range(n - 1):
        smallest_position = i
        for j in range(i + 1, n):
            if items[j] < items[smallest_position]:
                smallest_position = j
        items[i], items[smallest_position] = items[smallest_position], items[i]
    return items

def demonstrate_algorithms():
    data = [65, 72, 48, 90, 55, 72, 48, 72]
    print("Total:", total_of(data))
    print("Mean:", mean_of(data))
    print("Highest:", max_of(data))
    print("Lowest:", min_of(data))
    print("Range:", range_of(data))
    print("Above mean:", above_mean(data))
    print("First 72:", find_first(data, 72))
    print("All 72 positions:", find_all(data, 72))
    print("Count of 72:", count_of(data, 72))
    print("Mode:", mode_of(data))
    print("Tied modes:", mode_of([1, 2, 2, 3, 3]))
    print("Bubble sorted:", bubble_sort(data))
    print("Selection sorted:", selection_sort(data))
    print("Original unchanged:", data)

def valid_number(number):
    return len(number) == 7 and number.isdigit()

def valid_mark(text):
    return text.isdigit() and int(text) <= 100

# 5.2 Add a learner with a unique number and valid marks
def add_learner(records, number, name, marks):
    if not valid_number(number) or number in records or name.strip() == "":
        return False
    for mark in marks:
        if not isinstance(mark, int) or mark < 0 or mark > 100:
            return False
    records[number] = {"name": name.strip(), "marks": marks[:]}
    return True

# 5.3 Search for learner by student number
def find_learner(records, number):
    if number in records:
        return records[number]
    return None

# 5.4 Update learner name
def rename_learner(records, number, new_name):
    if number not in records or new_name.strip() == "":
        return False
    records[number]["name"] = new_name.strip()
    return True

# 5.4 Add a valid mark
def add_mark(records, number, mark):
    if number not in records or not isinstance(mark, int) or mark < 0 or mark > 100:
        return False
    records[number]["marks"].append(mark)
    return True

# 5.4 Delete an existing learner
def delete_learner(records, number):
    if number not in records:
        return False
    del records[number]
    return True

# 5.5 Rank learners by average using descending bubble sort of tuples
def ranking(records):
    rows = []
    for number in records:
        average = mean_of(records[number]["marks"])
        if average is not None:
            rows.append((average, number))
    # Bubble sort descending by average, swapping adjacent tuples.
    n = len(rows)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if rows[j][0] < rows[j + 1][0]:
                rows[j], rows[j + 1] = rows[j + 1], rows[j]
    return rows

def show_ranking(records):
    rows = ranking(records)
    if len(rows) == 0:
        print("No learners with marks yet.")
        return
    print("Rank  Number    Name             Average")
    for i in range(len(rows)):
        average, number = rows[i]
        name = records[number]["name"]
        print(f"{i + 1:<6}{number:<10}{name:<17}{average:.2f}")

def read_marks():
    marks = []
    print("Enter marks from 0 to 100. Press Enter with no mark to finish.")
    while True:
        text = input("Mark: ").strip()
        if text == "":
            return marks
        if valid_mark(text):
            marks.append(int(text))
        else:
            print("Invalid mark. Enter a whole number from 0 to 100.")

# 5.1 Display numbered menu
def show_menu():
    print("\nLEARNER MARKS MANAGEMENT SYSTEM")
    print("1. Add learner")
    print("2. Find learner")
    print("3. Rename learner")
    print("4. Add mark")
    print("5. Delete learner")
    print("6. Show ranking")
    print("7. Show collections and algorithm examples")
    print("8. Exit")

# 5.1 Repeat menu until Exit and handle invalid choices
def main():
    choice = ""
    while choice != "8":
        show_menu()
        choice = input("Choice: ").strip()
        if choice == "1":
            number = input("Student number (7 digits): ").strip()
            name = input("Name: ").strip()
            if not valid_number(number) or name == "" or number in learners:
                print("Invalid details or duplicate student number.")
            else:
                marks = read_marks()
                if add_learner(learners, number, name, marks):
                    print("Learner added.")
        elif choice == "2":
            number = input("Student number: ").strip()
            record = find_learner(learners, number)
            if record is None:
                print("Learner not found.")
            else:
                print("Name:", record["name"], "Marks:", record["marks"])
        elif choice == "3":
            number = input("Student number: ").strip()
            name = input("New name: ").strip()
            print("Learner updated." if rename_learner(learners, number, name) else "Learner not found or name invalid.")
        elif choice == "4":
            number = input("Student number: ").strip()
            text = input("New mark (0-100): ").strip()
            if not valid_mark(text):
                print("Invalid mark.")
            elif add_mark(learners, number, int(text)):
                print("Mark added.")
            else:
                print("Learner not found.")
        elif choice == "5":
            number = input("Student number: ").strip()
            if delete_learner(learners, number):
                print("Learner deleted.")
            else:
                print("Learner not found.")
        elif choice == "6":
            show_ranking(learners)
        elif choice == "7":
            demonstrate_collections()
            demonstrate_algorithms()
        elif choice == "8":
            print("Goodbye.")
        else:
            print("Invalid choice. Enter 1 to 8.")


# 6.1 Test expected and actual outcomes
def run_tests():
    tests = [
        ("Empty list mean", None, mean_of([])),
        ("Empty list maximum", None, max_of([])),
        ("Empty list minimum", None, min_of([])),
        ("One mark mean", 65.0, mean_of([65])),
        ("Repeated marks count", 3, count_of([72, 72, 48, 72], 72)),
        ("Tied modes", [2, 3], mode_of([1, 2, 2, 3, 3])),
        ("Missing target", -1, find_first([65, 72], 99)),
        ("Missing learner", None, find_learner(learners, "9999999")),
        ("Bubble sort", [48, 48, 55, 65, 72, 72, 72, 90], bubble_sort([65, 72, 48, 90, 55, 72, 48, 72])),
    ]
    for name, expected, actual in tests:
        print(name, "| Expected:", expected, "| Actual:", actual,
              "|", "PASS" if expected == actual else "FAIL")


if __name__ == "__main__":
    main()
