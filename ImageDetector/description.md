# Image Detector Project

## Overview
The **Image Detector** is a Django-based web application designed to identify and classify objects within uploaded images using deep learning. It leverages the pre-trained **ResNet50** model, which has been trained on the extensive **ImageNet** dataset.

## Core Features
- **Image Upload**: Users can select and upload images directly through a simple web interface.
- **Object Classification**: The system processes the uploaded image and predicts the most likely objects present.
- **Detailed Results**: Displays the top 3 predictions along with their respective confidence percentages.

## Technology Stack
- **Web Framework**: [Django](https://www.djangoproject.com/) (Python)
- **Deep Learning Library**: [Keras](https://keras.io/) / [TensorFlow](https://www.tensorflow.org/)
- **Model**: [ResNet50](https://keras.io/api/applications/resnet/#resnet50-function) (Pre-trained on ImageNet)
- **Image Processing**: [Pillow (PIL)](https://python-pillow.org/)
- **Numerical Computing**: [NumPy](https://numpy.org/)

## Project Structure
- `ImageDetector/`: Core project configuration (settings, URLs).
- `imgUpload/`: Main application logic, including forms and views for image processing.
- `templates/`: HTML templates for the user interface (`home.html`, `results.html`).
- `manage.py`: Django's command-line utility for administrative tasks.

## Workflow
1. **Home Page**: The user visits the homepage and uploads an image file.
2. **Processing**: The `imageprocess` view receives the file and uses the ResNet50 model to analyze it.
3. **Prediction**: The model generates a list of potential objects and their probability scores.
4. **Results**: The top three results are formatted and displayed on the results page for the user.
