# --importing Libraries-- #
import json
import boto3
import os
'''
##### --Parameter Store Access Client-- ######  
'''
ssm_client = boto3.client('ssm')

'''
##### --Get Environment Values-- ######  
'''
config_name = os.environ["CONFIG_KEY"]
region_name = os.environ['REGION_NAME']

'''
##### --Get the nCall Resource Config from Parameter Store-- ######  
'''
parameter_from_store = ssm_client.get_parameter(Name=config_name, WithDecryption=True)
config_data = json.loads(parameter_from_store["Parameter"]["Value"])

'''
##### --DB Information Needed-- ######  
'''
db_name = config_data["db"]["db_name"]
username = config_data["db"]["username"]
password = config_data["db"]["password"]
host_read_replica = config_data["db"]["host_read_replica"]
host_write_replica = config_data["db"]["host_write_replica"]
config = {"db_name": db_name, "username": username, "password": password}

'''
##### --Redis Information Needed-- ######  
'''
redis_endpoint = config_data["redis"]["endpoint"]

'''
##### --SQS Information Needed-- ######  
'''
sqs_queue_name = config_data["sqs"]["queue_name"]
sqs_queue_arn = config_data["sqs"]["queue_arn"]
sqs_queue_url = config_data["sqs"]["queue_url"]

'''
##### --AWS Cognito  Information Needed-- ######  
'''
user_pool_id = config_data["cognito"]["user_pool_id"]
client_id = config_data["cognito"]["client_id"]
client_secret = config_data["cognito"]["client_secret"]

'''
##### --AWS Invocation Functions Information Needed-- ######  
'''
email_invocation_fxn = config_data["invocation_functions"]["email_notifier"]
similar_incident_fxn = config_data["invocation_functions"]["similar_incident"]
update_incident_fxn = config_data["invocation_functions"]["update_incident"]
slack_invocation_fxn = config_data["invocation_functions"]["slack_invocation"]

'''
##### --Tables Name Under Database-- ######  
'''
# Category: Incidents Managing Tables
incident_master_table = config_data["tables"]["incident_master"]
incident_timeline_table = config_data["tables"]["incident_timeline"]
incident_assigned_team_data_table = config_data["tables"]["incident_assigned_team"]
similar_incident_table = config_data["tables"]["similar_incidents"]
tags_table = config_data["tables"]["tags"]

# Category: Notes Table
notes_history_table = config_data["tables"]["notes_history"]

# Category: Runbook Managing Table
runbook_table = config_data["tables"]["runbook"]
runbook_with_alerts_n_remedies_table = config_data["tables"]["runbook_with_alerts_n_remedies"]
runbook_customize_structure_table = config_data["tables"]["runbook_customize_structure"]

# Category: User and Services Managing Table
services_table = config_data["tables"]["services"]
users_mapping_table = config_data["tables"]["users_mapping"]
users_roles_table = config_data["tables"]["users_roles"]
roles_type_table = config_data["tables"]["roles_type"]
features_table = config_data["tables"]["features"]
shift_scheduler_table = config_data["tables"]["shift_scheduler"]
slack_details_table = config_data["tables"]["slack_details"]

# Category: Document Feature  Managing Table
client_documents_table = config_data["tables"]["client_documents"]
document_listing_table = config_data["tables"]["document_listing"]

'''
##### --Domain Name-- #####
'''
domain_name = config_data["domain"]
