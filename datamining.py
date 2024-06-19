import numpy as np
import pandas as pd
from statistics import mean
from sklearn.naive_bayes import GaussianNB
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix
from sklearn import preprocessing
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import scipy.stats as stats

data = pd.read_csv("./calonpembelimobil.csv")

# ambil atribut dalam variabel dataMissing
dataMissing = data.loc[:,['Usia','Status','Kelamin','Memiliki_Mobil','Penghasilan','Beli_Mobil']]
print(dataMissing.head())
print()

# detect missing value
print("Deteksi Missing Value")
print(dataMissing.isna().sum())
print("\n")
print("Hapus Missing Value")
dataMissing = dataMissing.dropna()
print(dataMissing.isna().sum())
print("\n")

print("Deteksi Outlier")
outliers = []
def detect_outlier(data):
    threshold = 3
    mean = np.mean(data)
    std = np.std(data)
    
    for x in data:
        z_score = (x-mean)/std
        if np.abs(z_score)>threshold:
            outliers.append(x)
    return outliers

# Mencetak Outlier
outlier1 = detect_outlier(data['Usia']) 
print("outlier kolom Usia : ",outlier1) 
print("banyak outlier Usia: ",len(outlier1)) 
print()

outlier2 = detect_outlier(data['Status'])
print("outlier kolom Status: ",outlier2)
print("banyak outlier Status: ",len(outlier2)) 
print()

outlier3 = detect_outlier(data['Kelamin']) 
print("outlier kolom Kelamin': ",outlier3)
print("banyak outlier Kelamin': ",len(outlier3)) 
print()

outlier4 = detect_outlier(data['Memiliki_Mobil']) 
print("outlier kolom Memiliki Mobil': ",outlier4)
print("banyak outlier Memiliki Mobil': ",len(outlier4)) 
print()

outlier5 = detect_outlier(data['Penghasilan']) 
print("outlier kolom Penghasilan': ",outlier5)
print("banyak outlier Penghasilan': ",len(outlier5)) 
print()

outlier6 = detect_outlier(data['Beli_Mobil']) 
print("outlier kolom Beli Mobil': ",outlier6)
print("banyak outlier Beli Mobil': ",len(outlier6)) 
print()


# Penanganan Outlier
variabel = ['Usia','Status','Kelamin','Memiliki_Mobil','Penghasilan','Beli_Mobil'] 
for var in variabel:
    outlier_datapoints = detect_outlier(data[var])
    print("Outlier ", var, " = ", outlier_datapoints) 
    rata = mean(data[var])
    print("Outlier ", var, "telah diganti menjadi mean : ") 
    data[var] = data[var].replace(outlier_datapoints, rata) 
    print(data)

print("===================================================================")
print("\n")

# z-score
zscore = stats.zscore(data, axis= 1)
print("Hasil z-score =")
print(zscore)
print("============================================================")



#grouping yang dibagi menjadi dua
print("GROUPING VARIABEL".center(75,"="))
X=data.iloc[:,0:5].values
y=data.iloc[:,5].values
print("data variabel".center(75,"="))
print(X)
print("data kelas".center(75,"="))
print(y)
print("============================================================")
print("\n")

#pembagian training dan testing
print("SPLITTING DATA 20-80".center(75,"="))
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
print("instance variabel data training".center(75,"="))
print(X_train)
print("\n")
print("instance kelas data training".center(75,"="))
print(y_train)
print("\n")
print("instance variabel data testing".center(75,"="))
print(X_test)
print("\n")
print("instance kelas data testing".center(75,"="))
print(y_test)
print("============================================================")
print("\n")


atribut_kmeans = data[['Beli_Mobil']].values

# Standarisasi data
scaler = StandardScaler()
atribut_kmeans_scaled = scaler.fit_transform(atribut_kmeans)



inertia = []
for i in range(1, 8):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(atribut_kmeans_scaled)
    inertia.append(kmeans.inertia_)

# Menampilkan grafik Elbow
plt.plot(range(1, 8), inertia, marker='o')
plt.title('Metode Elbow untuk Menentukan Jumlah Kluster')
plt.xlabel('Jumlah Kluster')
plt.ylabel('Inersia')
plt.show()

silhouette_scores = []
for i in range(2, 11):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(atribut_kmeans_scaled)
    silhouette_scores.append(silhouette_score(atribut_kmeans_scaled, kmeans.labels_))

plt.plot(range(2, 11), silhouette_scores, marker='o')
plt.title('Silhouette Score untuk Menentukan Jumlah Kluster')
plt.xlabel('Jumlah Kluster')
plt.ylabel('Silhouette Score')
plt.show()

# Menentukan jumlah kluster
jumlah_kluster = 2

# Melakukan K-means
kmeans = KMeans(n_clusters=jumlah_kluster, random_state=0)
data['Kluster_Beli_Mobil'] = kmeans.fit_predict(atribut_kmeans_scaled)

# Menampilkan hasil kluster
print("Hasil Klustering:")
print(data[['Beli_Mobil', 'Kluster_Beli_Mobil']])

# Visualisasi hasil kluster
plt.figure(figsize=(10, 8))
plt.scatter(data['Usia'], data['Penghasilan'], c=data['Kluster_Beli_Mobil'], cmap='rainbow', s=50)
plt.title('Hasil Klustering dengan K-means')
plt.xlabel('Usia')
plt.ylabel('Penghasilan')
plt.show()

#data baru
data2 = pd.read_csv("./hasil_clustering.csv")

# ambil atribut dalam variabel dataMissing
dataBaru = data2.loc[:,['Usia','Status','Kelamin','Memiliki_Mobil','Penghasilan','Beli_Mobil','Kluster_Beli_Mobil']]
print(dataMissing.head())
print()

#grouping yang dibagi menjadi dua
print("GROUPING VARIABEL".center(75,"="))
X=dataBaru.iloc[:,0:5].values
y=dataBaru.iloc[:,5].values
print("data variabel".center(75,"="))
print(X)
print("data kelas".center(75,"="))
print(y)
print("============================================================")
print("\n")

#pembagian training dan testing
print("SPLITTING DATA 20-80".center(75,"="))
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
print("instance variabel data training".center(75,"="))
print(X_train)
print("\n")
print("instance kelas data training".center(75,"="))
print(y_train)
print("\n")
print("instance variabel data testing".center(75,"="))
print(X_test)
print("\n")
print("instance kelas data testing".center(75,"="))
print(y_test)
print("============================================================")
print("\n")



# Pemodelan Naive Bayes
print("MODEL NAIVE BAYES".center(75, "="))
naive_bayes = GaussianNB()
naive_bayes.fit(X_train, y_train)

Y_pred_nb = naive_bayes.predict(X_test)
accuracy_nb = accuracy_score(y_test, Y_pred_nb)
precision_nb = precision_score(y_test, Y_pred_nb)
recall_nb = recall_score(y_test, Y_pred_nb)
f1_score_nb = f1_score(y_test, Y_pred_nb)

print('CLASSIFICATION REPORT NAIVE BAYES'.center(75,'='))
print(classification_report(y_test, Y_pred_nb, zero_division=1))

print('Akurasi Naive Bayes : ', accuracy_nb * 100, "%")
print('Precision Naive Bayes : ' + str(precision_nb))
print('Recall Naive Bayes : ' + str(recall_nb))
print('F1-Score Naive Bayes : ' + str(f1_score_nb))
print("============================================================")

#perhitungan confusion matrix
cm_nb = confusion_matrix(y_test, Y_pred_nb)
print('Confusion matrix for Naive Bayes\n',cm_nb)
f, ax = plt.subplots(figsize=(8,5))

#show naive bayes
sns.heatmap(confusion_matrix(y_test, Y_pred_nb), annot=True, fmt=".0f", ax=ax)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()


print('CLASSIFICATION REPORT NAIVE BAYES'.center(75,'='))
print(classification_report(y_test, Y_pred_nb, zero_division=1))

print('Akurasi Naive Bayes : ', accuracy_nb * 100, "%")
print('Precision Naive Bayes : ' + str(precision_nb))
print('Recall Naive Bayes : ' + str(recall_nb))
print('F1-Score Naive Bayes : ' + str(f1_score_nb))
print("============================================================")


#COBA INPUT
print("CONTOH INPUT".center(75, '='))
usia = float(input("usia = "))
status = int(input("status = "))
kelamin = int(input("kelamin = "))
memilikiMobil = float(input("Memiliki mobil = "))
penghasilan = float(input("penghasilan = "))
beliMobil = int(input("beliMobil = "))

Train = [usia,status,kelamin,memilikiMobil,penghasilan,beliMobil]
print(Train)

test = pd.DataFrame([Train], columns=['Usia', 'Status', 'Kelamin', 'Memiliki_Mobil', 'Penghasilan', 'Beli_Mobil'])
# Memisahkan fitur dan kelas
X_test = test.iloc[:, 0:5].values
y_test = test.iloc[:, 5].values

predtest = naive_bayes.predict(X_test)

if predtest == 0:
    print("tidak beli mobil (naive bayes)")
else:
    print("beli mobil (naive bayes)")


# databaru = pd.DataFrame(data)
# databaru.to_csv('hasil_clustering.csv', index=False)