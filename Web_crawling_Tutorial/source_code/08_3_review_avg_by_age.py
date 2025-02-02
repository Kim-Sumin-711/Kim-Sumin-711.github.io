import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

plt.rc('font',family = "Malgun Gothic")
df = pd.read_csv('csv/07_hanatour.csv')

#3. 나이별 평균 평점 비교
# 각 연령대별로 평균 평점을 비교해서 어떤 연령대가 평균적으로 좋은 리뷰를 남기는지 확인하자.

# 나이별 평균 평점 확인
# sort_values , sort_index : 평균값 오름차순 정렬, 나이대 오름차순 정렬
age_rating = df.groupby("Age")["Rating"].mean().sort_index()

plt.figure(figsize=(10,6))
sns.barplot(x=age_rating.index,y=age_rating.values,palette="viridis")

plt.title("나이별 평균 평점")
plt.xlabel("나이")
plt.ylabel("평균 평점")

#평점을 보니 전부 4점 이상이다. 그러니 y축의 범위를 재조정해보자.
plt.ylim(4,5)
#y축 리미트를 4와 5사이로 조정했다.

plt.xticks(rotation=45)
plt.grid(axis="y",linestyle = "--",alpha = 0.7)
plt.tight_layout()
plt.show()

#부록
#강의 자료가 촬영된 날에 데이터를 긁었을 때 age col에 날짜가 들어가는 경우도 있다고 하였다.
#지금은 괜찮은 듯.
#원인은 아마 어떤 정보가 부족해서 find_elements했을 때 개수 차이가 col에 따라 잘 정렬되지 않게 만든 듯.
#그런 경우는 이렇게 해결해보자.

#df_age = df[df["Age"].str.endswith('대')]
#df_age라는 새로운 df를 만들것이다. 여기서 df의 Age col을 series로 가져와서
#각 elem을 str로 변환한다. 그리고  '대'로 끝나는 아이들만 가져와서 df_age에 담는다.
#endswith는 ~~로 끝나는 친구들 찾을 때 쓰는 메소드이다.

#만일 Rating에 null값이 들어 있는 경우는 이렇게 해결하자.
#df_rating = df_age[df_age["Rating"].notnull()]
#df_age로 1차 걸러진 데이터에서 Rating항목이 null이 아닌 elem만 가져와서 저장한다.

