import module_a
import module_b

def main():
    file_name = 0
    file_name = int(input("연도를 선택하세요\n1. 2020\n2. 2021\n3. 2022\n4. 2023\n중 택1 (번호로 입력하세요)\n"))
    file_name = file_name+2019
    for i in range(4):
        if file_name == 2020+i:
            file_name = file_name*10000+1231
            break   
    file_name = str(file_name) 
    dataframe = module_a.read_file(f"{file_name}.csv")

    subjects = module_a.subject_and_type(dataframe)
    selected_subject = module_a.selectsubject(subjects)
    selected_subject_index = subjects.tolist().index(selected_subject) + 1

    if selected_subject_index in [1, 2]:
        module_b.module_b(dataframe, selected_subject)
    else:
        types = module_a.typefromsubject(dataframe, selected_subject)
        selected_type = module_a.type(types) if len(types) > 0 else None
        module_b.module_b(dataframe, selected_subject, selected_type)

if __name__ == "__main__":
    main()
