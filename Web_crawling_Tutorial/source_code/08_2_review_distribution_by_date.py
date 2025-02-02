import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib import dates as mdates

plt.rc('font',family = "Malgun Gothic")
#2. 날짜별 리뷰 분포 시각화
#날짜별로 리뷰가 어떻게 분포되어 있는지 시각화한다.
#특히 리뷰가 많거나 적은 때를 확인한다.
#날짜를 datetime형식으로 변환한다.

df = pd.read_csv('csv/07_hanatour.csv')

#시계열 데이터를 pd.to_datetime으로 타입 변환해준다.
df["Date"] = pd.to_datetime(df["Date"])

#날짜별 리뷰 수 계산
#value_counts로 날짜 별 리뷰를 추려주고, 그 객체의 sort_index메소드를 사용한다.
#Date가 index이므로 Date를 오름차순으로 정렬한다.
#datetime으로 타입 변환한 이유는 오름차순으로 정렬하기 편하도록 하기 위함.
date_counts = df["Date"].value_counts().sort_index()

plt.figure(figsize=(30,10))
#꺽은선 그래프를 생각하자.
#x축과 y축의 데이터를 셋팅하고,
#marker는 각 데이터를 표기. 여기서는 o로 표시함.
#color는 오랜지색으로 표시.
sns.lineplot(x=date_counts.index,y=date_counts.values, marker='o', color="orange")

plt.title("날짜별 리뷰 수")
plt.xlabel("날짜")
plt.ylabel("리뷰 수")

#xticks에 날짜 형식 설정.
#날짜 형식 파라미터는 구글링해서 알아보자.
date_format = mdates.DateFormatter('%Y-%m')
plt.gca().xaxis.set_major_formatter(date_format)
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=50)

plt.grid(axis = 'y',linestyle = "--",alpha = 0.7)
plt.tight_layout()
plt.show()

