import boto3

def lambda_handler(event, context):
   
  ec2 = boto3.client('ec2',
             aws_access_key_id= "AKIASR3C243CR2QSJKGS",
             aws_secret_access_key="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",
             region_name="ap-south-1"
            )
  
  instances = ec2.describe_instances(Filters=[  {'Name':'tag:Name', 'Values':["webserver"]},
                                              {'Name':'tag:Project', 'Values':["Uber"]},
                                              {'Name':'tag:env', 'Values':["dev"]}
                                           ]
                                    )

  for item in instances['Reservations']:
    
    instance = item['Instances'][0]
    instance_id = instance['InstanceId']
    print("Starting Instance : {}".format(instance_id))
    ec2.start_instances(InstanceIds=[ instance_id ])
