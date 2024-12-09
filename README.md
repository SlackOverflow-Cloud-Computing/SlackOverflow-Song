# SlackOverflow-Song

## Description
This is the application part of the song microservice.

## Installation

### Local Test
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/SlackOverflow-Cloud-Computing/SlackOverflow-Song
   cd SlackOverflow-Song
   
2. **Install Dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt

3. **Run the Program:**
   ```bash
   uvicorn app.main:app --reload --port 8081


### AWS Deployment
