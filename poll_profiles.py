import json

import aws_auth
from ec2_instance import Ec2Instance

def write_output_json(resp:dict) -> None:
    """Useful for testing to get raw boto3 output.
    Writes to 2output.json in json format."""
    with open("output.json", 'w', encoding="UTF-8") as outfile:
        outfile.write(json.dumps(resp, default=str))

def enum_instances(raw_list: list) -> list:
    inst_list = [Ec2Instance(raw_list[i]["Instances"][0]) for i in range(len(raw_list)) if raw_list is not None]
    return inst_list

def enum_profiles(inst_list: list) -> list:
    prof_list = []
    for inst in inst_list:
        if inst.profile not in prof_list:
            prof_list.append(inst.profile)
    return prof_list

def check_s3_get_object(prof_list:list) -> list:
    good_profs = []
    for prof in prof_list:
        pass
    return good_profs

def main():
    ec2 = aws_auth.botosesh.client('ec2')
    res = ec2.describe_instances()
    if aws_auth.validate_response_code(res):
        _raw_response_data:dict= res["Reservations"]
        if _raw_response_data is not None:
            write_output_json(res)
            ec2_instances:list = enum_instances(_raw_response_data)
            instance_profiles:list = enum_profiles(ec2_instances)
            valid_profiles:list = check_s3_get_object(instance_profiles)


if __name__ == "__main__":
    main()
    
# TODO - Check each instance_profile's role for the right policy. Might need to parse the terraform state to get the necessary policy name
# Boto3 Resources: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#instanceprofile
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_instance_profile
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_role_policy
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_role