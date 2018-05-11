# Create an Interactive Dashboard

Quickly and easily create and share interactive dashboards and infographics using your data.
<br></br>
To check out the Live Infographic that has been created using this tutorial click here:  
[https://dataplatform.ibm.com/dashboards/842d6d62-bfa1-4c31-bc5a-a43c89a49073/view/5820aa256eac11cb5cd1e2e407cc28017b322108b5bb8b0088d07b490d312097f36a40c2c82f4f5cdc180536fbb9165ec0](https://dataplatform.ibm.com/dashboards/842d6d62-bfa1-4c31-bc5a-a43c89a49073/view/5820aa256eac11cb5cd1e2e407cc28017b322108b5bb8b0088d07b490d312097f36a40c2c82f4f5cdc180536fbb9165ec0)
<hr></hr>

1. Upload `customer_demographics.csv` dataset into Watson Studio. Dataset is provided in this folder.  
![1](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/1.jpg?raw=true)
<br></br>

2. From Watson Studio's main dashboard, select **New Dashboard** from Dashboards panel.  
![2](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/2.jpg?raw=true)
<br></br>

3. Type a name for your dashboard. Make sure you have a `dashboard analytics` service instance running and selected, if not you'll be prompted to create one then reload to select it. Click **Save**.  
![3](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/3.jpg?raw=true)
<br></br>

4. Select the template you wish to create, here I used an Infographic template.  
![4](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/4.jpg?raw=true)
<br></br>

5. Select the page layout and click **Ok**.  
![5](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/5.jpg?raw=true)
<br></br>

6. Select a source for the data that will be used.  
![6](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/6.jpg?raw=true)
<br></br>

7. We'll select our Customer Demographics dataset and click **Select**. Note that the names shown in the image may be different from what you have.  
![7](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/7.jpg?raw=true)
<br></br>

8. Click on the dataset to expand it.  
![9](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/9.jpg?raw=true)
<br></br>

9. We now see all the rows.  
![10](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/10.jpg?raw=true)
<br></br>

10. Let's select columns for a visualisation. You can select multiple columns by pressing `Ctrl` or `Cmd` while selecting the columns. Here, I selected `job` and `balance`. Drag and drop your selected columns to where you want to place them on the infographic template.  
![11](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/11.jpg?raw=true)
<br></br>

11. A visualization will be automatically picked for you, based on the data in the columns you selected. Here a **Columns Chart** was picked.  
![12](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/12.jpg?raw=true)
<br></br>

12. If you need to edit the visualization, click on the crossing arrows on top of the visualization and a side panel will appear. Click on the visualization image as shown below.  
![13](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/13.jpg?raw=true)
<br></br>

13. To select another visualization method, select one from the listed options. Here, I wanted more customization for the current visualization so click on **More**.  
![14](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/14.jpg?raw=true)
<br></br>

14. Confirm the Column Chart option to proceed.  
![15](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/15.jpg?raw=true)
<br></br>

15. Here, we'll select the method of summarization of the balance column. It has continuous values and they were originally represented as a sum.  
![16](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/16.jpg?raw=true)
<br></br>

16. Let's change the summary into **Average**.  
![17](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/17.jpg?raw=true)
<br></br>

17. The change has been reflected.  
![18](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/18.jpg?raw=true)
<br></br>

18. Now for making a better UI, let's choose a way to color the columns. Here, I picked coloring the columns according to the distinct categories of jobs we have, so I inserted `job` column into the color property.  
![19](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/19.jpg?raw=true)
<br></br>

19. Let's enter a title for our visualization. Choose the multimedia option from the left side-panel.  
![20](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/20.jpg?raw=true)
<br></br>

20. Select the text option and drag it to where you want on the infographic template.  
![21](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/21.jpg?raw=true)
<br></br>

21. Adding a title to the Infographic.  
![22](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/22.jpg?raw=true)
<br></br>

22. You can choose **Properties** from the top toolbar to change the properties of any object in the visualization. Here I chose text properties.  
![23](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/23.jpg?raw=true)
<br></br>

23. Changing the font weight, alignment and color.  
![24](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/24.jpg?raw=true)
<br></br>

24. You can choose different themes for the visualization. Let's switch to a **Dark** theme.  
![25](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/25.jpg?raw=true)
<br></br>

25. Other properties available for customization.  
![26](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/26.jpg?raw=true)
<br></br>

26. Let's create another visualization. This time let's pick the `marital` column from our dataset.  
![27](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/27.jpg?raw=true)
<br></br>

27. Let's customize the visualization. I chose a **Pie Chart** for representing the different categories (summary ===> count) of the columns data. I chose to color the chart by `marital` data as well, a differnt color for each category.  
![28](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/28.jpg?raw=true)
<br></br>

28. Added a couple of other visualizations. You can try different styles.  
![29](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/29.jpg?raw=true)
<br></br>

29. After finishing the Infographic or the Dashboard, you can create a link to a **Read-Only** version of it and share it with anyone.
![30](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/30.jpg?raw=true)
<br></br>

30. All visualizations are interactive!  
![31](https://github.com/HebaNAS/IBM-Watson-Studio-Enablement/blob/master/06-CustomerDemographicsDashboard/imgs/interactive.gif?raw=true)
<br></br>
