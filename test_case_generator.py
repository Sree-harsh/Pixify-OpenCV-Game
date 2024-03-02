import os
import random
import time
import shutil
import cv2
import numpy as np

def slow_type(sentence):

    for letter in sentence:
        if letter == " ":
            time.sleep(random.choice([.05,.1,.15,.2,.25,.3,.35,.4,.45,.5, .55]))
        else:
            time.sleep(0.12)
        print(letter , end = "")

def random_word_generator():

    words_dict  = ["Pixplorer",
                   "Pixartist",
                   "Imagifer",
                   "Pixelcrafter",
                   "Pixelpizaaz",
                   "Pixel Prodigy",
                   "Snapsolver",
                   "Pixelpeek",
                   "Puzzlarama",
                   "Pixelizer",
                   "Pixelaazi",
                   "CyberSquirrel",
                   "PixelPirate",
                   "BinaryBanana",
                   "CodeChameleon",
                   "Quantumpatakka",
                   "SyntaxSasquatch",
                   "ASCIIAlligator",
                   "EncryptionElephant",
                   "CaffeineCircuit",
                   "BugBanisher",
                   "CyborgCheetah",
                   "CodeCheetah",
                   "ByteBison",
                   "QuantumQuesadilla",
                   "OpticOstrich",
                   "SightseeingSloth",
                   "GazeGiraffe",
                   "VisionaryVampire",
                   "PupilPython",
                   "GlanceGecko",
                   "CV_Coder_Cheetah",
                   "PythonVisionary",
                   "NumpyNarwhal",
                   "ContourCheetah",
                   "PixelPioneerPython",
                   "CannyCat",
                #    "ContourCheetah",
                #    "ContourCheetah",
                #    "ContourCheetah",
                #    "ContourCheetah",
                #    "ContourCheetah",
                #    "ContourCheetah",
                #    "ContourCheetah",
                #    "ContourCheetah",
                #    "ContourCheetah",
                #    "ContourCheetah",




                   ]
    #     "chudail":"Kitna hihi karegi",
    #     "Pixplorer": " ",
    #     "blahblah":"huh haaaa hu haaaa",
    #     "sree":"23",
    #     "sai":"56",
    #     "ram":"564",
    #     "senapati":"23455",
    #     "kuladeep":"23423",
    #     "pandiri":"234",
    #     "ganesh":"456",
    #     "health":"5678",
    #     "baaledhu":"567",
    # }
    word =random.choice(list(words_dict))
    # desc = words_dict[word]
    return word

def square_counter(alphabet):
    if alphabet == " " :
        letter_number = 32
    else:
        letter_number = ord(alphabet) - 96
    yellow_units = random.choice(list(range(0,letter_number+1,2)))
    yellow_squares = yellow_units/2
    red_squares_and_shapes = letter_number - yellow_units
    shapes_units = random.choice(list(range(0,red_squares_and_shapes+1)))
    red_squares = red_squares_and_shapes - shapes_units

    return yellow_squares , red_squares , shapes_units

def generate_test_case(no_of_yellow_squares , no_of_red_squares , shapes_units , letter_counter):

    squares = list(range(1,37))
    red_squares = []
    yellow_squares = []
    shapes_squares = random.sample(range(1,26),shapes_units)
    shapes=["square","circle","triangle"]
    colors = {"pink":(180,0,255),"green":(0,255,0),"orange":(0,127,255),"skyblue":(255,255,0)}

    for red_square in range(0,no_of_red_squares):

        element = random.choice(squares)
        red_squares+=[element]
        squares.remove(element)

    for yellow_square in range(0,no_of_yellow_squares):

        element = random.choice(squares)
        yellow_squares+=[element]
        squares.remove(element)

    # sample_img = cv2.imread("test_frame.png")
    sample_img = cv2.imread("sample_image_without_grid.png")

    for y in range(100,700,100):

        cv2.rectangle(sample_img,(95,y-5),(605,y+5),(0,0,0),-1)


    for x in range(100,700,100):

        cv2.rectangle(sample_img,(x-5,95),(x+5,605),(0,0,0),-1)

    for y in range(100,700,100):

        for x in range(100,700,100):

            cv2.rectangle(sample_img,(x-5,y-5),(x+5,y+5),(255,0,0),-1)

    cv2.putText(sample_img , "A" , (93,78),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,0),2 , cv2.LINE_AA)
    cv2.putText(sample_img , "B" , (193,78),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,0),2 , cv2.LINE_AA)
    cv2.putText(sample_img , "C" , (293,78),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,0),2 , cv2.LINE_AA)
    cv2.putText(sample_img , "D" , (393,78),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,0),2 , cv2.LINE_AA)
    cv2.putText(sample_img , "E" , (493,78),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,0),2 , cv2.LINE_AA)
    cv2.putText(sample_img , "F" , (593,78),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,0),2 , cv2.LINE_AA)

    cv2.putText(sample_img , "1" , (66,108),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,0),2 , cv2.LINE_AA)
    cv2.putText(sample_img , "2" , (66,208),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,0),2 , cv2.LINE_AA)
    cv2.putText(sample_img , "3" , (66,308),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,0),2 , cv2.LINE_AA)
    cv2.putText(sample_img , "4" , (66,408),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,0),2 , cv2.LINE_AA)
    cv2.putText(sample_img , "5" , (66,508),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,0),2 , cv2.LINE_AA)
    cv2.putText(sample_img , "6" , (66,608),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,0),2 , cv2.LINE_AA)

    for square in red_squares:

        if square%6==0:
            row_no = int(square/6) 
        else:
            row_no = int(square/6) + 1

        column_no = square - (row_no-1)*6
        # print(f"for {square} row is {x} and column in {y}")
        coordinate = (column_no*100 , row_no*100)

        cv2.rectangle(sample_img , (coordinate[0]-5 ,  coordinate[1]-5),(coordinate[0]+5 ,  coordinate[1]+5) , (0,0,255) , -1)

    for square in yellow_squares:

        if square%6==0:
            row_no = int(square/6) 
        else:
            row_no = int(square/6) + 1

        column_no = square - (row_no-1)*6
        # print(f"for {square} row is {x} and column in {y}")
        coordinate = (column_no*100 , row_no*100)

        cv2.rectangle(sample_img , (coordinate[0]-5 ,  coordinate[1]-5),(coordinate[0]+5 ,  coordinate[1]+5) , (0,255,255) , -1)
    
    for square in shapes_squares:

        #inside square 
        if square%5==0:
            row_no = int(square/5) 
        else:
            row_no = int(square/5) + 1

        column_no = square - (row_no-1)*5
        # print(f"for {square} row is {row_no} and column in {column_no}")
        centre_coordinate = (150 + (column_no-1)*100 , 150 + (row_no-1)*100)

        number_of_shapes = random.choice(range(1,5))

        shape_coordinates_key = {1:(centre_coordinate[0] - 20 , centre_coordinate[1] - 20) , 2:(centre_coordinate[0] + 20 , centre_coordinate[1] - 20),3:(centre_coordinate[0] - 20 , centre_coordinate[1] + 20),4: (centre_coordinate[0] + 20 , centre_coordinate[1] + 20)}

        # print(f"number of shapes in {square} are {number_of_shapes}")
        for shape_number in range(1,number_of_shapes+1):

            # print(f"shape centre coordinates are {shape_coordinates_key[shape_number]}")
            shape_coordinates = shape_coordinates_key[shape_number]

            shape = random.choice(shapes)
            # print(shape)
            shape_color = random.choice(list(colors.keys()))
            # print(shape_color)

            if shape == "square":
                cv2.rectangle(sample_img , (shape_coordinates[0]-10 ,  shape_coordinates[1]-10),(shape_coordinates[0]+10 ,  shape_coordinates[1]+10) , (colors[shape_color][0],colors[shape_color][1],colors[shape_color][2]) , -1)

            if shape == "circle":
                cv2.circle(sample_img , shape_coordinates , 10 ,(colors[shape_color][0],colors[shape_color][1],colors[shape_color][2]) , -1)
            
            if shape == "triangle":
                pt1 = (shape_coordinates[0], shape_coordinates[1] -11)
                pt2 = (shape_coordinates[0]-10,shape_coordinates[1] +9 )
                pt3 = (shape_coordinates[0]+10, shape_coordinates[1]+9)
                triangle_cnt = np.array( [pt1, pt2, pt3] )
                cv2.drawContours(sample_img, [triangle_cnt], 0, (colors[shape_color][0],colors[shape_color][1],colors[shape_color][2]), -1)
            
    cv2.imwrite(os.getcwd()+"/test_cases/test_image_"+str(letter_counter)+".png" , sample_img)



start = "\033[1m"
end = "\033[0;0m"   
# print("*************************************************************")
print("-------------------------------------------------------------------")
time.sleep(1)
print(f"Hello !!!!!!! \n{start}Welcome to Pixify Test Case Generator ........{end}")
time.sleep(0.75)
print("Please Enter your Name to generate a more personalized token for you :) --> " , end="")
name=input("")
time.sleep(0.5)
print("Acquiring Key Word ........")

cwd = os.getcwd()
dir = cwd+"\\test_cases"
# print(dir)
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)
print("Generating appropriate test cases ........")

word= random_word_generator()
word += " " + name.lower()
word = word.lower()
letter_counter = 1
print(f"word is {word}")
for letter in word:
    no_of_yellow_squares , no_of_red_squares , shapes_units = square_counter(letter)
    generate_test_case(int(no_of_yellow_squares) , no_of_red_squares , shapes_units , letter_counter)
    letter_counter+=1

time.sleep(2)
# print("\nTese cases generated !!!")
print("Test cases generated !!!" )
print(f"Test cases saved to {dir}")

print(f"There you go {start}{name}{end}, hope you {start}Pixify{end} the code-word embedded in the images correctly XD ..... ")