#Program to convert miles to Kilometers.
def main():
    #Display the intro screen.
    intro()
#Try-Except function
    try:
    #Get the number of miles.
      miles_requested = float(input('Please, enter the number of miles you have driven: '))
#Convert the miles to kilometers.
      miles_a_km(miles_requested)
    except:
    #Display an error message.
      print()
      print('Please try again using numbers only.')
      print()
      print()
      main()
#The intro function displays an introductory screen.
def intro():
    print ('Welcome to the miles-kilometers convertor.')
    print()
    print('For your reference 1 mile equals to 1.60934 kilometers.')
#The miles_a_km function accepts a number of miles and displays the equivalent number of kilometers.
def miles_a_km(miles):
    km = miles * 1.60934
    print()
    print('Total of miles driven', miles, 'miles.')
    print('Equivalent distance in kilometers', km, 'kilometers.')
    print('Drive safe, and have a nice day.')
#Call the main function
main()