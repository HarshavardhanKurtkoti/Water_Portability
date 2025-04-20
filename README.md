# Water Potability Prediction with MLOps

Welcome to the **Water Potability Prediction** project! This repository demonstrates an **end-to-end Machine Learning** workflow for predicting water potability, from data collection and processing to model training, evaluation, and deployment. The project incorporates **MLOps best practices**, including **data versioning**, **containerization**, and **cloud deployment**.

A machine learning project that predicts water potability using a FastAPI backend and a modern React + Vite frontend. The project features data processing, model training, and deployment workflows following MLOps best practices, with a user-friendly UI for real-time predictions.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [Technologies Used](#technologies-used)
4. [Project Setup](#project-setup)
5. [Data Version Control (DVC)](#data-version-control-dvc)
6. [Model Deployment](#model-deployment)
7. [Containerization with Docker](#containerization-with-docker)
8. [Environment Setup](#environment-setup)
9. [Contributing](#contributing)
10. [License](#license)

## Project Overview

This project aims to predict whether water is potable (safe for drinking) using a Machine Learning model. The workflow includes:

- **Data Collection & Preprocessing**: Handling raw water quality data and preparing it for modeling.
- **Model Training & Evaluation**: Building and evaluating a classification model.
- **Model Deployment**: Serving predictions via a FastAPI backend, containerized with Docker.
- **MLOps Practices**: Data versioning with DVC, reproducible pipelines, and easy deployment.

## Architecture

The project follows a modular and scalable architecture:

1. **Data Collection & Preprocessing**: Scripts for ingesting and cleaning water quality data.
2. **Feature Engineering & Model Training**: Training a model to classify water as potable or not.
3. **Model Evaluation**: Assessing model performance and saving metrics.
4. **Model Serving**: Exposing the model via a FastAPI REST API.
5. **Frontend**: (Optional) A React+Vite frontend can consume the API for real-time predictions.
6. **Containerization**: Docker is used for consistent deployment.

## Technologies Used

- **Python**: Core language for data processing and modeling.
- **FastAPI**: For serving the model as a REST API.
- **Pandas, scikit-learn**: Data manipulation and machine learning.
- **DVC**: Data and model version control.
- **Docker**: Containerization for deployment.
- **Render**: Cloud deployment of the backend API.
- **React + Vite**: (Optional) Frontend for user interaction.

## Project Setup

### Prerequisites

- **Python 3.8+**
- **Docker** (for containerization)
- **DVC** (for data versioning)
- **Git**

### Clone the Repository

```bash
git clone <your-repo-url>
cd Water_Portability
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Data Preparation

- Raw data is stored in `data/raw/`.
- Processed data is stored in `data/processed/`.
- Use the scripts in `src/` for data processing and model training.

### Model Training

```bash
python src/model_building.py
```

### Model Evaluation

```bash
python src/model_eval.py
```

## Data Version Control (DVC)

We use **DVC** to version datasets and model artifacts. This ensures reproducibility and easy collaboration.

- Track data and models:

```bash
dvc add data/raw/train.csv
dvc add model/model.pkl
```

- Push data to remote storage (configure your DVC remote first):

```bash
dvc push
```

- View experiment history:

```bash
dvc exp show
```

## Model Deployment

The trained model is served using FastAPI. The main API code is in `src/main.py`.

- **Endpoints:**
  - `GET /` — Welcome message
  - `POST /predict` — Predicts water potability from input features

### Running the API Locally

```bash
uvicorn src.main:app --reload
```

## Containerization with Docker

The project is fully containerized for easy deployment.

### Build Docker Image

```bash
docker build -t water-potability-api -f dockerfile .
```

### Run Docker Container

```bash
docker run -p 8000:8000 water-potability-api
```

## Environment Setup

- All Python dependencies are listed in `requirements.txt`.
- Data and model paths are managed in the code for easy configuration.

## File Structure

```
Water_Portability/
├── data/
│   ├── raw/
│   └── processed/
├── model/
│   ├── model.pkl
│   └── metrics.json
├── src/
│   ├── data_collection.py
│   ├── data_model.py
│   ├── data_prep.py
│   ├── main.py
│   ├── model_building.py
│   ├── model_eval.py
│   └── static/
├── requirements.txt
├── dockerfile
├── docker-compose.yml
├── dvc.yaml
├── dvc.lock
└── test.py
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
