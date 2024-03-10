class BaseFile:

    def __init__(self, filename, size, created_at, created_by, file_extension, *args, **kwargs):
        self.filename = filename
        self._size = self._check_size(size)
        self.created_at = created_at
        self.created_by = created_by
        self.file_extension = file_extension

    @staticmethod
    def _check_size(size):
        if size > 4_294_967_295:
            raise ValueError("File is too big")

    @property
    def extension(self):
        return self.file_extension

    @extension.setter
    def extension(self, new_extension):
        self.file_extension = new_extension



class MediaFile(BaseFile):

    def __init__(self, filename, size, created_at, created_by, file_extension, *args, **kwargs):
        super().__init__(filename, size, created_at, created_by, file_extension)


class AudioFile(MediaFile):

    def __init__(self, filename, size, created_at, created_by, file_extension,
                 audio_name=None, author=None, album=None, publication_date=None):
        super().__init__(filename, size, created_at, created_by, file_extension)

        self.audio_name = audio_name
        self.author = author
        self.album = album
        self.publication_date = publication_date


class VideoFile(MediaFile):

    def __init__(self, filename, size, created_at, created_by, file_extension,
                 duration, resolution, capture_time=None, camera_model=None, geolocation=None):

        super().__init__(filename, size, created_at, created_by, file_extension)
        self.duration = duration
        self.resolution = resolution
        self.capture_time = capture_time
        self.camera_model = camera_model
        self.geolocation = geolocation


class ImageFile(MediaFile):

    def __init__(self, filename, size, created_at, created_by, file_extension,
                 resolution, capture_time=None, camera_model=None, geolocation=None):

        super().__init__(filename, size, created_at, created_by, file_extension)
        self.resolution = resolution
        self.capture_time = capture_time
        self.camera_model = camera_model
        self.geolocation = geolocation


class StorageService:

    def __init__(self):
        pass

    def check_existence(self, file):
        # проверяет существование файла, если файл существует, возвращает True
        pass

    def create(self, file):
        if self.check_existence(file):
            raise FileExistsError('This file already exists')
        else:
            # тут код для создания файла
            print('Created')

    def update(self, file):
        if self.check_existence(file):
            # тут код для обновления файла
            print('Updated')
        else:
            raise FileNotFoundError('File not found')

    def delete(self, file):
        if self.check_existence(file):
            # тут код для удаления файла
            print('Deleted')
        else:
            raise FileNotFoundError('File not found')


class LocalStorageService(StorageService):

    def __init__(self):
        super().__init__()


class S3StorageService(StorageService):

    def __init__(self, host):
        super().__init__()
        self.host = host

    def check_existence(self, file):
        # запрос в s3 с проверкой на существование файла
        pass


# Вопрос - много ли кода придется дописать / переписать при добавлении новых типов файлов и способов их хранения?

# при появлении новых хранилищ необходимо будет создавать новые классы от класса StorageService

# при появлении новых метаданных - нужно будет добавлять их в __init__ для каждого класса, наследуемого от
# MediaFile (AudioFile, ImageFile, VideoFile)

# при появлении новых типов файлов - необходимо будет наследовать классы от  BaseFile
