import module_a_1
import module_b_1

def main():
    file_name = int(input("연도를 선택하세요 (2020, 2021, 2022, 2023 중 하나를 입력하세요): "))
    if file_name not in [2020, 2021, 2022, 2023]:
        print("잘못된 입력입니다. 프로그램을 종료합니다.")
        return
    file_name = file_name * 10000 + 1231
    file_name = str(file_name)
    dataframe = module_a_1.read_file(f"{file_name}.csv")

    subjects = module_a_1.subject_and_type(dataframe)
    subjects = subjects.tolist() 
    selected_subject = module_a_1.selectsubject(subjects)
    selected_subject_index = subjects.index(selected_subject) + 1

    if int(file_name[:4]) == 2020:
        types = module_a_1.typefromsubject(dataframe, selected_subject)
        if len(types) == 0 or dataframe[dataframe.iloc[:, 0] == selected_subject].iloc[:, 1].isna().all():
            module_b_1.module_b(dataframe, selected_subject, year=(file_name[:4]))
        else:
            selected_type = module_a_1.type(types)
            module_b_1.module_b(dataframe, selected_subject, selected_type, year=(file_name[:4]))
    else:
        types = module_a_1.typefromsubject(dataframe, selected_subject)
        if len(types) > 0 and not dataframe[dataframe.iloc[:, 0] == selected_subject].iloc[:, 1].isna().all():
            selected_type = module_a_1.type(types)
            module_b_1.module_b(dataframe, selected_subject, selected_type, year=(file_name[:4]))
        else:
            module_b_1.module_b(dataframe, selected_subject, year=(file_name[:4]))

if __name__ == "__main__":
    main()