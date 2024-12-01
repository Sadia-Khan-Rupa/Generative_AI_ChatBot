# Generative_AI_ChatBot

As the final weeks of my Data Science Bootcamp come to a close, I find myself playing with Generative AI and dreaming of the possibilities. One idea that comes to mind is asking my LLM model to act like a financial expert and suggest stocks to invest in. Perhaps Solana? 😜

On the other hand, a career counselling chatbot would be incredibly helpful at this stage 😓 . I could ask, "How can I get a data scientist job in Germany?" Exciting times ahead! 😄

The project is described step by step here [Career ChatBot](https://medium.com/p/41bafc68bd3a#1a98-ddb8fe3909af)

A Streamlit-based AI chatbot designed to provide career guidance and networking advice using Llama models and FAISS.

📋 Table of Contents
About the Project
Demo
Features
Getting Started
Prerequisites
Installation
Usage
Customization
Technologies Used
Contributing
License
Contact
Acknowledgments

💡 About the Project
This chatbot assists users with career development strategies, providing insightful advice based on real-world scenarios. It uses advanced language models (Llama) and a FAISS-based vector database to retrieve and deliver personalized information.

🌐 Demo
Include a link to your live Streamlit app or a short GIF/image showing the chatbot in action.

✨ Features
Career Guidance: Provides tips on skill development and career planning.
Networking Insights: Shares examples and stories on effective networking.
Conversational Memory: Remembers the context to maintain a coherent conversation.
User-Friendly Interface: Built with Streamlit for an interactive experience.
⚙️ Getting Started
🛠️ Prerequisites

Ensure you have the following installed:

Python 3.8+
Streamlit
LlamaCpp
FAISS
HuggingFace Transformers

📥 Installation

Clone the repository and install dependencies:

git clone https://github.com/your-username/career-chatbot.git  
cd career-chatbot  
pip install -r requirements.txt  
🚀 Usage
Run the chatbot:
streamlit run app.py  
Interact through the Streamlit interface: Open the provided localhost link in your browser.
🎨 Customization
You can customize:

Model Path: Adjust in init_llm() function.
Prompt Template: Modify the template variable for different responses.
Number of Retrievals: Change k in search_kwargs for FAISS retriever.
🛠️ Technologies Used
Streamlit: For building the web interface.
LlamaCpp: For running Llama models locally.
FAISS: For fast similarity search and retrieval.
HuggingFace Transformers: For text embeddings.

🤝 Contributing
We welcome contributions!

Fork the project.
Create your feature branch: git checkout -b feature/new-feature
Commit your changes: git commit -m "Add some feature"
Push to the branch: git push origin feature/new-feature
Open a Pull Request.

📞 Contact
Sadia Khan Rupa: khanrupasadia@gmail.com
LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/sadia-khan-rupa/)

🙌 Acknowledgments
Thanks to the LangChain and Streamlit communities.
Inspired by the need for better career guidance tools.

