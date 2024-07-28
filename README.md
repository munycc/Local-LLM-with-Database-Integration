# Local LLM with Database Integration

Run LLM on your local machine, connected to a personal database. In this example, we can query construction materials and their precise properties using a conversational interface and our own database.

Big shout out to @nicknochnack for the inspiration for this project. 

## Features
- Local execution of Llama.cpp
- Database integration for personalized data access
- Streamlit interface for easy interaction

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/munycc/Local-LLM-with-Database-Integration
   cd Local-LLM-with-Database-Integration
   ```

2. **Run the make commands**

   - For macOS:
     ```bash
     cd llama.cpp && make
     ```

   - For Windows:
     1. Download the latest Fortran version of w64devkit.
     2. Extract w64devkit on your PC.
     3. Run `w64devkit.exe`.
     4. Use the `cd` command to reach the `llama.cpp` folder.
     5. Run:
        ```bash
        make
        ```

3. **Install Python Dependencies**
   ```bash
   pip install openai 'llama-cpp-python[server]' pydantic streamlit
   ```

4. **Download and Store the Model**

Download the Mistral model from Hugging Face:

Mistral: https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF

Save the model file in the Models folder of your project directory.


5. **Run the Server**
   Double-click on the file `run_server_and_app.bat`.



# Disclaimer
The material property values provided in this database have been modified from their original sources and are not necessarily accurate. These changes ensure that the database contains original and non-proprietary data. They are intended for illustrative purposes only. Users should verify any critical data and consult original sources or professional references before making engineering or design decisions.


## Support
Contributions to enhance functionality are always welcome.

## License
Code available under the MIT License, permitting reuse, modification, and distribution.
```

