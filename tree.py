from sklearn.tree import DecisionTreeClassifier


data = [
    ["Oil Filter", 8000, 3],
    ["Brake Pads", 12000, 4],
    ["Chain Lubrication", 5000, 2],
    ["Air Filter", 9000, 3],
    ["Spark Plugs", 7000, 2],
    ["Brake Fluid", 11000, 4]
]


X = [[row[1], row[2]] for row in data]  
y = [row[0] for row in data]             


clf = DecisionTreeClassifier()


clf.fit(X, y)


def recommend_maintenance():
    
    odometer = input("apakah motor anda lebih dari 10000km? (yes/no): ").lower()
    lifespan = input("apakah motor anda berumur 5 tahun? (yes/no): ").lower()

    
    odometer_reading = 1 if odometer == 'yes' else 0
    motorcycle_lifespan = 1 if lifespan == 'yes' else 0

    
    prediction = clf.predict([[odometer_reading, motorcycle_lifespan]])

    
    print("Recommended maintenance:")
    for part in prediction:
        print("-", part)


recommend_maintenance()