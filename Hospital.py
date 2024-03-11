from queue import Queue

patients_queue = Queue()
next_patient = Queue()

#Function to interact with desk manager
while True:
    print("Desk Manager System")
    print("1. Register Patient")
    print("2. Remove Patient after Meeting Doctor")
    print("3. Display Patient Queue")
    print("4. Exit")

    choice = input("Enter your choice: ")
 
#Function to register patient
    if choice == "1":
        name = input("Enter patient name: ")
        patients_queue.put(name)
        print(f"Patient '{name}' registered")

#Function to remove next patient after meeting the doctor
    elif choice == "2":
        if not patients_queue.empty():
            next_patient = patients_queue.get()
            print(f"patient {next_patient} removed after meeting the doctor")

#Function to display current patient
    elif choice == "3":
        if not patients_queue.empty():
            print("Current Patient Queue:")
            for index, patient in enumerate(list(patients_queue.queue), start=1):
                print(f"{index}. {patient}")
    else:
        print("exited.")





