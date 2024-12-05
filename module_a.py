import pandas as pd 

def read_file(file_name="20231231.csv", directory="."):
    file_path = f"{directory}/{file_name}"
    return pd.read_csv(file_path, encoding='cp949') 

def subject_and_type(dataframe):
    subjects = dataframe.iloc[:, 0].unique()
    return subjects

def typefromsubject(dataframe, subject):
    types = dataframe[dataframe.iloc[:, 0] == subject].iloc[:, 1].dropna().unique() 
    return types

def selectsubject(subjects):
    print("\n과목 목록:\n")
    for i, subject in enumerate(subjects):
        print(f"{i + 1}. {subject}")
    selected_index = int(input("\n원하는 과목의 번호를 작성하세요: ")) - 1
    return subjects[selected_index]

def type(types):
    print("\n유형 목록:")
    for i, type_ in enumerate(types):
        print(f"{i + 1}. {type_}")
    selected_index = int(input("\n원하는 유형의 번호를 선택하세요: ")) - 1
    return types[selected_index]