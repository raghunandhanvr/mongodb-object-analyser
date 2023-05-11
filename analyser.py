from datetime import datetime, timedelta
from random import randint
from bson.objectid import ObjectId

def analyze_object_id(object_id):
    timestamp = int(str(object_id)[:8], 16)
    timestamp_dt = datetime.fromtimestamp(timestamp)
    machine_identifier = int(str(object_id)[8:14], 16)
    process_id = int(str(object_id)[14:18], 16)
    counter = int(str(object_id)[18:], 16)

    print(f"Object ID: {object_id}")
    print(f"Timestamp: {timestamp} in decimal = {timestamp_dt}")
    print(f"Machine Identifier: {machine_identifier}")
    print(f"Process ID: {process_id}")
    print(f"Counter: {counter}")

    # Generate similar object IDs within the same second
    similar_object_ids = []
    for i in range(counter-5, counter+6):
        similar_object_id = str(object_id)[:18] + format(i, 'x').zfill(6)
        similar_object_ids.append(similar_object_id)

    print("\nSimilar Object IDs:")
    for similar_id in similar_object_ids:
        print(similar_id)

    # Generate similar object IDs with timestamp variation
    time_variation_object_ids = []
    time_variation_seconds = 5  # Adjust as desired
    for sec in range(-time_variation_seconds, time_variation_seconds+1):
        new_timestamp_dt = timestamp_dt + timedelta(seconds=sec)
        new_timestamp = int(new_timestamp_dt.timestamp())
        time_variation_object_id = str(new_timestamp) + str(object_id)[8:]
        time_variation_object_ids.append(time_variation_object_id)

    print("\nObject IDs with Timestamp Variation:")
    for time_variation_id in time_variation_object_ids:
        print(time_variation_id)

    # Generate similar object IDs with machine and process ID variation
    # Replace the machine_identifier and process_id with actual values
    machine_variation_object_ids = []
    process_variation_object_ids = []
    for _ in range(10):
        machine_variation_id = str(format(randint(0, 0xFFFFFF), 'x')).zfill(6) + str(object_id)[6:]
        machine_variation_object_ids.append(machine_variation_id)

        process_variation_id = str(object_id)[:14] + format(randint(0, 0xFF), 'x').zfill(4) + str(object_id)[18:]
        process_variation_object_ids.append(process_variation_id)

    print("\nObject IDs with Machine Identifier Variation:")
    for machine_variation_id in machine_variation_object_ids:
        print(machine_variation_id)

    print("\nObject IDs with Process ID Variation:")
    for process_variation_id in process_variation_object_ids:
        print(process_variation_id)

# Usage example
object_id = "5f2459ac9fa6dc2500314019"
analyze_object_id(object_id)
