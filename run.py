import fpstimer
import cv2
import numpy as np
from playsound import playsound
import os.path
from os import path

#ASCI CHARACTERS
ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]{?}-_+~<>i!lI;:,\"^`'. "
gscale2 = " ."
gscale3 = ".$"

#Get Video
video = cv2.VideoCapture('video.mp4')
convertedWidth = 92
FRAMES_DIR = "./frames/"


def getImage(count):

    hasFrames,image = video.read()
    if hasFrames:
        # Resize image
        width = image.shape[1]
        height = image.shape[0]
        ratio = height / width
        
        newHeight = int(ratio * convertedWidth)
        resizedImage = cv2.resize(image,(convertedWidth, newHeight))

        #grayscale convert to black and white
        grayImage = cv2.cvtColor(resizedImage, cv2.COLOR_BGR2GRAY)
        (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    
        # cv2.imwrite("frames/image"+str(count)+".jpg", grayImage)
        newWidth = blackAndWhiteImage.shape[1]
        
        #convert to characters
        characters = "".join([gscale3[int(pixel // 255) ] for pixel in np.nditer(blackAndWhiteImage)])

        #convert to ascii 'image'
        pixelCount = len(characters)
        asciiImage = "\n".join(characters[i:(i+newWidth)]for i in range(0, pixelCount, newWidth))
        
        # write to txt file -> this is bad cuz large file size 
        output = "./frames/" + "frame" + str(count) + ".txt" 
        f = open(output, 'w', encoding="utf-8")
        for row in asciiImage: 
            f.write(row)
        # print(asciiImage)
    return hasFrames
    
def main():
    count = 0
    fps = 30
    

    if (not path.exists('./frames')):
        print("frame folder not found, creating frame folder")
        os.mkdir("frames")

    total = len([name for name in os.listdir('./frames')])
    if (total < 6572):
        print("preparing frames...")
        success = getImage(count)
        while success:
            count += 1       
            success = getImage(count)
        total = len([name for name in os.listdir('./frames')])
    os.system("cls")
    timer = fpstimer.FPSTimer(float(fps)) 
    playsound('music.mp3', False)
    for i in range(total):
        file = open(FRAMES_DIR + "frame" + str(i) + ".txt","r", encoding="utf-8")
        asciiImage = file.read()
        print(asciiImage)
        timer.sleep()
    

   


os.system("mode con: cols=92 lines=66")
main()
 # image = Image.open("./frames/" + "image" + str(i) + ".jpg")
        # # newImage = resize(image);
        # pixels = greyscaleData(image)
        # characters = "".join([gscale1[int(pixel / 3.7) ] for pixel in pixels])
        # width, height = image.size
        # pixelCount = len(characters)
        # asciiImage = "\n".join(characters[i:(i+width)]for i in range(0, pixelCount, width))