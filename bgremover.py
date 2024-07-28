import os
from rembg import remove
from PIL import Image

# Define input and output paths
input_path = r'C:\Users\prajw\OneDrive\Pictures\Capture.png'
output_path = r'C:\Users\prajw\OneDrive\Desktop\Python Programming\Project\bg remover\Capture.png'

# Check if the input file exists
if not os.path.exists(input_path):
    print(f"Input file does not exist: {input_path}")
else:
    # Open the input image
    inp = Image.open(input_path)

    # Remove the background
    output = remove(inp)

    # Save the result
    output.save(output_path)
    print(f"Output saved to: {output_path}")
