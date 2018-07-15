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

This project consists of three core components (as of now):

- Setting up the drone hardware. programming Raspberry Pi, abstracting motor controls.
- Setting up web portal ( for selecting the drop location, getting live status of the drone, manual override ), hooking up listener events on drone side.
- Implementing face recognition, training models, hooking up verification module to drone.

We will be using Python with Raspberry Pi for all drone related functionalities, openCV for face recognition and AWS (may change) for server hosting.

The workflow of the drone delivery will be:

Attach package to drone -> Select location on Drone Admistrative PanEL (DAPEL) -> Drone flies using the route calculated -> Once at the selected Location, verifies person face using inboard camera -> Unlocks Package.

# Todos

// TODO: Consider AWS Lambda

// TODO: Write it more formally
