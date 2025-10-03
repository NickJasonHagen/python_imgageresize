import argparse
from PIL import Image
import os

def resize_image(image_path, output_path, width, height):
    try:
        with Image.open(image_path) as img:
            img = img.resize((width, height))
            img.save(output_path)
    except Exception as e:
        print(f"Error resizing image: {e}")

def main():
    parser = argparse.ArgumentParser(description='Resize an image file')
    parser.add_argument('--i', help='Path to the image file')
    parser.add_argument('--o', help='Path to the image file')
    parser.add_argument('--w', type=int, default=800, help='New width of the resized image')
    parser.add_argument('--h', type=int, default=600, help='New height of the resized image')

    args = parser.parse_args()

    if not os.path.exists(args.i):
        print(f"Error: Image file '{args.image_path}' does not exist")
        return

    output_path = f"{os.path.splitext(args.i)[0]}_{args.w}x{args.h}{os.path.splitext(args.o)[1]}"
    resize_image(args.i, args.o, args.w, args.h)
    print(f"Resized image saved to '{args.o}'")

#if __name__ == "__main__":
main()
