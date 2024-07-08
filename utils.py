import re
import numpy as np

def filter_plate(text):

    plate = []
    for string in text:
        filtered_string = re.sub(r'[^A-Za-z0-9]', '', string)

        if len(filtered_string) == 6:
            plate.append(filtered_string.upper())
            
    return plate

sharp_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])