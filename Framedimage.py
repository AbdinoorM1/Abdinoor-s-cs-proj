# ----------------------------------------
# Integrity pledge: This work is my own A.M
# Name: Abdinoor Moallin
# Program: L10Q1AM.py
# ----------------------------------------
# Purpose: fixing a frame, creating a new image, pasting new image on frame
# ----------------------------------------
from PIL import Image, ImageDraw

def fix_frame(file_name):
#Purpose: fixes the frame, resizes/rotates/pastes the crops onto fixed frame. 
    
    image = Image.open("broken_600.png")
    width, height = image.size    
    print("Width , height=", width,height)
    green_crop = image.crop(( width//2 , height//4 , width , int(height* 0.75)))
    green_crop = green_crop.resize((width//2,height//2))
    print("Green crop size =", green_crop.size)
    rotated_green = green_crop.transpose(Image.ROTATE_180)
    
    yellow_crop = image.crop(( width//4, height*0, width//2, height//2))
    yellow_crop = yellow_crop.resize((width//2,height//2))
    print("yellow crop size =", yellow_crop.size)
    
    blue_crop = image.crop(( width*0, height//2, width//4, int(height * 0.75)))
    blue_crop = blue_crop.resize((width//2,height//2))
    print("blue crop size =", blue_crop.size)
    rotated_blue = blue_crop.transpose(Image.ROTATE_270)  
    
    red_crop = image.crop(( width//4, int(height * 0.75), width//2, height))
    red_crop = red_crop.resize((width//2,height//2))
    print("red crop size =", red_crop.size)
    rotated_red = red_crop.transpose(Image.ROTATE_90)

    pasted_frame = Image.new ("RGB", (width,height), (255, 255, 255))
    print("Pasted frame size =", pasted_frame.size)
    print("Complete frame size =",pasted_frame.size)

    pasted_frame.paste(rotated_red, (width*0,height*0)) 
    pasted_frame.paste(rotated_blue, (width//2,height*0))
    pasted_frame.paste(yellow_crop, (width*0,height//2)) 
    pasted_frame.paste(rotated_green, (width//2,height//2))     
    
    return pasted_frame


def draw_picture():
#Purpose: Draws the shapes created, pastes it on complete frame
    
    picture = Image.new("RGB", (200,200), (107,107,107))
    shapes = ImageDraw.Draw(picture)
    shapes.ellipse((0, 0, 50, 50), fill=(0, 0, 0)) 
    shapes.ellipse((20, 0, 40, 50), fill=(255, 255, 0 )) 
    shapes.ellipse((140, 0, 200, 50), fill=(0, 0, 0)) 
    shapes.ellipse((168, 0, 188, 50), fill=(255, 255, 0 )) 
    shapes.rectangle((0, 70 , 200, 100), fill=(255, 0, 0))
    shapes.rectangle((0, 150 , 200, 180), fill=(255, 0, 0))
    shapes.polygon([(10, 100) , (20, 150), (30,100)], fill=(255, 255, 255))
    shapes.polygon([(170, 100) , (180, 150), (190,100)], fill=(255, 255, 255))
    shapes.line([(65, 10), (90, 50)], 10)
    shapes.line([(115, 10), (90, 50)], 10)
    shapes.text((120,180), "Angry Vampire.", (201,194,252))
    
    return picture


def frame_picture(file_name):
#Purpose: Main function calls 2 helper functions, resizes image, shows the final framed picture
    
    complete_frame = fix_frame(file_name)    
    width,height = complete_frame.size
    complete_image = draw_picture()
    complete_image = complete_image.resize((int(width*0.80), int(height*0.80)))
    complete_frame.paste(complete_image, (int(width*0.10), int(height*0.10)))
    complete_frame.show()
    
frame_picture("broken_600.png")
