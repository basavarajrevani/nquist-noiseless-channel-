# Nyquist Calculator with Interactive GUI

## Overview
This project implements a Nyquist Theorem Calculator with a graphical user interface (GUI) to calculate and visualize the maximum data rate in a noiseless channel. The calculator helps users understand the relationship between channel bandwidth, signal levels, and maximum achievable data rate.

## Features
- Interactive GUI with input validation
- Real-time calculations using Nyquist Theorem
- Support for multiple bandwidth units (Hz, KHz, MHz, GHz)
- Visual analysis through graphs
- Detailed text analysis of relationships
- Error handling and user-friendly messages

main.py: Entry point of the application
gui.py: GUI implementation using tkinter
nyquist_calculator.py: Core calculation logic
input_handler.py: Input validation and processing
utils.py: Utility functions for validation

## Installation
1. Ensure Python 3.x is installed on your system
2. Clone the repository:
```bash
git clone <repository-url>
cd noiseless

Run the application: python main.py

## User Input Parameters:
Channel Bandwidth: Enter the bandwidth value
Unit Selection: Choose from Hz, KHz, MHz, or GHz
Signal Levels: Enter the number of distinct signal levels
Available Actions:
Click "Calculate" for basic calculation
Click "Analyze & Plot" for detailed analysis with graphs
Output and Visualization

## Basic Calculation
Shows:
Input bandwidth with selected unit
Maximum data rate in appropriate units (bps, Kbps, Mbps, Gbps)

## Analysis Tabs
Text Analysis Tab
Displays:
Bandwidth variation analysis (50% to 150% of input)
Signal levels analysis
Data rates for each variation
Bandwidth Graph Tab
Shows:

X-axis: Bandwidth in selected unit
Y-axis: Data Rate (bps)
Blue line graph showing the linear relationship
Points marked for easy reference
Levels Graph Tab
Shows:

X-axis: Number of Signal Levels
Y-axis: Data Rate (bps)
Blue line graph showing the logarithmic relationship
Points marked for easy reference

## Technical Details
Nyquist Theorem Implementation
The maximum data rate is calculated using the formula:   
Data Rate = 2 * Bandwidth * log2(Signal Levels)

## Graph Details
Bandwidth Graph:
Shows how data rate increases linearly with bandwidth
Useful for capacity planning
Helps visualize the direct relationship
Levels Graph:
Shows how data rate increases logarithmically with signal levels
Helps understand diminishing returns
Useful for optimizing signal level selection


##Channel Bandwidth:
This is the frequency range available for data transmission in the communication channel
Input Requirements:
Must be a positive number
Can be entered in different units: Hz, KHz, MHz, or GHz
No upper limit is enforced, but practical values depend on the physical channel
The GUI allows analysis of bandwidth variations from 50% to 150% of the input value

##Signal Levels:
This is the number of distinct signal levels available in the communication channel
Input Requirements:
Must be a positive integer
Must be greater than 1 (as verified in nyquist_calculator.py)
No upper limit is enforced, but practical values depend on the physical channel
The GUI allows analysis of signal level variations from 1 to 1000

##Importance and What It Tells: 
The combination of bandwidth and signal levels determines the maximum data rate in a noiseless channel according to Nyquist's Theorem:
The maximum data rate is calculated using the formula: Data Rate = 2 * Bandwidth * log2(Signal Levels)
Higher bandwidth allows for more rapid signal changes per second
More signal levels allow for more bits to be encoded in each signal change

This calculator helps users understand:
How increasing bandwidth linearly increases maximum data rate
How increasing signal levels logarithmically increases maximum data rate
The trade-offs between bandwidth and signal levels in digital communication
The theoretical maximum data rate possible in a noiseless channel
