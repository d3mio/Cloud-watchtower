
import asyncio
import logging
from azure.identity import DefaultAzureCredential
from azure.mgmt.monitor import MonitorManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.core.exceptions import HttpResponseError

class CloudMonitor:
    def __init__(self, config, interval, threshold):
        self.config = config
        self.interval = interval
        self.threshold = threshold
        self.credential = DefaultAzureCredential()
        self.monitor_client = MonitorManagementClient(self.credential, self.config.get('subscription_id'))
        self.compute_client = ComputeManagementClient(self.credential, self.config.get('subscription_id'))

    async def run(self):
        while True:
            await self.check_usage()
            await asyncio.sleep(self.interval)

    async def check_usage(self):
        try:
            # Get current usage
            usage = self.get_usage()

            # Check for anomalies
            anomalies = self.detect_anomalies(usage)

            # Alert teams
            if anomalies:
                self.alert_teams(anomalies)
        except HttpResponseError as e:
            logging.error(f'Error: {e}')

    def get_usage(self):
        # Get current usage from Azure Monitor
        usage = self.monitor_client.usage.list(self.config.get('resource_group_name'))
        return usage

    def detect_anomalies(self, usage):
        # Detect anomalies using threshold
        anomalies = []
        for resource in usage:
            if resource.usage > self.threshold:
                anomalies.append(resource)
        return anomalies

    def alert_teams(self, anomalies):
        # Alert teams using Microsoft Teams webhook
        import requests
        webhook_url = self.config.get('webhook_url')
        payload = {'title': 'Anomaly detected', 'text': 'Resource usage exceeds threshold'}
        requests.post(webhook_url, json=payload)
