import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    rows_to_delete = []
    for index, row in students.iterrows():
        if row['name'] == None:
            rows_to_delete.append(index)

    students.drop(rows_to_delete, inplace=True)
    print(students)

columns = ['student_id','name', 'age']
data = [(32, 'Pipper', 5), (217, None, 19), (779, 'Georgia', 20), (849, 'Willow', 14)]
df = pd.DataFrame(data, columns=columns)
dropMissingData(df)