# Create a Credit Card Approval Model using IBM Watson Studio Automatic Modeler

IBM Watson Studio Automatic Modeler is a quick and easy to use tool for building Machine Learning models, evaluating and deploting them without the need to write any code. You just provide the data.


1. In Watson Studio's mani dashboard, select **New Model** from the Models panel.  
![1](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/1.jpg?raw=true)
<br></br>

2. Type a name for your model. Make sure a **Machine Learning** service instance is selected, if not you'll be prompted to create one. Please refer to the README.md in the root of this repository.  
Select **Modeler** as Model Type.  
Select a **Spark** service. If one was not found you'll be asked to create one then click reload to select the newly created service.  
Select **Automatic** for more convenience, or **Manual** for more configurability in choosing the models.  
Click **Create**.
![2](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/2.jpg?raw=true)
<br></br>

3. First step is to choose the dataset you want to train the model on. In this case we will select `Credit_Card_Applicants.csv`. If you're following along the tutorials in the sequence of the folder numbering, you should have the dataset uploaded and imported in Watson Studio. If not, please refer to the relevant steps in the folder `02-CreditCardApprovalModel` in this repository.  
After choosing the dataset click **Next**.  
![3](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/3.jpg?raw=true)
<br></br>

4. The dataset will be loaded.  
![4](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/4.jpg?raw=true)
<br></br>

5. You'll move on to the train step. You need to pick first your target (labels) column. In our case, it will be the last column `COLUMN16`.  
![5](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/5.jpg?raw=true)
<br></br>

6. Let's select the feature columns we want to feed into the model. You can pick as many as you want, here we will pick them all.  
![6](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/6.jpg?raw=true)
<br></br>

7. After selecting features and labels, the modeler will automatically suggest a technique for building the model based on the dataset. Here it selected **Binary Classification**. The modeler will select the train and test split percentages as well. We will go ahead with that and click **Next**.  
![7](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/7.jpg?raw=true)
<br></br>

8. Training the model will start.  
![8](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/8.jpg?raw=true)
<br></br>

9. An algorithm will be automatically selected based on the dataset, here **Logistic Regression** was selected.  
![9](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/9.jpg?raw=true)
<br></br>

10. After the training process is finished, the model's performance will be evaluated on the test split automatically done in an earlier step. It will print out model's evaluation using different metrics. We are satisfied with the result of the training her and we will go ahead and **Save** the model.  
![10](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/10.jpg?raw=true)
<br></br>

11. Confirm model saving.  
![11](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/11.jpg?raw=true)
<br></br>

12. You will be redirected to a summary about your model.  
![12](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/12.jpg?raw=true)
<br></br>

13. Now, we want to deploy the trained model to use it in prodcution on new data. Let's select the model, go to **Deployments** tab and click on **New Deployment**.  
![13](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/13.jpg?raw=true)
<br></br>

14. There are 3 options for deploying your model. `Web Service` allows integration with a web/mobile app and calling the model using REST API. `Batch Prediction` allows for sending batches of data at once for the model to produce predictions on. Lastly, `Real-time Streaming Predictions` is useful when you have data streamed continuously from some source (IoT device for example). The Implementation tab provides useful snippets of code that help you integrate your model with your app.  
In our case we will choose **Web Service** and we will type in a name for our service and then click **Save**.  
![14](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/14.jpg?raw=true)
<br></br>

15. After deployment success you should see the following screen.  
![15](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/15.jpg?raw=true)
<br></br>

16. Let's select the recent deployment we made to test the model.  
![16](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/16.jpg?raw=true)
<br></br>

17. Go to **Test** tab.  
![17](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/17.jpg?raw=true)
<br></br>

18. Provide input for your model, then hit **Predict**. Here I used some data from our dataset for easiness.  
![18](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/18.jpg?raw=true)
<br></br>

19. We can now see the model's prediction for the data we provided. The prediction is showing the predicted class `+` which means the applicant will be accepted and it also shows the confidence of the model's decision for each class.  
![19](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/19.jpg?raw=true)
<br></br>

20. Comparing that with our dataset, indeed the prediction is correct.  
![20](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/04-CreditCardApprovalWMLModeler/imgs/20.jpg?raw=true)
<br></br>
