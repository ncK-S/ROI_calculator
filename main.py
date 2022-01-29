class Calculator:
    def calcROI(self, a, b):
        return (b/a) * 100
# to determine ROI, divide income generated by the property (B)
# by the ammount of your out of pocket expenses on the 
# property (A). then multiply the quotient by 100 to achieve a percentage.
my_roi = Calculator()
#creating calculator object^
while True:

    print("1: Calculate ROI")
    print("2: Exit")
    
    user = int(input("Select action: "))
    
    
    if user in (1, 2):
        
        #option for user to exit program
        if(user == 2):
            print('goodbye')
            break
        
        #if user selects 1, run methods        
        a = int(input("How much were your out of pocket expenses on the property?: "))
        b = int(input("How much did you generate in income from the property?: "))
        
        if(user == 1):
            print(f" You returned", my_roi.calcROI(a, b), "% on your investment")
        
    
    else:
        print("Invalid Input")
# this calculator is calculating annual ROI

