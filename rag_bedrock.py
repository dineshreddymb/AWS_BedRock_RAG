import os
import streamlit as st
import boto3
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

st.set_page_config(page_title="Simple KB Chat", page_icon="💬")
st.title("Simple Bedrock Knowledge Base Chat")

region = os.getenv("AWS_REGION", "ca-central-1")
knowledge_base_id = os.getenv("KNOWLEDGE_BASE_ID", "LOWUMUPZ8P")
model_arn = os.getenv("MODEL_ARN", "global.amazon.nova-2-lite-v1:0")

st.write("Ask a question to your Amazon Bedrock Knowledge Base.")

question = st.text_input("Enter your question")

if st.button("Ask"):
    if not knowledge_base_id:
        st.error("Set KNOWLEDGE_BASE_ID as an environment variable.")
    elif not model_arn:
        st.error("Set MODEL_ARN as an environment variable.")
    elif not question.strip():
        st.error("Please enter a question.")
    else:
        try:
            client = boto3.client("bedrock-agent-runtime", region_name=region)

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

            answer = response["output"]["text"]
            st.subheader("Answer")
            st.write(answer)

        except ClientError as e:
            st.error(f"AWS Error: {e.response['Error']['Message']}")
        except Exception as e:
            st.error(f"Error: {str(e)}")