""" Module used to manage profiles located in profiles.json """

import json
import discord

##### PROFILES.JSON MANAGEMENT #####

def get_profiles() -> list[dict]:
    """returns the list of all profiles"""

    with open("profiles.json", "r") as data_r:
        profiles: list = json.load(data_r)
    return profiles

def dump_profiles(new_data: list[dict]):
    """dump data in profiles.json to be set as new"""

    with open("profiles.json", "w") as data_w:
        json.dump(new_data, data_w, indent=4, separators=(",", ": "))
    return



##### PROFILE MANAGEMENT #####

def make_profile(user: discord.User):
    """creates a new profile with the given user to be added in profiles.json"""

    #load json to var profiles
    profiles = get_profiles()

    #add new profile to profiles
    profiles.append({
        "name": user.name,
        "id": user.id,
        "coin": 100,
        "level": 1,
    })
    #dump profiles as new
    dump_profiles(profiles)
    add_id(user.id)
    return

def delete_profile(profile: dict):
    """delete the profile given from profiles.json"""
    
    profiles = get_profiles()
    profiles.remove(profile)
    dump_profiles(profiles)
    return

def check_profile(user_id: int) -> bool:
    """checks if a profile is in profiles.json, returns bool"""

    for profile in get_profiles():
        if profile['id'] == user_id:
            return True
    return False

def get_profile(user_id: int) -> dict[str, any]:
    """returns a profile if the given id matches, returns None if no profile was found"""

    for profile in get_profiles():
        if profile['id'] == user_id:
            return profile
    return None

def modify_profile(new_profile: dict[str: any]):
    """takes a modified profile and saves the modifications to profiles.json"""

    profiles = get_profiles()
    for index, profile in enumerate(profiles):
        if profile['id'] == new_profile['id']:
            profiles[index] = new_profile
            break

    dump_profiles(profiles)
    return


##### ID JSON MANAGEMENT #####

def check_id(user_id: int) -> bool:
    """checks if given id is in the ids.json, returns bool"""
    with open("ids.json", "r") as ids:
        ids_lst: list = json.load(ids)

    #check if id is in list, returns TRUE/FALSE
    if user_id in ids_lst:
        return True
    return False

def add_id(user_id: int):
    """add given id to the ids.json file"""
    with open("ids.json", "r") as ids_r:
        ids: list = json.load(ids_r)
        ids.append(user_id)

    with open("ids.json", "w") as ids_w:
        json.dump(ids, ids_w, indent=4, separators=(",", ": "))
    return