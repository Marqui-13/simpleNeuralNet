from keras.models import Sequential
from keras.layers import Dense

# Define the model
model = Sequential()
model.add(Dense(32, input_dim=500, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Evaluate the model
score = model.evaluate(X_test, y_test, batch_size=32)
