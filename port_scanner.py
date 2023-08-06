'''
  .-')                ('-.         .-') _      .-') _             .-') _                     _ (`-.              _  .-')   .-') _     .-')    
 ( OO ).             ( OO ).-.    ( OO ) )    ( OO ) )           ( OO ) )                   ( (OO  )            ( \( -O ) (  OO) )   ( OO ).  
(_)---\_)   .-----.  / . --. /,--./ ,--,' ,--./ ,--,' ,-.-') ,--./ ,--,'  ,----.           _.`     \ .-'),-----. ,------. /     '._ (_)---\_) 
/    _ |   '  .--./  | \-.  \ |   \ |  |\ |   \ |  |\ |  |OO)|   \ |  |\ '  .-./-')       (__...--''( OO'  .-.  '|   /`. '|'--...__)/    _ |  
\  :` `.   |  |('-..-'-'  |  ||    \|  | )|    \|  | )|  |  \|    \|  | )|  |_( O- )       |  /  | |/   |  | |  ||  /  | |'--.  .--'\  :` `.  
 '..`''.) /_) |OO  )\| |_.'  ||  .     |/ |  .     |/ |  |(_/|  .     |/ |  | .--, \       |  |_.' |\_) |  |\|  ||  |_.' |   |  |    '..`''.) 
.-._)   \ ||  |`-'|  |  .-.  ||  |\    |  |  |\    | ,|  |_.'|  |\    | (|  | '. (_/       |  .___.'  \ |  | |  ||  .  '.'   |  |   .-._)   \ 
\       /(_'  '--'\  |  | |  ||  | \   |  |  | \   |(_|  |   |  | \   |  |  '--'  |        |  |        `'  '-'  '|  |\  \    |  |   \       / 
 `-----'    `-----'  `--' `--'`--'  `--'  `--'  `--'  `--'   `--'  `--'   `------'         `--'          `-----' `--' '--'   `--'    `-----'  
'''
## The Libraries We need
import socket #lIBRARY CALLED SOCKET WE CALL THE LIBRARY TO USE ITS FUNCTIONS


#### The variables we need
target = "54.186.177.106" #The Ip of the target
ports = [19,20,21,22,23,443,80] #iNDICATES THE PORTS to Scan (we can mention a range in the for loop tho)


## Scanning the port
for p in ports: #The loop to test every port in the array list ...
 s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Specify address Family(IPv4) and connection-oriented TCP protocol.
 s.settimeout(1) #wait 1s if it doesnt respond
 r=s.connect_ex((target,p)) # with the target and the port you need to know if the port is open, if it is open the r will get the number 0


## Cheking if the port is open to mention it
 if r==0: #the condition is achieved
  service=socket.getservbyport(p) #get the name of the port ex: 443 is for https
  print("--[*{}* is open --> {}]".format(p,service)) #the output in the indicate format 


## Close the connection 
s.close() #close the connection when we end the process