# Korea_car_number_detector

원본 소스(Reference) : https://github.com/Mactto/License_Plate_Recognition  

The program code was written using Python and Opencv, and it is a program source that Detecting Republic of Korea Detection and Labeling car number

해당 프로그램 코드는 Python, Opencv를 이용하여 대한민국의 차량 번호판을 탐지하고 라벨링된 차량 번호를 반환하는 프로그램 입니다.

Improved recognition from existing references and added vehicle number correction.

위에 명시한 레퍼런스 소스에서 정확도를 향상시키고 성능을 개선하였습니다.  

파일 확장자는 .png 파일로 테스트 해보는 것을 권장하며 Object Detection 모델과 함께 사용하거나 CCTV등 범용성을 높인 리소스입니다.

테스트에 사용된 이미지 : 아반떼MD, 그랜저 IG, 쉐보레 말리부

아반떼 외 이미지는 구글에서 다운 받은 이미지로 문제가 생길 시 바로 삭제하겠습니다.

거의 라인바이 라인으로 주석을 쳐놨으나 주석과 기능이 일치 하지 않을 수 있습니다. 이 점은 지속적으로 개선 하겠습니다.  

이미지를 테스트 할 때 이미지의 파일 타입은 .png를 권장하며, 만약 오류가 난다면 .shape 함수를 이용하여 height, width를 확인하세요.  
height는 800, width 는 1000 미만의 크기로 resize 하는 것을 권장합니다.

1차 수정

연속으로 2장 이상 프로세싱 시도 시 2회 이후 부터는 번호판이 부풀려 지는 현상 해결  

2차 수정  

연속으로 2장 이상 입력 시 컨투어가 충돌나는 현상 해결



# Program excute image

![캡처](https://user-images.githubusercontent.com/83262616/167460854-fd9677be-3b76-4197-91db-443080e5a725.PNG)
