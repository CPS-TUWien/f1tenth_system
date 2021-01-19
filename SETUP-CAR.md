# Setup on racecar hardware
_as installed on 2021-01-19_

## Fresh intall
* Flash fresh OS with [nvidia Jetpack]
* Flash modified OS with [Orbitty Carrier Board drivers]
* Configure WLAN to connect to _racetrack_ automatically
* Configure eth0 for LIDAR: static 192.168.0.15/24 (LIDAR IP: 192.168.0.10)
* Install [ROS Melodic]
* `apt-get install ros-melodic-driver-common ros-melodic-laser-proc ros-melodic-urg-c screen mc nano cmatrix`
* Install udev-rules (`10-racecar.rules`)
* add user to `docker` and `dailout` group

## Adjustments after cloning one car to another
* change hostname (`/etc/hostname`)
* change Interface/Mac on eth0 for LIDAR (GUI network manager)
* update IP in `~/.bashrc`

## Notes for testing
* `jstest /dev/`


[nvidia Jetpack]: https://developer.nvidia.com/EMBEDDED/Jetpack
[Orbitty Carrier Board drivers]: https://connecttech.com/product/orbitty-carrier-for-nvidia-jetson-tx2-tx1/
[ROS Melodic]: http://wiki.ros.org/melodic/Installation/Ubuntu