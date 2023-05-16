import unittest
from agents.routing_agent import RoutingAgent
from agents.content_delivery_agent import ContentDeliveryAgent
from agents.interaction_agent import InteractionAgent
from agents.assignment_feedback_agent import AssignmentFeedbackAgent
from agents.metrics_agent import MetricsAgent

class TestAgents(unittest.TestCase):

    def setUp(self):
        self.routing_agent = RoutingAgent()
        self.content_delivery_agent = ContentDeliveryAgent()
        self.interaction_agent = InteractionAgent()
        self.assignment_feedback_agent = AssignmentFeedbackAgent()
        self.metrics_agent = MetricsAgent()

    def test_routing_agent(self):
        # Test the routing agent's functions
        # For example:
        self.assertTrue(self.routing_agent.route_task('content delivery'), "Routing failed")

    def test_content_delivery_agent(self):
        # Test the content delivery agent's functions
        # For example:
        self.assertTrue(self.content_delivery_agent.deliver_content('course material'), "Content delivery failed")

    def test_interaction_agent(self):
        # Test the interaction agent's functions
        # For example:
        self.assertTrue(self.interaction_agent.interact('Hello, AI'), "Interaction failed")

    def test_assignment_feedback_agent(self):
        # Test the assignment feedback agent's functions
        # For example:
        self.assertTrue(self.assignment_feedback_agent.give_feedback('assignment solution'), "Feedback failed")

    def test_metrics_agent(self):
        # Test the metrics agent's functions
        # For example:
        self.assertTrue(self.metrics_agent.log_metric('test metric', 1), "Metrics logging failed")
        self.assertTrue(self.metrics_agent.trigger_alarm('test metric', 1), "Alarm triggering failed")


if __name__ == "__main__":
    unittest.main()
