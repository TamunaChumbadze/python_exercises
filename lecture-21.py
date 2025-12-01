def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"
    # print(f"{student[0]} from {student[1]}")
    print(f"{student['name']} from {student['house']}")

def get_student():
    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__": # ახორციელებს მხოლოდ მაშინ, როცა ფაილი პირდაპირ არის გაშვებული, სხვა შემთხვევაში არა
    main()

# გავაგრძელებთ შემდეგზეეე :დ :დ