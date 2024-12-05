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
    subjects = subjects.tolist()
    selected_subject = module_a.selectsubject(subjects)
    selected_subject_index = subjects.index(selected_subject) + 1

    if selected_subject_index in [1, 2] and int(file_name[:4]) != 2020:
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

