import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

plt.rc('font',family = "Malgun Gothic")
#1. 카테고리별 리뷰 수 시각화
#각 카테고리(가족여행, 친구모임, 커플여행 등) 별로 리뷰 수를 시각화, 어떤 유형이 가장 많은가?

df = pd.read_csv('csv/07_hanatour.csv')

#카테고리별 리뷰 수
category_count = df['Category'].value_counts()


plt.figure(figsize = (15,6))
category_count.plot(kind='bar',color="skyblue")

#제목
plt.title("카테고리 별 리뷰 수")

#각 축의 이름
plt.xlabel("카테고리")
plt.ylabel("리뷰 수")

#x축의 각 elem의 이름을 rotation만큼 회전해서 표시한다.
plt.xticks(rotation=10)

#그래프 바탕?에 선 추가
#axis : 어떤 축 기준으로 격자를 표시할 것인가?
#linestyle : 격자는 어떤 식으로 표시할 것인가? 여기서는 선 스타일을 text로 전달함
#alpha : 격자선의 투명도를 조정한다. 0~1사이의 값을 입력.
plt.grid(axis="y",linestyle = "--", alpha=0.7)

#그래프나 표가 예쁘게 표시되도록 자동 맞춤
#화면에서 넘치지 않도록 조정.
plt.tight_layout()
#그래프를 표시한다.
plt.show()
