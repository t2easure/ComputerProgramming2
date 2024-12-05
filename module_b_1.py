import matplotlib.pyplot as plt
import matplotlib
import numpy as np
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
    
    # 점수 범위를 5점 단위로 그룹화
    subject_data['표준점수_그룹'] = (subject_data["표준점수"] // 5) * 5
    grouped_data = subject_data.groupby("표준점수_그룹").sum()
    
    standard_scores = grouped_data.index
    male_scores = grouped_data["남자"].dropna()
    female_scores = grouped_data["여자"].dropna()
    
    bar_width = 0.35
    index = np.arange(len(standard_scores))
    
    plt.bar(index, male_scores, bar_width, label='남자', color='blue')
    plt.bar(index + bar_width, female_scores, bar_width, label='여자', color='red')
    
    plt.title(title)
    plt.xlabel('표준점수 (5점 단위)')
    plt.ylabel('학생 수')
    plt.xticks(index + bar_width / 2, standard_scores, rotation=45)
    plt.legend()
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()
