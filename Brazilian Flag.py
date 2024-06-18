# ----------------------------------------
# Integrity pledge: This work is my own A.M
# Name: Abdinoor Moallin
# Program: Brazillian Flag.py
# ----------------------------------------
# Purpose: To recreate the flag of Brasil using Image & ImageDraw.
# ----------------------------------------

from PIL import Image, ImageDraw

def draw_background():
#Purpose: Creates a new image of size: (800,600) and returns it 
#New image is the background of flag 
    
    outer_green = Image.new("RGB", (800,560), color = (4, 156, 73))
    width, height = outer_green.size
    print("\nWidth of flag is:", width, "\n\nHeight of flag is:", height)
    
    return outer_green
    

def shape(): 
#Purpose: To create a yellow diamond centered in the middle of the flag, returns diamond 
    
    im = Image.new("RGB", (800,560), (4,156,73))
    width,height = im.size 
    
    diamond_x = 370
    diamond_y= 240
    
    shape = ImageDraw.Draw(im)
    shape.polygon([(width//2, height//2 - diamond_y),(width//2 + diamond_x, height//2),(width//2, height//2 + diamond_y),(width//2 - diamond_x, height//2)], fill=(254,224,0)) 

    return im   


def sphere():
# Purpose: This function imports the circle and resizes it, then it iterates through the pixels to change them to their proper colors
    
    middle_circle = Image.open("/Users/Abdinoor/CMPT 101/circle.png")
    
    width, height = middle_circle.size
        
    print("\nOriginal circle width:", width, " Original circle height:", height)
    
    new_width = int(width * 0.95) 
    new_height = int(height * 0.95)  
    middle_circle = middle_circle.resize((new_width, new_height))
    
    print("\nNew circle width:", new_width, " New circle height:", new_height)
    
    circle_background = (0, 255, 0)
    wanted_background = (254, 224, 0)
    
    for x in range(new_width): # Need nested for loop to iterate pixels
        for y in range(new_height):
            if middle_circle.getpixel((x, y)) == circle_background:
                middle_circle.putpixel((x, y), wanted_background)
                    
    return middle_circle

def complete_image():
# Purpose: Main function, Calls all helper functions and shows the complete image, also centers the shapes on the background
    
    flag = draw_background()
    width, height = flag.size
    yellow_diamond = shape()
    d_width, d_height = yellow_diamond.size
    
    pasted_x = (width - d_width) // 2
    pasted_y = (height - d_height) // 2
    
    flag.paste(yellow_diamond, (pasted_x, pasted_y))
    
    circle = sphere()
    
    flag.paste(circle, (int(width*0.32), int(height*0.25)))
    
    flag.show()

complete_image()