import os, requests
import joblib
import stringcolor


def download(url, save_path):
    """
    Downloads a file by sending GET request.
    Parameters:
        url = The URL of the file.
        save_path = The File path for saving the downloaded file.
    """
    continue_download = True

    if os.path.exists(save_path):
        if (
            not input(
                stringcolor.cs(
                    fr"The specified path '{save_path}' does exist. Rewrite the file? [Y/n]: ",
                    "green",
                )
            )
            == "Y"
        ):
            continue_download = False

    if continue_download:
        print(stringcolor.cs("\nSending GET request to website....", "cyan"))
        try:
            file_content = requests.get(url).content
        except requests.exceptions.MissingSchema:
            print(
                stringcolor.cs(
                    f"{url} is not an appropriate URL. Terminating Download Operation.",
                    "red",
                ).bold()
            )
            return

        print(stringcolor.cs(f"Downloading Buffer... Saving it in {save_path}", "cyan"))

        with open(save_path, "wb") as file:
            file.write(file_content)
        print(
            stringcolor.cs(
                f"The file {save_path} has successfully been downloaded!", "cyan"
            )
        )
    else:
        print(
            stringcolor.cs(
                "Terminating Download Operation... Reason: the file {} already exists",
                "red",
            ).bold()
        )


def save_object(obj, save_path):

    """
    Saves a Python Object in .pkl format.
    Parameters: 
        obj = The Python Object.
        save_path = The File Path for saving the .pkl file.
    """

    if not save_path.endswith(".pkl"):
        print(
            stringcolor.cs(
                f"The {save_path} is not in '.pkl' format.\nTerminating Operation...",
                "red",
            ).bold()
        )
        return

    continue_saving = True

    if os.path.exists(save_path):
        if (
            not input(
                stringcolor.cs(
                    f"{save_path} already exists. Rewrite it? [Y/n]: ", "green"
                )
            )
            == "Y"
        ):
            continue_saving = False
    if continue_saving:
        joblib.dump(obj, save_path)
        print(stringcolor.cs(f"\nObject saved at Path: {save_path}", "cyan"))
    else:
        print(
            stringcolor.cs(
                f"Terminating Saving Operation. Reason: {save_path} already exists.",
                "red",
            ).bold()
        )
