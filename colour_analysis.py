import cv2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
def extract_dominant_colors(image,k=5):
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    reshaped=image.reshape(-1,3)
    kmeans=KMeans(n_clusters=k, random_state=42)
    kmeans.fit(reshaped)
    colors=kmeans.cluster_centers_.astype(int)
    counts=np.bincount(kmeans.labels_)
    sorted_idx=np.argsort(counts)[::-1]
    colors=colors[sorted_idx]
    return colors
def color_harmony_score(image, k=5):
    colors = extract_dominant_colors(image, k)
    warm = cool = 0
    for color in colors:
        r, g, b = color
        hue = np.arctan2(np.sqrt(3) * (g - b), 2 * r - g - b)
        hue_deg = np.degrees(hue) % 360
        if 0 <= hue_deg <= 90 or 330 <= hue_deg <= 360:
            warm += 1
        else:
            cool += 1
        harmony = abs(warm - cool)
        if harmony == 0:
            score = 10
        elif harmony == 1:
            score = 8
        elif harmony == 2:
            score = 6
        elif harmony == 3:
            score = 4
        else:
            score = 2
        return score







