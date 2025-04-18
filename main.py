from pet import Pet

def print_menu():
    print("\n===== DIGITAL PET SIMULATOR =====")
    print("1. Feed your pet")
    print("2. Let your pet sleep")
    print("3. Play with your pet")
    print("4. Check pet status")
    print("5. Train pet a new trick")
    print("6. Show pet's tricks")
    print("7. Exit")
    print("================================")

def main():
    print("🐶 Welcome to the Digital Pet Simulator! 🐱")
    pet_name = input("What would you like to name your pet? ")
    pet_type = input("What type of animal is your pet? ")
    
    my_pet = Pet(pet_name)
    
    print(f"\nYou now have a {pet_type} named {pet_name}!")
    print(f"Take good care of {pet_name} by feeding, playing, and letting them rest.")
    
    while True:
        print_menu()
        choice = input("What would you like to do? (1-7): ")
        
        if choice == "1":
            my_pet.eat()
        elif choice == "2":
            my_pet.sleep()
        elif choice == "3":
            my_pet.play()
        elif choice == "4":
            my_pet.get_status()
        elif choice == "5":
            trick = input("What trick would you like to teach your pet? ")
            my_pet.train(trick)
        elif choice == "6":
            my_pet.show_tricks()
        elif choice == "7":
            print(f"Goodbye! {pet_name} will miss you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()