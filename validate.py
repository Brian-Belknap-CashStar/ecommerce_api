########################################################################################
# CAREFUL:
#
# This runs in CodeDeploy/host's python2.7 environment (not the VE of this app when it's run)
# Take care with your imports and what versions of things you think you can access
#
#########################################################################################
import requests


#########################################################################################
#
# This is called by CodeDeploy in the ValidateService step, after the ApplicationStart step.
# For more on where this fits into build/deploy:
# see https://cashstar.atlassian.net/wiki/display/ARCH/CI+and+Deployment+pipeline
#
# NOTE: Info written to stdout here will be in CodeDeploy's logs, to get at them
# see: https://cashstar.atlassian.net/wiki/display/DevOps/showproject%2C+elbcontrol+usage%2C+and+codedeploy+logs
#
#########################################################################################

# Uncomment each of the validation functions for the ways that this project can be deployed.
# The host's 'appconfig' ec2 tag determines which function is called.
# ie. validate_{appconfig}_deployment

# NOTES:
# -App is running, but not in the ELB.
# -All interactions here need to be against the local instance of this app...don't touch the ELB
# def validate_web_deployment(**kwargs):

# NOTES:
# -App is running, but not in the ELB.
# -All interactions here need to be against the local instance of this app...don't touch the ELB
# def validate_utility_deployment(**kwargs):

# NOTES:
# -Service is running, but not in the ELB.
# -All interactions here need to be against the local instance of this app...don't touch the ELB
# def validate_services_deployment(**kwargs):

# NOTES:
# -Worker is running and working items from the queue already.
# def validate_worker_deployment(**kwargs):
#
# NOTES:
# -Beats are running.
# def validate_celerybeat_deployment(**kwargs):
#
# NOTES:
# -Crons are running.
# def validate_proc_deployment(**kwargs):
#
# NOTES:
# -Crons are running.
# def validate_reactor_proc_deployment(**kwargs):
#
# NOTES:
# -App is running, but not in the ELB.
# -All interactions here need to be against the local instance of this app...don't touch the ELB
def validate_classic_deployment(**kwargs):
    response = requests.get('https://localhost:9206/version/', verify=False, timeout=1)

    if response.status_code == 200:
        return True

    return False
