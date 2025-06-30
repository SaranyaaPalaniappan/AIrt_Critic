import numpy as np
import pandas as pd
import colorsys
import cv2
def emotion_score(image):
    image=cv2.resize(image,(300,300))
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    reshaped=image.reshape(-1,3)
    brightness_values=[]
    saturation_values=[]
    for pixel in reshaped:
        r,g,b=pixel/255.0
        h,s,v=colorsys.rgb_to_hsv(r,g,b)
        brightness_values.append(v)
        saturation_values.append(s)
        avg_brightness=np.mean(brightness_values)
        avg_saturation=np.mean(saturation_values)
        if avg_brightness > 0.6 and avg_saturation > 0.5:
            emotion = "Happy"
        elif avg_brightness < 0.4 and avg_saturation < 0.4:
            emotion = "Sad"
        elif avg_brightness > 0.6 and avg_saturation < 0.4:
            emotion = "Calm"
        elif avg_brightness < 0.4 and avg_saturation > 0.5:
            emotion = "Angry"
        else:
            emotion = "Neutral"
            
        return emotion

        
    
