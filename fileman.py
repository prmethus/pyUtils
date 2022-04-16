import os, requests


def download(url, save_path):
    continue_download = True

    if os.path.exists(save_path):
        if (
            not input(
                fr"The specified path '{save_path}' does exist. Rewrite the file? [Y/n]: "
            )
            == "Y"
        ):
            continue_download = False

    if continue_download == True:
        print("\nSending GET request to website....")
        try:
            file_content = requests.get(url).content
        except requests.exceptions.MissingSchema:
            print(f"{url} is not an appropriate URL. Terminating Download Operation.")
            return

        print(f"Downloading Buffer... Saving it in {save_path}")

        with open(save_path, "wb") as file:
            file.write(file_content)
        print(f"The file {save_path} has successfully been downloaded!")
    else:
        print("Terminating Download Operation... Reason: the file {} already exists")
