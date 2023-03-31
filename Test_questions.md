
Kokchun Giang
1 / 4
Instuderingsfrågor maskininlärning AI21
Facit finns inte till nedanstående frågor. Frågorna ska utgöra ett stöd för er att lära er teori för
maskininlärning. Samarbeta gärna och diskutera gärna med varandra.

1. Vad är data leakage, varför är det dåligt och hur kan du undvika data leakage?  

  
Svar: 

2. Beskriv vad poängen kan vara att dela upp datasetet till träningsdata och testdata för maskininlärning?  

  
Svar: 

3. Beskriv vad poängen kan vara att dela upp datasetet till tränings-, validerings- och testdataset för maskininlärning?  

  
Svar: 

4. Hur skiljer sig batch gradient descent och mini batch gradient descent?  

  
Svar: 

5. Vad är en aktiveringsfunktion i en artificiell neuron? Ge två exempel på aktiveringsfunktioner.  

  
Svar: 

6. Du har ett program som klassificerar email till spam eller hams (inte spam). Vilka evalueringsmetrics ska
du kolla på och varför?  

  
Svar: 

7. Ett brandlarm larmar ofta när det inte brinner. Tror du precision är högt eller lågt, förklara varför.  

  
Svar: 

8. Förklara vad curse of dimensionality är och hur det kan påverka en maskininlärningsmodell.  

  
Svar: 

9. Vad är skillnaden på feature standardization och normalization?  

  
Svar: 

10. Du har ett dataset som ser ut som följande (1000 observationer):

```temperatur i °C vind (m/s)
22.5    2.0
8.3     10.3
13.2    4
```

... ...  
En meterolog vill gruppera dessa. Ge ett förslag på hur hen skulle kunna göra med en
maskininlärningsalgoritm.  

  
Svar: 

11. Många maskininlärningsmodeller har svårt att arbeta med textdata direkt. Ge förslag på hur man skulle
kunna förbearbeta en textsträng.  

  
Svar: 

12. Du ska använda KNN för klassificering. Ge förslag på hur du skulle kunna gå tillväga för att   
ett lämpligt värde på antalet neighbors.  

  
Svar: 

13. Beskriv begreppen: perceptron, multilayered perceptron, feedforward network, fully connected layers.  

  
Svar: 

14. Aktiveringsfunktionen rectified linear unit (ReLU) är definierad som . En nod i ett MLP
har denna aktiveringsfunktion och får inputs och har vikterna och bias  

. Beräkna output för denna nod.  

  
Svar: 

15. XOR grind i digitalteknik är en exklusiv disjunktion vilket innebär:
A B A XOR B
___
1 1 0
___
1 0 1
___
0 1 1
___
0 0 0

Visa att följande MLP kan simulera XOR-grind. Varje nod är en perceptron, dvs att aktiveringsfunktionen
är en stegfunktion.  

![image.png](../Data/assets/image_1680160707975_0.png)

  
Svar: 

16. Formeln för Naive Bayes är:  

![image.png](../Data/assets/image_1680160809548_0.png)

Du har ett dataset som består 100 reviews, varav 80 var positiva och 20 negativa. Nedan finns tabeller
på hur frekvent olika ord förekommer för positiva respektive   
Positiva reviews:  

<p style="margin-left: px">


| |happy|go|od|bookauthor|bad|
|--|--|--|--|--|--|
|Antal |50 |60 |20 |10 |1|
</p>  

<p style="margin-left: 100px">

Negativa reviews:

| |happy|go|od|bookauthor|bad|
|--|--|--|--|--|--|
|Antal |2 |5 |40 |40 |40|
</p>

Vi får ett review med texten "happy bad", använd Naive Bayes och klassificera den till positiv eller
negativ review.  

  
Svar: 

17. Beskriv kort skillnaderna mellan decision tree och random forest.  

  
Svar: 

18. Ge ett exempel på ett maskininlärningsproblem där man kan applicera logistisk regression.  

  
Svar: 

19. Beskriv kort skillnader mellan supervised learning och unsupervised learning.  

  
Svar: 

20. Beskriv kort skillnader mellan regression och klassificering.  

Svar: 

21. Rita upp ett decision tree baserat på följande figur. Tolka därefter detta decision tree.
![image.png](../Data/assets/image_1680161559841_0.png)  
  
Svar: 
  

22. Hitta det logiska felet i följande kod:  
```py
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

X, y = df.drop["default"], df["default"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33,
random_state=42)

scaler = StandardScaler()

scaled_X_train = scaler.fit_transform(X_train)
scaled_X_test = scaler.fit_transform(X_test)

model_SVC = SVC()
model_SVC.fit(scaled_X_train, y_train)

y_pred = model_SVC.predict(scaled_X_test)
# evaluation code ...
```
Svar: 

23. Ett brandlarm har låg precision och hög recall. Diskutera konsekvenserna kring detta brandlarm. På
vilket sätt kan detta vara bra, respektive dåligt?  

Svar: 