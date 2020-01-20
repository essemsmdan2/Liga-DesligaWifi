import pyautogui
import sys

input('bitch! show me where to click you lazy punk!')
x, y = pyautogui.position()

input('bitch! show me where to click you lazy punk![2]')
x1, y1 = pyautogui.position()

input('bitch! show me where to click you lazy punk![3]')
x2, y2 = pyautogui.position()

input('bitch! show me where to click you lazy punk![4]')
x3, y3 = pyautogui.position()

input('bitch! show me where to click you lazy punk![5]')
x4, y4 = pyautogui.position()
input('bitch! show me where to click you lazy punk![6]')
x5, y5 = pyautogui.position()


result = f'[[{x},{y}],[{x1},{y1}],[{x2},{y2}],[{x3},{y3}],[{x4},{y4}],[{x5},{y5}]]'
print(result)

xy = result

for count, ele in enumerate(xy):
    pyautogui.moveTo(xy[count][0], xy[count][1], .25)
    print(xy[count][0], xy[count][1])
    print('click!')
    pyautogui.click()
