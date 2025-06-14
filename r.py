#!/usr/bin/env python3
import os
import sys
import requests

API_ENDPOINT = "https://api.remove.bg/v1.0/removebg"
API_KEY = os.getenv("REMOVE_BG_API_KEY")  # Set your API key in environment variable

def remove_background(input_path, output_path):
    if not API_KEY:
        print("Error: REMOVE_BG_API_KEY environment variable not set.")
        sys.exit(1)

    if not os.path.isfile(input_path):
        print(f"Error: Input file '{input_path}' does not exist.")
        sys.exit(1)

    with open(input_path, "rb") as image_file:
        response = requests.post(
            API_ENDPOINT,
            headers={"X-Api-Key": API_KEY},
            files={"image_file": image_file},
            data={"size": "auto"}
        )

    if response.status_code == requests.codes.ok:
        with open(output_path, "wb") as out_file:
            out_file.write(response.content)
        print(f"Background removed successfully. Saved to '{output_path}'.")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: python remove_bg_cli.py <input_image> <output_image>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    remove_background(input_path, output_path)

if __name__ == "__main__":
    main()
