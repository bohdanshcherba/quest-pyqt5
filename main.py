import pandas as pd
df = pd.read_csv("train.csv")

df.drop(['id', 'city', 'langs', 'life_main','people_main', "occupation_name", 'occupation_type', "last_seen", 'bdate', 'career_start', 'career_end'], axis=1, inplace=True)



def set_education(education):
    match education:
        case "Undergraduate applicant":
            return 0
        case "Student (Bachelor's)":
            return 1
        case "Alumnus (Bachelor's)":
            return 2
        case "Student (Master's)":
            return 3
        case "Alumnus (Master's)":
            return 4
        case "Student (Specialist)":
            return 5
        case "Alumnus (Specialist)":
            return 6
        case "PhD":
            return 7
        case "Candidate of Sciences":
            return 8
        case _:
            return 0
        
df['education_status'] = df['education_status'].apply(set_education)

def set_education_form(form):
    match form:
        case "Distance Learning":
            return 0
        case "Full-time":
            return 2
        case "Part-time":
            return 1


df['education_form'] = df['education_form'].apply(set_education)


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

X = df.drop("result", axis=1)
Y = df["result"]

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.25)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifer = KNeighborsClassifier()
classifer.fit(X_train, Y_train)

pred = classifer.predict(X_test)

for i in pred:
    print(i)
