# Technology Stack Document

## Introduction

This document outlines the technology stack that our AI-powered online bootcamp will use. The chosen technologies play a crucial role in enabling the functionalities of the system and ensuring that it runs smoothly and efficiently.

## Tools and Platforms

The key tools and platforms used in our system include:

1. **Discord**: We will use Discord as the primary communication platform for the course. It enables real-time communication between the students and the AI LLM agent, supporting both text-based and voice-based interactions. It also supports the creation of different channels for different topics, making it easy to organize discussions and keep track of conversations.

2. **Google Docs**: Google Docs will serve as the platform for course content and assignments. It allows for collaborative editing and commenting, which is useful for peer learning and feedback. It also integrates well with the AI LLM agent, which can automatically generate and share course content and assignments.

3. **Replit**: Replit will be used for code execution and collaboration. It provides a powerful, cloud-based IDE that supports many programming languages. It also supports real-time collaborative coding and integrates with GitHub for version control.

4. **Grafana**: Grafana is a powerful open-source platform for visualization and monitoring. We will use Grafana to visualize the key metrics that we track, enabling us to monitor the performance of the system and the progress of the students in real-time.

## AI LLM Agent

The AI LLM agent will be built using the OpenAI GPT-3 model. It will be designed as a routing agent that can engage in conversation with the students and call the right child agents for specific tasks.

The agent will be implemented in Python, using the OpenAI API for interaction with the GPT-3 model. It will use Celery for task queuing and asynchronous execution, ensuring that it can handle multiple tasks concurrently and respond to students promptly.

## Child Agents

The child agents will also be implemented in Python. They will use various APIs and libraries to interact with the other tools and platforms in the system, including the Discord API for sending and receiving messages, the Google Docs API for managing documents, and the Replit API for executing code.

The child agents will include the Content Delivery Agent, the Interaction Agent, the Assignment and Feedback Agent, and the Metrics Agent. Each agent will have specific responsibilities and will be designed to work both independently and in coordination with the other agents.

## Database

We will use Google Sheets as the database for the MVP. It will store key data such as student information, course content, and assignment submissions. It is easy to use and integrates well with the rest of our tech stack. The Metrics Agent will also use the data stored in Google Sheets to update the key metrics in Grafana.
