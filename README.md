# Multi-Terrain-Robot

### Overview
Many applications that include search and rescue, surveillance and security, require information about an unexplored terrain that may be potentially hazardous for humans. To explore such places we need mobile autonomous robots with multi-terrain traversing capability. Robotic platforms suitable for these applications can be wheeled, legged or one of the many other types in between. Wheeled robots are very efficient on smooth and continuous surfaces but suffer serious limitations in rough terrain and discontinuous paths. On the contrary, legged robots provides superior mobility in natural terrain. They adapt to surface irregularities by using discrete footholds and making contact with ground at the selected points.

### Technologies used
Raspberry Pi 3 model B is used to control and assemble the robot. The robot runs Python 2 scripts for walking. Simple and small servo motors are used to control the rotation of legs and lower limbs through specific angles. The Raspberry Pi has Raspian OS pre-installed on it. Therefore, all codes run on a Linux environment
An Android app connects to the server cloud created by the Raspberry Pi to control the bot wirelessly. The Android app is compatible with any android version greater than 4.0.

### Software
The multi-terrain bot uses Python scripts to walk on various surfaces. Each leg of the bot is programmed separately to give us more customisability over its walking style. The walking gait of the bot is inspired from spiders. Although a spider has more than 4 legs, it moves its legs distinctively unlike that of any four legged creature. For example, a dog or a cat walk forward with moving its alternate or side legs simultaneously. This walking gait may not be practical in a rocky surface as the bot make collapse or one of its leg can get caught in between rocks. That’s why chose a spider-like gait.

## Flowchart
<img src="images/block_diagram.png" width="400" alt="my image">

Each leg of the bot is made of two servos. In our cases the servo motors gave us the correct angles at a slightly different duty cycle. For example, it gave us the correct 90 degrees at a 7 duty cycle instead of 7.5. Therefore, we had to calibrate each motor using the formula, req_dutycycle=((req_angle/18)+2). 

### Walking GAIT: 
Initially, all the eight servos are set to 90 degrees. The knee servo of the Leg_1 servo rotates the lower limb to 45 degrees and the the thigh servo rotates the whole leg to 45 degrees. The knee servo then again rotates the lower limb back to 90 degrees, so that the bot is back on four legs. This process rotates for all four legs. Once all four thigh servos of the legs are at 45 degrees, the reset back to 90 degrees pushing the bot forward. This process goes on continuously until the loop terminates.
For turning the bot towards left, only the right side legs will operate in the similar fashion as discussed above. And the left legs will remain off. Exactly opposite will happen to turn the bot towards right. 

### Android Application
WiFiBot Application :
-Application acts as a client which uses IP address of the Raspberry Pi (the server) and  thus connects, and performs the operation of controlling the bot. It consists of 4 Buttons, 1 Edit-Text, 1 Text-Box. When a button is clicked a connection is made between the application and raspberry pi and the motion is carried. Connections are made using the socket programming class in java, which needs IP address and port number as the input.
