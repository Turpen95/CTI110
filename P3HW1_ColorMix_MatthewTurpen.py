#CTI-110
#P3HW1 - Color Mixer
#Matthew Turpen
#26 Feb 2020
##Recieve input of the first color.
##Recieve input of the second color.
##If color1 = red or blue and color2 = blue or red, print 'purple'.
##If color1 = red or yellow and color2 = yellow or red, print 'orange'.
##If color1 = blue or yellow and color2 = yellow or blue, print 'green'.
##else display an error and inform user what colors to use.
def main():  
    primaryColor = input('Enter your first color: ');
    secondaryColor = input('Enter your second color: ');
    if primaryColor == 'red' or 'blue' and secondaryColor == 'blue' or 'red':
        print('Red and blue makes purple.');
    elif primaryColor == 'red' or 'yellow' and secondaryColor == 'yellow' or 'red':
        print('Red and yellow makes orange.');
    elif primaryColor == 'blue' or 'yellow' and secondaryColor == 'yellow' or 'blue':
        print('Blue and yellow makes green.');
    else:
        print('Error. Please only use the colors: Red, blue or yellow');
main()
