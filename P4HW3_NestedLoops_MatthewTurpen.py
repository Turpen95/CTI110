#Nested Loops
#9 March 2020
#CTI-110 P4HW3
#Matthew Turpen

def main():
#Denote decision for range of 6
#if false end, else print"#'
#Denote another decison
#if false print '#' else print ' '
    
    for r in range(0, 6):
        print('#', end='')
        for c in range(r):
            print(' ', end='')
        print('#')
        
main()
        
