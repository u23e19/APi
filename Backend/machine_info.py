import pandas as pd
import psycopg2

#Define your PostgreSQL database connection parameters
db_host = "localhost"
db_port = "5432"
db_name = "Sail_template"
db_user = "postgres"
db_password = "admin77"

# Create a connection to the PostgreSQL database
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    database=db_name,
    user=db_user,
    password=db_password
)

# Define the SQL query to fetch data from the "alert_template" table
sql_query = "SELECT * FROM alert_template"
sql_query_raw= "SELECT COUNT(Alarm) from alert_template where Division = 'Raw Material Transport'"
sql_query_mix= "SELECT COUNT(Alarm) from alert_template where Division = 'Mixing and Nodulizing Plant '"
sql_query_sinc= "SELECT COUNT(Alarm) from alert_template where Division = 'Sinter Cooler'"
sql_query_hearth= "SELECT COUNT(Alarm) from alert_template where Division = 'Hearth Layer and Return Fines Handling'"
sql_query_ign= "SELECT COUNT(Alarm) from alert_template where Division = 'Ignition Furnace'"
sql_query_dos= "SELECT COUNT(Alarm) from alert_template where Division = 'Dosing Plant'"
sql_query_sins= "SELECT COUNT(Alarm) from alert_template where Division = 'Sinter Screening'"
sql_query_sinp= "SELECT COUNT(Alarm) from alert_template where Division = 'Sinter Product Handling'"
sql_query_wat= "SELECT COUNT(Alarm) from alert_template where Division = 'Water System'"
sql_query_pro= "SELECT COUNT(Alarm) from alert_template where Division = 'Process Fans and Ducts'"
sql_query_plant= "SELECT COUNT(Alarm) from alert_template where Division = 'Plant Dedusting'"
sql_query_sinm= "SELECT COUNT(Alarm) from alert_template where Division = 'Sinter machine'"
sql_query_chilled= "SELECT COUNT(Alarm) from alert_template where Division = 'Chilled Water System'"
sql_query_process= "SELECT COUNT(Alarm) from alert_template where Division = 'Process Gas Dedusting'"
# Fetch data from the database and store it in a Pandas DataFrame
df = pd.read_sql_query(sql_query, conn)
cursor = conn.cursor()
cursor.execute(sql_query_raw)
rawmaterialtransport = cursor.fetchone()[0]
cursor.execute(sql_query_mix)
mixingandnodulizingplant = cursor.fetchone()[0]
cursor.execute(sql_query_sinc)
sintercooler = cursor.fetchone()[0]
cursor.execute(sql_query_hearth)
hearthlayerandreturnfineshandling = cursor.fetchone()[0]
cursor.execute(sql_query_ign)
ignitionfurnace = cursor.fetchone()[0]
cursor.execute(sql_query_dos)
dosingplant = cursor.fetchone()[0]
cursor.execute(sql_query_sins)
sinterscreening = cursor.fetchone()[0]
cursor.execute(sql_query_sinp)
sinterproducthandling = cursor.fetchone()[0]
cursor.execute(sql_query_wat)
watersystem= cursor.fetchone()[0]
cursor.execute(sql_query_pro)
processfansandducts= cursor.fetchone()[0]
cursor.execute(sql_query_plant)
plantdedusting= cursor.fetchone()[0]
cursor.execute(sql_query_sinm)
sintermachine= cursor.fetchone()[0]
cursor.execute(sql_query_chilled)
chilledwatersystem= cursor.fetchone()[0]
cursor.execute(sql_query_process)
processgasdedusting= cursor.fetchone()[0]

cursor.close()
# Close the database connection
conn.close()


#Raw Material Transport

raw_df=df[df['division'] == 'Raw Material Transport']
raw_df1 = raw_df[['division','machine_no', 'machine_type']]

raw_df2 = raw_df.groupby('machine_no')['alarm'].count().reset_index()

raw_df3 = raw_df.groupby('machine_no')['health_score'].max().reset_index()
merged_raw = pd.merge(raw_df2, raw_df1, on='machine_no', how='inner')
merged_raw1 = pd.merge(raw_df3, merged_raw, on='machine_no', how='inner')
merged_raw1 =merged_raw1.drop_duplicates()
merged_raw1=merged_raw1.reset_index(drop=True)
rawhigh = merged_raw1[merged_raw1['health_score']>=80]

raw_high = []
for _, row in rawhigh.iterrows():
    raw_high.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

raw_high1=sorted(raw_high, key=lambda x: x['HealthScore'], reverse=True)

rawmed = merged_raw1[(merged_raw1['health_score'] >= 51) & (merged_raw1['health_score'] <= 79)]

raw_med = []
for _, row in rawmed.iterrows():
    raw_med.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

raw_med1=sorted(raw_med, key=lambda x: x['HealthScore'], reverse=True)

rawlow = merged_raw1[merged_raw1['health_score'] <= 50]

raw_low = []
for _, row in rawlow.iterrows():
    raw_low.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

raw_low1=sorted(raw_low, key=lambda x: x['HealthScore'], reverse=True)

#Mixing and Nodulizing plant
mix_df=df[df['division'] == 'Mixing and Nodulizing Plant ']
mix_df1 = mix_df[['division','machine_no', 'machine_type']]

mix_df2 = mix_df.groupby('machine_no')['alarm'].count().reset_index()

mix_df3 = mix_df.groupby('machine_no')['health_score'].max().reset_index()
merged_mix = pd.merge(mix_df2, mix_df1, on='machine_no', how='inner')
merged_mix1 = pd.merge(mix_df3, merged_mix, on='machine_no', how='inner')
merged_mix1 =merged_mix1.drop_duplicates()
merged_mix1=merged_mix1.reset_index(drop=True)
mixhigh = merged_mix1[merged_mix1['health_score']>=80]


mix_high = []
for _, row in mixhigh.iterrows():
    mix_high.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

mix_high1=sorted(mix_high, key=lambda x: x['HealthScore'], reverse=True)

mixmed = merged_mix1[(merged_mix1['health_score'] >= 51) & (merged_mix1['health_score'] <= 79)]

mix_med = []
for _, row in mixmed.iterrows():
    mix_med.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

mix_med1=sorted(mix_med, key=lambda x: x['HealthScore'], reverse=True)

mixlow = merged_mix1[merged_mix1['health_score'] <= 50]

mix_low = []
for _, row in mixlow.iterrows():
    mix_low.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

mix_low1=sorted(mix_low, key=lambda x: x['HealthScore'], reverse=True)

# Sinter Cooler
sin_df=df[df['division'] == 'Sinter Cooler']
sin_df1 = sin_df[['division','machine_no', 'machine_type']]

sin_df2 = sin_df.groupby('machine_no')['alarm'].count().reset_index()

sin_df3 = sin_df.groupby('machine_no')['health_score'].max().reset_index()
merged_sin = pd.merge(sin_df2, sin_df1, on='machine_no', how='inner')
merged_sin1 = pd.merge(sin_df3, merged_sin, on='machine_no', how='inner')
merged_sin1 =merged_sin1.drop_duplicates()
merged_sin1=merged_sin1.reset_index(drop=True)
sinhigh = merged_sin1[merged_sin1['health_score']>=80]

sin_high = []
for _, row in sinhigh.iterrows():
    sin_high.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

sin_high1=sorted(sin_high, key=lambda x: x['HealthScore'], reverse=True)


sinmed = merged_sin1[(merged_sin1['health_score'] >= 51) & (merged_sin1['health_score'] <= 79)]

sin_med = []
for _, row in sinmed.iterrows():
    sin_med.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

sin_med1=sorted(sin_med, key=lambda x: x['HealthScore'], reverse=True)

sinlow = merged_sin1[merged_sin1['health_score'] <= 50]

sin_low = []
for _, row in sinlow.iterrows():
    sin_low.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

sin_low1=sorted(sin_low, key=lambda x: x['HealthScore'], reverse=True)




# Hearth Layer and Return Fines Handling
Hear_df=df[df['division'] == 'Hearth Layer and Return Fines Handling']
Hear_df1 = Hear_df[['division','machine_no', 'machine_type']]

Hear_df2 = Hear_df.groupby('machine_no')['alarm'].count().reset_index()

Hear_df3 = Hear_df.groupby('machine_no')['health_score'].max().reset_index()
merged_Hear = pd.merge(Hear_df2, Hear_df1, on='machine_no', how='inner')
merged_Hear1 = pd.merge(Hear_df3, merged_Hear, on='machine_no', how='inner')
merged_Hear1 =merged_Hear1.drop_duplicates()
merged_Hear1=merged_Hear1.reset_index(drop=True)
#Hearhigh = merged_Hear1[merged_sin1['health_score']>=80]
Hearhigh = merged_Hear1[merged_Hear1['health_score'] >= 80].reset_index(drop=True)


Hear_high = []
for _, row in Hearhigh.iterrows():
    Hear_high.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Hear_high1=sorted(Hear_high, key=lambda x: x['HealthScore'], reverse=True)

Hearmed = merged_Hear1[(merged_Hear1['health_score'] >= 51) & (merged_Hear1['health_score'] <= 79)]

Hear_med = []
for _, row in Hearmed.iterrows():
    Hear_med.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Hear_med1=sorted(Hear_med, key=lambda x: x['HealthScore'], reverse=True)

Hearlow = merged_Hear1[merged_Hear1['health_score'] <= 50]

Hear_low = []
for _, row in Hearlow.iterrows():
    Hear_low.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Hear_low1=sorted(Hear_low, key=lambda x: x['HealthScore'], reverse=True)

#Ignition Furnace

Ign_df=df[df['division'] == 'Ignition Furnace']
Ign_df1 = Ign_df[['division','machine_no', 'machine_type']]

Ign_df2 = Ign_df.groupby('machine_no')['alarm'].count().reset_index()

Ign_df3 = Ign_df.groupby('machine_no')['health_score'].max().reset_index()
merged_Ign = pd.merge(Ign_df2, Ign_df1, on='machine_no', how='inner')
merged_Ign1 = pd.merge(Ign_df3, merged_Ign, on='machine_no', how='inner')
merged_Ign1 =merged_Ign1.drop_duplicates()
merged_Ign1=merged_Ign1.reset_index(drop=True)
#Ignhigh = merged_Ign1[merged_sin1['health_score']>=80]
Ignhigh = merged_Ign1[merged_Ign1['health_score'] >= 80].reset_index(drop=True)

Ign_high = []
for _, row in Ignhigh.iterrows():
    Ign_high.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Ign_high1=sorted(Ign_high, key=lambda x: x['HealthScore'], reverse=True)


Ignmed = merged_Ign1[(merged_Ign1['health_score'] >= 51) & (merged_Ign1['health_score'] <= 79)]

Ign_med = []
for _, row in Ignmed.iterrows():
    Ign_med.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Ign_med1=sorted(Ign_med, key=lambda x: x['HealthScore'], reverse=True)


Ignlow = merged_Ign1[merged_Ign1['health_score'] <= 50]


Ign_low = []
for _, row in Ignlow.iterrows():
    Ign_low.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Ign_low1=sorted(Ign_low, key=lambda x: x['HealthScore'], reverse=True)

#Dosing Plant
Dos_df=df[df['division'] == 'Dosing Plant']
Dos_df1 = Dos_df[['division','machine_no', 'machine_type']]

Dos_df2 = Dos_df.groupby('machine_no')['alarm'].count().reset_index()

Dos_df3 = Dos_df.groupby('machine_no')['health_score'].max().reset_index()
merged_Dos = pd.merge(Dos_df2, Dos_df1, on='machine_no', how='inner')
merged_Dos1 = pd.merge(Dos_df3, merged_Dos, on='machine_no', how='inner')
merged_Dos1 =merged_Dos1.drop_duplicates()
merged_Dos1=merged_Dos1.reset_index(drop=True)
Doshigh = merged_Dos1[merged_Dos1['health_score'] >= 80].reset_index(drop=True)

Dos_high = []
for _, row in Doshigh.iterrows():
    Dos_high.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Dos_high1=sorted(Dos_high, key=lambda x: x['HealthScore'], reverse=True)

Dosmed = merged_Dos1[(merged_Dos1['health_score'] >= 51) & (merged_Dos1['health_score'] <= 79)]

Dos_med = []
for _, row in Dosmed.iterrows():
    Dos_med.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Dos_med1=sorted(Dos_med, key=lambda x: x['HealthScore'], reverse=True)


Doslow = merged_Dos1[merged_Dos1['health_score'] <= 50]


Dos_low = []
for _, row in Doslow.iterrows():
    Dos_low.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Dos_low1=sorted(Dos_low, key=lambda x: x['HealthScore'], reverse=True)


#Sinter Screening
Sint_df=df[df['division'] == 'Sinter Screening']
Sint_df1 = Sint_df[['division','machine_no', 'machine_type']]

Sint_df2 = Sint_df.groupby('machine_no')['alarm'].count().reset_index()

Sint_df3 = Sint_df.groupby('machine_no')['health_score'].max().reset_index()
merged_Sint = pd.merge(Sint_df2, Sint_df1, on='machine_no', how='inner')
merged_Sint1 = pd.merge(Sint_df3, merged_Sint, on='machine_no', how='inner')
merged_Sint1 =merged_Sint1.drop_duplicates()
merged_Sint1=merged_Sint1.reset_index(drop=True)
Sinthigh = merged_Sint1[merged_Sint1['health_score'] >= 80].reset_index(drop=True)

Sint_high = []
for _, row in Sinthigh.iterrows():
    Sint_high.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Sint_high1=sorted(Sint_high, key=lambda x: x['HealthScore'], reverse=True)

Sintmed = merged_Sint1[(merged_Sint1['health_score'] >= 51) & (merged_Sint1['health_score'] <= 79)]

Sint_med = []
for _, row in Sintmed.iterrows():
    Sint_med.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Sint_med1=sorted(Sint_med, key=lambda x: x['HealthScore'], reverse=True)


Sintlow = merged_Sint1[merged_Sint1['health_score'] <= 50]


Sint_low = []
for _, row in Sintlow.iterrows():
    Sint_low.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Sint_low1=sorted(Sint_low, key=lambda x: x['HealthScore'], reverse=True)

#Sinter Product Handling
Sinp_df=df[df['division'] == 'Sinter Product Handling']
Sinp_df1 = Sinp_df[['division','machine_no', 'machine_type']]

Sinp_df2 = Sinp_df.groupby('machine_no')['alarm'].count().reset_index()

Sinp_df3 = Sinp_df.groupby('machine_no')['health_score'].max().reset_index()
merged_Sinp = pd.merge(Sinp_df2, Sinp_df1, on='machine_no', how='inner')
merged_Sinp1 = pd.merge(Sinp_df3, merged_Sinp, on='machine_no', how='inner')
merged_Sinp1 =merged_Sinp1.drop_duplicates()
merged_Sinp1=merged_Sinp1.reset_index(drop=True)
Sinphigh = merged_Sinp1[merged_Sinp1['health_score'] >= 80].reset_index(drop=True)

Sinp_high = []
for _, row in Sinphigh.iterrows():
    Sinp_high.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Sinp_high1=sorted(Sinp_high, key=lambda x: x['HealthScore'], reverse=True)


Sinpmed = merged_Sinp1[(merged_Sinp1['health_score'] >= 51) & (merged_Sinp1['health_score'] <= 79)]

Sinp_med = []
for _, row in Sinpmed.iterrows():
    Sinp_med.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Sinp_med1=sorted(Sinp_med, key=lambda x: x['HealthScore'], reverse=True)


Sinplow = merged_Sinp1[merged_Sinp1['health_score'] <= 50]


Sinp_low = []
for _, row in Sinplow.iterrows():
    Sinp_low.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Sinp_low1=sorted(Sinp_low, key=lambda x: x['HealthScore'], reverse=True)

#Water System

Water_df=df[df['division'] == 'Water System']
Water_df1 = Water_df[['division','machine_no', 'machine_type']]

Water_df2 = Water_df.groupby('machine_no')['alarm'].count().reset_index()

Water_df3 = Water_df.groupby('machine_no')['health_score'].max().reset_index()
merged_Water = pd.merge(Water_df2, Water_df1, on='machine_no', how='inner')
merged_Water1 = pd.merge(Water_df3, merged_Water, on='machine_no', how='inner')
merged_Water1 =merged_Water1.drop_duplicates()
merged_Water1=merged_Water1.reset_index(drop=True)
Waterhigh = merged_Water1[merged_Water1['health_score'] >= 80].reset_index(drop=True)

Water_high = []
for _, row in Waterhigh.iterrows():
    Water_high.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Water_high1=sorted(Water_high, key=lambda x: x['HealthScore'], reverse=True)


Watermed = merged_Water1[(merged_Water1['health_score'] >= 51) & (merged_Water1['health_score'] <= 79)]

Water_med = []
for _, row in Watermed.iterrows():
    Water_med.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Water_med1=sorted(Water_med, key=lambda x: x['HealthScore'], reverse=True)

Waterlow = merged_Water1[merged_Water1['health_score'] <= 50]


Water_low = []
for _, row in Waterlow.iterrows():
    Water_low.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Water_low1=sorted(Water_low, key=lambda x: x['HealthScore'], reverse=True)

#Process Fans and Ducts

Process_df=df[df['division'] == 'Process Fans and Ducts']
Process_df1 = Process_df[['division','machine_no', 'machine_type']]

Process_df2 = Process_df.groupby('machine_no')['alarm'].count().reset_index()

Process_df3 = Process_df.groupby('machine_no')['health_score'].max().reset_index()
merged_Process = pd.merge(Process_df2, Process_df1, on='machine_no', how='inner')
merged_Process1 = pd.merge(Process_df3, merged_Process, on='machine_no', how='inner')
merged_Process1 =merged_Process1.drop_duplicates()
merged_Process1=merged_Process1.reset_index(drop=True)
Processhigh = merged_Process1[merged_Process1['health_score'] >= 80].reset_index(drop=True)

Process_high = []
for _, row in Processhigh.iterrows():
    Process_high.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Process_high1=sorted(Process_high, key=lambda x: x['HealthScore'], reverse=True)


Processmed = merged_Process1[(merged_Process1['health_score'] >= 51) & (merged_Process1['health_score'] <= 79)]

Process_med = []
for _, row in Processmed.iterrows():
    Process_med.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Process_med1=sorted(Process_med, key=lambda x: x['HealthScore'], reverse=True)


Processlow = merged_Process1[merged_Process1['health_score'] <= 50]


Process_low = []
for _, row in Processlow.iterrows():
    Process_low.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Process_low1=sorted(Process_low, key=lambda x: x['HealthScore'], reverse=True)

#Plant Dedusting

Plant_df=df[df['division'] == 'Plant Dedusting']
Plant_df1 = Plant_df[['division','machine_no', 'machine_type']]

Plant_df2 = Plant_df.groupby('machine_no')['alarm'].count().reset_index()

Plant_df3 = Plant_df.groupby('machine_no')['health_score'].max().reset_index()
merged_Plant = pd.merge(Plant_df2, Plant_df1, on='machine_no', how='inner')
merged_Plant1 = pd.merge(Plant_df3, merged_Plant, on='machine_no', how='inner')
merged_Plant1 =merged_Plant1.drop_duplicates()
merged_Plant1=merged_Plant1.reset_index(drop=True)
Planthigh = merged_Plant1[merged_Plant1['health_score'] >= 80].reset_index(drop=True)

Plant_high = []
for _, row in Planthigh.iterrows():
    Plant_high.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Plant_high1=sorted(Plant_high, key=lambda x: x['HealthScore'], reverse=True)


Plantmed = merged_Plant1[(merged_Plant1['health_score'] >= 51) & (merged_Plant1['health_score'] <= 79)]

Plant_med = []
for _, row in Plantmed.iterrows():
    Plant_med.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Plant_med1=sorted(Plant_med, key=lambda x: x['HealthScore'], reverse=True)


Plantlow = merged_Plant1[merged_Plant1['health_score'] <= 50]


Plant_low = []
for _, row in Plantlow.iterrows():
    Plant_low.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Plant_low1=sorted(Plant_low, key=lambda x: x['HealthScore'], reverse=True)

#Sinter Machine
Sinter_df=df[df['division'] == 'Sinter Machine']
Sinter_df1 = Sinter_df[['division','machine_no', 'machine_type']]

Sinter_df2 = Sinter_df.groupby('machine_no')['alarm'].count().reset_index()

Sinter_df3 = Sinter_df.groupby('machine_no')['health_score'].max().reset_index()
merged_Sinter = pd.merge(Sinter_df2, Sinter_df1, on='machine_no', how='inner')
merged_Sinter1 = pd.merge(Sinter_df3, merged_Sinter, on='machine_no', how='inner')
merged_Sinter1 =merged_Sinter1.drop_duplicates()
merged_Sinter1=merged_Sinter1.reset_index(drop=True)
Sinterhigh = merged_Sinter1[merged_Sinter1['health_score'] >= 80].reset_index(drop=True)

Sinter_high = []
for _, row in Sinterhigh.iterrows():
    Sinter_high.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Sinter_high1=sorted(Sinter_high, key=lambda x: x['HealthScore'], reverse=True)


Sintermed = merged_Sinter1[(merged_Sinter1['health_score'] >= 51) & (merged_Sinter1['health_score'] <= 79)]

Sinter_med = []
for _, row in Sintermed.iterrows():
    Sinter_med.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Sinter_med1=sorted(Sinter_med, key=lambda x: x['HealthScore'], reverse=True)


Sinterlow = merged_Sinter1[merged_Sinter1['health_score'] <= 50]


Sinter_low = []
for _, row in Sinterlow.iterrows():
    Sinter_low.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Sinter_low1=sorted(Sinter_low, key=lambda x: x['HealthScore'], reverse=True)

#Chilled Water System

Chilled_df=df[df['division'] == 'Chilled Water System']
Chilled_df1 = Chilled_df[['division','machine_no', 'machine_type']]

Chilled_df2 = Chilled_df.groupby('machine_no')['alarm'].count().reset_index()

Chilled_df3 = Chilled_df.groupby('machine_no')['health_score'].max().reset_index()
merged_Chilled = pd.merge(Chilled_df2, Chilled_df1, on='machine_no', how='inner')
merged_Chilled1 = pd.merge(Chilled_df3, merged_Chilled, on='machine_no', how='inner')
merged_Chilled1 =merged_Chilled1.drop_duplicates()
merged_Chilled1=merged_Chilled1.reset_index(drop=True)
Chilledhigh = merged_Chilled1[merged_Chilled1['health_score'] >= 80].reset_index(drop=True)

Chilled_high = []
for _, row in Chilledhigh.iterrows():
    Chilled_high.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Chilled_high1=sorted(Chilled_high, key=lambda x: x['HealthScore'], reverse=True)


Chilledmed = merged_Chilled1[(merged_Chilled1['health_score'] >= 51) & (merged_Chilled1['health_score'] <= 79)]

Chilled_med = []
for _, row in Chilledmed.iterrows():
    Chilled_med.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Chilled_med1=sorted(Chilled_med, key=lambda x: x['HealthScore'], reverse=True)


Chilledlow = merged_Chilled1[merged_Chilled1['health_score'] <= 50]


Chilled_low = []
for _, row in Chilledlow.iterrows():
    Chilled_low.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

Chilled_low1=sorted(Chilled_low, key=lambda x: x['HealthScore'], reverse=True)

#Process Gas Dedusting
ProcessG_df=df[df['division'] == 'Process Gas Dedusting']
ProcessG_df1 = ProcessG_df[['division','machine_no', 'machine_type']]

ProcessG_df2 = ProcessG_df.groupby('machine_no')['alarm'].count().reset_index()

ProcessG_df3 = ProcessG_df.groupby('machine_no')['health_score'].max().reset_index()
merged_ProcessG = pd.merge(ProcessG_df2, ProcessG_df1, on='machine_no', how='inner')
merged_ProcessG1 = pd.merge(ProcessG_df3, merged_ProcessG, on='machine_no', how='inner')
merged_ProcessG1 =merged_ProcessG1.drop_duplicates()
merged_ProcessG1=merged_ProcessG1.reset_index(drop=True)
ProcessGhigh = merged_ProcessG1[merged_ProcessG1['health_score'] >= 80].reset_index(drop=True)

ProcessG_high = []
for _, row in ProcessGhigh.iterrows():
    ProcessG_high.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

ProcessG_high1=sorted(ProcessG_high, key=lambda x: x['HealthScore'], reverse=True)


ProcessGmed = merged_ProcessG1[(merged_ProcessG1['health_score'] >= 51) & (merged_ProcessG1['health_score'] <= 79)]

ProcessG_med = []
for _, row in ProcessGmed.iterrows():
    ProcessG_med.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

ProcessG_med1=sorted(ProcessG_med, key=lambda x: x['HealthScore'], reverse=True)


ProcessGlow = merged_ProcessG1[merged_ProcessG1['health_score'] <= 50]


ProcessG_low = []
for _, row in ProcessGlow.iterrows():
    ProcessG_low.append({
        'Division': row['division'],
        'MachineNo': row['machine_no'],
        'MachineType': row['machine_type'],
        'AlertCount': row['alarm'],
        'HealthScore': row['health_score']
    })

ProcessG_low1=sorted(ProcessG_low, key=lambda x: x['HealthScore'], reverse=True)



