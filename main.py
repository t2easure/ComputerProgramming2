import module_a
import module_b

def main():
    file_name = int(input("연도를 선택하세요 (2020, 2021, 2022, 2023 중 하나를 입력하세요): "))
    if file_name not in [2020, 2021, 2022, 2023]:
        print("잘못된 입력입니다. 프로그램을 종료합니다.")
        return
    file_name = file_name * 10000 + 1231
    file_name = str(file_name)
    dataframe = module_a.read_file(f"{file_name}.csv")

    subjects = module_a.subject_and_type(dataframe)
    subjects = subjects.tolist()  # Convert to list to use list operations
    selected_subject = module_a.selectsubject(subjects)
    selected_subject_index = subjects.index(selected_subject) + 1

    # Check if year is 2020 and the subject should not have a type (e.g., 국어 with no type distinction)
    if int(file_name[:4]) == 2020 and dataframe[dataframe.iloc[:, 0] == selected_subject].iloc[:, 1].isna().all():
        module_b.module_b(dataframe, selected_subject, year=(file_name[:4]))
    elif int(file_name[:4]) == 2020 and dataframe[dataframe.iloc[:, 0] == selected_subject].iloc[:, 1].nunique() == 1:
        # If the subject has only one type in 2020, skip type selection
        module_b.module_b(dataframe, selected_subject, year=(file_name[:4]))
    else:
        types = module_a.typefromsubject(dataframe, selected_subject)
        if len(types) > 0:
            selected_type = module_a.type(types)
            module_b.module_b(dataframe, selected_subject, selected_type, year=(file_name[:4]))
        else:
            module_b.module_b(dataframe, selected_subject, year=(file_name[:4]))

if __name__ == "__main__":
    main()
