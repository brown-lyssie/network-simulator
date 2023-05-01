# Network Simulator

## Purpose

**What it is**: A simple simulator for a network of hosts and links that each have some probability of failure.

**Why we created it**: Final project for Computer Engineering 400 (Networks) at UNR.

## Overview
Python version 3.8.10 (ish)

Convention: return 0 if successful, return -1 if error (except main)

This is a simulator.


## Plans

```
Host Class
Attributes:
- std::queue<Packet> Send (Outgoing) Buffer (FIFO)
- std::queue<Packet> Receive (Incoming) Buffer (FIFO)
- 
```

```
Packet Class
Attributes:
- std::string Contents in roughly IPV6 Format
```

```
Network Class
Attributes:
- Graph<Subgraph>