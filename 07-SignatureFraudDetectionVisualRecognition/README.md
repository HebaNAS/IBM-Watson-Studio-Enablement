# Create a Signature Fraud Detection Model using Watson Visual Recognition

IBM Watson Visual Recognition service provides you an easy way to train a model on a dataset of images that you provide and use that model later as a classifier on new images. Leverage the power of Watson by using Transfer Learning technique, where you use Watson Visual Recognition pre-trained, highly accurate models and adjust only some layers to retrain on your own images to match your specific use case. All of this is done behind the scenes for you and the process of creating a new model is easy and quick thanks to a user-friendly UI.
<br></br>

1. Let's create a new **Visual Recognition** service instance from IBM **Cloud**.  
![1](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/07-SignatureFraudDetectionVisualRecognition/imgs/1.jpg?raw=true)
<br></br>

2. Don't change any settings and click **Create**. Note that you should always prefer _US-South_ as a region/location.  
![2](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/07-SignatureFraudDetectionVisualRecognition/imgs/2.jpg?raw=true)
<br></br>

3. Now you have the service up and running.  
![3](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/07-SignatureFraudDetectionVisualRecognition/imgs/3.jpg?raw=true)
<br></br>

4. Let's go back to Watson Studio's main dashboard. Click **New visual recognition model** from Visual Recognition panel.  
![4](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/07-SignatureFraudDetectionVisualRecognition/imgs/4.jpg?raw=true)
<br></br>

5. Make sure that the visual recognition service instance name matches that created on IBM **Cloud** for things to run smoothly. Note that in this tutorial you'll find them different as I used 2 accounts to create this tutorial. That shouldn't be the normal case.  
Download the Training Datasets from these links and to your desktop:
- [https://ibm.box.com/v/GenuineSignature](https://ibm.box.com/v/GenuineSignature)
- [https://ibm.box.com/v/ForgedSignature](https://ibm.box.com/v/ForgedSignature)  
Upload these zip files into the allocated area by dragging and dropping or browsing and selecting these datasets from their storage destination.  
![5](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/07-SignatureFraudDetectionVisualRecognition/imgs/5.jpg?raw=true)
<br></br>

6. Selected both datasets and click on the menu as shown below, then select **Add selected to model**.  
![6](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/07-SignatureFraudDetectionVisualRecognition/imgs/6.jpg?raw=true)
<br></br>

7. Wait for a few minutes till the datasets are fully loaded. They will be added to separate classes based on the name of the zip files you provided. Now our model is ready for training, so let's hit **Train Model**.  
![7](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/07-SignatureFraudDetectionVisualRecognition/imgs/7.jpg?raw=true)
<br></br>

8. Give Watson a few minutes to train the model on the provided images.  
![8](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/07-SignatureFraudDetectionVisualRecognition/imgs/8.jpg?raw=true)
<br></br>

9. After training is finished, you should arrive at a screen similar to below. Now let's test our model.  
![9](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/07-SignatureFraudDetectionVisualRecognition/imgs/9.jpg?raw=true)
<br></br>

10. Click on **Test** tab.  
![10](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/07-SignatureFraudDetectionVisualRecognition/imgs/10.jpg?raw=true)
<br></br>

11. Drag and drop or browse to choose new images to test the model. Test images are provided in this folder `TestImages`, with their relevant key sheet.  
![11](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/07-SignatureFraudDetectionVisualRecognition/imgs/11.jpg?raw=true)
<br></br>

12. Give the model a minute to run and come up with results.  
![12](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/07-SignatureFraudDetectionVisualRecognition/imgs/12.jpg?raw=true)
<br></br>

13. The model gives us these results.  
![13](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/07-SignatureFraudDetectionVisualRecognition/imgs/13.jpg?raw=true)
<br></br>

14. Let's compare the results to our Correct answers sheet provided also in `TestImages` folder. The results are correct.   
![18](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/07-SignatureFraudDetectionVisualRecognition/imgs/18.jpg?raw=true)
<br></br>

15. Let's click on the **Implementation** tab to take a look at the available help resources.  
![14](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/07-SignatureFraudDetectionVisualRecognition/imgs/14.jpg?raw=true)
<br></br>

16. You will find snippets of code in different languages to help you integrate the model with your apps. You can also integrate it with Apple's Core ML to use your model on Apple's devices natively. 
![15](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/07-SignatureFraudDetectionVisualRecognition/imgs/15.jpg?raw=true)
<br></br>

17. Let's test our model using the `cURL` interface. We'll bring up the terminal, navigate to the folder where we have our TestImages (should be downloaded for this step), then type in the following command:
```
curl -X POST --form "images_file=@Q002.png" --form "classifier_ids=SignatureCheckModel_744601344" "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify?api_key={USE_YOUR_API_KEY}&version=2016-05-20"
```
and hit return. Note that you will need the Visual Recognition service API key from IBM **Cloud** as shown earlier.   
![16](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/07-SignatureFraudDetectionVisualRecognition/imgs/16.jpg?raw=true)
<br></br>

18. The results that came back match what we had in the GUI.  
![17](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/07-SignatureFraudDetectionVisualRecognition/imgs/17.jpg?raw=true)
<br></br>
