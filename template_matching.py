import cv2
import numpy as np

def solveAndFill(grid_map, img_rgb):
    for i in range(0, 6):
        ans = grid_map[i][0]
        if grid_map[i][1] == "-":
            ans = ans - grid_map[i][2]
        if grid_map[i][1] == "+":
            ans = ans + grid_map[i][2]
        if grid_map[i][3] == "-":
            ans = ans - grid_map[i][4]
        if grid_map[i][3] == "+":
            ans = ans + grid_map[i][4]
    	grid_map[i][5] = ans
        if ans > 9 or ans < 0:
            m = 50
        else:
            m = 25
        x, y = (550, i * 100 + 50)
        cv2.putText(img_rgb, str(ans), (x - m, y + 25), cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 4)
    cv2.imshow("Final", img_rgb)
    cv2.imwrite('Images\output.jpg', img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img_rgb = cv2.imread('Images\demo.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

grid_line_x = 7
grid_line_y = 7
m=600/(grid_line_x-1)
n=600/(grid_line_y-1)
grid_map = [ [ 0 for i in range(grid_line_y-1) ] for j in range(grid_line_x-1) ]

digits_img = [r"Images\Digits\0.jpg", r"Images\Digits\1.jpg", r"Images\Digits\2.jpg", r"Images\Digits\3.jpg", r"Images\Digits\4.jpg", 
                r"Images\Digits\5.jpg", r"Images\Digits\6.jpg", r"Images\Digits\7.jpg", r"Images\Digits\8.jpg", r"Images\Digits\9.jpg", 
                r"Images\Digits\minus.jpg", r"Images\Digits\plus.jpg"]

for i in range(0, 12):
    temp = cv2.imread(digits_img[i], 0)
    h, w = temp.shape
    cv2.rectangle(temp, (0, 0), (w, h), 0, 2)
    # Generates a grayscale image having pixel values according to what extent img and temp matches
    res = cv2.matchTemplate(img_gray, temp, cv2.TM_CCOEFF_NORMED) 
    if i in range(0, 10):
        threshold = 0.98
    elif i == 10:
        threshold = 0.95
    else:
        threshold = 0.99
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        i1 = pt[1] / n
        j1 = pt[0] / m
        if i in range(0, 10):
            grid_map[i1][j1] = i
        elif i == 10:
             grid_map[i1][j1] = "-"
        else:
            grid_map[i1][j1] = "+"
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)

print grid_map
cv2.imshow("Grid", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
for i in range(0, 6):
    for j in range(0, 6):
        if grid_map[i][j] == 0 and (j == 1 or j == 3):
            grid_map[i][j] = "+"
solveAndFill(grid_map, img_rgb)
"""
