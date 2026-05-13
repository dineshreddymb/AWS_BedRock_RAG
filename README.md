# Simple Bedrock Knowledge Base Chat

A simple Streamlit-based Retrieval-Augmented Generation (RAG) application that connects to an Amazon Bedrock Knowledge Base, retrieves relevant context for a user query, and generates a final response using a Bedrock foundation model or inference profile. Amazon Bedrock Knowledge Bases support querying source data and generating grounded responses through the `RetrieveAndGenerate` workflow.[1][2][3][4]

## Overview

This project demonstrates how to build a lightweight question-answering application on top of Amazon Bedrock Knowledge Bases using Python and Streamlit.[1][2]

Users enter a question in the Streamlit interface, the application sends that question to Bedrock, retrieves relevant chunks from the configured knowledge base, and returns a generated answer grounded in the retrieved information.[1][3][4]

## Features

- Streamlit-based web interface for asking questions interactively.[5][6]
- Integration with Amazon Bedrock Knowledge Bases for retrieval-augmented generation.[1][2]
- Uses the `retrieve_and_generate` API to combine retrieval and answer generation in a single call.[3][4]
- Environment-variable-based configuration for AWS Region, Knowledge Base ID, model ID, and credentials.[4]
- Beginner-friendly structure suitable for demos, prototypes, and learning projects.[7][8]

## Project Structure

```bash
AWSBedrock_Project/
├── rag_bedrock.py
├── .env
├── requirements.txt
└── README.md
```

## Tech Stack

- Python
- Streamlit
- Boto3
- Amazon Bedrock
- Amazon Bedrock Knowledge Bases
- python-dotenv

## How It Works

1. The user enters a question in the Streamlit app.
2. The app creates a Bedrock Agent Runtime client using Boto3.
3. The app calls `retrieve_and_generate()` with the configured Knowledge Base ID and model or inference profile.
4. Bedrock retrieves relevant source chunks from the knowledge base.
5. Bedrock generates a final answer using the retrieved context.[1][3][4]

## Prerequisites

Before running this project, make sure you have:

- An AWS account with Amazon Bedrock access enabled.[2][4]
- A configured Amazon Bedrock Knowledge Base.[2]
- An IAM user or role with permission to access Bedrock and the knowledge base resources.[4]
- Python 3.9+ installed locally.
- AWS credentials configured through environment variables or AWS CLI profile support.[4]

## Environment Variables

Create a `.env` file in the project root:

```env
AWS_REGION=ca-central-1
KNOWLEDGE_BASE_ID=YOUR_KNOWLEDGE_BASE_ID
MODEL_ARN=YOUR_MODEL_ID_OR_INFERENCE_PROFILE
AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_KEY
```

### Example

```env
AWS_REGION=ca-central-1
KNOWLEDGE_BASE_ID=LOWUMUPZ8P
MODEL_ARN=global.amazon.nova-2-lite-v1:0
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
```

## Installation

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file yet, you can use:

```txt
streamlit
boto3
python-dotenv
```

## Run the App

```bash
streamlit run rag_bedrock.py
```

After starting the app, open the local Streamlit URL shown in your terminal, enter a question, and submit it to query your knowledge base.

## Sample Code Flow

```python
response = client.retrieve_and_generate(
    input={"text": question},
    retrieveAndGenerateConfiguration={
        "type": "KNOWLEDGE_BASE",
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": knowledge_base_id,
            "modelArn": model_arn,
        },
    },
)
```

This request asks Bedrock to retrieve relevant content from the configured knowledge base and generate an answer using the specified model or inference profile.[3][4]

## Common Issues

### 1. NoCredentialsError
Boto3 cannot find AWS credentials. Configure `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_REGION`, or run `aws configure` locally.[4]

### 2. AccessDeniedException
Your IAM user or role does not have the necessary Bedrock, Lambda, or S3 Vectors permissions. Update IAM policies accordingly.[4]

### 3. Inference profile required
Some Bedrock models, including parts of the Amazon Nova family, may require an inference profile instead of direct on-demand invocation.[3][4]

### 4. Model not found
Make sure the selected model ID or inference profile is available in your account and supported in your AWS Region.[2][4]

## Use Cases

- Internal document Q&A
- Knowledge assistant prototypes
- Learning Retrieval-Augmented Generation (RAG)
- AWS Bedrock demo projects
- Domain-specific chatbot applications[7][1][2]

## Security Notes

- Never commit your `.env` file or AWS credentials to GitHub.
- Add `.env` to your `.gitignore` file.
- Use IAM least-privilege policies whenever possible.
- Prefer inference profiles or approved models supported by your Region and Bedrock configuration.[4]

## Future Improvements

- Add chat history support.
- Show citations or source references from the response.[3]
- Add better error handling and retry logic.
- Support model selection from the UI.
- Add document upload and knowledge base sync automation.

## License

This project is for learning and demo purposes. You can add an MIT License if you want to make the repository open source.
