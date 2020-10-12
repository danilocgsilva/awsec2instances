import json

class Formatter:

    def extractRegions(self, json_formatted_string: str) -> list:

        region_entries = []

        j = json.loads(json_formatted_string)

        for region_data in j["Regions"]:
            region_entries.append(region_data["RegionName"])

        return region_entries

    def extractInstanceType(self, instanceInfos):
        return instanceInfos["InstanceType"]

    def extractInstanceId(self, instanceInfos):
        return instanceInfos["InstanceId"]

    def extractPublicIpAddress(self, instanceInfos):
        if "PublicIpAddress" in instanceInfos:
            return instanceInfos["PublicIpAddress"]
        else:
            return "---"

    def extractName(self, instanceInfos):
        if "Tags" in instanceInfos:
            listTags = instanceInfos["Tags"]

            for tag in listTags:
                if tag["Key"] == "Name":
                    return tag["Value"]

        return "---"

    def extracState(self, instanceInfos):
        return instanceInfos["State"]["Name"]