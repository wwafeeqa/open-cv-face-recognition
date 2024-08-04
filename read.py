import cv2 as cv
# reading photos
# img = cv.imread('photos/a_cat.jpg')

# cv.imshow('Cat', img)

# cv.waitKey(0)

#reading videos

capture = cv.VideoCapture('media/cat_vid.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('cat video', frame)

    if cv.waitKey(20) & 0xff==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
