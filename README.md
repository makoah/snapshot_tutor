# snapshotalyzer-3000
Demo Project to manage AWS EC2 instance snapshots

This project is a demo and uses boto2 to manage AWS EC2 instance snapshots

## Configuring
shotty uses the configuration file created by the AWS cli e.g.
'aws configure --profile shotty'

## Running
'pipenv run python shotty/shotty.py <command> <--project=PROJECT>'

*command* is list, start or stop_instances
*project* is optional
