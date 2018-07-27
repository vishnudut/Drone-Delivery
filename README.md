# Drone based smart delivery system using Raspberry Pi

**Course**: CSE 3009 Internet Of Things

**Faculty:** Prof. Vaidehi Vijayakumar

## Team Members

- [Sridhar Pandian](https://github.com/SridharPandian/). // 16BEC1277
- [Vishnu Dut](https://github.com/vishnudut) // 16BCE1103
- [Sriram Ravichandran](https://github.com/digi0ps) // 16BCE1026

## Stack

- Raspberry Pi 3
- DC Motors
- Camera
- Sensors
- A system with Python
- openCV

## Abstract

In this project, we are trying to improvise the delivery of purchased online goods by implementing an autonomous drone based delivery service. At this level, we are aiming for the delivery of lightweight packages with automated route mapping and face verification based delivery.

This project consists of three core components:

- Setting up the drone hardware:

  Involves programming the Raspberry Pi to make the drone fly and abstracting motor controls to access it manually.

- Setting up web portal:
  Website (using React for frontend and AWS ElasticBeanstalk) for selecting the drop location, seeing live status of the drone, manual override ), hooking up listener events on drone side.

- Face verification:
  Implementing Face Verification in openCV, training models, adding this module to the Raspberry Pi as to verify the package receiver.

We will be using Python with Raspberry Pi for all drone related functionalities, openCV for face recognition and AWS for server hosting.

The workflow of the drone delivery will be:

Attach package to drone -> Select location on Drone Admistrative Panel -> Drone flies using the route calculated -> Once at the selected Location, verifies person face using inboard camera -> Unlocks Package.

# TODOs

- [ ] Make drone fly
- [ ] Make drone fly to a selected point
- [ ] Implement Web Interface
- [ ] Face verify
