import base64

def upload_image(image_path, output_file):
    # Read the image in binary mode
    with open(image_path, 'rb') as image_file:
        # Encode the image to base64
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    # Write the encoded image to a file
    with open(output_file, 'w') as file:
        file.write(encoded_string)

# Example usage:
# upload_image('path/to/your/image.jpg', 'encoded_image.txt')