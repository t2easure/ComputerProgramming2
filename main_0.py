import module_a_0
import module_b_0

def main():
    dataframe = module_a_0.read_file("20231231.csv")

    subjects = module_a_0.subject_and_type(dataframe)
    selected_subject = module_a_0.selectsubject(subjects)
    selected_subject_index = subjects.tolist().index(selected_subject) + 1

    if selected_subject_index in [1, 2]:
        module_b_0.module_b(dataframe, selected_subject)
    else:
        types = module_a_0.typefromsubject(dataframe, selected_subject)
        selected_type = module_a_0.type(types) if len(types) > 0 else None
        module_b_0.module_b(dataframe, selected_subject, selected_type)

if __name__ == "__main__":
    main()