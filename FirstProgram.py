#FirstProgram.py
#Name: Nidhi Agarwal
#Date: 01/21/2025
#Assignment: 1

def main():
  print("First Program")
  
  print ("Hello")
  name = input ("What is your name?")
  print(f"Nice to meet you, {name}!")
  age = int(input("How old are you? "))
  current_year = 2026
  print(f"Current Year, {current_year}!")
  birth_year = current_year - age
  print(f"You were born in {birth_year}.")

if __name__ == '__main__':
    main()   