import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Definisikan kolom
col_names = ['sparepart', 'merk', 'Harga', 'kualitas', 'spesifikasi teknis', 'ratings', 'id', 'km']

# Baca data dari file Excel
pima = pd.read_excel("./dataafterfix.xlsx", names=col_names)

# Periksa dan tampilkan nilai yang tidak dapat diubah menjadi float
for value in pima['Harga']:
    try:
        float(value)
    except ValueError:
        print("Nilai yang tidak dapat diubah menjadi float:", value)


# Split dataset into features and target variable
feature_cols = ['Harga', 'ratings']
X = pima[feature_cols]  # Features
y = pima['sparepart']   # Target variable, assuming 'Sparepart' is the label

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)  # 70% training and 30% test

# Create Decision Tree classifier object
clf = DecisionTreeClassifier()

# Train Decision Tree classifier
clf = clf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
