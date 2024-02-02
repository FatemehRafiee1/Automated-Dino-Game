import time
import pyautogui   as pg
from PIL import ImageGrab

def locate_on_screen(path):
    pg.useImageNotFoundException()
    try:
        location = pg.locateOnScreen(path, confidence=0.96)
        print(location)
        return location
    except pg.ImageNotFoundException:
        print(f'Cannot locate {path}')
        return None      

def calc_pos(location):
    try:
        x, y = pg.center(location)
        return x, y
    except ValueError:
        return -1, -1

def click_on_image(image_path, timeout=1):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            center_x, center_y = calc_pos(locate_on_screen(image_path))
            pg.click(center_x, center_y)
            return 
        except:
            print(f'cannot click on {image_path}.')

def capture_and_check_for_green(left, top, right, bottom):
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

    if is_green_pixel_present(screenshot):
        pg.keyDown('space')
        print("Cactus found.")
    else: 
        print("No cactus.")

def is_green_pixel_present(image):
    # Iterate through each pixel to find a green one
    width, height = image.size
    for x in range(width):
        for y in range(height): 
            pixel = image.getpixel((x, y))
            # Check if the pixel is green 
            if pixel[0] == 64 and pixel[1] == 144 and pixel[2] == 22:
                return True 
    return False 

click_on_image('C:/Users/LENOVO/Felicity/pg/dino.png')
pg.press('space')
click_on_image('C:/Users/LENOVO/Felicity/pg/gov.png')
                         
t0 = time.time()
while time.time() - t0 < 30:
    # Capture a region from (x=220, y=300) to (x=330, y=470)
    capture_and_check_for_green(220, 300, 330 , 470)

