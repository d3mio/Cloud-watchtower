
import os
import logging
import argparse
import asyncio
from cloud_monitor import CloudMonitor
from config import Config

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define CLI flags
parser = argparse.ArgumentParser(description='Real-Time Cloud Resource Monitor and Anomaly Detector')
parser.add_argument('--config', help='Path to configuration file', default='config.yml')
parser.add_argument('--interval', help='Interval between checks in seconds', type=int, default=60)
parser.add_argument('--threshold', help='Threshold for anomaly detection', type=float, default=0.1)
parser.add_argument('--verbose', help='Enable verbose logging', action='store_true')

# Parse CLI flags
args = parser.parse_args()

# Load configuration
config = Config(args.config)

# Set up cloud monitor
cloud_monitor = CloudMonitor(config, args.interval, args.threshold)

# Run cloud monitor
async def run():
    await cloud_monitor.run()

# Run the main loop
async def main():
    try:
        await run()
    except Exception as e:
        logging.error(f'Error: {e}')

# Run the application
if __name__ == '__main__':
    asyncio.run(main())
