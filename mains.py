import cv2
import label as lb
MIN_WIDTH, MIN_HEIGHT = 3, 8
MIN_RATIO, MAX_RATIO = 0.3, 1.0
MIN_AREA = 80
car_img = cv2.imread("temp2.png")
plate_img = lb.labeling_bulid_1(car_img)
     # 라벨링이 끝난 번호를 반환합니다
result_char = lb.labeling_bulid_2(MIN_AREA, MIN_WIDTH, MIN_HEIGHT, MIN_RATIO, MAX_RATIO, plate_img)
max_len = len(result_char) - 1
correction_char = ''
if result_char[max_len] < '0' or result_char[max_len] > '9' :
    for i in range(0, max_len) :
        correction_char += result_char[i]
    result_char = correction_char
print(result_char)