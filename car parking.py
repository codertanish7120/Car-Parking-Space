import cv2
import pickle

image = cv2.imread('carParkImg.png')

width, height = 78, 28

try:
    with open('CarParkPos', 'rb') as f:
        posList=pickle.load(f)
except:
     posList = []

def mouseClick(events, x,y,flags,parameters):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1,y1=pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)

    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)

while True:
    image = cv2.imread('carParkImg.png')
    for pos in posList:
        cv2.rectangle(image,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)

    cv2.imshow("Image",image)
    cv2.setMouseCallback("Image",mouseClick)
    cv2.waitKey(1)
