# Build and compare models performances using IBM SPSS Modeler

If you want more flexibility in preparing your data and building your models than what Watson Studio's Automatic Modeler offers, but still want the ease of use of a GUI interface and less code writing and complexity, you can use IBM SPSS Modeler for exactly that.
<br></br>

1. Create a **New Flow** from Modeler Flows in the main dashboard of Watson Studio.  
![1](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/1.jpg?raw=true)
<br></br>

2. Type a **Name** for your Modeler task, select **Modeler Flow** as flow type and select **IBM SPSS Modeler** as runtime.  
![2](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/2.jpg?raw=true)
<br></br>

3. Let's start by importaning our dataset. Click on **Import** on the left-side panel.  
![3](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/3.jpg?raw=true)
<br></br>

4. Drag and drop **Data Assets** node into the Modeler canvas.  
![4](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/4.jpg?raw=true)
<br></br>

5. Double-click the node on the canvas to start editing its properties.  
![5](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/5.jpg?raw=true)
<br></br>

6. Click on **Change Data Asset** to define the source of our data.  
![6](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/6.jpg?raw=true)
<br></br>

7. A list of all the data assets you have in this project will be listed. Let's select `customers_credit_status.csv`, available [here](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/03-LoanApprovalModel/customers_credit_status.csv).  
If you have been following along the tutorials in their numbered sequence, you should have the dataset imported already and available.  
Note: Names of datasets in the screenshots may be different from what you have.  
After selecting the dataset, click **Ok**.  
![7](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/7.jpg?raw=true)
<br></br>

8. Making sure the dataset is imported. Click **Save**.  
![8](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/8.jpg?raw=true)
<br></br>

9. Let's check our data quality. Drag and drop **Data Audit** node.  
![9](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/9.jpg?raw=true)
<br></br>

10. Connect the nodes.  
![10](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/10.jpg?raw=true)
<br></br>

11. Let's run the flow to get the results of the data audit.  
![11](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/11.jpg?raw=true)
<br></br>

12. Wait for the process to finish.  
![12](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/12.jpg?raw=true)
<br></br>

13. In the right-side panel, under the **Outputs** tab, let's select the most recent output (most recent is always on top) to view the results of running the flow so far.  
![13](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/13.jpg?raw=true)
<br></br>

14. We get an idea about some statistics of the data and the distribution of the features. We find that the data needs some kind of normalization.  
![14](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/14.jpg?raw=true)
<br></br>

15. Let's go back to our Modeler and continue working there.  
![15](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/15.jpg?raw=true)
<br></br>

16. We want to split our data into Train and Test sets, we will do so using the **Partition** node.  
![16](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/16.jpg?raw=true)
<br></br>

17. Double-clicking on the **Partition** node to explore its properties. We'll leave everything as it is.  
![17](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/17.jpg?raw=true)
<br></br>

18. We'll add **Auto Data Prep** to automatically find issues in our dataset and fix it.  
![18](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/18.jpg?raw=true)
<br></br>

19. We'll do another **Data Audit** to check the results of the previous step.  
![19](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/19.jpg?raw=true)
<br></br>

20. View the results.  
![20](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/20.jpg?raw=true)
<br></br>

21. The data has been normalized and issues have been fixed.  
![21](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/21.jpg?raw=true)
<br></br>

22. Now let's select a model, let's try **LSVM**.  
![22](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/22.jpg?raw=true)
<br></br>

23. Double-clicking on the **LSVM** node to change its properties. Check **Use custom field roles**, then select `class_transformed` as the target(labels) column and select all other columns as **Inputs**. Click **Save**.  
![23](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/23.jpg?raw=true)
<br></br>

24. Let's run the flow.  
![24](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/24.jpg?raw=true)
<br></br>

25. Wait for the process to finish. It may take a few minutes.  
![25](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/25.jpg?raw=true)
<br></br>

26. After the model runs, it will produce a new node that holds information about the performance of the model.  
![26](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/26.jpg?raw=true)
<br></br>

27. Let's add an **Analysis** node to peak into the model results node.  
![27](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/27.jpg?raw=true)
<br></br>

28. Connect the nodes.  
![28](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/28.jpg?raw=true)
<br></br>

29. View the output.  
![29](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/29.jpg?raw=true)
<br></br>

30. Information about how our model performed.  
![30](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/30.jpg?raw=true)
<br></br>

31. I added a few other models for comparison. Feel free to try your own combinations.  
![31](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/31.jpg?raw=true)
<br></br>

32. If we click on the **LSVM** model node again and choose **View model**, we will get more detailed information about different performance metrics.  
![36](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/36.jpg?raw=true)
<br></br>
![37](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/37.jpg?raw=true)
<br></br>
![38](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/38.jpg?raw=true)
<br></br>
![39](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/39.jpg?raw=true)
<br></br>

33. Checking another model's performance as we did in the previous step.  
![32](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/32.jpg?raw=true)
<br></br>
![33](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/33.jpg?raw=true)
<br></br>
![34](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/34.jpg?raw=true)
<br></br>
![35](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/35.jpg?raw=true)
<br></br>

34. We're satisfied with our first model, it has better overall performance. Let's click on its node **LSVM** and select **Save branch as model**.  
![40](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/40.jpg?raw=true)
<br></br>

35. Type a name for your model and a machine learning service should be detected and added automatically. Then click **Save**.  ![41](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/41.jpg?raw=true)
<br></br>

36. The model has been saved successfully.  
![42](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/42.jpg?raw=true)
<br></br>

37. You can access it as we have seen in other demos through the Models panel in the main dashboard.  
![43](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/05-LoanApprovalSPSSModeler/imgs/43.jpg?raw=true)
<br></br>
