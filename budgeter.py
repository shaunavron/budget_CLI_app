
FILE_PATH_PREFIX = "user_data/" 
FILE_PATH_SUFFIX = ".csv"

class Profile:
    def __init__(self, username, file_name) -> None:
        self.username = username
        self.file_name = file_name


    def create_profile_file(username, file_name):
        pass
        # Create new profile file and write data to file 

    def edit_profile_file(username, file_name):
        pass
        # Edit pre-existing profile file

    def read_profile(username, file_name) -> dict:
        profile_data = {"salary": None, "savings": None}
        pass
        # Read file to find profile data

        return profile_data
