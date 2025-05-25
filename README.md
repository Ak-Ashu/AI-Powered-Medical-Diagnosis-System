# AI-Powered-Medical-Diagnosis-System
**The AI-Powered Medical Diagnosis System is an innovative project that leverages machine learning algorithms to predict and diagnose medical conditions like Parkinson's disease and lung cancer. Designed as a user-friendly web application, it allows individuals to input symptoms and demographic details, enabling the system to provide accurate and timely predictions. By integrating advanced AI models and an intuitive frontend interface, the project aims to empower healthcare providers and patients with accessible diagnostic tools, enhancing early detection and improving health outcomes.**
Certainly! Below is a detailed `README.md` file for your project. This will help users understand its purpose, installation steps, usage, and troubleshooting.

---

# Disease Prediction System

## Overview
The Disease Prediction System is a web-based application that uses machine learning to predict diseases based on user-provided symptoms. It is built using **Streamlit** for the frontend along with a trained machine learning model.

## Features
- **User-Friendly Interface:** Built with Streamlit for an interactive UI.
- **Machine Learning-Powered Predictions:** Uses trained models for disease classification.
- **Symptom-Based Diagnosis:** Takes user-input symptoms and provides potential diseases.
- **Real-Time Processing:** Fast results with optimized backend logic.

## Technologies Used
- **Frontend:** Streamlit
- **Machine Learning:** Scikit-learn, Pandas, NumPy
- **Deployment:** Local Server

## Installation
Follow these steps to set up the project:

1. **Clone the Repository:**
  https://github.com/Ak-Ashu/AI-Powered-Medical-Diagnosis-System

2. **Create a Virtual Environment:** _(Optional but recommended)_
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   streamlit run DiseasePage.py
   ```

## Usage
1. Open the application in your web browser.
2. Select symptoms from the provided options.
3. Submit the form to receive a predicted disease diagnosis.
4. Review additional information or recommended actions.

## Troubleshooting
### Incorrect Predictions
- Ensure the model is trained on high-quality, diverse data.
- Check feature scaling and symptom encoding.

### Streamlit Not Running
- Make sure you are using the correct command:  
  ```bash
  streamlit run DiseasePage.py
  ```
- Verify that Streamlit is installed:
  ```bash
  pip install streamlit
  ```

## Contributing
If you'd like to contribute to this project:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Make your changes and push them.
4. Submit a pull request.

## Contact
For any issues or improvements, contact:  
**Ashish Kumar**  
Email: `ashishak6969@gmail.com`
