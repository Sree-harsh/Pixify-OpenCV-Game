import numpy as np
import cv2
import os
import sys
import time
import random
import pixify_decode



def slow_type(sentence):
    for letter in sentence:
        if letter == " ":
            time.sleep(random.choice([.05,.1,.15,.2,.25,.3,.35,.4,.45,.5, .55]))
        else:
            time.sleep(0.12)
        print(letter , end = "")

def generate_code(image):

    yellow_squares = 0
    red_squares = 0
    shape_squares = 0

    for x in range(100,700,100):
        for y in range(100,700,100):
            pix = image[y,x]
            # print(pix)
            if np.array_equal(pix,np.array([0,255,255])):#pix.any() == np.array([0,255,255]):
                yellow_squares+=1
            elif np.array_equal(pix,np.array([0,0,255])):
                red_squares+=1

    for x in range(150,650,100):
        for y in range(150,650,100):
            if not np.array_equal(image[x-20,y-20],np.array([255,255,255])):
                shape_squares+=1
                continue
            elif not np.array_equal(image[x+20,y-20],np.array([255,255,255])):
                shape_squares+=1
                continue
            elif not np.array_equal(image[x-20,y+20],np.array([255,255,255])):
                shape_squares+=1
                continue
            elif not np.array_equal(image[x+20,y+20],np.array([255,255,255])):
                shape_squares+=1
                continue
        pass
    if yellow_squares*2+red_squares+shape_squares == 32:
        return " "
    else:
        return chr(yellow_squares*2+red_squares+shape_squares+96)

words_dict  = {
        "pixplorer":"You were a Pixplorer, navigating the binary landscapes and unraveling the mysteries of code to craft your own digital masterpiece",
        "pixartist":"You were a Pixartist, weaving pixels into a symphony of visual wonders, turning code into your vibrant canvas of digital artistry",
        "imagifer":"You were an Imagifer, sculpting dreams and breathing life into the code, forging a world where imagination and technology converge in a harmonious dance",
        "pixelcrafter":"You were a Pixelcrafter, melding the digital hues of code into a masterpiece, each line a stroke, every algorithm a chapter in your visual saga of creative ingenuity",
        "pixelpizaaz":"You were a Pixelpizaaz, infusing your code with a dash of digital dazzle, turning algorithms into a vibrant spectacle of creativity and flair",
        "pixelprodigy":"You emerged as a PixelProdigy, orchestrating symphonies of code to create visual masterpieces, transcending the binary canvas with an innate brilliance that defined your coding journey",
        "snapsolver":"As a Snapsolver, you transformed code challenges into visual epiphanies, capturing the essence of problem-solving in each pixel, creating a dynamic mosaic of solutions",
        "pixelpeek":"Unveiling the unseen, you were a PixelPeek, delving into code's hidden realms to reveal the intricate details, your digital curiosity shaping a mosaic of insight and discovery",
        "puzzlarama":"In the grand Puzzlarama, you wove intricate code puzzles into a vibrant tapestry of challenges, each solved piece contributing to the mosaic of your coding expertise",
        "pixelizer":"As a Pixelizer, you enchanted the code, pixel by pixel, crafting a digital dreamscape where every algorithmic stroke brought life to a mesmerizing symphony of visual enchantment",
        "pixelaazi":"Within the realm of Pixelaazi, you conjured digital magic, infusing code with a whimsical touch, transforming algorithms into a visual spell that painted the canvas of your coding prowess",
        "cybersquirrel":"In the virtual treetops of code, you thrived as a CyberSquirrel, navigating the branches of algorithms with nimble precision, collecting bytes and acorns to build a nest of digital mastery",
        "pixelpirate":"As the PixelPirate, you sailed the binary seas, plundering lines of code to uncover hidden treasures, leaving a trail of creativity and mischief in your wake",
        "binarybanana":"As the BinaryBanana enthusiast, you peeled away the layers of code, revealing a potassium-rich tapestry of digital delights, turning algorithms into a vibrant banana-coded masterpiece",
    }


start = "\033[1m"
end = "\033[0;0m"
print("Welcome to Pixify Code Verifying executable ........")
time.sleep(0.5)
print("Please enter your Name (as entered while generating test cases) to verify the authenticity of the test cases :) --> ", end="")
name=input("")
# print("Acquiring Key Word ........")
dir = os.getcwd()
list_dir = os.listdir(dir+"/test_cases/")
code_sree =""
result = ""
go = True
if len(list_dir) == 0:
    time.sleep(0.5)
    print(f"No files present in {dir}\\test_cases\\")
    go = False
else:
    time.sleep(0.5)
    print(f"found {len(list_dir)} files in {dir}\\test_cases\\")
    for i in range(1, len(list_dir)+1):
        image_file_name = "test_image_"+str(i)+".png"
        if image_file_name in list_dir:
            code_sree+= generate_code(cv2.imread(dir+"\\test_cases\\"+image_file_name))
        else:
            time.sleep(0.5)
            print(start+"Inorrect file name / something other than test image found !!!!!! Aborting !!!!"+end)
            go = False
            break
    
    if go:
        time.sleep(1)
        print("Verifying authenticity of the generated test cases")
        if name.lower() in code_sree :
            time.sleep(0.5)
            print("Genuine test cases ! Press Enter to check your code's solution" , end = " ")
            m = input()
            print()
            for i in range(1, len(list_dir)+1):
                image_file_name = "test_image_"+str(i)+".png"
                print("*******************************************************************")
                print(f"Testing your code on {image_file_name}")
                word_user = pixify_decode.decode(cv2.imread(dir+"\\test_cases\\"+image_file_name))
                result+=word_user
                print(f"letter generated :- {word_user}")
                time.sleep(1.5)
            print("*******************************************************************")
            print(f"Code-word decoded by player's program: {result}")
            print("-------------------------------------------------------------------")
            if result == code_sree:
                name_modified = " "+name
                str_list = code_sree.split(name_modified)
                time.sleep(1)
                # print("CoNgRaTuLaTiOnS!! You were able to PIXIFY the code embedded with ease ..... Hope you had a great time getting your hands on OPENCV. BTW , we did observe something based on your coding skills :)")
                if str_list[0] in list(words_dict.keys()):
                    print(start+"CoNgRaTuLaTiOnS!! You were able to PIXIFY the code embedded with ease ..... Hope you had a great time getting your hands on OPENCV. BTW "+str(name)+ ", we did observe something based on your coding skills :)"+end)
                    desc = words_dict[str_list[0]]
                    result = result.title()
                    time.sleep(0.5)
                    print("-------------------------------------------------------------------")
                    time.sleep(1)
                    print(f"{result} :- {desc}")
                    print("Have a Great day ahead !!!")
                else:
                    print(start+"CoNgRaTuLaTiOnS!! You were able to PIXIFY the code embedded with ease ..... Hope you had a great time getting your hands on OPENCV."+end)
        else:
            time.sleep(1)
            print(f"{start}Test cases not generated by {name}. Make sure you run the test_case_generator.exe beforehand{end}")

