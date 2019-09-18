# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/migrationec2.html

# instance-state-code (16-bit unsigned integer)
# # 0 (pending)
# # 16 (running) 
# # 32 (shuttingdown)
# # 48 (terminated)
# # 64 (stopping)
# # 80 (stopped)

import sys
import boto3

pending = 0
running = 16
shuttingdown = 32 
terminated = 48
stopped = 80
stopping = 64


iid = 'i-0c304db8649b93df1'; 
ec2 = boto3.resource('ec2')

class Plutonium(object):
    def main(self, argv):
        print ('XXX===>>  BUILD_ID')
        for x in argv[1:]:
            if x in 'start':
                print('START INSTANCE');
                self.status(iid)
                self.start()
            elif x in 'stop':
                print('START INSTANCE');
            else:
                print('Invalid command ... [start|stop]');    
    
    
    def start(self):
        if self.status(iid) == stopped:
            print('*** STARTING INSTANCE ***');
        
    
        
        
        
    def stop(self):
        print('*** STOPPING INSTANCE ***');
        
        
        
    def status(self, iid):
        instance = ec2.Instance(iid);
        key,val = instance.state.values()
        return key
        
        
        
        
        
        
        
# --------------------------------------------------------------
        
        
        
        
if __name__ == '__main__':
    loader = Plutonium()
    loader.main(sys.argv)