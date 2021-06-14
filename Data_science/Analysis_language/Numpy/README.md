*Numpy (Numerical python)*
=====  
> Python에서 계산 작업을 편리하게 도와주는 도구  
  
  
*왜 중요한가?*
-----  
> numpy는 numpy array를 사용하며, python 리스트와 비슷한 개념  
> python의 긴 코드 작성은 --> 시간 소요  
> 이때, Numpy는 여러 값을 효율적으로 사용할 수 있다.  
  
  
*Python과 Numpy의 차이점*
-----  
> python은 리스트에 여러 값들이 들어갈 수 있다.  
> Ex) [10, 5, "Hello", True]  
  
> numpy는 한가지 타입만 들어갈 수 있다.  
> Ex_01) [1,2,5,4,8,9,10]  
> Ex_02) ["Hello","Dog","Alignment"]  
<br>
  

*언제 어떤것을 사용해야하는가?*
-----  
> 값을 추가하고 제거하는일에는 python 
> 수치 계산이 많고 복잡할 때 행렬같은 다차원 배열의 경우 numpy  
  
  
*Numpy library*
=====  
> numpy 라이브러리는 기본적인 통계 기능도 제공합니다.  


*최댓값, 최솟값*
-----  
> max 메소드와 min 메소드를 사용하면 numpy array의 최댓값과 최솟값을 구할 수 있습니다.  
```python
import numpy as np

array1 = np.array([14, 6, 13, 21, 23, 31, 9, 5])

print(array1.max()) # 최댓값
print(array1.min()) # 최솟값
```  
> 결과 값  
> 31, 5  
  

*평균 값*
-----  
> mean 메소드를 사용하면 numpy array의 평균값을 구할 수 있습니다.  
```python
import numpy as np

array1 = np.array([14, 6, 13, 21, 23, 31, 9, 5])

print(array1.mean()) # 평균값
```  
> 결과 값  
> 15.25  

> 위 예시에서, 총합(14 + 6 + 13 + 21 + 23 + 31 + 9 + 514+6+13+21+23+31+9+5)을 총 개수(88)로 나누면 15.2515.25입니다.  
  

*중앙 값*
-----  
> median 메소드를 사용하면 중간값을 구할 수 있는데요. 특이하게 median은 numpy array의 메소드가 아니라 numpy의 메소드입니다.  
```python
import numpy as np

array1 = np.array([8, 12, 9, 15, 16])
array2 = np.array([14, 6, 13, 21, 23, 31, 9, 5])

print(np.median(array1)) # 중앙값
print(np.median(array2)) # 중앙값
```  
> 결과 값  
> 12.0  
> 13.5  
> array1을 정렬하면 중앙값이 1212입니다.

> array2에는 짝수개의 요소가 있기 때문에 중앙값이 1313과 1414 두 개입니다. 둘의 평균값을 내면 13.513.5입니다.  
  

*표준 편차, 분산*
-----  
> 표준 편차와 분산은 값들이 평균에서 얼마나 떨어져 있는지 나타내는 지표입니다.  
```python
import numpy as np

array1 = np.array([14, 6, 13, 21, 23, 31, 9, 5])

print(array1.std()) # 표준 편차
print(array1.var()) # 분산
```  
> 결과 값  
> 8.496322733983215  
> 72.1875  
<br>

  
[Top Button](#)
