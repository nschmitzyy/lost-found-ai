from PIL import Image

def validate_image(uploaded_file):
    if uploaded_file.size > 5 * 1024 * 1024:
        return False, "File too large (max 5MB)."

    if uploaded_file.type not in ["image/jpeg", "image/png"]:
        return False, "Only JPG and PNG files allowed."

    return True, None

def open_image(uploaded_file):
    return Image.open(uploaded_file)
