# Setup on racecar hardware
_as installed on 2021-01-19_

## Fresh intall
* Flash fresh OS with [nvidia Jetpack]
* Flash modified OS with [Orbitty Carrier Board drivers]
* Configure WLAN to connect to _racetrack_ automatically
* Configure eth0 for LIDAR: static 192.168.0.15/24 (LIDAR IP: 192.168.0.10)
* Install [ROS Melodic]
* `apt-get install ros-melodic-driver-common ros-melodic-laser-proc ros-melodic-urg-c screen mc nano cmatrix python3-pip`
* `pip3 install rosdep rospkg`
* Install udev-rules (`10-racecar.rules`)
* add user to `docker` and `dailout` group
### Very often needed:
* `sudo apt-get install ros-melodic-tf2-geometry-msgs ros-melodic-ackermann-msgs ros-melodic-joy ros-melodic-map-server`   

## Adjustments after cloning one car to another
* change hostname (`/etc/hostname`)
* change Interface/Mac on eth0 for LIDAR (GUI network manager)
* update IP in `~/.bashrc` (adjust the IP below for the specific car):

`
export ROS_MASTER_URI=http://192.168.1.103:11311
export ROS_HOSTNAME=192.168.1.103
export ROS_IP=192.168.1.103
`

## Notes for testing
* `jstest /dev/`


[nvidia Jetpack]: https://developer.nvidia.com/EMBEDDED/Jetpack
[Orbitty Carrier Board drivers]: https://connecttech.com/product/orbitty-carrier-for-nvidia-jetson-tx2-tx1/
[ROS Melodic]: http://wiki.ros.org/melodic/Installation/Ubuntu
