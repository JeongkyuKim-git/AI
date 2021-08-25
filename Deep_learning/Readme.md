Deep Learning
=============  

> Artificial neural network (인공 신경망), Neural network representation (신경망 표현), Neural network learning (신경망 학습), Deep learning (딥러닝)  

*Example dataset MNIST? (숫자로 이루어진 이미지)*
-------------  
MNIST (Modified National Institute of Standards and Technology database)  

> 데이터셋 (이미지-사진 데이터)  
> 손 글씨로 쓴 숫자를 모아놓은 흑백 데이터로 총 6만 개의 학습 데이터와 만 개의 테스트 데이터가 존재한다.  
 
<img src="https://user-images.githubusercontent.com/66001539/118546551-12e4eb80-b793-11eb-8a8a-2206f50ac0d9.png" width="600px" height="300px" title="px(픽셀) 크기 설정" alt="MNIST"></img><br/>  

> 입력 변수: 픽셀 데이터  
> 출력 변수: 이미지가 나타내는 숫자  
 
> MNIST의 각 픽셀 데이터가 원래 회색 척도를 나타내는 건 맞지만 0~1 사이의 소수가 아니라 0&#126;255의 자연수로 표현된다. 하지만 min-max normalization이라는 전처리를 적용해 0&#126;255 사이의 자연수로 이뤄져 있는 각 픽셀 데이터를 모두 최댓값에서 최솟값을 뺀 값으로 (255-0 = 255)나누는 방식을 하여, Ex) 픽셀 값이 100이라면 100/255 = 0.39이다. 모든 데이터는 0-1사이 소수로 이루어져 있으며, 정사각형 MNIST 전체는 28*28 = 784개의 픽셀 데아터로 컴퓨터에서는 파이썬 리스트처럼 일렬로 정리되어 있다.  
> [0, 0, 0, 0, ..., 0.66, 0.12, 0.99, 0.80, 0.77, 0.55, ..., 0, 0, 0, 0]  

> 마지막으로 MNIST는 픽셀 값이외에도 어떤 숫자를 나타내는지에 대한 정보도 저장되어 있다. Ex) 5  
> ([0, 0, 0, 0, ..., 0.66, 0.12, 0.99, 0.80, 0.77, 0.55, ..., 0, 0, 0, 0], 5)  

[참조 내용-Codeit_Example_URL](https://www.codeit.kr/)  

[Top Button](#)
