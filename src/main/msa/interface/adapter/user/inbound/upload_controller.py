import os
from time import time

import aiofiles as aiofiles
from fastapi import APIRouter, File, UploadFile

router = APIRouter()


@router.post('/files/')
async def upload(file: bytes = File()) -> None:

    return {'file_size': len(file)}


@router.post('/uploadfile/')
async def create_upload_file(file: UploadFile):
    UPLOAD_DIRECTORY = 'D:/test/'
    start = time()

    try:
        async with aiofiles.open(os.path.join(UPLOAD_DIRECTORY,file.filename), 'wb') as f:
            while True:
                contents = await file.read(1024*1024)
                if not contents:
                    print('Read Done')
                    break
                end = time()
                print(f'now len...... {len(contents)}, time : {end - start}')
                await f.write(contents)
    except Exception as e:
        return {'message': 'There was an error uploading the file'}
    finally:
        await file.close()
    print('Upload Done')
    done = time()
    print(done - start)
    return {'time elapsed': done - start}