import pandas as pd
df_surgery=pd.read_csv("docs\quests\data\SpineSurgeryList.csv")
print(df_surgery)

def receive_params(params):
    BMI = params.loc['체중']/((params.loc['신장']/100)**2)
    return BMI

df_surgery["BMI"]= df_surgery[['신장','체중']].apply(receive_params,axis=1)
pass

def convert_time(x):
    try:    
        hour = int(x/60)
        min = int(x%60)
        time = pd.to_datetime(f"{hour}, {min}", format="%H, %M")
        return time
    except:
        pass
pass
df_surgery['수술시간_datetime'] = df_surgery["수술시간"].apply(convert_time)
df_surgery['수술시간_datetime'] = df_surgery['수술시간_datetime'].dt.time
pass

# df_surgery['수술시간_datetime']
# 0       01:08:00
# 1       00:31:00
# 2       01:18:00
# 3       01:13:00
# 4       00:29:00
#           ...   
# 1889    01:20:00
# 1890    00:20:00
# 1891    00:50:00
# 1892    00:25:00
# 1893    00:45:00
# Name: 수술시간_datetime, Length: 1894, dtype: object

# df_surgery['BMI']
# 0       17.361111
# 1       17.361111
# 2       17.361111
# 3       17.361111
# 4       17.361111
#           ...    
# 1889    17.361111
# 1890    17.361111
# 1891    17.361111
# 1892    17.361111
# 1893    17.361111
# Name: BMI, Length: 1894, dtype: float64