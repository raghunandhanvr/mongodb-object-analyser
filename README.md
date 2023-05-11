# MongoDB Object ID Analyzer
This Python script analyzes a MongoDB Object ID and generates similar object IDs based on different variations. It provides insights into the components of the object ID and allows you to explore similar object IDs within the same second, with timestamp variation, and with machine and process ID variation.

## Prerequisites
To run the script, ensure that you have the following dependencies installed:

Python 3.x
bson library (pip install bson)
Usage
Clone the repository or download the script file (mongodb_object_id_analyzer.py) to your local machine.

Open a terminal or command prompt and navigate to the directory where the script is located.

## Execute the script by running the following command:

```python mongodb_object_id_analyzer.py```

The script will prompt you to enter a MongoDB Object ID. Provide a valid Object ID and press Enter.

### The script will analyze the Object ID and generate the following information:

**Timestamp:** The timestamp in both hexadecimal and decimal formats, representing the creation time of the Object ID.
**Machine Identifier:** The machine identifier component of the Object ID.
**Process ID:** The process ID component of the Object ID.
**Counter:** The counter component of the Object ID.
The script will then generate and display similar Object IDs based on the following variations:

<img width="472" alt="image" src="https://github.com/raghunandhanvr/mongodb-object-analyser/assets/65498602/06e3b2eb-d2b9-46e4-a05f-aed155f069e9">


Similar Object IDs within the same second
Object IDs with timestamp variation (adjustable time range)
Object IDs with machine identifier variation (randomly generated)
Object IDs with process ID variation (randomly generated)
Each set of similar Object IDs will be printed to the console.

Customization
Adjust the time_variation_seconds variable in the script to change the time range for timestamp variation.
Replace the placeholder values in the script (machine_identifier and process_id) with the actual values relevant to your MongoDB setup to generate machine and process ID variation.
