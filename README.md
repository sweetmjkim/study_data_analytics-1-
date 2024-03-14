# study_data_analytics

<details open>
<summary>
  <h2>PANDAS</h2>
</summary>

|구분|이름|설명|비고|
|--|--|--|--|
|0|[정리본](https://github.com/nohjuhyeon/study_data_analytics/wiki/Pandas)|정리본|
|1|[Series](./docs/pandas/01_pandas_series.ipynb)|pandas의 series에 대하여 이해하기||
|2|[DataFrame](./docs/pandas/02_pandas_DataFrame_iloc.ipynb)|pandas의 Dataframe에 대하여 이해하기||
|3-1|[Datetime](./docs/pandas/03_1_pandas_datetimes.ipynb)|날짜형 데이터 다루기||
|3-2|[Datetime(python)](./docs/pandas/03_1_pandas_datetimes.py)|날짜형 데이터 다루기(python)||
|5|[change Datetime](./docs/pandas/04_pandas_apply.py)|datetime 변환하기||
|5|[Datatype](./docs/pandas/05_pandas_TitanicFromDisaster_train.ipynb)|데이터 타입 이해하기<br/>데이터 타입 변환하기||
|6|[Pivot table](./docs/pandas/06_pandas_aggregations.ipynb)|pivot table 다루기||
|7|[Filtering](./docs/pandas/07_pandas_filtering_conditional.ipynb)|데이터 필터링 하기||
|8|[Preprocessing-missing values](./docs/pandas/08_pandas_preprocessing_missingvalues.ipynb)|결측치 전처리 하기||
|9|[Preprocessing-outlier](./docs/pandas/09_pandas_preprocessing_outlier.ipynb)|이상치 전처리 하기||
|10-1|[Data segmentation 1](./docs/pandas/10_1_pandas_usefuls.ipynb)|연속형 데이터를 범주형 데이터로 변환하기|.cut()|
|10-2|[Data segementation 2 & excel read](10_2_pandas_usefuls./docs/pandas/.ipynb)|연속형 데이터를 범주형 데이터로 변환하기<br>excel 파일 가져오기||
|11|[Data merge](./docs/pandas/11_pandas_merges.ipynb)|데이터 병합하기||
|12|[Drop duplicate](./docs/pandas/12_drop_duplicates.ipynb)|중복값 제거||
</details>

<details open>
<summary><h2>VISUALIZATION</h2></summary>

|구분|이름|설명|비고|
|--|--|--|--|
|0|[정리본](https://github.com/nohjuhyeon/study_data_analytics/wiki/Visualization)|정리본|
|1|[matplotlib](./docs/visualization/01_visualization_matplotlib_simple_korean.ipynb)|matplotlib 사용하여 시각화하기||
|2|[series visualization](./docs/visualization/02.visualization_univariate.ipynb)|단일변수 시각화하기|countplot : 막대그래프<br/>boxplot : 데이터 분포 확인과 이상값  찾기|
|3|[Data Frame visualization](./docs/visualization/03_visuallization_multivariate.ipynb)|다변수 시각화하기|barplot : 막대그래프<br/>boxplot : 데이터 분포 확인과 이상값 찾기<br/>scatterplot(산점도)<br/>lmplot : 산점도와 회귀선 같이 확인<br/>jointplot : 산점도와 히스토그램 같이 확인<br/>corr : 상관관계 수치로 확인<br/>pairplot : 상관관계 그래프로 확인<br/>lineplot : 선그래프|
|4|[visualization example](./docs/visualization/04_visualization_example.ipynb)|시각화 활용 예시||
</details>

<details open>
<summary><h2>EDA</h2></summary>

|구분|이름|설명|비고|
|--|--|--|--|
|0-1|[Data analysis : 정리본](https://github.com/nohjuhyeon/study_data_analytics/wiki/03-:-Data-Analysis)|정리본 : 데이터 분석|
|0-2|[DDA : 정리본](https://github.com/nohjuhyeon/study_data_analytics/wiki/03‐1-:-DDA)|정리본 : DDA|
|0-3|[EDA : 정리본](https://github.com/nohjuhyeon/study_data_analytics/wiki/03‐2-:-EDA)|정리본 : EDA|
|1|[DDA & EDA example](docs/EDA/EDA_RentalCarOfContractType_together.ipynb)|DDA, EDA 과정 예시||
</details>

<details open>
<summary><h2>CDA</h2></summary>

|구분|이름|설명|비고|
|--|--|--|--|
|0-1|[CDA : 정리본](https://github.com/nohjuhyeon/study_data_analytics/wiki/03‐3-:-CDA)|정리본 : CDA|
|0-2|[CDA : flowchart](https://app.diagrams.net/#G1RhsRvUFJK5r3qpLDKXI4z3ot9JtmnmSY)|CDA 순서도||
|1|[CDA : Categories](docs/CDA/01_CDA_RentalCarOfContractType_categories.ipynb)|x(범주형),y(범주형) 데이터 분석||
|2|[CDA : Normality test](docs/CDA/02_CDA_RentalCarOfContractType_univariate.ipynb)|연속형 데이터의 정규성 검정||
|3|[CDA : continuous](docs/CDA/03_CDA_RentalCarOfContractType_continuous.ipynb)|x(연속형),y(연속형) 데이터 분석||
|4|[CDA : mixed datas with unnormal data](docs/CDA/04_CDA_RentalCarOfContractType_mixed_unNormal.ipynb)|x(범주형),y(연속형 : 비정규 분포) 데이터 분석||
|5|[CDA : mixed datas with normal data](docs/CDA/05_CDA_RentalCarOfContractType_mixed_Normal.ipynb)|x(범주형),y(연속형 : 정규 분포) 데이터 분석||
</details>

<details open>
<summary><h2>QUEST</h2></summary>

|구분|이름|     설명      |비고|
|--|--|--|--|
|PANDAS|[Titanic dataset](./docs/quests/pandas/Titanic_dataset.ipynb)|데이터프레임의 정보 확인하기|.describe()<br/>.unique()<br/>.columns|
|PANDAS|[SpineSurgery List](./docs/quests/pandas/SpineSurgeryList.ipynb)|연속형 데이터를 범주형 데이터로 변환하기|.astype()|
|VISUALIZATION|[multivariate Orders Delivery List](./docs/quests/visualizations/multivariate_OrdersDeliveryList.ipynb)|데이터 타입에 적절한 함수 사용하여 시각화하기|.sort_values(by=data, ascending=True/False)<br/>.reset_index(inplace=True)|
|VISUALIZATION|[multivariate Orders Delivery Lists quest](./docs/quests/visualizations/multivariate_OrdersDeliveryLists_quest.ipynb)|데이터 필터링 연습하기|.str.slice(2,10)<br/>.str.startswith('')|
|DDA|[dataset datatypes](./docs/quests/DDA/dataset_datatypes.md)|데이터의 데이터 타입 분석하기||
|DDA|[extract 5](./docs/quests/DDA/extract_5.ipynb)|범주형 데이터 시각화하기||
|DDA|[Spine Surgery List : datetime](./docs/quests/DDA/SpineSurgeryList_datetime.ipynb)|시간형 데이터 시각화하기||
|DDA|[Spine Surgery List : apply](./docs/quests/DDA/SpineSurgeryList_apply.py)|시간형 데이터로 변환하기하여 새로운 column 만들기||
|EDAs|[preprocessing : titanic train](./docs/quests/EDAs/preprocessing_titanic_train.ipynb)|전처리 연습하기||
|EDAs|[EDA : Rental Car Of Contract Type](./docs/quests/EDAs/EDA_RentalCarOfContractType.ipynb)|DDA & EDA 실습|이상치, 결측치 처리하기|
|EDAs|[EDA : Shopping Mall Delivery With Date](./docs/quests/EDAs/EDA_ShoppingMallDeliveryWithDate.ipynb)|DDA & EDA 실습|이상치, 결측치 처리하기 </br>연속형 데이터를 범주형 데이터로 변환하기|
|EDAs|[EDA : kaggle air quality in covid19](./docs/quests/EDAs/EDA_kaggle_air_quality_in_covid19.ipynb)|DDA & EDA 실습|이상치, 결측치 처리하기|
|CDAs|[CDA : categories](./docs/quests/CDAs/CDA_categories.ipynb)|범주형 데이터 검증하기||
|CDAs|[CDA : continuous](./docs/quests/CDAs/CDA_continuous.ipynb)|연속형 데이터 검증하기||
|CDAs|[CDA :  mixed unVar](./docs/quests/CDAs/CDA_mixed_unVar.ipynb)|비정규 분포인 연속형 데이터가 포함된 데이터 검증하기||
|CDAs|[CDA : mixed unVar second](./docs/quests/CDAs/CDA_mixed_unVar_second.ipynb)|비정규 분포인 연속형 데이터가 포함된 데이터 검증하기2||
</details>
