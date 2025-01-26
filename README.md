# Looksy: A Virtual Dressing Room 👚👕

A web-based application that enables users to virtually try on various t-shirt designs in real time using a webcam. It tracks body movements to position the shirt correctly using computer vision, adjusting the size and fit dynamically. Users can switch between designs, see how the shirts look on them, take screenshots, and even save them to create their own virtual wardrobe.

## Features 🛠️

- **Real-time Pose Detection:** Utilizes Mediapipe for detecting and tracking body landmarks.
- **Dynamic Image Overlay:** Automatically resizes and positions t-shirt designs on users based on their body posture.
- **Interactive Buttons:** Enables users to switch between different t-shirt designs. Able to create own digital wardrobe and save them.
- **Web-based Interface:** Hosted using Flask for a seamless experience.

## Demo 🎥
<img src="https://github.com/user-attachments/assets/fab4de56-5030-486c-8501-95cab9e1b6c2" alt="loosky1" width="700"/>
<img src="https://github.com/user-attachments/assets/d99334b9-b4c7-42eb-a2f6-8008144adc5b" alt="outfit-screenshot (3)" width="705"/>

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
|-- Looksy/
|   |-- app.py                # Main Flask application
|   |-- camera.py             # Camera-based pose detection
|   |-- .env/                  # Virtual environment (optional)
|   |-- requirements.txt
|   |-- Static
|       |-- logo.png
|       |-- outfit.png
|       |-- shirt.png
|   |-- Resources/            # Media assets (shirts, buttons, etc.)
|       |-- Shirts/
|           |-- 1.png         # Shirt design 1
|           |-- 2.png         # Shirt design 2
|           |-- ...
|       |-- button.png       
|-- templates/
|   |-- camera.html           
|   |-- login.html
|   |-- upload.html
|   |-- wardrobe.html   
```

## Usage 🎮

1. **Switching T-Shirts:**
   - Use the pink arrow buttons on the screen to change between different designs.
   - Real-time updates ensure proper scaling and placement based on body movements.

2. **Stopping the Application:**
   - Press `ctrl + c` to close the webcam stream.


Enjoy exploring the world of virtual try-ons! 🥳
