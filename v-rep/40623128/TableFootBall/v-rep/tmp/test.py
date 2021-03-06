import vrep
import sys, math
# child threaded script: 
# 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
#simExtRemoteApiStart(19999)
 
vrep.simxFinish(-1)
 
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
 
if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')
 
#errorCode,Revolute_joint_handle=vrep.simxGetObjectHandle(clientID,'Prismatic_joint',vrep.simx_opmode_oneshot_wait)
#errorCode,Prismatic_joint_handle=vrep.simxGetObjectHandle(clientID,'R1',vrep.simx_opmode_oneshot_wait)
#errorCode=simxStart(clientID,simx_opmode_oneshot)
errorCode= vrep.simxStopSimulation(clientID,vrep.simx_opmode_oneshot)
errorCode= vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot)
if errorCode == -1:
    print('Can not find left or right motor')
    sys.exit()
    
def stop():
    errorCode = vrep.simxStopSimulation(clientID,vrep.simx_opmode_oneshot)
    
def start():
    errorCode = vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot)

vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)
vrep.simxStopSimulation(clientID,vrep.simx_opmode_oneshot_wait)
print(vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait))
print(vrep.simxStopSimulation(clientID,vrep.simx_opmode_oneshot_wait))