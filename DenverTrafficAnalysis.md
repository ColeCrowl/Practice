```python
pip install matplotlib
```

    Requirement already satisfied: matplotlib in c:\users\cjcro\anaconda3\lib\site-packages (3.3.4)
    Requirement already satisfied: cycler>=0.10 in c:\users\cjcro\anaconda3\lib\site-packages (from matplotlib) (0.10.0)
    Requirement already satisfied: numpy>=1.15 in c:\users\cjcro\anaconda3\lib\site-packages (from matplotlib) (1.20.1)
    Requirement already satisfied: kiwisolver>=1.0.1 in c:\users\cjcro\anaconda3\lib\site-packages (from matplotlib) (1.3.1)
    Requirement already satisfied: pillow>=6.2.0 in c:\users\cjcro\anaconda3\lib\site-packages (from matplotlib) (8.2.0)
    Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3 in c:\users\cjcro\anaconda3\lib\site-packages (from matplotlib) (2.4.7)
    Requirement already satisfied: python-dateutil>=2.1 in c:\users\cjcro\anaconda3\lib\site-packages (from matplotlib) (2.8.1)
    Requirement already satisfied: six in c:\users\cjcro\anaconda3\lib\site-packages (from cycler>=0.10->matplotlib) (1.15.0)
    Note: you may need to restart the kernel to use updated packages.
    


```python
import matplotlib
matplotlib.__version__
```




    '3.3.4'




```python
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import datetime
import time
import seaborn as sns
print('done')
```

    done
    


```python
df = pd.read_csv(r"C:\Users\cjcro\OneDrive\Documents\City_of_Denver_Traffic_Report\Data\traffic_accidents.csv")
df.count()
```




    shape                            198179
    incident_id                      206125
    offense_id                       206126
    offense_code                     206125
    offense_code_extension           206125
    top_traffic_accident_offense     206125
    first_occurrence_date            206125
    last_occurrence_date               2661
    reported_date                    206125
    incident_address                 206125
    geo_x                            198179
    geo_y                            198179
    geo_lon                          198179
    geo_lat                          198179
    district_id                      203148
    precinct_id                      180316
    neighborhood_id                  179516
    bicycle_ind                      197124
    pedestrian_ind                   197124
    HARMFUL_EVENT_SEQ_1              206125
    HARMFUL_EVENT_SEQ_2              206125
    HARMFUL_EVENT_SEQ_3              206125
    road_location                    206125
    ROAD_DESCRIPTION                 206125
    ROAD_CONTOUR                     206125
    ROAD_CONDITION                   206125
    LIGHT_CONDITION                  206125
    TU1_VEHICLE_TYPE                 206125
    TU1_TRAVEL_DIRECTION             206125
    TU1_VEHICLE_MOVEMENT             206125
    TU1_DRIVER_ACTION                206125
    TU1_DRIVER_HUMANCONTRIBFACTOR    206125
    TU1_PEDESTRIAN_ACTION            206121
    TU2_VEHICLE_TYPE                 206125
    TU2_TRAVEL_DIRECTION             206125
    TU2_VEHICLE_MOVEMENT             206125
    TU2_DRIVER_ACTION                206125
    TU2_DRIVER_HUMANCONTRIBFACTOR    206125
    TU2_PEDESTRIAN_ACTION            206123
    SERIOUSLY_INJURED                205668
    FATALITIES                       205668
    FATALITY_MODE_1                  206125
    FATALITY_MODE_2                  206125
    SERIOUSLY_INJURED_MODE_1         206125
    SERIOUSLY_INJURED_MODE_2         206125
    POINT_X                               0
    POINT_Y                               0
    dtype: int64




```python
df.columns
df = df.drop(columns=['shape', 'incident_id', 'offense_id', 'offense_code',
       'offense_code_extension', 'last_occurrence_date', 'reported_date', 'last_occurrence_date', 'reported_date','HARMFUL_EVENT_SEQ_1', 'HARMFUL_EVENT_SEQ_2',
       'HARMFUL_EVENT_SEQ_3', 'FATALITIES', 'FATALITY_MODE_1', 'district_id', 'neighborhood_id', 'FATALITY_MODE_2', 'SERIOUSLY_INJURED_MODE_1',
       'SERIOUSLY_INJURED_MODE_2',])
```


```python
df.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>top_traffic_accident_offense</th>
      <th>first_occurrence_date</th>
      <th>incident_address</th>
      <th>geo_x</th>
      <th>geo_y</th>
      <th>geo_lon</th>
      <th>geo_lat</th>
      <th>precinct_id</th>
      <th>bicycle_ind</th>
      <th>pedestrian_ind</th>
      <th>...</th>
      <th>TU1_PEDESTRIAN_ACTION</th>
      <th>TU2_VEHICLE_TYPE</th>
      <th>TU2_TRAVEL_DIRECTION</th>
      <th>TU2_VEHICLE_MOVEMENT</th>
      <th>TU2_DRIVER_ACTION</th>
      <th>TU2_DRIVER_HUMANCONTRIBFACTOR</th>
      <th>TU2_PEDESTRIAN_ACTION</th>
      <th>SERIOUSLY_INJURED</th>
      <th>POINT_X</th>
      <th>POINT_Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TRAF - ACCIDENT</td>
      <td>2022-01-10 17:00:00</td>
      <td>8800 BLOCK E MLK BLVD</td>
      <td>3173144.0</td>
      <td>1702273.0</td>
      <td>-104.884136</td>
      <td>39.759934</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>OTHER</td>
      <td>OTHER</td>
      <td>OTHER</td>
      <td>OTHER</td>
      <td>OTHER</td>
      <td>OTHER</td>
      <td>OTHER</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TRAF - ACCIDENT - SBI</td>
      <td>2021-10-15 12:10:00</td>
      <td>PARK AVE / E 20TH AVE</td>
      <td>3146731.0</td>
      <td>1697578.0</td>
      <td>-104.978179</td>
      <td>39.747499</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>OTHER</td>
      <td>MOTORCYCLE</td>
      <td>SOUTH</td>
      <td>GOING STRAIGHT</td>
      <td>0</td>
      <td>NO APPARENT</td>
      <td>OTHER</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TRAF - ACCIDENT</td>
      <td>2021-12-28 17:50:00</td>
      <td>I25 HWYNB / I225 HWYNB</td>
      <td>3167089.0</td>
      <td>1656410.0</td>
      <td>-104.906738</td>
      <td>39.634141</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>OTHER</td>
      <td>OTHER</td>
      <td>OTHER</td>
      <td>OTHER</td>
      <td>OTHER</td>
      <td>OTHER</td>
      <td>OTHER</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TRAF - ACCIDENT - HIT &amp; RUN</td>
      <td>2022-01-06 15:58:00</td>
      <td>900 BLOCK N MARIPOSA ST</td>
      <td>3139945.0</td>
      <td>1691429.0</td>
      <td>-105.002432</td>
      <td>39.730724</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>OTHER</td>
      <td>OTHER</td>
      <td>OTHER</td>
      <td>OTHER</td>
      <td>OTHER</td>
      <td>OTHER</td>
      <td>OTHER</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TRAF - ACCIDENT</td>
      <td>2022-01-07 08:18:00</td>
      <td>E 12TH AVE / N LOGAN ST</td>
      <td>3145598.0</td>
      <td>1693074.0</td>
      <td>-104.982300</td>
      <td>39.735153</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>OTHER</td>
      <td>PASSENGER CAR/VAN</td>
      <td>NORTH</td>
      <td>GOING STRAIGHT</td>
      <td>0</td>
      <td>NO APPARENT</td>
      <td>OTHER</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 30 columns</p>
</div>




```python
df['FOD'] = pd.to_datetime(df['first_occurrence_date'], format='%Y-%m-%d')

df2013 = df.loc[(df['FOD'] >= '2013-01-01')
               & (df['FOD'] < '2013-12-31')]

df2013_Jan = df.loc[(df['FOD'] >= '2013-01-01')
               & (df['FOD'] < '2013-01-31')]

df201307 = df.loc[(df['FOD'] >= '2013-01-07')
               & (df['FOD'] < '2013-01-07')]
df2013.count()
```




    top_traffic_accident_offense     21570
    first_occurrence_date            21570
    incident_address                 21570
    geo_x                            20787
    geo_y                            20787
    geo_lon                          20787
    geo_lat                          20787
    precinct_id                      20787
    bicycle_ind                      21227
    pedestrian_ind                   21227
    road_location                    21570
    ROAD_DESCRIPTION                 21570
    ROAD_CONTOUR                     21570
    ROAD_CONDITION                   21570
    LIGHT_CONDITION                  21570
    TU1_VEHICLE_TYPE                 21570
    TU1_TRAVEL_DIRECTION             21570
    TU1_VEHICLE_MOVEMENT             21570
    TU1_DRIVER_ACTION                21570
    TU1_DRIVER_HUMANCONTRIBFACTOR    21570
    TU1_PEDESTRIAN_ACTION            21570
    TU2_VEHICLE_TYPE                 21570
    TU2_TRAVEL_DIRECTION             21570
    TU2_VEHICLE_MOVEMENT             21570
    TU2_DRIVER_ACTION                21570
    TU2_DRIVER_HUMANCONTRIBFACTOR    21570
    TU2_PEDESTRIAN_ACTION            21570
    SERIOUSLY_INJURED                21570
    POINT_X                              0
    POINT_Y                              0
    FOD                              21570
    dtype: int64




```python
df2013total = df2013.groupby(pd.Grouper(key='FOD', axis=0, 
                      freq='m')).count()
```


```python
df2013total['first_occurrence_date']
```




    FOD
    2013-01-31    1873
    2013-02-28    1569
    2013-03-31    1678
    2013-04-30    1721
    2013-05-31    1724
    2013-06-30    1737
    2013-07-31    1882
    2013-08-31    1887
    2013-09-30    1895
    2013-10-31    1896
    2013-11-30    1813
    2013-12-31    1895
    Freq: M, Name: first_occurrence_date, dtype: int64




```python
df.ROAD_CONDITION.unique()
```




    array(['  ', 'DRY', 'UNDER INVESTIGATION', nan, 'WET', 'ICY', 'SNOWY',
           'ICY WITH VISIBLE ICY ROAD TREATMENT', 'SLUSHY',
           'SNOWY WITH VISIBLE ICY ROAD TREATMENT',
           'DRY WITH VISIBLE ICY ROAD TREATMENT', 'MUDDY',
           'WET WITH VISIBLE ICY ROAD TREATMENT',
           'SLUSHY WITH VISIBLE ICY ROAD TREATMENT', 'FOREIGN MATERIAL'],
          dtype=object)




```python
df2013.ROAD_CONDITION.value_counts()
```




    DRY                                       17953
    WET                                        1524
    ICY                                         779
    SNOWY                                       565
                                                453
    SLUSHY                                      120
    DRY WITH VISIBLE ICY ROAD TREATMENT          42
    WET WITH VISIBLE ICY ROAD TREATMENT          41
    SNOWY WITH VISIBLE ICY ROAD TREATMENT        38
    SLUSHY WITH VISIBLE ICY ROAD TREATMENT       28
    ICY WITH VISIBLE ICY ROAD TREATMENT          22
    MUDDY                                         3
    FOREIGN MATERIAL                              2
    Name: ROAD_CONDITION, dtype: int64




```python
df2013_graph = df2013.groupby(pd.Grouper(key='FOD', axis=0, 
                      freq='m')).ROAD_CONDITION.value_counts()

```


```python
df2013_graphH = df2013_Jan.groupby(pd.Grouper(key='FOD', axis=0, 
                      freq='H')).count()
dft = df201307.groupby(pd.Grouper(key='FOD', axis=0, 
                      freq='H')).count()
df2013_graphH.first_occurrence_date.mean()
```




    2.522284122562674




```python
df2013_graph.plot(x="FOD", y="ROAD_CONDITION", kind="bar", figsize=(20,10))
plt.title("Road Conditions of Accidents 2013", fontsize=25)
plt.ylabel('Accidents')
plt.xlabel('Time/Road Condition')
```




    Text(0.5, 0, 'Time/Road Condition')




    
![png](output_13_1.png)
    



```python
df2013_graphH.plot(y="first_occurrence_date", kind="area", figsize=(20,10))
plt.title("Number of Traffic Accidents", fontsize=25)
plt.ylabel('Accidents')
plt.xlabel('Day of Month')


```




    Text(0.5, 0, 'Day of Month')




    
![png](output_14_1.png)
    



```python
df2013_graphH
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>top_traffic_accident_offense</th>
      <th>first_occurrence_date</th>
      <th>incident_address</th>
      <th>geo_x</th>
      <th>geo_y</th>
      <th>geo_lon</th>
      <th>geo_lat</th>
      <th>precinct_id</th>
      <th>bicycle_ind</th>
      <th>pedestrian_ind</th>
      <th>...</th>
      <th>TU1_PEDESTRIAN_ACTION</th>
      <th>TU2_VEHICLE_TYPE</th>
      <th>TU2_TRAVEL_DIRECTION</th>
      <th>TU2_VEHICLE_MOVEMENT</th>
      <th>TU2_DRIVER_ACTION</th>
      <th>TU2_DRIVER_HUMANCONTRIBFACTOR</th>
      <th>TU2_PEDESTRIAN_ACTION</th>
      <th>SERIOUSLY_INJURED</th>
      <th>POINT_X</th>
      <th>POINT_Y</th>
    </tr>
    <tr>
      <th>FOD</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01 00:00:00</th>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>...</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2013-01-01 01:00:00</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>...</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2013-01-01 02:00:00</th>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>5</td>
      <td>5</td>
      <td>...</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2013-01-01 03:00:00</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>...</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2013-01-01 04:00:00</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2013-01-30 17:00:00</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>...</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2013-01-30 18:00:00</th>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>...</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2013-01-30 19:00:00</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>...</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2013-01-30 20:00:00</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2013-01-30 21:00:00</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>...</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>718 rows × 30 columns</p>
</div>




```python

```


```python
print(dft['first_occurrence_date'])
```

    Series([], Freq: H, Name: first_occurrence_date, dtype: int64)
    


```python
print(df2013_graphH['first_occurrence_date'])
```

    FOD
    2013-01-01 00:00:00    7
    2013-01-01 01:00:00    3
    2013-01-01 02:00:00    6
    2013-01-01 03:00:00    5
    2013-01-01 04:00:00    1
                          ..
    2013-01-30 17:00:00    5
    2013-01-30 18:00:00    8
    2013-01-30 19:00:00    2
    2013-01-30 20:00:00    1
    2013-01-30 21:00:00    2
    Freq: H, Name: first_occurrence_date, Length: 718, dtype: int64
    


```python

```
