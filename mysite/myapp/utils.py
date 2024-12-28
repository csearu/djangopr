from PIL import Image, ImageFilter

def format_image(image_path, formatted_path):
    with Image.open(image_path) as img:
        # Resize the image to a fixed size (e.g., 300x300)
        img = img.resize((300, 300), Image.Resampling.LANCZOS)
        # Apply a filter (optional, e.g., BLUR or SHARPEN)
        img = img.filter(ImageFilter.SHARPEN)
        # Save the formatted image
        img.save(formatted_path)
