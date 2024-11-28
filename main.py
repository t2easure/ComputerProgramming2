import module_a
import module_b

def main():
    dataframe = module_a.read_file("20231231.csv")

    subjects = module_a.subject_and_type(dataframe)
    selected_subject = module_a.selectsubject(subjects)
    types = module_a.typefromsubject(dataframe, selected_subject)
    selected_type = module_a.type(types) if len(types) > 0 else None
    
    module_b.module_b(dataframe, selected_subject, selected_type)

if __name__ == "__main__":
    main()