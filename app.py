from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/model',methods=['POST'])
def model():
    model1 = pickle.load(open('KNeighborsClassifier.pkl', 'rb'))
    model2 = pickle.load(open('LinearSVC.pkl', 'rb'))
    model3 = pickle.load(open('LogisticRegression.pkl', 'rb'))
    model4 = pickle.load(open('DecisionTreeClassifier.pkl', 'rb'))
    
    final_data = [np.array([x for x in request.form.values()])]
    prediction1 = model1.predict(final_data)
    prediction2 = model2.predict(final_data)
    prediction3 = model3.predict(final_data)
    prediction4 = model4.predict(final_data)

    if (prediction1[0] == 1):
        pred1 = "No"
        recommendation1 = "These customers should be given schemes accordingly to increase their purchase which will indirectly increase oneoff purchase and installment purchases."
        insight1 = "Customers of cluster 1 have a pretty good credit limit and balance but these customers have a very low oneoff purchase and purchases in comparison to cash advance. This means they take more cash advance and spend less through purchasing."
    elif (prediction1[0] == 0):
        pred1 = "Yes"
        insight1 = "Credit limit of customers of cluster 0 is lowest amongst all. These customers have a low balance but they have quite good purchase and installment purchases."
        recommendation1 = "These customers can be given discount offer on buying things so that they will start using their credit card more frequently."
    elif (prediction1[0] == 2):
        pred1 = "No"
        recommendation1 = "These customers should be encouraged by giving schemes to spend more and to increase the balance by keeping a minimum balance."
        insight1 = "These customers have a good credit limit but their balance, oneoff urchase, purchases, installment purchases is very low."
    elif (prediction1[0] == 3):
        pred1 = "Yes"
        recommendation1 = "These customers should be encouraged to keep decent balance in their account by keeping a minimum balance rule."
        insight1 = "These customers have the highest credit limit and oneoff purchase followed by purchases and installment purchases. They have highest payment of all clusters."
    else:
        pred1 = "Error"
        insight1 = "Error"
        recommendation1 = "Error"

    if (prediction2[0] == 0):
        pred2 = "No"
        insight2 = "Their Balance is less but they purchase without cash advances. They prefer instalments for purchases and make sure to repay the same at time."
        recommendation2 = "They are good customers even with less balance they purchase stuff. So give them schemes of discounts on some expensive products so that they are attracted to buy more stuff since they are frequent buyers . They are quite in number so the company should surely focus on them."
    elif (prediction2[0] == 1):
        pred2 = "Yes"
        insight2 = "Rich people with a lot of balance but not frequent buyers. Take a lot of cash advance to purchase expensive stuff."
        recommendation2 = "Come up with schemes that provide discounts on both expensive as well as ordinary items."
    elif (prediction2[0] == 2):
        pred2 = "No"
        insight2 = "Cream customer who have been there for a long time now and even do a lot of purchases. Take minimal cash advance and installments to do purchases."
        recommendation2 = "Make sure not to lose them .Come up with schemes which benefits them the most."
    elif (prediction2[0] == 3):
        pred2 = "Yes"
        insight2 = "Less balance and not much purchases. They don’t even take cash advance and installments to do purchases."
        recommendation2 = "Focus a lot on them as they are a lot in number and aren't giving much profits. Come up with the schemes that make them active users."
    else:
        pred2 = "Error"
        insight2 = "Error"
        recommendation2 = "Error"

    if (prediction3[0] == 0):
        pred3 = "No"
        insight3 = "The patient is not diagnosed with cancer."
        recommendation3 = "You must take care."
    elif (prediction3[0] == 1):
        pred3 = "Yes"
        insight3 = "The patient is diagnosed with cancer."
        recommendation3 = "You must take care."
    elif (prediction3[0] == 2):
        pred3 = "No"
        insight3 = "Cream customer who have been there for a long time now and even do a lot of purchases. Take minimal cash advance and installments to do purchases."
        recommendation3 = "Make sure not to lose them .Come up with schemes which benefits them the most."
    elif (prediction3[0] == 3):
        pred3 = "Yes"
        insight3 = "Less balance and not much purchases. They don’t even take cash advance and installments to do purchases."
        recommendation3 = "Focus a lot on them as they are a lot in number and aren't giving much profits. Come up with the schemes that make them active users."
    else:
        pred3 = "Error"
        insight3 = "Error"
        recommendation3 = "Error"

    if (prediction4[0] == 0):
        pred4 = "No"
        insight4 = "Their Balance is less but they purchase without cash advances. They prefer instalments for purchases and make sure to repay the same at time."
        recommendation4 = "They are good customers even with less balance they purchase stuff. So give them schemes of discounts on some expensive products so that they are attracted to buy more stuff since they are frequent buyers . They are quite in number so the company should surely focus on them."
    elif (prediction4[0] == 1):
        pred4 = "Yes"
        insight4 = "Rich people with a lot of balance but not frequent buyers. Take a lot of cash advance to purchase expensive stuff."
        recommendation4 = "Come up with schemes that provide discounts on both expensive as well as ordinary items."
    elif (prediction4[0] == 2):
        pred4 = "No"
        insight4 = "Cream customer who have been there for a long time now and even do a lot of purchases. Take minimal cash advance and installments to do purchases."
        recommendation4 = "Make sure not to lose them .Come up with schemes which benefits them the most."
    elif (prediction4[0] == 3):
        pred4 = "Yes"
        insight4 = "Less balance and not much purchases. They don’t even take cash advance and installments to do purchases."
        recommendation4 = "Focus a lot on them as they are a lot in number and aren't giving much profits. Come up with the schemes that make them active users."
    else:
        pred4 = "Error"
        insight4 = "Error"
        recommendation4 = "Error"

    return render_template('index.html', prediction1=f'Cluster {prediction1[0]}', insight1=insight1, recommendation1=recommendation1, pred1=pred1, prediction2=f'Cluster {prediction2[0]}', insight2=insight2, recommendation2=recommendation2, pred2=pred2, prediction3=f'Cluster {prediction3[0]}', insight3=insight3, recommendation3=recommendation3, pred3=pred3, prediction4=f'Cluster {prediction4[0]}', insight4=insight4, recommendation4=recommendation4, pred4=pred4)

if __name__ == "__main__":
    app.run(debug=True)