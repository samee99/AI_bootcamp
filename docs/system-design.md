# System Design Document

## Introduction

This document outlines the system design for an AI-powered online bootcamp MVP. The bootcamp aims to create an environment conducive to self-paced, active learning that leverages peer collaboration and industry-relevant project work. The key tenets of the bootcamp are:

1. Art of Learning: Incorporating effective learning strategies and techniques.
2. Active Learning: Encouraging students to be active participants in their learning.
3. Peer Learning: Facilitating collaboration and shared knowledge among students.
4. Simulating Industry Environment: Providing practical experience through a project-centric approach.
5. Upskilling in Technical and Soft-Skills: Offering feedback on both technical and soft skills to provide a rounded learning experience.

## System Overview

Our system consists of a main AI Large Language Model (LLM) agent that acts as a routing agent, interfacing with the students via Discord. It also triggers child agents responsible for specific tasks such as content delivery, interaction management, assignment feedback, and metrics tracking. The main AI LLM agent uses Celery to manage task queues and to perform task routing among the child agents.

The child agents are designed to automate various aspects of the online bootcamp:

- Content Delivery Agent: Handles course content dissemination via Google Docs. It uses a drip content delivery approach, releasing content as per the predefined schedule and student progress.
- Interaction Agent: Manages discussions and communications on Discord. It simulates a peer learning environment and encourages active participation.
- Assignment and Feedback Agent: Interfaces with Replit for assignment submissions and automated feedback. It also encourages the Feynman Technique by having students explain their assignments.
- Metrics Agent: Tracks key metrics like student engagement, goal completion, and feedback. It communicates with Grafana to visualize these metrics in a comprehensive dashboard.

## Data Flow

- The main AI LLM agent receives student queries and requests from Discord.
- Depending on the nature of the request, it routes tasks to the appropriate child agent via Celery.
- Each child agent performs its specific function, either responding directly to the user (in the case of the Interaction Agent), or updating system states and data (Content Delivery Agent, Assignment and Feedback Agent).
- The Metrics Agent periodically collects data and updates the Grafana dashboard. Alerts are raised if certain thresholds or conditions are breached.

## Key Technologies

- **Discord:** Serves as the primary communication platform for students and the AI LLM agent.
- **Google Docs:** Used as the main content delivery platform, offering an easy-to-use interface for content creation and sharing.
- **Replit:** Enables a collaborative and interactive coding environment for students to complete assignments and receive feedback.
- **Grafana:** Provides a powerful visualization platform for tracking key metrics and system performance.
- **Celery:** A task queue system used to distribute work across threads or machines.
- **OpenAI GPT-3:** Powers the AI LLM agents, providing the natural language processing capabilities.

This document provides a high-level overview of the system design. Each component will be further elaborated upon during the implementation phase.
