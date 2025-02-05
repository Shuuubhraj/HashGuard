# HashGuard - File Integrity Checker 

HashGuard is a **file integrity checker** built with Python and Flask. It allows users to upload files and calculates multiple hash values (MD5, SHA-1, SHA-256) and CRC32 checksum to verify the integrity of the uploaded files. This tool can be used to detect if a file has been tampered with or corrupted.

## Features

- **File Upload**: Simple file upload interface for users to choose a file to check.
- **Multiple Hash Calculations**: Supports the calculation of MD5, SHA-1, SHA-256 hashes, and CRC32 checksum.
- **Copy Hash Values**: Users can easily copy the hash values to their clipboard for further use.
- **Error Handling**: Displays error messages if no file is selected or if an issue occurs.
- **Clear Results**: Users can clear the results and reset the form to start a new check.

### Screenshot 1

Here is a screenshot of the app's main interface:

[![Screenshot 1](https://i.imgur.com/L8tqgoZ.png)](https://i.imgur.com/L8tqgoZ.png)

### Screenshot 2

This screenshot demonstrates the results of a file integrity check:

[![Screenshot 2](https://i.imgur.com/PtW1FL1_d.webp?maxwidth=1520&fidelity=grand)](https://i.imgur.com/PtW1FL1_d.webp?maxwidth=1520&fidelity=grand)

## Technologies Used

- **Flask**: A lightweight web framework for Python used to build the backend.
- **Hashlib**: Python library for generating MD5, SHA-1, and SHA-256 hash values.
- **Zlib**: A Python module used to compute the CRC32 checksum.
- **HTML/CSS**: For the frontend layout and styling.
- **JavaScript**: For dynamic interactions such as displaying file names, handling errors, and copying hash values to the clipboard.

## Installation

### Prerequisites

Ensure that you have the following installed:
<p align="left">
  <img alt="Python Version" src="https://img.shields.io/badge/Python-3.x-blue.svg">
</p>
- Python 3.x

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Shuuubhraj/HashGuard.git

   
<p>
  <ul>
    <h2>Author</h2>
    <li>Name: Rajput Shubhraj Singh</li>
    <li>GitHub: <a href="https://github.com/shuuubhraj">https://github.com/shuuubhraj</a></li>
  </ul>
</p>
