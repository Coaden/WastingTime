#!/usr/bin/env python3

import cv2
import shutil


def charsToMap(chars):
    ascii_map = dict()
    for i in range(26):
        for j in range(10):
            ascii_map[i * 10 + j] = chars[i]
    return ascii_map


chars = "__Xx;;::,,..                          "
ascii_map = charsToMap(chars)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, shutil.get_terminal_size())
    img = cv2.flip(img, 1)  # Make it a mirror please
    # cv2.imshow("frame", img)
    screen = "\n".join(["".join([ascii_map[col] for col in row])
                        for row in img])
    print(screen, end="")
    cv2.waitKey(10)

# Release everything
cap.release()
cv2.destroyAllWindows()
