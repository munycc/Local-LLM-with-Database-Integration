import streamlit as st
from openai import OpenAI
from database_operations import get_material_properties
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Initialize OpenAI client

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="123",
)

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "system",
            "content": """You are a helpful assistant in construction. If you do not know the answer, reply I don't know 
                don't make things up.""",
        }
    ]

# Title
st.title('🪵Construction Material Assistant ')

# Display chat messages
for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])



#Handling User Input
prompt = st.chat_input('Enter your query about construction materials (e.g., "Tell me about the mechanical properties of Concrete, High Strength")')
if prompt:
    

    # Process the input with spaCy
    prompt_lower = prompt.lower()
    doc = nlp(prompt_lower)

    # Define material names and properties
    materials = {
        'Clay brick': ['clay brick', 'claybrick', 'clay bricks', 'clay'],
        'Concrete, high strength': ['concrete high strength', 'concretehighstrength'],
        'Concrete, lightweight': ['concrete lightweight', 'concretelightweight'],
        'Concrete, gravel or crushed stone aggregate': ['concrete gravel or crushed stone aggregate', 'concretegravelorcrushedstoneaggregate'],
        'European beech wood': ['european beech wood', 'europeanbeechwood'],
        'European black pine (austrian pine) wood': ['european black pine wood', 'austrian pine wood'],
        'European oak wood': ['european oak wood', 'europeanoakwood'],
        'European scots pine wood': ['european scots pine wood', 'europeanscotspinewood'],
        'European spruce (norway spruce) wood': ['european spruce wood', 'norway spruce wood', 'europeansprucewood'],
        'European white oak wood': ['european white oak wood', 'europeanwhiteoakwood'],
        'Glass fiber reinforced concrete': ['glass fiber reinforced concrete', 'glassfiberreinforcedconcrete'],
        'Glued-laminated timber (glulam)': ['glued-laminated timber', 'glulam', 'gluedlaminatedtimber'],
        'Granite': ['granite'],
        'Hard sandstone': ['hard sandstone', 'hardsandstone'],
        'Laminated veneer lumber (LVL)': ['laminated veneer lumber', 'lvl', 'laminatedveneerlumber'],
        'Limestone': ['limestone'],
        'Medium sandstone': ['medium sandstone', 'mediumsandstone'],
        'Spruce pine wood': ['spruce pine wood', 'sprucepinewood'],
        'Stainless steel plates': ['stainless steel plates', 'stainlesssteelplates']
    }

    properties = {
        'physical': ['physical'],
        'mechanical': ['mechanical'],
        'thermal': ['thermal']
    }

    def find_material(user_input):
        for material, variations in materials.items():
            for var in variations:
                if var in user_input:
                    return material
        return None

    def find_property(user_input):
        for key, variations in properties.items():
            for var in variations:
                if var in user_input:
                    return key
        return None

    # Extract material name and property type from the text
    material_name = find_material(prompt_lower)
    property_type = find_property(prompt_lower)

    if material_name and property_type:
        properties = get_material_properties(material_name, property_type)

        if properties:
            # Format properties for the LLM prompt
            formatted_properties = "\n".join(
                [f"- {prop[0]}: Metric: {prop[1]}, English: {prop[2]}, Comments: {prop[3]}" for prop in properties]
            )
            detailed_prompt = (f"User asked about the {property_type} properties of {material_name}.\n"
                               f"Here are the properties found in the database:\n{formatted_properties}\n\n"
                               "Please provide a detailed explanation, including correcting any units if necessary, "
                               "and explaining what these properties mean.")

        else:
            detailed_prompt = (f"User asked about the {property_type} properties of {material_name}, "
                               f"but no information was found in the database.\n"
                               "Please provide a detailed explanation based on your expertise.")

    else:
        detailed_prompt = (f"User query '{prompt}' could not be recognized.\n"
                           "Please provide a detailed explanation based on your expertise.")

    st.chat_message("user").markdown(detailed_prompt)
    st.session_state.messages.append({"role": "user", "content": detailed_prompt})

    response = client.chat.completions.create(
        model="llama.cpp/Models/mixtral-8x7b-instruct-v0.1.Q2_K.gguf",
        messages=st.session_state.messages,
        stream=True,
    )

    complete_response = ""
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                complete_response += chunk.choices[0].delta.content
                message_placeholder.markdown(complete_response + "▌")
                message_placeholder.markdown(complete_response)
    st.session_state.messages.append(
        {"role": "assistant", "content": complete_response}
    )



            
