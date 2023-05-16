import logging
import requests

class MetricsAgent:
    def __init__(self, grafana_url, grafana_api_key):
        self.grafana_url = grafana_url
        self.grafana_api_key = grafana_api_key
        self.headers = {
            "Authorization": f"Bearer {self.grafana_api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def log_metric(self, metric_name, metric_value):
        # Log the metric to the console
        logging.info(f"{metric_name}: {metric_value}")

        # Send the metric to Grafana
        data = {
            "series": [{
                "name": metric_name,
                "values": metric_value
            }]
        }
        response = requests.post(f"{self.grafana_url}/api/ds/query", headers=self.headers, json=data)
        if response.status_code != 200:
            logging.error(f"Failed to send metric to Grafana: {response.content}")

    def check_threshold(self, metric_name, threshold):
        # Check if the metric has breached the threshold and trigger an alarm if it has
        # This is a placeholder function. In the real world, you would get the metric value from
        # your metrics database or monitoring tool.
        metric_value = 0  # replace with actual metric value
        if metric_value > threshold:
            self.trigger_alarm(metric_name, metric_value, threshold)

    def trigger_alarm(self, metric_name, metric_value, threshold):
        # Trigger an alarm
        # This is a placeholder function. In the real world, you would integrate with your
        # alerting system to trigger an alarm.
        logging.warning(f"Alarm triggered: {metric_name} has exceeded the threshold. "
                        f"Metric value: {metric_value}, Threshold: {threshold}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    grafana_url = 'your-grafana-url'  # replace with your Grafana URL
    grafana_api_key = 'your-grafana-api-key'  # replace with your Grafana API key
    agent = MetricsAgent(grafana_url, grafana_api_key)
    agent.log_metric("test_metric", 123)
    agent.check_threshold("test_metric", 100)
