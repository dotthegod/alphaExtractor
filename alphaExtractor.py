import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image
import os

def convert_to_rgba(img):
    """Convert the image to RGBA mode if it's not already in that mode."""
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    return img

def extract_alpha_channel(image_path):
    """Extract the alpha channel from the image and save it as a separate PNG file."""
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Convert to RGBA format
        img = convert_to_rgba(img)
        
        # Split the image into RGBA channels
        r, g, b, a = img.split()
        alpha_img = Image.merge('L', [a])
        
        # Create the path for the new alpha channel image
        base_name, ext = os.path.splitext(image_path)
        alpha_image_path = f"{base_name}_alpha.png"
        
        # Save the alpha channel image
        alpha_img.save(alpha_image_path)
        print(f"Alpha channel saved as '{alpha_image_path}'.")
        status_label.config(text=f"Alpha channel saved as '{alpha_image_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
        status_label.config(text=f"An error occurred: {e}")

def drop(event):
    """Handle the drop event to process the file."""
    file_path = event.data.strip('{}')
    extract_alpha_channel(file_path)

# Create the Tkinter GUI
root = TkinterDnD.Tk()
root.title("PNG Alpha Channel Extractor")
root.geometry("400x200")

status_label = tk.Label(root, text="Drag and drop a PNG file here", padx=10, pady=10)
status_label.pack(expand=True, fill=tk.BOTH)

# Register the drop target and bind the drop event
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

# Start the main loop
root.mainloop()
