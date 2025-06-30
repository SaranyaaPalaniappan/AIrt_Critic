import cv2
import numpy as np
import pandas as pd
def composition_score(image):
    image=cv2.resize(image,(300,300))
    gray=cv2.cvtColor((image),cv2.COLOR_BGR2GRAY)
    edges=cv2.Canny(gray,50,150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return 2
    centers=[]
    for cnt in contours:
        M=cv2.moments(cnt)
        if(M["m00"])!=0:
            cx=int(M["m10"]/M["m00"])
            cy=int(M["m01"]/M["m00"])
            centers.append((cx,cy))
    thirds_x=[100,200]
    thirds_y=[100,200]
    score=2
    for(x,y) in centers:
        for tx in thirds_x:
            for ty in thirds_y:
                dist = np.sqrt((x - tx)**2 + (y - ty)**2)
                if dist<=30:
                    score+=2
    return min(score,10)
