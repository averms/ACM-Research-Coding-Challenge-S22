## Classification of mushrooms

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, LabelBinarizer
from sklearn.compose import make_column_transformer

mushrooms = pd.read_csv(
    "mushrooms.csv", dtype="category", na_values="?", keep_default_na=False
)

# Drop the column with N/A values (stalk-root).
mushrooms = mushrooms.dropna(axis=1)

# Encode class. 1 for edible, 0 for poisonous.
mushrooms_y = (mushrooms["class"] == "e").to_numpy().astype("float64")

# Encode features.
ohe = OneHotEncoder(sparse=False)
mushrooms_x = ohe.fit_transform(mushrooms.drop("class", axis=1).to_numpy())

# Split into training and test.
x_train, x_test, y_train, y_test = train_test_split(
    mushrooms_x,
    mushrooms_y,
    train_size=0.2,
)

# Train model and test.
log_model = LogisticRegression()
log_model.fit(x_train, y_train)
predictions = log_model.predict(x_test)
print(classification_report(y_test, predictions))
