# Image Detector 🖼️🔍

A powerful and simple web application built with **Django** and **Keras** that uses deep learning to identify and classify objects in images.

## 🌟 Overview

The **Image Detector** project allows users to upload images and receive instant feedback on what objects are present within them. It utilizes the **ResNet50** convolutional neural network, pre-trained on the vast **ImageNet** dataset, to provide high-accuracy classification across 1,000 different object categories.

## ✨ Features

- **Intuitive Web Interface**: Simple drag-and-drop or file selection for image uploads.
- **Instant Classification**: Rapid analysis using deep learning models.
- **Top-N Predictions**: Displays the top 3 most likely classifications with their confidence scores.
- **Responsive Design**: Works across different screen sizes.

## 🛠️ Technology Stack

- **Backend**: [Django 6.0+](https://www.djangoproject.com/)
- **Machine Learning**: [Keras](https://keras.io/) & [TensorFlow](https://www.tensorflow.org/)
- **Model**: ResNet50 (Pre-trained)
- **Image Processing**: [Pillow (PIL)](https://python-pillow.org/)
- **Numerical Processing**: [NumPy](https://numpy.org/)

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/thajucp123/image-identifier.git
   cd ImageDetector
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000/`

## 📂 Project Structure

```text
ImageDetector/
├── ImageDetector/       # Project configuration (settings, URLs)
├── imgUpload/          # Main app logic (views, forms, image processing)
├── templates/          # HTML templates (home.html, results.html)
├── manage.py           # Django administrative utility
└── db.sqlite3          # Local database (automatically created)
```

## 📋 Usage

1. Navigate to the **Home Page**.
2. Click **Choose File** and select an image from your device.
3. Click the **Upload** button.
4. View the **Results Page** to see the identified objects and confidence percentages.

## 📸 Example Results

<img src="fig.jpg" alt="Fig image" width="300" height="200">

| Object | Confidence |
| :--- | :--- |
| Fig | 99.99% |
| crate | 0.00% |
| grocery_store | 0.00% |

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---
*Developed as part of a Machine Learning and AI study.*
