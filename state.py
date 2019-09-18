import boto3
ec2 = boto3.resource('ec2')

# ec2.Instance(fid)
#for instance in ec2.instances.all():
   
# instance-state-code (16-bit unsigned integer)
# # 0 (pending)
# # 16 (running) 
# # 32 (shutting-down)
# # 48 (terminated)
# # 64 (stopping)
# # 80 (stopped)
   
   
    
iid = 'i-0c304db8649b93df1';
    
instance = ec2.Instance(iid);
print (instance.id , instance.state);
