REM Start the FastAPI server
start /b python -m uvicorn api_server:app --host 0.0.0.0 --port 8000 --reload

REM Wait for the server to start (adjust the timeout if needed)
timeout /t 10

REM Start the LLaMA.cpp server
start /b python -m llama_cpp.server --model Models\mistral-7b-instruct-v0.1.Q4_0.gguf --n_gpu -1

REM Wait for the LLaMA.cpp server to start (adjust the timeout if needed)
timeout /t 10

REM Run Streamlit app
streamlit run app.py