from langchain.llms import LlamaCpp
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.memory import ConversationBufferMemory
import streamlit as st
import os


#llm
@st.cache_data
def init_llm():
   # TODO dowloading the model 
   return LlamaCpp(model_path = '/Users/sadiakhanrupa/Bootcamp Main Phase/Chapter_8_generative_Ai/Model/faiss_index/mistral-7b-instruct-v0.1.Q4_K_M.gguf',
                  max_tokens = 2000,
                  temperature = 0.1,
                  top_p = 1,
                  n_gpu_layers = -1,
                  n_ctx=1024)

llm = init_llm()



# Define the embedding model
embedding_model = 'sentence-transformers/all-MiniLM-l6-v2'

# Get the current working directory
current_folder = os.getcwd()

# Set the folder to store the embeddings cache
embeddings_folder = current_folder

# Create an instance of the HuggingFaceEmbeddings class
embeddings = HuggingFaceEmbeddings(model_name=embedding_model, cache_folder=embeddings_folder)
#faiss_index2

# load Vector Database
# allow_dangerous_deserialization is needed. Pickle files can be modified to deliver a malicious payload that results in execution of arbitrary code on your machine
vector_db = FAISS.load_local("/Users/sadiakhanrupa/Bootcamp Main Phase/Chapter_8_generative_Ai/faiss_index2", embeddings, allow_dangerous_deserialization=True)

# retriever
retriever = vector_db.as_retriever(search_kwargs={"k": 2})

#memory
@st.cache_data
def init_memory(_llm):
   return ConversationBufferMemory(
      llm=llm,
      output_key= 'answer',
      memory_key= 'chat_history',
      return_messages= True)

memory = init_memory(llm)

template = """
<s> [INST]
You are polite and professional question-answering AI assistant. You must provide a helpful response to the user.

In your response, PLEASE ALWAYS:
  (0) Be a career Analyst: give precise answers how one person can develop his career
  (1) Provide examples of other people: how growing network has been helpful for them
  (2) If the context enables you to answer the question, write a detailed, helpful, and easily understandable answer
  (3) Do not make answers too boring, add some humor with your answer
[/INST]
[INST]
Answer the following question using the context provided.
The question is surrounded by the tags <q> </q>.
The context is surrounded by the tags <c> </c>.
<q>
{question}
</q>
<c>
{context}
</c>
[/INST]
</s>
[INST]
Helpful Answer:
[INST]
"""

prompt = PromptTemplate(template = template,
                        input_variables = ['context', 'question'])

# chain
chain = ConversationalRetrievalChain.from_llm(llm,
                                              retriever=retriever,
                                              memory=memory,
                                              return_source_documents=True,
                                              combine_docs_chain_kwargs={"prompt": prompt})


###streamlit###

st.title('Welcome to your Networking Consultant')

#initialize chat history
#chat history saves the previous messages to be displayed
if 'messages' not in st.session_state:
   st.session_state.messages = []

#Display chat messages from history on app rerun
for message in st.session_state.messages:
   with st.chat_message(message['role']):
      st.markdown(message['content'])

#React to use r content

if prompt:= st.chat_input('What do you want to know?'):

   #Display user message in chat message conatiner
   st.chat_message('user').markdown(prompt)

    # Add user message to chat history
   st.session_state.messages.append({'role': 'user', 'content':prompt})
   # Begin spinner before answering question so it's there for the duration
   with st.spinner ('searching your answer'):

      # send question to chain to get answer
      answer = chain(prompt)
      
      #extract answer from dictionary returned by chain
      response = answer['answer']

      # Display chatbot response in chat message container
      with st.chat_message('career consultant'):
         st.markdown(answer['answer'])

      # Add assistant response to chat history
      st.session_state.messages.append({'role':'career consultant', 'content':response})


