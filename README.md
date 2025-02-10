# **Modelo: Random Forest - Detección de Fraudes / Fraud Detection**

---

## **📌 Elección del Modelo / Model Selection**
Se eligió **Random Forest** debido a su capacidad para manejar datos complejos con superposición entre clases. A diferencia de otros modelos como Isolation Forest o Gaussian Mixture, que están más orientados a la detección de anomalías sin etiquetas, Random Forest es un modelo supervisado que utiliza la información etiquetada para mejorar la precisión en la clasificación.

**Random Forest** was chosen due to its ability to handle complex data with class overlap. Unlike other models such as Isolation Forest or Gaussian Mixture, which are more oriented toward detecting anomalies without labels, Random Forest is a supervised model that leverages labeled data to improve classification accuracy.

### **🔹 Razones principales para elegir Random Forest / Key Reasons to Choose Random Forest:**
- **✅ Robustez / Robustness:** Resistente al sobreajuste gracias a múltiples árboles de decisión.  
  Resistant to overfitting due to the use of multiple decision trees.
- **✅ Manejo de ruido y datos desbalanceados / Handling Noise and Imbalanced Data:** Capaz de manejar datos con separaciones poco claras entre clases.  
  Can handle datasets where class separation is not entirely clear.
- **✅ Interpretabilidad / Interpretability:** Permite analizar la importancia de las características en la clasificación.  
  Allows analyzing feature importance in decision-making.
- **✅ Flexibilidad / Flexibility:** Se adapta bien a diferentes tipos de datos sin mucho preprocesamiento.  
  Adapts well to various data types without extensive preprocessing.

---

## **📊 Resultados del Modelo / Model Results**

### **📋 Matriz de Confusión / Confusion Matrix**
La matriz de confusión muestra el desempeño del modelo clasificando casos de fraude (clase 1) y no fraude (clase 0).  
The confusion matrix shows the model's performance in classifying fraud cases (class 1) and non-fraud cases (class 0).

<img src="https://github.com/RicardoRobledo/CreditCardFraudDetector/blob/main/matrix.png" alt="Matriz de Confusión / Confusion Matrix" width="400" height="300">

---

## **📊 Análisis de Resultados / Results Analysis**

1. **Reducción de Falsos Positivos y Negativos / Reduction of False Positives and Negatives:**
   - El modelo demostró alta precisión para distinguir entre transacciones fraudulentas y no fraudulentas.  
     The model demonstrated high accuracy in distinguishing between fraudulent and non-fraudulent transactions.

2. **Desempeño en Datos Balanceados / Performance on Balanced Data:**
   - Las clases positivas (fraude) y negativas (no fraude) tienen resultados equilibrados, lo que muestra que el modelo no está sesgado.  
     Positive (fraud) and negative (non-fraud) classes have balanced results, showing no bias in the model.

3. **Relevancia de las Características / Feature Importance:**
   - Random Forest permite identificar las características más importantes para la detección de fraudes, facilitando futuras optimizaciones.  
     Random Forest identifies the most important features for fraud detection, enabling future optimizations.

---

## **Conclusiones / Conclusions**
- El modelo **Random Forest** demostró ser una herramienta poderosa y confiable para la detección de fraudes bancarios.  
  The **Random Forest** model proved to be a powerful and reliable tool for detecting banking fraud.

- Los resultados confirman que el modelo es efectivo y confiable para implementarse en entornos reales.  
  The results confirm that the model is effective and reliable for implementation in real-world environments.
