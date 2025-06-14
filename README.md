
# RemoveBackground

A simple and efficient tool to remove image backgrounds using the remove.bg API with Python CLI.

## Overview

RemoveBackground is a Python command-line utility that leverages the [remove.bg](https://www.remove.bg/) API to automatically remove the background from images. It is designed for quick and easy background removal in bulk or single images directly from your terminal.

## Features

- Remove backgrounds from images using the remove.bg API
- Command-line interface for easy integration into scripts and workflows
- Supports common image formats (JPEG, PNG, etc.)
- Saves output images with transparent backgrounds (PNG format)
- Error handling for invalid inputs and API issues

## Installation

1. Clone the repository:

```
git clone https://github.com/DexterZero/RemoveBackground.git
cd RemoveBackground
```

2. Install required dependencies:

```
pip install -r requirements.txt
```

## Setup

1. Obtain your API key from [remove.bg](https://www.remove.bg/api).
2. Set your API key as an environment variable:

```
export REMOVE_BG_API_KEY="your_api_key_here"
```

## Usage

Run the script from the command line:

```
python remove_background.py input_image.jpg output_image.png
```

- `input_image.jpg`: Path to the input image file.
- `output_image.png`: Path where the output image with background removed will be saved.

## Example

```
python remove_background.py photo.jpg photo_no_bg.png
```

This command will process `photo.jpg` and save the background-removed image as `photo_no_bg.png`.

## Troubleshooting

- Ensure your API key is correctly set in the environment variable `REMOVE_BG_API_KEY`.
- Verify that the input file path is correct.
- Check your internet connection as the script requires API access.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.

