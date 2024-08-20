# Hajj Chatbot

## Overview

This project is a Gradio-based web application that interacts with the OpenAI GPT-3.5 Turbo model to provide real-time assistance for pilgrims during Hajj and Umrah. The application is designed to answer questions in Arabic, specifically related to Hajj, Umrah, and the holy cities of Makkah and Madinah. The model responds in Arabic and focuses on providing guidance relevant to the religious context.

## Features

- **Real-time AI Interaction**: The application streams responses from the OpenAI GPT-3.5 Turbo model as the user inputs their question.
- **Arabic Language Support**: The AI is specifically programmed to understand and respond in Arabic.
- **Focus on Hajj and Umrah**: The AI provides answers that are relevant to the religious practices of Hajj and Umrah, and the holy cities of Makkah and Madinah.
- **User-Friendly Interface**: The application features a simple and intuitive interface built using Gradio, allowing users to easily input their questions and view responses.

## Installation

### Prerequisites

- Python 3.7+
- Gradio
- OpenAI Python client library

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install the required packages**:
   ```bash
   pip install gradio openai
   ```

3. **Set your OpenAI API key**:
   Replace `"YOUR_API_KEY_HERE"` in the code with your actual OpenAI API key or set it as an environment variable:

   ```python
   os.environ['OPENAI_API_KEY'] = "YOUR_API_KEY_HERE"
   ```

## Usage

1. **Run the application**:
   ```bash
   python app.py
   ```

2. **Interact with the AI**:
   - The web interface will open in your default browser.
   - Enter your question in Arabic in the provided textbox and click on "إرسال".
   - The AI's response will be displayed in the response textbox.

## Project Structure

- `app.py`: The main script that launches the Gradio web application.
- `README.md`: This file, providing an overview and instructions for the project.

## Customization

- **Model Customization**: You can modify the prompt in the `get_ai_response` function to change the behavior or focus of the AI.
- **Interface Customization**: The Gradio interface can be customized by modifying the layout or adding additional elements such as examples.


## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
