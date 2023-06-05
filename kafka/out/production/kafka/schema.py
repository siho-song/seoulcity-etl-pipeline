import fastavro

# Avro file path
avro_file_path = "test.avro"

# Open the Avro file in read mode
with open(avro_file_path, "rb") as avro_file:
    # Read the Avro file
    reader = fastavro.reader(avro_file)
    
    # Iterate over the records in the Avro file
    for record in reader:
        # Process each record
        print(record)
