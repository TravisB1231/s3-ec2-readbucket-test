"""Data class for EC2 instance data."""
class Ec2Instance:
    """
    Filters out irrelevant boto3 EC2 data. Adds custom/enriches current EC2 data.
    Makes tag data easier to work with.
    """
    def __init__(self, instance_data:dict):
        self.id = instance_data["InstanceId"]
        if "IamInstanceProfile" in instance_data:
            self.profile = instance_data["IamInstanceProfile"]["Arn"]
        else:
            self.profile = None
    