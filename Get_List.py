# write a script to remove some content from file and construct data in tabular format seperate data on each line

input_data = """
Service1
Active
"""

lines = input_data.splitlines()

# Remove "Active" and keep only service names
service_names = [line for line in lines if line.strip() != "Active"]

# Print in column format (tabular look)
for name in service_names:
    print(name)