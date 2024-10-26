# Jose Franco
# 10/22/2024
# Assignment 1.3 - On the Wall + Flowchart

# Loop to print the number of bottles
def beer_countdown(bottles):
    while bottles > 1:
        print(f"\n{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles -= 1
        print(f"Take one down and pass it around, {bottles} bottle{'s' if bottles != 1 else ''} of beer on the wall.")

    # Handle the last bottle
    print(f"\n{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
    print("Take it down and pass it around, no more bottles of beer on the wall.")

# Ask the user for the number of bottles.
def main():
    while True:
        try:
         bottles = int(input("How many bottles of beer are on the wall? "))
         if bottles < 1:
             #Error if user enters a number less than 1  
             print("\nThere is no song if we have no bottles. Please enter a number greater than zero.\n")
         else:
              beer_countdown(bottles)
              print("\nTime to buy more bottles of beer!")
              break
        except ValueError:
            #Error if user enters a non integer value
            print("\nInvalid input. Please enter a positive integer.\n")

if __name__ == "__main__":
    main()
