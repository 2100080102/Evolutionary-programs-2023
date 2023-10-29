import numpy as np
import tensorflow as tf
from tensorflow.keras. layers import Dense from tensorflow.keras.models import Sequential
#Define the input vector
input vector = np.array ([- 1, 1, 1, 1])
# Create a simple autoassociative network
model = Sequential ([ Dense (2, activation='relu', input_shape= ( 4 ,)) Dense (4, activation="linear")])
#Compile the model
model.compile(optimizer='adam', loss="mean_squared error")
#Train the model to Learn the identity function
model.fit(np.array([input_vector]), np.array([input_vector]), epochs=1000)
#Test the network with the original input
output= model.predict(np.array([input_vector])) 
print("Original Input:", Input vector)
print("Output of Autoassociative Network:", output)
      
""" Now, let's test the trained autoassociative network with various scenarios:
One Missing Entry:
Remove one element from the input vector and feed it to the network. For example, test it with [- 1, 1, 1] .
One Wrong Entry:
Change one element in the input vector and feed it to the network. For example, test it with [- 1, - 1, - 1, - 1, - 1, - 1] ]
Two Wrong Entries:
Change two elements in the input vector and feed it to the network. For example, test it with \{1, - 1, - 1, - 1\}
Two Missing Entries:
Remove two elements from the input vector and feed it to the network. For example, test it with [- 1, 1] ."""
