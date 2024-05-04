import os
from fastapi import UploadFile

async def save_upload_file(*, filename: str, upload_file: UploadFile, dest_folder: str):
    try:
        file_name = f"{filename}"  # assuming the file is a png
        file_path = os.path.join(dest_folder, file_name)

        with open(file_path, "wb") as buffer:
            content = await upload_file.read()  # async read
            buffer.write(content)

        return file_name

    finally:
        await upload_file.close()
