# Create and experiment with Deep Learning Models using Neural Network Modeler and Experiments

Deep Learning is an efficient technique to solve complex problems, and the "Science" part of Data Science is all about experimenting with different settings and comparing results. Using Watson Studio you can easily architect a Neural Network using a friendly GUI, download the model as code in your favorite framework's settings and create experiments to compare between different hyperparameter optimization settings.
<br></br>
In this tutorial, we will build a model that detects signature fraud by training on signature images provided. Images are resized to 128x64 and are read into numpy arrays and are pickled.

1. For this tutorial, you'll need to download all the assets provided in this folder.
<br></br>

2. You'll also need to upload 2 files to your **Object Storage**. You can access it by going to [IBM **Cloud** Dashboard](https://console.bluemix.net/dashboard/).  
![6](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/6.jpg?raw=true)
<br></br>

3. Create a **New Bucket** to be easy to find the data you'll upload in the next step.  
![7](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/7.jpg?raw=true)
<br></br>

4. Name the new bucket and leave all other settings as they are, then click **Create**.  
![8](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/8.jpg?raw=true)
<br></br>

5. Start adding objects to your newly created bucket.  
![9](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/9.jpg?raw=true)
<br></br>

6. Click **Add Files** and upload both of these files `training.pickle` and `test.pickle` (that you've downloaded from this folder beforehand).  
![10](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/10.jpg?raw=true)
<br></br>

7. Click **Upload Objects**.  
![11](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/11.jpg?raw=true)
<br></br>

8. Wait till the process finishes.  
![12](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/12.jpg?raw=true)
<br></br>

9. Now you have your files uploaded successfully.  
![13](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/13.jpg?raw=true)
<br></br>

10. Create a **New Flow** from Watson Studio's main dashboard.  
![1](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/1.jpg?raw=true)
<br></br>

11. Type a name for your model and select **Neural Network Modeler** then click **Create**.  
![2](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/2.jpg?raw=true)
<br></br>

12. We need to provide data for our model. To do that, let's select **Image Data** from the Input Section.  
![3](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/3.jpg?raw=true)
<br></br>

13. Drag and drop the node on to the canvas, then double-click it to modify its properties.  
![5](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/5.jpg?raw=true)
<br></br>

14. First we need to create a new connection to our Object Storage instance (COS) or select one if already exists.  
![14](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/14.jpg?raw=true)
<br></br>

15. Select the bucket you created in this tutorial earlier. Mine was `singatures` so I chose it.  
![15](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/15.jpg?raw=true)
<br></br>

16. Select the training data file `training.pickle`.  
![16](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/16.jpg?raw=true)
<br></br>

17. Select the test data file `test.pickle`.  
![17](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/17.jpg?raw=true)
<br></br>

18. Now close the **Data** Section and switch to **Settings** Section in the same right-side panel. Adjust all settings as shown in the screenshot below and click **Save**.  
![18](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/18.jpg?raw=true)
<br></br>

19. Now let's start building the Neural Network. First Layer we will add is a 2D Convolutional Layer. Select **Conv 2D** node from Convolution section and drag and drop it on to the canvas.  
![19](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/19.jpg?raw=true)
<br></br>

20. Connect the nodes, double-click on **Conv 2D** node to edit its properties to the same as shown below and click **Save**.  
![20](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/20.jpg?raw=true)
<br></br>

21. Let's add another **Conv 2D** Layer.  
![21](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/21.jpg?raw=true)
<br></br>

22. Edit the second **Conv 2D** node's properties as in the screenshot below and click **Save**.  
![22](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/22.jpg?raw=true)
<br></br>

23. Now we'll add a Max-Pooling layer. Drag and drop **Pool 2D** from Convolution section on to the canvas.  
![23](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/23.jpg?raw=true)
<br></br>

24. Double-click **Pool 2D** node to edit its properties. Use settings as shown below and click **Save**.  
![24](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/24.jpg?raw=true)
<br></br>

25. Next we'll add a Dropout. Select **Dropout** from Core section and drag and drop it onto the canvas. Double-click the node and change its settings to what's shown below then click **Save**.  
![25](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/25.jpg?raw=true)
<br></br>

26. Add a **Flatten** node from Core section.  
![26](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/26.jpg?raw=true)
<br></br>

27. Add **Dense** node from Core section to the canvas, change settings to that shown below and click **Save**.  
![28](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/28.jpg?raw=true)
<br></br>

28. Add another **Dropout** node.  
![29](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/29.jpg?raw=true)
<br></br>

29. Add **Dense** node and change its settings as shown below and click **Save**.  
![30](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/30.jpg?raw=true)
<br></br>

30. I addd another 4 nodes, **Softmax** from Activation section, then Sigmoid Cross-Entropy from Loss Section and Accuracy from Metrics, both connected to the last layer we had. Lastly, connect a **SGD** node for Optimization.  
![31](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/31.jpg?raw=true)
<br></br>

31. You can save your flow chart as a model. You can download the code accroding to your choice of framework.  
![32](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/32.jpg?raw=true)
<br></br>

32. You can also directly publish the model to Watson Studio's repository and train it later.  
![33](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/33.jpg?raw=true)
<br></br>

33. For publishing, type a name for the training definition and make sure there is a machine learning instance connected, then click **Publish**.  
![34](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/34.jpg?raw=true)
<br></br>

34. Now let's use the training definition we just published to actually train the model. Go to Watson Studio's main Dashboard and select **New Experiment** from Experiments panel.  
![35](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/35.jpg?raw=true)
<br></br>

35. Connect to you Object Storage instance, use the existing connection.  
![36](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/36.jpg?raw=true)
<br></br>

36. Select the bucket containing the training data. As we defined earlier, it will be the bucket you created on Object Storage. Mine was `signatures`, so I chose that.  
![37](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/37.jpg?raw=true)
<br></br>

37. Select a bucket for saving the training results. You can choose to save it in the same bucket as your training definitions, but here I picked another bucket.   
![38](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/38.jpg?raw=true)
<br></br>

38. After finishing the previous step, click **Add Training Definition** as shown below.  
![41](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/41.jpg?raw=true)
<br></br>

39. Let's pick the training definition we just published from the Neural Network Modeler. Follow the screenshot below then click **Add**.  
![39](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/39.jpg?raw=true)
<br></br>

39. You'll be redirected to a page where all your training jobs will be listed and you can monitor them. You can add more training runs as well.  
![40](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/40.jpg?raw=true)
<br></br>

40. You can import your own model written in python and not use the Neural Network Modeler. It's a bit tricky as you need to integrate with Watson Studio's evaluation metrics.  
Provided in this folder a Keras model `CNN.py` (originally downloaded from the previously created Neural Network Flow), the code was edited by adding some global variables to tell the system where to look for the training data and where to save the model. Added also some functions to evaluate the model and some logging functionality.  
Also provided `emetrics.py` which is crucial to run evaluation metrics and provide the platform with results on which you can comare different models.  
The training and test data are also enclosed in this folder.  
All files are archived into `CNN.zip` for easiness. You can download that to your local machine and follow the steps in refernce to the screenshot below to create a **New Training Definition** based on your written code.  
![42](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/42.jpg?raw=true)
<br></br>

41. The training definition we added should run successfully and when done, it will show as **Completed**. You can click it to get more details about the job. In the image below we monitor the model training and metrics across the process.  
![44](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/44.jpg?raw=true)
<br></br>

42. You can also view the logs to get more details about the progress or errors in the process.  
![45](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/45.jpg?raw=true)
<br></br>

43. Another important functionality you have is to optimize the hyperparameters of the model to tweak its performance.  
![43](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/43.jpg?raw=true)
<br></br>

44. You can compare different runs of the same model, but with different hyperparameters.  
![47](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/47.jpg?raw=true)
<br></br>
![48](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/48.jpg?raw=true)
<br></br>

45. Once you're satisfied with a model, you can save it and access it from Models panel in Watson Studio's main dashboard.  
![46](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/46.jpg?raw=true)
<br></br>

46. Saving the model. You only need to provide a name for your model, then click **Save**.  
![49](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/49.jpg?raw=true)
<br></br>

47. You'll be notified when the process finishes, and you can click to view model details or access it from the Dashboard in the Models panel.  
![50](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/50.jpg?raw=true)
<br></br>

48. Let's deploy our model to use it and test it.  
![51](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/51.jpg?raw=true)
<br></br>

49. We'll deploy it as a **Web Service**, you can choose Batch Prediction if you have several files containing data needing prediction at once.  
![52](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/52.jpg?raw=true)
<br></br>

50. Once deployment is successful, we'll click on the deployment.  
![53](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/53.jpg?raw=true)
<br></br>

51. Click on the **Test** tab, and enter the raw input as provided in this gist: [https://gist.github.com/HebaNAS/47e21e45ea803365fc5555abbd58a07d](https://gist.github.com/HebaNAS/47e21e45ea803365fc5555abbd58a07d). Click **Predict**. You'll get a response back from the model.   
![54](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/08-SignatureFraudDetectionNNModeler/imgs/54.jpg?raw=true)
<br></br>
