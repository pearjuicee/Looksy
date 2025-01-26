# Looksy: A Virtual Dressing Room 👚👕

A web-based application that enables users to virtually try on various t-shirt designs in real time using a webcam. It tracks body movements to position the shirt correctly using computer vision, adjusting the size and fit dynamically. Users can switch between designs, see how the shirts look on them, take screenshots, and even save them to create their own virtual wardrobe.

## Features 🛠️

- **Real-time Pose Detection:** Utilizes Mediapipe for detecting and tracking body landmarks.
- **Dynamic Image Overlay:** Automatically resizes and positions t-shirt designs on users based on their body posture.
- **Interactive Buttons:** Enables users to switch between different t-shirt designs. Able to create own digital wardrobe and save them.
- **Web-based Interface:** Hosted using Flask for a seamless experience.

## Demo 🎥

Include screenshots or a short video showcasing the application in action:
![T-Shirt Overlay](pose_tracking_full_body_landmarks.png)

## Installation ⚙️

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository 
```bash
git clone https://github.com/pearjuicee/Looksy.git
```

### 2. Set Up the Environment (optional) 
#### For Mac/Linux 🍎: 
```bash
python3 -m venv env
source env/bin/activate
```
#### For Windows 🪟:
```bash
python -m venv env
env\Scripts\activate
```

### 3. Install Dependencies 
Run the following commands to install the required libraries:
```bash
pip install opencv-python
pip install mediapipe
pip install cvzone==1.5.6
pip install flask
pip install firebase-admin
pip install Pillow
pip install flask authlib python-dotenv requests

```

### 4. Run the Application 
1. **Backend:**
   Start the Flask server:
   ```bash
   python app.py
   ```

## Project Structure 📂

```
|-- hackathon/
|   |-- app.py                # Main Flask application
|   |-- camera.py             # Camera-based pose detection
|   |-- env/                  # Virtual environment (optional)
|   |-- Resources/            # Media assets (shirts, buttons, etc.)
|       |-- Shirts/
|           |-- 1.png         # Shirt design 1
|           |-- 2.png         # Shirt design 2
|           |-- ...
|       |-- button.png        # Interactive button image
|-- templates/
|   |-- index.html            # Webpage for hosting the app
```

## Usage 🎮

1. **Switching T-Shirts:**
   - Use the pink arrow buttons on the screen to change between different designs.
   - Real-time updates ensure proper scaling and placement based on body movements.

2. **Stopping the Application:**
   - Press `ctrl + c` to close the webcam stream.

## Dependencies 🧩

Make sure the following dependencies are installed:
- Python 3.8 or later
- OpenCV (`pip install opencv-python`)
- Mediapipe (`pip install mediapipe`)
- CVZone (`pip install cvzone==1.5.6`)
- Flask (`pip install flask`)


Enjoy exploring the world of virtual try-ons! 🥳
