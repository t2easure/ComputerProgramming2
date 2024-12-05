import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc

matplotlib.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

matplotlib.use('TkAgg')

def module_b(dataframe, subject, type_=None, year=None):
    plt.figure(figsize=(10, 6))
    if type_:
        subject_data = dataframe[(dataframe.iloc[:, 0] == subject) & (dataframe.iloc[:, 1] == type_)]
        title = f'{int(year) + 1} 수능 {subject} ({type_}) 점수 분포 (남자/여자)'
    else:
        subject_data = dataframe[dataframe.iloc[:, 0] == subject]
        title = f'{int(year) + 1} 수능 {subject} 점수 분포 (남자/여자)'
    
    standard_scores = subject_data["표준점수"]
    male_scores = subject_data["남자"].dropna()
    female_scores = subject_data["여자"].dropna()
    
    plt.plot(standard_scores, male_scores, label='남자', color='blue')
    plt.plot(standard_scores, female_scores, label='여자', color='red')
    
    plt.title(title)
    plt.xlabel('표준점수')
    plt.ylabel('학생 수')
    plt.legend()
    plt.grid(axis='y', linestyle='--')
    plt.show()
