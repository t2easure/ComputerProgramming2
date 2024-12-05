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
    selected_subject = module_a.selectsubject(subjects)
    selected_subject_index = subjects.tolist().index(selected_subject) + 1

    if selected_subject_index in [1, 2]:
        module_b.module_b(dataframe, selected_subject, year=(file_name[:4]))
    else:
        types = module_a.typefromsubject(dataframe, selected_subject)
        selected_type = module_a.type(types) if len(types) > 0 else None
        module_b.module_b(dataframe, selected_subject, selected_type, year=(file_name[:4]))

if __name__ == "__main__":
    main()
