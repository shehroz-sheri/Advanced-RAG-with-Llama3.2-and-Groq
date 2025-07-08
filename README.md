# ChatGroq Demo with Streamlit

## Overview

The **ChatGroq Demo** is an AI-powered application leveraging open-source models exclusively to provide efficient and accurate question-answering functionality. This project is unique in its approach as it utilizes the **Groq Language Processing Unit (LPU)** for fast AI inference, coupled with a Streamlit frontend, ensuring accessibility and affordability.

## Key Features
- **Open-source models only**: This project uses completely free and open-source models, ensuring no additional costs for proprietary APIs like OpenAI.
- **Streamlit frontend**: The application uses Streamlit for a simple, efficient, and interactive user interface.
- **Powered by Groq**: Fast AI inference is achieved using Groq technology, delivering exceptional performance and energy efficiency.
- **Document-based Q&A**: The app enables users to load documents and perform context-based question answering using LangChain components.


---

## What is Streamlit?
Streamlit is an open-source app framework used to build interactive web applications with Python. It's particularly useful for creating data applications and machine learning demos, allowing developers to quickly prototype and deploy apps.

For more details, visit [Streamlit's website](https://streamlit.io/) _(opens in a new tab)_.

---

## What is Ollama?
Ollama provides access to large language models (LLMs) like Llama3.2. It allows you to run models locally, offering an easy-to-use platform for interacting with AI-powered models.

For more details, visit [Ollama's website](https://ollama.com/) _(opens in a new tab)_.

---
## What is Groq?
Groq represents a paradigm shift in AI inference, enabling instant intelligence for developers and enterprises. Its highlights include:

- **The Groq Language Processing Unit (LPU)**: A hardware solution designed specifically for AI inference and language tasks, offering unparalleled speed, affordability, and scalability.
- **Cloud and on-premises availability**: Users can access Groq’s capabilities via GroqCloud™ or deploy LPUs in on-premise AI compute centers.
- **Energy efficiency**: Groq’s design focuses on delivering maximum performance while minimizing energy consumption.

Groq is committed to democratizing AI by making its technology accessible to everyone.

For more details, visit [Groq's website](https://groq.com/) _(opens in a new tab)_.



## Usage of Groq in This Project
In this project, Groq’s **LPU** is leveraged to power the inference engine for the ChatGroq API. This ensures:

1. **Fast AI inference**: Rapid and responsive user interactions.
2. **Scalability**: Support for complex and high-volume queries.
3. **Energy efficiency**: Reduced resource consumption compared to traditional inference methods.

---

## Project Structure
```plaintext
ChatGroq-Demo-with-Streamlit/
├── groq/
│   ├── app.py            #  application
│  
├── .env                  # Environment variables for API key
├── requirements.txt      # Dependencies list
├── README.md             # Project documentation
└── venv/                 # Virtual environment (optional, created manually)
```

## Project Components

### Dependencies
The following Python libraries are used:
- **Streamlit**: For creating the user interface.
- **LangChain**: To handle document loading, embeddings, and retrieval.
- **FAISS**: A vector store for document similarity search.
- **OllamaEmbeddings**: For generating embeddings from documents.

### Workflow
1. **Document Loading**: Documents are fetched using the `WebBaseLoader` from LangChain.
2. **Text Splitting**: Documents are split into manageable chunks using `RecursiveCharacterTextSplitter`.
3. **Vector Store**: FAISS is used to store vectorized document chunks for efficient retrieval.
4. **Prompt Handling**: A `ChatPromptTemplate` is designed to provide the context and structure for answering questions.
5. **Retrieval and Response**: A retrieval chain combines document retrieval with language model inference to provide accurate and context-specific answers.

## How to Run the Project

### Prerequisites
- Python 3.8 or later.
- An API key for Groq (“GROQ_API_KEY”).
- Ollama (for Llama3.2 model)

### Installing Ollama
1. Visit [Ollama's website](https://ollama.com/) to download and install Ollama for your operating system.
2. After installation, download the Llama3.2 model using the following command:
   ```bash
   ollama run llama3.2
   ```
  

### Steps
## 1. Clone the repository:
   ```bash
   git clone https://github.com/Sithum-Bimsara/Advanced-RAG-with-Open-Source-LLMs-and-Groq.git
   cd Advanced-RAG-with-Open-Source-LLMs-and-Groq
   ```
## 2. Create a Virtual Environment
On Windows:
```bash
python -m venv venv
```
On macOS/Linux:
```bash
python3 -m venv venv
```

## 3. Activate the Virtual Environment
On Windows:
```bash
.\venv\Scripts\activate
```
On macOS/Linux:
```bash
source venv/bin/activate
```

## 4. Install Dependencies
Install the required dependencies for the backend:
```bash
pip install -r requirements.txt
```   
   
## 5. Set up the environment variables:
   - Create a `.env` file in the root directory.
   - Add the Groq API key:
     ```
     GROQ_API_KEY="your_groq_api_key_here"
     ```
Replace `your_groq_api_key_here` with your actual Groq API key.


## 6. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
## 7. Access the application in your browser at `http://localhost:8501`.


----


## Application Usage
1. Load documents from the web using the built-in loader.
2. Input a prompt in the text field to ask a question.
3. View the AI’s response and relevant document context.
4. Explore document similarity results in the expandable section.

## Example Usage
- **Scenario**: Load AI-related documents and ask, “What is Generative AI”
- **Response**: The system provides a detailed explanation of Generative AI, its features, and its benefits.

## Contribution Guidelines
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request describing your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
Special thanks to:
- The Groq team for their innovative AI inference technology.
- The LangChain community for building robust tools for AI development.
- Streamlit for enabling rapid prototyping of AI applications.

