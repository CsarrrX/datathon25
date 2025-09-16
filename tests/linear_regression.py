from sklearn.datasets import load_diabetes
import numpy as np
import matplotlib.pyplot as plt 

diabetes = load_diabetes() 
epocas = 10000
learning_rate = 0.01
weights = np.zeros(10) 
bias = 0
x = diabetes.data
y = diabetes.target
m = len(y)

for epoch in range(epocas):
    y_pred = x @ weights + bias  

    error = y_pred - y

    dw = (1/m) * (x.T @ error)  
    db = (1/m) * np.sum(error)  

    weights -= learning_rate * dw
    bias -= learning_rate * db

    if epoch % 50 == 0:
        loss = (1/(2*m)) * np.sum(error**2)
        print(f"Epoch {epoch}, Loss: {loss:.4f}")

print("Pesos finales:", weights)
print("Bias final:", bias)

y_pred_final = x @ weights + bias

plt.scatter(y, y_pred_final)
plt.xlabel("Valores reales")
plt.ylabel("Predicciones")
plt.title("Predicciones vs Valores Reales")
plt.show()
