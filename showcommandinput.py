from netmiko import ConnectHandler
from datetime import datetime
import paramiko,sys
import getpass


device_list = ['cisco1','cisco2','cisco3']

user_name = input ("Enter your username: ")
user_password = getpass.getpass("Enter your password: ")

# user_name = 'amit'
# user_password ='secret password'

start_time = datetime.now()


for a_device in device_list:
    host_name = a_device
    net_connect = ConnectHandler(device_type='cisco_ios', host=host_name, username=user_name, password=user_password)
    #output = net_connect.send_command(command_input)
    router_hostname = net_connect.send_command("show run | in hostname")
    router_hostname = router_hostname[8:]
    print("\n-------you are connected{} -----".format(router_hostname))
    #print("\n-------you are connected{} -----".format(router_hostname[8:]))
   # for device_x in device_list:
    x = 1
    while x > 0:
        print("\n Type your command or type 'quit' or 'no' to exit")
        command_input = input(':')
        if command_input=='quit' or command_input=='QUIT' or command_input=='no' or command_input=='NO':
            print("\n----you are now disconnected from{} ---".format(router_hostname))
            break
        else:
            router_output = net_connect.send_command(command_input)
            print("Here is the output of your device {}----\n".format(router_hostname))
            with open('c://router_output.txt', 'a') as f:
                f.write ("**************** Output for device {}************ \n". format(router_hostname))
                f.write(router_output)
                f.write ("\n############## End of Output for device {}################# \n". format(router_hostname))
                
            print (router_output)
            #with open ('c://router_output.txt','r') as rf:
             #   router_contents = rf.readlines()
                
            #print (router_content for router_content in router_contents)

    print("--------- End ---------")
end_time = datetime.now()
total_time = end_time - start_time
print(" Total time to execute the command is {}".format(total_time))
