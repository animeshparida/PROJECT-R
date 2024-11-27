Diabetic Retinopathy Detection
Overview
Diabetic retinopathy is a severe complication of diabetes that affects the retina and can lead to vision loss if untreated. This project aims to provide a solution for early detection of diabetic retinopathy using machine learning and deep learning techniques.

Features
Preprocessing retinal fundus images.
Automated classification of retinal images into different severity levels of diabetic retinopathy.
Visual explanation of model predictions using techniques like Grad-CAM.

![image](https://github.com/user-attachments/assets/e32fd46c-4676-4c7d-a039-dbadd20aa9a2)
![image](https://github.com/user-attachments/assets/086e458c-a652-4faa-867a-e084cdfb3496)
![image](https://github.com/user-attachments/assets/3c526c29-7590-4ecc-8a6a-b38da031534b)
![image](https://github.com/user-attachments/assets/aa25b367-a8c0-4d02-9022-4c519bb8c629)





Integration of a simple user interface for non-technical users.
Table of Contents
Installation
Usage
Dataset
Model Architecture
Results
Contributing
License
Installation
To set up the project locally:

Requirements
Python 3.8+
pip
Virtual environment (optional but recommended)
Steps
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/diabetic-retinopathy.git
cd diabetic-retinopathy
Install dependencies:

bash
Copy code
pip install -r requirements.txt
(Optional) Set up a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Usage
Training the Model
Place the dataset in the data/ folder.
Run the training script:
bash
Copy code
python train.py
Training logs and model checkpoints will be saved in the logs/ directory.
Evaluating the Model
Run the evaluation script:

bash
Copy code
python evaluate.py --model_path <path_to_model>
Deploying the Model
You can deploy the model locally using Flask:

bash
Copy code
python app.py
The web application will be available at http://127.0.0.1:5000.

Dataset
Sources
Kaggle Diabetic Retinopathy Dataset :https://www.kaggle.com/code/sidhantrajj/diabetic-retinopathy-detection










