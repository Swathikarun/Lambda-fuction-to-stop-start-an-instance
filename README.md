# Lambda-fuction-to-stop-start-an-instance

AWS Lambda is Amazon’s serverless compute service. You can run your code on it without having to manage servers or even containers. It will automatically scale depending on how much work you feed into it. And it build event-driven functions for easy communication between decoupled services. Reduce costs by running applications during times of peak demand i.e you need to pay only for the time taken to execute the code. The key features of Lambda function are : 

- Run code without provisioning or managing infrastructure. Simply write and upload code as a .zip file or container image
- Automatically respond to code execution requests at any scale, from a dozen events per day to hundreds of thousands per second.
- Save costs by paying only for the compute time you use by per-millisecond instead of provisioning infrastructure upfront for peak capacity.
- Optimize code execution time and performance with the right function memory size. 

## Synopsis

First we will be creating a lambda function to stop/start testing instance in order to reduce cost. Then we will create a python code to stop, start instance and upload it to Lambda. Now we will apply a trigger on lambda function using AWS cloudwatch events. We have crontab facility in AWS cloudwatch, so we schedule a cronjob to apply the trigger on lambda at the demanding time.

## Requirements

- Boto module

  ```
  # pip3 install boto3
  ```
  - Python code to stop/start instance (stop.py, start.py)

## Provisioning

### 1. Create an IAM Role 

 An IAM role with "AmazonEC2FullAccess" premission is created to allow Lambda functions to call AWS services.

![role1](https://user-images.githubusercontent.com/94472101/153706177-565f2320-7cef-4be3-b8ec-3558e4502b43.png)
![role2](https://user-images.githubusercontent.com/94472101/153706184-0fd33cca-de90-4be0-a6f6-b0fd56fbbaa2.png)
![role3](https://user-images.githubusercontent.com/94472101/153706186-82ef4f16-ef42-4b01-ae72-22525ce5829d.png)

### 2. Create a Lambda function 

For that navigate to Lambda >> Functions >> create function - provide the Basic information, select the pre-created IAM role "ec2-stop-start" >> Create Function

![lambda10](https://user-images.githubusercontent.com/94472101/153706405-e36e315a-a421-4697-82b0-5373a8bebc86.png)

The created lambda function interface will be as below :

![lambda11](https://user-images.githubusercontent.com/94472101/153706441-0b6e095e-32e4-4377-94cd-827df5a42244.png)

Now replace the default code with our python code to stop the instance and click on the "Deploy" button to update/upload the code to the lambda fuction.

![lambda13](https://user-images.githubusercontent.com/94472101/153707547-a9fb0fae-88c9-4f0e-ae71-eb372d1dddd8.png)

### 3. Apply Trigger

Now we will apply a trigger on Lambda function using the AWS Cloudwatch to run the code on our time demanded. We have crontab feature in AWS Cloudwatch to schedule a cronjob.

Navigate to AWS Cloudwatch >> Events >> Rule >> Create Rule

![lambda14](https://user-images.githubusercontent.com/94472101/153707846-1460c9dc-b6c1-44a0-a7e7-2bf19e7d1594.png)

Select Cron Expression under Schedule and set a cronjob. Now set up Trigger by Adding Target for lambda function and select the precreated  Lambda function "test-instance-stop" 

![lambda15](https://user-images.githubusercontent.com/94472101/153707875-944530e2-cd12-47e7-bf3d-ab6edf501950.png)

On selecting the created rule we can see next 10 Trigger Dates listed

![Screenshot from 2022-02-12 16-20-05](https://user-images.githubusercontent.com/94472101/153708373-af656542-fab4-4589-8a42-9a7c503fae14.png)

>> NOTE :: Follow the same proceedure to create a lambda function to start an instance by replacing a single line in the code "ec2.stop_instances(InstanceIds=[ instance_Id ])" to "ec2.start_instances(InstanceIds=[ instance_Id ])".

## Result

A lambda function is created to stop and start a testing instance during times of peak demand by reducing the cost.

![lambda18](https://user-images.githubusercontent.com/94472101/153708472-97780b5e-f6ea-48cd-bdad-bb0da360f8f0.png)

![start](https://user-images.githubusercontent.com/94472101/153709007-c746623c-879e-407d-8156-4262711599e5.png)






