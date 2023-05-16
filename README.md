# AI LLM Agent System

The AI LLM Agent System is a comprehensive system designed to automate various aspects of a learning bootcamp, including content delivery, interaction, assignments, and feedback. This system leverages the power of AI and machine learning to provide personalized, efficient, and effective learning experiences.

## Table of Contents
- [Getting Started](#getting-started)
- [System Design](#system-design)
- [Technologies Used](#technologies-used)
- [Agents](#agents)
- [Running the Tests](#running-the-tests)
- [Contributing](#contributing)
- [License](#license)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3.8 or later
- Discord
- Google Docs
- Replit
- Grafana

### Installation
1. Clone the repository:
git clone https://github.com/samee99/ai-llm-agent-system.git

2. Install the necessary Python libraries:
pip install -r requirements.txt


## System Design
For a detailed explanation of the system design, see [system-design.md](system-design.md).

## Technologies Used
- Discord: For interaction and communication.
- Google Docs: For content delivery.
- Replit: For coding assignments and collaboration.
- Grafana: For metrics visualization.
- Celery: For task routing.

For more information, see [tech-stack.md](tech-stack.md).

## Agents
- Routing Agent
- Content Delivery Agent
- Interaction Agent
- Assignment Feedback Agent
- Metrics Agent

Each agent's functionalities are defined in their respective Python scripts in the `agents/` directory.

## Running the Tests
To run the tests, navigate to the `tests/` directory and execute the test scripts:

python test_discord_bot.py
python test_agents.py


## Contributing
Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
